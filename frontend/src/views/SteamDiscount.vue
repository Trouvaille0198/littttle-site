

<template>
  <v-container>
    <v-row>
      <v-col v-for="item in discounts" :key="item.name" lg="3" cols="6">
        <v-card>
          <a :href="item.link" target="_blank">
            <v-img :src="item.img_url" height="150px"></v-img
          ></a>

          <v-card-title
            v-text="item.name"
            class="pa-3 pink lighten-5 grey--text text--darken-3"
          >
          </v-card-title>
          <v-divider inset> </v-divider>

          <v-card-text class="black--text text-subtitle-1 pt-2">
            <div class="text-decoration-line-through grey--text my-0">
              {{ item.previous_price }}
            </div>
            <div class="font-weight-bold text-h6 pink--text">
              {{ item.current_price }}
            </div>
            <v-btn
              class="d-none d-md-flex"
              absolute
              color="pink"
              right
              bottom
              rounded
              outlined
              :href="item.link"
              target="_blank"
            >
              {{ item.discount }}
            </v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-btn
        v-if="show_more"
        @click="addDiscounts"
        class="pink lighten-3 white--text ma-3"
      >
        MORE
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
import { readDiscountAPI } from "@/api/steamDiscount";
export default {
  name: "SteamDiscount",
  data() {
    return {
      discounts: [],
      page_num: 1,
      show_more: false,
    };
  },
  mounted: function () {
    readDiscountAPI().then((res) => {
      this.show_more = true;
      this.discounts = res;
    });
  },
  methods: {
    addDiscounts() {
      let params = {
        page: this.page_num + 1,
      };
      readDiscountAPI(params).then((res) => {
        this.page_num++;
        console.log(res);
        this.discounts = this.discounts.concat(res);
      });
    },
  },
};
</script>

<style>
</style>