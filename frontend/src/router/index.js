import { createRouter, createWebHistory } from 'vue-router'
import Login from '../pages/Login.vue'
import Register from '../pages/Register.vue'
import Reporteria from '../pages/Reporteria.vue'

const routes = [
  { path: '/', name: 'Login', component: Login },
  { path: '/login', name: 'LoginAlias', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/reporteria', component: Reporteria }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
