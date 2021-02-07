/*
 * @Date: 2021-02-03 06:34:40
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-06 21:08:52
 */
import Vue from 'vue'
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
