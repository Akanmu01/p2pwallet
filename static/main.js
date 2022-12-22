// import Vue from 'https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.esm.browser.min.js'
import { Navbar } from './components/navbar.js'
import { MainTemplate } from './templates/app.js'
import { Home } from './components/home.js'
import { Register } from './components/register.js'

Vue.use(VueRouter)

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');




const router = new VueRouter({
  routes: [
  {
    path: '',
    component: Home,
    name: "Home Page"
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
    },
    router,
    template: MainTemplate,
    getCookie,
})
