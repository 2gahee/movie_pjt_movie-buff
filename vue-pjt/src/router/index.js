import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticlesView from '@/views/ArticlesView.vue'
import NewAccountView from '@/views/NewAccountView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      component: HomeView
    },
    {
      path:'/community',
      component: ArticlesView
    },

    {
      path:'/signup',
      component: NewAccountView
    }
  ],
})

export default router
