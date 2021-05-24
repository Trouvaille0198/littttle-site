
import requests
from bs4 import BeautifulSoup
from urllib import request
import os
import re
from utils import logger


class SteamDiscountCrawler(object):
    def __init__(self) -> None:
        super().__init__()

    def GetMaxPage(self):
        url = []
        url.append("https://store.steampowered.com/search/?specials=1&page=1")
        soup = self.GetSoup(self.GetUrlContents(url))
        node = soup[0].find_all("div", class_="search_pagination_right")
        return int(node[0].contents[5].contents[0])

    def CreateUrls(self, pages):
        urls = []
        for i in range(pages):
            urlExample = "https://store.steampowered.com/search/?specials=1&page={}".format(
                i + 1)
            urls.append(urlExample)
        return urls

    def GetUrlByPage(self, page):
        """
        获取指定页面, 使用列表存储以避免发生冲突
        """
        urls = []
        url = "https://store.steampowered.com/search/?specials=1&page={}".format(
            page)
        urls.append(url)
        return urls

    def GetUrlContents(self, urls):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/ 90.0.4430.93 Safari/605.1.15'}
        responseList = []
        contentList = []
        for i in range(len(urls)):
            try:
                response = requests.get(urls[i], headers=headers)
            except requests.exceptions.ConnectionError:
                logger.error('Steam disconnected!')
                exit()
            responseList.append(response)
            contentList.append(responseList[i].text)
        return contentList

    def GetSoup(self, contentList):
        soup = []
        for i in range(len(contentList)):
            soup.append(BeautifulSoup(contentList[i], "html.parser"))
        return soup

    def GetGameNames(self, contentList):
        names = []
        soup = self.GetSoup(contentList)
        for i in range(len(contentList)):
            names.extend(soup[i].find_all("span", class_="title"))
        for i in range(len(names)):
            names[i] = names[i].string
        return names

    def GetGameUrls(self, contentList):
        urls = []
        soup = self.GetSoup(contentList)
        urlPrefix = "https://store.steampowered.com/"
        for i in range(len(contentList)):
            for node in soup[i].find_all("a"):
                temp = node.get("href")
                if (urlPrefix + "app/" in temp or urlPrefix + "bundle/" in temp or urlPrefix + "sub/" in temp) and "view" not in temp:
                    urls.append(node.get("href"))
        return urls

    def GetPrices(self, contentList):
        previousPrices = []
        nowPrices = []
        discounts = []
        soup = self.GetSoup(contentList)
        for i in range(len(contentList)):
            count = 0
            unpurchaseableIndex = []
            for node in soup[i].find_all("div", class_="col search_discount responsive_secondrow"):
                discount = node.text.strip("\n")
                if discount == "":
                    discounts.append("0")
                    unpurchaseableIndex.append(count)
                else:
                    discounts.append(discount)
                count += 1
            for node in soup[i].find_all("div", class_="col search_price discounted responsive_secondrow"):
                previousPrices.append(node.contents[1].contents[0].contents[0])
                nowPrices.append(node.contents[3].strip())
            for j in unpurchaseableIndex:
                previousPrices.insert(i * 25 + j, "Unpurchasable")
                nowPrices.insert(i * 25 + j, "Unpurchasable")
        return previousPrices, nowPrices, discounts

    def GetGameCovers(self, contentList):
        soup = self.GetSoup(contentList)
        count = 0
        gameCoverUrls = []
        for i in range(len(contentList)):
            for node in soup[i].find_all("div", class_="col search_capsule"):
                gameCoverUrls.append(node.contents[0].attrs["src"])
                count += 1
        gameCoverUrls = [url.replace(
            'capsule_sm_120.jpg', 'header.jpg') for url in gameCoverUrls]
        return gameCoverUrls

    def Merge(self, names, urls, previousPrices, nowPrices, discounts, gameCoverUrls):
        games = []
        for i in range(len(names)):
            dictionary = dict(name=names[i], link=urls[i], discount=discounts[i],
                              current_price=nowPrices[i], previous_price=previousPrices[i],
                              img_url=gameCoverUrls[i])
            games.append(dictionary)
        return games

    def Sort(self, games, sortRule=''):
        for i in range(len(games)):
            if games[i]["previous_price"] == "Unpurchasable":
                games[i]["previous_price"] = "1000000"
            if games[i]["current_price"] == "Unpurchasable":
                games[i]["current_price"] = "1000000"
            games[i]["previous_price"] = float(
                games[i]["previous_price"].strip("¥"))
            games[i]["current_price"] = float(
                games[i]["current_price"].strip("¥"))
            games[i]["discount"] = float(games[i]["discount"].strip("%"))
        if sortRule:
            games = sorted(games, key=lambda x: (x[sortRule], x["name"]))
        for i in range(len(games)):
            if games[i]["previous_price"] == 1000000:
                games[i]["previous_price"] = "Unpurchasable"
            else:
                games[i]["previous_price"] = "¥ " + \
                    str(games[i]["previous_price"])
            if games[i]["current_price"] == 1000000:
                games[i]["current_price"] = "Unpurchasable"
            else:
                games[i]["current_price"] = "¥ " + \
                    str(games[i]["current_price"])
            games[i]["discount"] = str(games[i]["discount"]) + "%"
        return games

    def start(self, page=1, sortRule=''):

        urls = self.GetUrlByPage(page)
        contentList = self.GetUrlContents(urls)
        gameNames = self.GetGameNames(contentList)
        gameUrls = self.GetGameUrls(contentList)
        previousPrices, nowPrices, discounts = self.GetPrices(contentList)
        gameCoverUrls = self.GetGameCovers(contentList)
        games = self.Merge(gameNames, gameUrls, previousPrices,
                           nowPrices, discounts, gameCoverUrls)
        # games = self.Sort(games, sortRule)
        return games
