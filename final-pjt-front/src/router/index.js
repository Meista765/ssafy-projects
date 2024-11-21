import { createRouter, createWebHistory } from 'vue-router'
import CurrencyConverterView from '@/views/CurrencyConverterView.vue'
import ArticleView from '@/views/Article/ArticleView.vue'
import DetailView from '@/views/Article/DetailView.vue'
import CreateView from '@/views/Article/CreateView.vue'
import SignUpView from '@/views/Auth/SignUpView.vue'
import LoginView from '@/views/Auth/LoginView.vue'
import { useAuthStore } from '@/stores/auth'
import ProFileView from '@/views/Auth/ProFileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/currency-converter',
      name: 'CurrencyConverter',
      component: CurrencyConverterView,
    },
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path:'/signup',
      name: 'SignUpView',
      component: SignUpView,
    },
    {
      path:'/login',
      name: 'LoginView',
      component: LoginView
    },
    {
      path:'/profile/:id',
      name: 'ProFileView',
      component: ProFileView
    },
  ],
})
router.beforeEach((to, from) => {
  const authStore = useAuthStore()
  // 만약 로그인 사용자가 회원가입 또는 로그인을 시도하면
  // 메인 페이지로 보냄
  if ((to.name === 'SignUpView' || to.name === 'LoginView') && (authStore.isLogin)) {
    window.alert('로그인 상태입니다.')
    return { name: 'ArticleView'}
  }
})
export default router
