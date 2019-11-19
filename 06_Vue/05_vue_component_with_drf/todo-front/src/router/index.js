import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

// VueRouter를 사용하기 위한 코드
Vue.use(VueRouter)

// router와 conponents를 연결(django의 urls.py와 유사)
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]

const router = new VueRouter({
  // vue-router를 설치할 때 설정했던 history 모드
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
