<template>
  <v-container class="d-flex justify-space-between align-center">
    <!-- 좌측: 로고 및 기능 관련 버튼 -->
    <div class="d-flex align-center">
      <!-- 홈으로 이동하는 로고 추가 -->
      <router-link :to="{ name: 'HomeView' }" class="text-decoration-none mr-2">
        <v-avatar size="48px">
          <v-img
            src="./src/assets/image/logo_img.png"
            alt="로고"
          ></v-img>
        </v-avatar>
      </router-link>

      <!-- 기존 버튼들 -->
      <v-btn :to="{ name: 'CurrencyConverter' }">환율 계산기</v-btn>
      <v-btn :to="{ name: 'findNearestBank' }">가까운 은행 찾기</v-btn>
      <v-btn :to="{ name: 'FinancialProduct' }">금융상품 정보</v-btn>
      <v-btn :to="{ name: 'ArticleView' }">게시판</v-btn>
    </div>

    <!-- 우측: 사용자 관련 버튼 -->
    <div>
      <template v-if="authStore.isLogin">
        <v-btn
          v-if="userId"
          :to="{ name: 'ProFileView', params: { id: userId } }"
        >
          프로필
        </v-btn>
        <v-btn @click="logOut">로그아웃</v-btn>
      </template>
      <template v-else>
        <v-btn :to="{ name: 'SignUpView' }">회원가입</v-btn>
        <v-btn :to="{ name: 'LoginView' }">로그인</v-btn>
      </template>
    </div>
  </v-container>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { ref, onMounted, watch } from 'vue'
import { RouterLink } from 'vue-router'
import axios from 'axios'

const authStore = useAuthStore()
const userId = ref(null)

const logOut = function () {
  authStore.logOut()
}

// 로그인한 유저정보 가져오기
const getCurrentUser = async () => {
  try {
    const response = await axios.get(`${authStore.BACKEND_SERVER_URL}/user/`, {
      headers: {
        Authorization: `Token ${authStore.token}`,
      },
    })
    userId.value = response.data.id
  } catch (err) {
    console.log('getCurrentUser', err)
  }
}

// 컴포넌트 마운트 시 현재 사용자 정보 가져오기
onMounted(() => {
  if (authStore.isLogin) {
    getCurrentUser()
  }
})

// authStore.isLogin의 변화를 감지하여 getCurrentUser 호출
watch(
  () => authStore.isLogin,
  (newVal) => {
    if (newVal) {
      getCurrentUser()
    } else {
      userId.value = null
    }
  }
)
</script>
