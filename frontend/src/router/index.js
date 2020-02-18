import Vue from 'vue'
import Router from 'vue-router'
import Account from '@/components/Account'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Account',
      component: Account,
      props: true
    },
    {
      path: '/account:id',
      name: 'Account',
      component: Account,
      props: true
    }
  ]
})
