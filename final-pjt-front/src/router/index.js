// Vue Router
import { createRouter, createWebHistory } from 'vue-router'

// Views
import CurrencyConverterView from '@/views/CurrencyConverter/CurrencyConverterView.vue'
import BankMapView from '@/views/Map/BankMapView.vue'

// Article Views
import ArticleView from '@/views/Article/ArticleView.vue'
import DetailView from '@/views/Article/DetailView.vue'
import CreateView from '@/views/Article/CreateView.vue'

// Auth Views
import SignUpView from '@/views/Auth/SignUpView.vue'
import LoginView from '@/views/Auth/LoginView.vue'

// Store
import { useAuthStore } from '@/stores/auth'
import ProFileView from '@/views/Auth/ProFileView.vue'
import FinancialInformationView from '@/views/Finance/FinancialInformationView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 메인 기능 라우트
    {
      path: '/currency-converter',
      name: 'CurrencyConverter',
      component: CurrencyConverterView,
    },
    {
      path: '/finance',
      name: 'financialInformation',
      component: FinancialInformationView,
    },
    {
      path: '/find-nearest-bank',
      name: 'findNearestBank',
      component: BankMapView,
    },

    // 게시판 관련 라우트
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

    // 인증 관련 라우트
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView,
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },
    {
      path:'/profile/:id',
      name: 'ProFileView',
      component: ProFileView
    },

    // // 404 페이지 (없는 경우 추가 권장)
    // {
    //   path: '/:pathMatch(.*)*',
    //   name: 'NotFound',
    //   redirect: '/articles'  // 또는 404 페이지 컴포넌트로 연결
    // }
  ],
})
router.beforeEach((to, from) => {
  const authStore = useAuthStore()
  // 로그인 사용자의 회원가입/로그인 페이지 접근 제한
  if ((to.name === 'SignUpView' || to.name === 'LoginView') && authStore.isLogin) {
    window.alert('로그인 상태입니다.')
    return { name: 'ArticleView' }
  }
  // 비로그인 사용자의 글작성 페이지 접근 제한
  if (to.name === 'CreateView' && !authStore.isLogin) {
    window.alert('로그인이 필요한 서비스입니다.')
    return { name: 'LoginView' }
  }
  // 다른 모든 경우에는 내비게이션 허용
  return true
})
export default router
