import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
export const useAuthStore = defineStore('auth', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })


  // 회원가입 요청 액션
  const signUp = function (payload) {
    const { username, password1 , password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        // console.log(res)
        const password = password1
        logIn({username,password})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 로그인 요청 액션
  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        // console.log(res.data)
        token.value = res.data.key
        // console.log(token)
        router.push({ name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })

    }
  // 로그아웃 요청 액션
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
  }
    return { signUp, logIn, token, isLogin, logOut }
  },
  { persist: true }
)
