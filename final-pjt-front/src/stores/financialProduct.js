import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from './auth'

export const useFinanceStore = defineStore(
  'Finance',
  () => {
    const authStore = useAuthStore()

    const financialProducts = ref([])
    const selectedProduct = ref(null)
    const BACKEND_SERVER_URL = import.meta.env.VITE_BACKEND_SERVER_URL

    const getFinancialProducts = async () => {
      await axios({
        method: 'get',
        url: `${BACKEND_SERVER_URL}/finances/infos/`,
      })
        .then((res) => {
          financialProducts.value = res.data.prdt_data
        })
        .catch((err) => console.log(err))
    }

    const getProductDetailFromServer = async (productUniqueId) => {
      await axios({
        method: 'get',
        url: `${BACKEND_SERVER_URL}/finances/infos/${productUniqueId}/`,
        headers: {
          Authorization: `Token ${authStore.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          selectedProduct.value = res.data
        })
        .catch((error) => {
          console.error('상품 정보 조회 실패:', error)
        })
    }

    return {
      financialProducts,
      selectedProduct,
      getFinancialProducts,
      getProductDetailFromServer,
    }
  },
  { persist: true }
)
