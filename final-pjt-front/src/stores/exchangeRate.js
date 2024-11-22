import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeRateStore = defineStore(
  'exchangeRate',
  () => {
    const exchangeRates = ref([])
    const BACKEND_SERVER_URL = import.meta.env.VITE_BACKEND_SERVER_URL

    const getExchangeRate = () => {
      axios({
        method: 'get',
        url: `${BACKEND_SERVER_URL}/exchange-rates/`
      })
        .then(res => {
          exchangeRates.value = res.data.exchange_rates_data
        })
        .catch((err) => console.log(err))
    }

    return { exchangeRates, getExchangeRate }
  },
  { persist: true }
)
