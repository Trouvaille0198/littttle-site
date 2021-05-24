import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

// 设置导航守卫
router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    let loginState = sessionStorage.getItem('loginState')
    if (loginState && loginState == 'true') {
      next()
    } else {
      next({ path: '/SHUlogin' })
    }
  } else {
    next()
  }
})

// 挂载
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

