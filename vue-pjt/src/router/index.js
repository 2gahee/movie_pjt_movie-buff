import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticlesView from '@/views/ArticlesView.vue'
import NewAccountView from '@/views/NewAccountView.vue'
import LoginView from '@/views/LoginView.vue' 
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import { useMovieStore } from '@/stores/counter'



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
      component:LoginView,
      name: 'Login'
      
    },
    {
      path:'/community/create/',
      component: ArticleCreateView,
      name: 'createArticle'
    }
  ],
})

router.beforeEach((to, from) => {
  const store = useMovieStore()
  // 만약 이동하는 목적지가 커뮤니티 페이지이면서
  // 현재 로그인 상태가 아니라면 로그인 페이지로 보냄
  if (to.name === 'Articles' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogIn' }
  }
})


export default router
