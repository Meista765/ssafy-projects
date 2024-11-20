import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeRateStore = defineStore(
  'exchangeRate',
  () => {
    const exchangeRates = ref([])
    const server_url = 'http://localhost:8000/exchange-rates/'

    const getExchangeRate = () => {
      axios
        .get(server_url)
        .then(res => {
          exchangeRates.value = res.data.exchange_rates_data
        })
        .catch((err) => console.log(err))
    }

    return { exchangeRates, getExchangeRate }
  },
  { persist: true }
)
