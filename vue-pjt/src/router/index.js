import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticlesView from '@/views/ArticlesView.vue'
import NewAccountView from '@/views/NewAccountView.vue'
import LoginView from '@/views/LoginView.vue' 
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import { useMovieStore } from '@/stores/counter'
import CurrentListView from '@/views/CurrentListView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      component: HomeView,
      name: 'Home'
    },
    {
      path:'/community',
      component: ArticlesView,
      name: 'Articles'
    },

    {
      path:'/signup',
      component: NewAccountView,
      name: 'Signup'
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
    },
    {
      path:'/now-on',
      component: CurrentListView,
      name: 'NowOns'
    },
    {
      path:'/community/:id',
      component: ArticleDetailView,
      name: 'articleDetail'
    },
    {
      path:'/movies/:id/',
      component: MovieDetailView,
      name: 'detail'
    },
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
  // 만약 로그인 사용자가 회원가입 또는 로그인 페이지로 이동하려고 하면
  // 메인(Home) 페이지로 보냄
  if ((to.name === 'Signup' || to.name === 'Login') && (store.isLogin)) {
    window.alert('이미 로그인 되어있습니다.')
    return { name: 'Home' }
  }
})


export default router
