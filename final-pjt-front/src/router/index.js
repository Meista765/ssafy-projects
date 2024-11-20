import { createRouter, createWebHistory } from 'vue-router'
import CurrencyConverterView from '@/views/CurrencyConverterView.vue'
import FinancialInformationView from '@/views/FinancialInformationView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/currency-converter',
      name: 'currencyConverter',
      component: CurrencyConverterView,
    },
    {
      path: '/finance',
      name: 'financialInformation',
      component: FinancialInformationView,
    },
  ],
})

export default router
