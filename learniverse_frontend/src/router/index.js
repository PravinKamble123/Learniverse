import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import( '../views/AboutView.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import( '../views/SignUp.vue')
  },
  {
    path: '/log-in',
    name: 'login',
    component: () => import( '../views/LogIn.vue')
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: () => import( '../views/dashboard/MyAccount.vue')
  },

  {
    path: '/courses',
    name: 'Courses',
    component: () => import( '../views/Courses.vue')
  },

  {
    path: '/courses/:slug',
    name: 'Course',
    component: () => import( '../views/Course.vue')
  },
  {
    path: '/authors/:id',
    name: 'Author',
    component: () => import( '../views/Author.vue')
  },
  {
    path: '/dashboard/create-course',
    name: 'CreateCourse',
    component: () => import( '../views/dashboard/CreateCourse.vue')
  }


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
