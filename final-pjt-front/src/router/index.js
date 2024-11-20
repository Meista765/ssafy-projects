import { createRouter, createWebHistory } from 'vue-router'
import CurrencyConverterView from '@/views/CurrencyConverterView.vue'
import BankMapView from '@/views/BankMapView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/currency-converter',
      name: 'currencyConverter',
      component: CurrencyConverterView,
    },
    {
      path: '/find-nearest-bank',
      name: 'findNearestBank',
      component: BankMapView,
    },
  ],
})

export default router
