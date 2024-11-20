import { createRouter, createWebHistory } from 'vue-router'
import CurrencyConverterView from '@/views/CurrencyConverterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/currency-converter',
      name: 'currencyConverter',
      component: CurrencyConverterView,
    },
  ],
})

export default router
