import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAuthStore = defineStore(
  'auth',
  () => {
    const BACKEND_SERVER_URL = import.meta.env.VITE_BACKEND_SERVER_URL
    const token = ref(null)
    const username = ref(null)
    const router = useRouter()

    const isLogin = computed(() => {
      return token.value ? true : false
    })

    const signUp = async (payload) => {
      await axios({
        method: 'post',
        url: `${BACKEND_SERVER_URL}/accounts/signup/`,
        data: payload,
      })
        .then((response) => {
          if (response.data.key) {
            token.value = response.data.key
            username.value = payload.username
            router.go(-1)
          }
        })
        .catch((error) => {
          console.error(error)
          throw error
        })
    }

    const logIn = async (payload) => {
      await axios({
        method: 'post',
        url: `${BACKEND_SERVER_URL}/accounts/login/`,
        data: payload,
      })
        .then((response) => {
          token.value = response.data.key
          username.value = payload.username
          router.go(-1)
        })
        .catch((error) => {
          console.error('로그인 실패:', error)
          alert('로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요.')
        })
    }

    const logOut = async () => {
      await axios({
        method: 'post',
        url: `${BACKEND_SERVER_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then(() => {
          token.value = null
          username.value = null
        })
        .catch((error) => {
          console.error('로그아웃 실패:', error)
        })
    }

    return {
      token,
      username,
      isLogin,
      BACKEND_SERVER_URL,
      signUp,
      logIn,
      logOut,
    }
  },
  {
    persist: true,
  }
)
