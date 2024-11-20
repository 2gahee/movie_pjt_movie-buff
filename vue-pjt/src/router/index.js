import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticlesView from '@/views/ArticlesView.vue'
import NewAccountView from '@/views/NewAccountView.vue'
import LoginView from '@/views/LoginView.vue' 
import ArticleCreateView from '@/views/ArticleCreateView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      component: HomeView
    },
    {
      path:'/community',
      component: ArticlesView,
      name: 'Articles'
    },

    {
      path:'/signup',
      component: NewAccountView
    },
    {
      path:'/login',
      component:LoginView
    },
    {
      path:'/community/create/',
      component: ArticleCreateView,
      name: 'createArticle'
    }
  ],
})

export default router
