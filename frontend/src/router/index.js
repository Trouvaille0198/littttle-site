import Vue from 'vue'
import VueRouter from 'vue-router'
import Examples from '../views/Examples.vue'
import Todo from '../views/Todo.vue'
import SteamDiscount from '../views/SteamDiscount.vue'
import CourseOld from '../views/CourseOld.vue'
import SHULogin from '../views/SHULogin.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/examples'
  },
  {
    path: '/examples',
    name: 'Examples',
    component: Examples
  },
  {
    path: '/todo',
    name: 'Todo',
    component: Todo
  },
  {
    path: '/steamdiscount',
    name: 'SteamDiscount',
    component: SteamDiscount
  },
  {
    path: '/course_old',
    name: 'CourseOld',
    component: CourseOld,
    meta: {
      requireAuth: true // 需要登陆才能访问
    }
  },
  {
    path: '/SHUlogin',
    name: 'SHULogin',
    component: SHULogin
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


export default router
