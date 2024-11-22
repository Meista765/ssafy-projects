import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useAuthStore } from './auth'

export const useArticleStore = defineStore('article', () => {
  const authStore = useAuthStore()
  const articles = ref([])
  const article = ref(null)
  const BACKEND_SERVER_URL = import.meta.env.VITE_BACKEND_SERVER_URL
  
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${BACKEND_SERVER_URL}/articles/`,
      headers: {
        Authorization: `Token ${authStore.token}`
      }
    })
      .then((res) => {
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getArticle = async (articleId) => {
    try {
      const response = await axios({
        method: 'get',
        url: `${BACKEND_SERVER_URL}/articles/${articleId}/`,
        headers: {
          Authorization: `Token ${authStore.token}`
        }
      })
      console.log(response)
      article.value = response.data
    } catch (error) {
      console.error('게시글 조회 실패:', error)
    }
  }

  const deleteArticle = async (articleId) => {
    try {
      await axios({
        method: 'delete',
        url: `${BACKEND_SERVER_URL}/articles/${articleId}/`,
        headers: {
          Authorization: `Token ${authStore.token}`
        }
      })
    } catch (error) {
      console.error('게시글 삭제 실패:', error)
      throw error
    }
  }

  return { 
    BACKEND_SERVER_URL, 
    articles, 
    article,
    getArticles,
    getArticle,
    deleteArticle
  }
}, {
  persist: true
})
