import axios from 'axios'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useFinanceStore = defineStore(
  'Finance',
  () => {
    const financialProducts = ref([])
    const BACKEND_SERVER_URL = import.meta.env.VITE_BACKEND_SERVER_URL

    const getExchangeRate = () => {
      axios({
        method: 'get',
        url: `${BACKEND_SERVER_URL}/finances/get_products_infos/`
      })
        .then(res => {
          financialProducts.value = res.data.prdt_data
        })
        .catch((err) => console.log(err))
    }

    return { financialProducts, getExchangeRate }
  },
  { persist: true }
)
