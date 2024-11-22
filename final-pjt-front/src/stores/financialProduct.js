import axios from 'axios'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useFinanceStore = defineStore(
  'Finance',
  () => {
    const financialProducts = ref([])
    const selectedProduct = ref(null)
    const BACKEND_SERVER_URL = import.meta.env.VITE_BACKEND_SERVER_URL

    const getFinancialProducts = () => {
      axios({
        method: 'get',
        url: `${BACKEND_SERVER_URL}/finances/get_products_infos/`
      })
        .then(res => {
          financialProducts.value = res.data.prdt_data
        })
        .catch((err) => console.log(err))
    }

    const getProductDetail = (productUniqueId) => {
      const product = financialProducts.value.find(product => product.unique_id === productUniqueId)
      if (product) {
        selectedProduct.value = product
      } else {
        console.log('상품을 찾을 수 없습니다.')
      }
    }

    return { 
      financialProducts, 
      selectedProduct,
      getFinancialProducts,
      getProductDetail
    }
  },
  { persist: true }
)
