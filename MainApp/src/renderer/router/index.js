/*
 * @Date: 2021-02-03 06:34:40
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-15 10:21:37
 */

import Vue from 'vue'

import { library, dom } from '@fortawesome/fontawesome-svg-core'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
// import { faTwitter } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Router from 'vue-router'
import { shortcut } from '../plugins/shortcut'
import {
  Button,
  Select,
  Container,
  Header,
  Aside,
  Main,
  Footer,
  Row,
  Col,
  Card,
  Progress,
  Input,
  Divider,
  Tag
} from 'element-ui'

library.add(fas, fab, far)
dom.watch()

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.prototype.$shortcut = shortcut
window.Vue = Vue
Vue.use(Tag)
Vue.use(Divider)
Vue.use(Input)
Vue.use(Router)
Vue.use(Button)
Vue.use(Progress)
Vue.use(Select)
Vue.use(Container)
Vue.use(Aside)
Vue.use(Main)
Vue.use(Header)
Vue.use(Footer)
Vue.use(Row)
Vue.use(Col)
Vue.use(Card)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: resolve => { require(['@/components/Main'], resolve) },
      meta: {
        id: 0
      },
      children: [
        {
          path: '/recent',
          name: 'recent',
          meta: {

          },
          component: resolve => { require(['@/components/Recent'], resolve) }
        },
        {
          path: '/notebook',
          name: 'notebook',
          meta: {
            id: 1
          },
          component: resolve => { require(['@/components/Notebook'], resolve) }
        },
        {
          path: '/word',
          name: 'word',
          meta: {
            id: 2
          },
          component: resolve => { require(['@/components/Word'], resolve) }
        }
      ]
    }
  ]
})
