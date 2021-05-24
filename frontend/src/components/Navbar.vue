<template>
  <div>
    <v-app-bar app class="white">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" color="pink">
      </v-app-bar-nav-icon>
      <v-tool-bar-title class="text-capitalize text-h4 mx-3">
        <span class="font-weight-light">Vuetify</span>
        <span>Learning</span>
      </v-tool-bar-title>
      <v-spacer></v-spacer>
      <v-btn icon color="pink">
        <v-icon>mdi-exit-to-app</v-icon>
      </v-btn>
    </v-app-bar>
    <!-- 导航栏 -->
    <v-navigation-drawer app v-model="drawer">
      <v-list>
        <v-list-item href="https://github.com/Trouvaille0198">
          <v-list-item-avatar>
            <v-img src="http://image.trouvaille0198.top/download.png"></v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="title">MelonSoul</v-list-item-title>
          </v-list-item-content>
          <v-list-item-action>
            <v-icon>mdi-menu-down</v-icon>
          </v-list-item-action>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <!-- 列表 -->
      <v-list nav>
        <v-list-item-group>
          <v-list-item
            v-for="(item, i) in listItems"
            :key="i"
            :to="item.link"
            active-class="pink--text text--accent-4"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> {{ item.text }} </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      drawer: false,

      listItems: [
        { text: "Examples", icon: "mdi-cards-outline", link: "/examples" },
        { text: "Todo", icon: "mdi-format-list-checks", link: "/todo" },
        { text: "Test", icon: "mdi-account-outline", link: "/test" },
        {
          text: "Steam Discount",
          icon: "mdi-account-outline",
          link: "/steamdiscount",
        },
        {
          text: "SHU course",
          icon: "mdi-account-outline",
          link: "/course_old",
        },
      ],
    };
  },
};
</script>
