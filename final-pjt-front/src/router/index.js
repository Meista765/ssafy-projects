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
import FinancialProductView from '@/views/Finance/FinancialProductView.vue'
import FinancialProductDetailView from '@/views/Finance/FinancialProductDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 1. 메인 기능 라우트
    // 환율 계산기
    {
      path: '/currency-converter',
      name: 'CurrencyConverter',
      component: CurrencyConverterView,
    },
    // 금융 상품 목록
    {
      path: '/financial-product',
      name: 'FinancialProduct',
      component: FinancialProductView
    },
    // 금융 상품 상세
    {
      path: '/financial-product/:productUniqueId',
      name: 'FinancialProductDetail',
      component: FinancialProductDetailView
    },
    // 은행 지도
    {
      path: '/find-nearest-bank',
      name: 'findNearestBank',
      component: BankMapView,
    },

    // 2. 게시판 관련 라우트
    // 게시글 목록
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    // 게시글 상세
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    // 게시글 작성
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },

    // 3. 인증 관련 라우트
    // 회원가입
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView,
    },
    // 로그인
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },
    // 프로필
    {
      path: '/profile/:id',
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
