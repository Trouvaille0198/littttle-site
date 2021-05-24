from typing import List
from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from schemas.discount import Discount
from utils import SteamDiscountCrawler


router = APIRouter()


@router.get('/discounts',  response_model=List[Discount], tags=['Get steam discounted games'])
def get_discounts(page: int = 1, sort_rule: str = '') -> list:
    crawler = SteamDiscountCrawler()
    discounts = crawler.start(page, sort_rule)
    return discounts
