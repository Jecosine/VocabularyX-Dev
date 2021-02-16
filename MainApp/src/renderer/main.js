/*
 * @Date: 2021-02-03 06:34:40
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-16 13:08:05
 */
import Vue from 'vue'
import axios from 'axios'

import App from './App'
import router from './router'
import store from './store'
import './theme/default/index.css'
import './theme/ff8623/index.css'
if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.http = Vue.prototype.$http = axios
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  components: { App },
  router,
  store,
  template: '<App/>'
}).$mount('#app')
