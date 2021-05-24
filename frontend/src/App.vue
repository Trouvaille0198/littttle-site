<template>
  <v-app class="purple lighten-1">
    <navbar></navbar>
    <v-main>
      <!-- page content -->
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar.vue";
export default {
  name: "App",
  components: { Navbar },
};
</script>
