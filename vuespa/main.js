import Vue from 'https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.esm.browser.min.js'
import { Navbar } from './components/navbar.js'
import { MainTemplate } from './templates/app.js'
import { Home } from './components/home.js'
import { About } from './components/about.js'
import { Login } from './components/login.js'
import { LoginForm } from './script/auth.js'
import { Register } from './components/register.js'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
  {
    path: '',
    component: Home,
    name: "Home Page"
  },
  {
    path: '/about',
    component: About,
    name: "About Us Page"
  },
  {
    path: '/login',
    component: Login,
    name: "Login Page"
  },
  {
    path: '/register',
    component: Register,
    name: "Register Page"
  },
]
})

new Vue({
    el: '#app', // This should be the same as your <div id=""> from earlier.
    components: {
      'navbar': Navbar,
      'about': About
    },
    router,
    template: MainTemplate
})
