<template>
  <v-container>
    <v-btn :to="{ name: 'CurrencyConverter' }">환율 계산기</v-btn>
    <v-btn :to="{ name: 'findNearestBank' }">가까운 은행 찾기</v-btn>

    <template v-if="authStore.isLogin">
      <v-btn @click="logOut">로그아웃</v-btn>
    </template>
    <template v-else>
      <v-btn :to="{ name: 'SignUpView' }">회원가입</v-btn>
      <v-btn :to="{ name: 'LoginView' }">로그인</v-btn>
    </template>

    <v-btn :to="{ name: 'ArticleView' }">게시판</v-btn>
  </v-container>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

const logOut = function () {
  authStore.logOut()
}
</script> 