<template>
  <v-container class="d-flex justify-space-between align-center">
    <!-- 좌측: 로고 -->
    <div class="d-flex align-center">
      <router-link :to="{ name: 'HomeView' }" class="text-decoration-none">
        <v-avatar size="48">
          <v-img :src="logoImg" alt="로고"></v-img>
        </v-avatar>
      </router-link>

      <!-- PC 화면에서 보이는 메뉴 -->
      <div class="d-none d-md-flex">
        <v-btn variant="text" :to="{ name: 'CurrencyConverter' }">환율 계산기</v-btn>
        <v-btn variant="text" :to="{ name: 'findNearestBank' }">가까운 은행 찾기</v-btn>
        <v-btn variant="text" :to="{ name: 'FinancialProduct' }">금융상품 정보</v-btn>
        <v-btn variant="text" :to="{ name: 'ArticleView' }">게시판</v-btn>
      </div>
    </div>
    
    <div class="d-none d-md-flex">
      <!-- PC 화면 사용자 메뉴 -->
      <template v-if="authStore.isLogin">
        <v-btn v-if="userId" :to="{ name: 'FinanceRecommendView', params: { id: userId } }">금융상품추천</v-btn>
        <v-btn v-if="userId" :to="{ name: 'ProFileView', params: { id: userId } }">프로필</v-btn>
        <v-btn @click="logOut">로그아웃</v-btn>
      </template>
      <template v-else>
        <v-btn variant="text" :to="{ name: 'SignUpView' }">회원가입</v-btn>
        <v-btn variant="text" :to="{ name: 'LoginView' }">로그인</v-btn>
      </template>
    </div>

    <!-- 모바일 햄버거 메뉴 -->
    <div class="d-md-none">
      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn icon v-bind="props">
            <v-icon>mdi-menu</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item :to="{ name: 'CurrencyConverter' }">
            <v-list-item-title>환율 계산기</v-list-item-title>
          </v-list-item>
          <v-list-item :to="{ name: 'findNearestBank' }">
            <v-list-item-title>가까운 은행 찾기</v-list-item-title>
          </v-list-item>
          <v-list-item :to="{ name: 'FinancialProduct' }">
            <v-list-item-title>금융상품 정보</v-list-item-title>
          </v-list-item>
          <v-list-item :to="{ name: 'ArticleView' }">
            <v-list-item-title>게시판</v-list-item-title>
          </v-list-item>

          <v-divider></v-divider>

          <!-- 모바일 사용자 메뉴 -->
          <template v-if="authStore.isLogin">
            <v-list-item v-if="userId" :to="{ name: 'FinanceRecommendView', params: { id: userId } }">
              <v-list-item-title>금융상품추천</v-list-item-title>
            </v-list-item>
            <v-list-item v-if="userId" :to="{ name: 'ProFileView', params: { id: userId } }">
              <v-list-item-title>프로필</v-list-item-title>
            </v-list-item>
            <v-list-item @click="logOut">
              <v-list-item-title>로그아웃</v-list-item-title>
            </v-list-item>
          </template>
          <template v-else>
            <v-list-item :to="{ name: 'SignUpView' }">
              <v-list-item-title>회원가입</v-list-item-title>
            </v-list-item>
            <v-list-item :to="{ name: 'LoginView' }">
              <v-list-item-title>로그인</v-list-item-title>
            </v-list-item>
          </template>
        </v-list>
      </v-menu>
    </div>
  </v-container>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { ref, onMounted, watch } from 'vue'
import { RouterLink } from 'vue-router'
import axios from 'axios'

import logoImg from '@/assets/image/logo_img.png'

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
