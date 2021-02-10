/*
 * @Date: 2021-02-03 06:34:40
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-10 08:41:24
 */

import Vue from 'vue'

import { library, dom } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
// import { faTwitter } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import Router from 'vue-router'
import {
  Button,
  Select,
  Container,
  Header,
  Aside,
  Main,
  Footer
} from 'element-ui'

library.add(fas, fab)
dom.watch()

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(Router)
Vue.use(Button)
Vue.use(Select)
Vue.use(Container)
Vue.use(Aside)
Vue.use(Main)
Vue.use(Header)
Vue.use(Footer)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: require('@/components/Main').default,
      meta: {
        id: 0
      },
      children: [
        {
          path: '/notebook',
          name: 'notebook',
          meta: {
            id: 1
          },
          component: require('@/components/Notebook').default
        }
      ]
    }
  ]
})
