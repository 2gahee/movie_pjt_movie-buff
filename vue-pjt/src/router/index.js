import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticlesView from '@/views/ArticlesView.vue'



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
  ],
})

export default router
