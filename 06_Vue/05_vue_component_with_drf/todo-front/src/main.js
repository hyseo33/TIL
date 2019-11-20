import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import Vuesession from 'vue-session'
import store from './store'

Vue.config.productionTip = false
// Vue.use(Vuesession)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
