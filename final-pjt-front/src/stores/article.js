import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useAuthStore } from './auth'

export const useArticleStore = defineStore('article', () => {
  const authStore = useAuthStore()
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`,
      headers: {
        Authorization: `Token ${authStore.token}`
      }
    })
      .then((res) => {
        console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
        // console.log(authStore)
        // console.log(autho)
      })
  }

    return { API_URL, articles, getArticles }
  },
  { persist: true }
)
