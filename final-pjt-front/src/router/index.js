import { createRouter, createWebHistory } from 'vue-router'
import ExchangeRateView from '@/views/ExchangeRateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/calc-exchange-rate',
      name: 'exchangeRateCalculator',
      component: ExchangeRateView,
    },
  ],
})

export default router
