import axios from 'axios'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useFinanceStore = defineStore(
  'Finance',
  () => {
    
    const financialProducts = ref([])
    const serverUrl = 'http://localhost:8000/finances/get_products_infos/'

    const getExchangeRate = () => {
      axios
        .get(serverUrl)
        .then(res => {
          financialProducts.value = res.data.prdt_data
        })
        .catch((err) => console.log(err))
    }

    return { financialProducts, getExchangeRate }
  },
  { persist: true }
)
