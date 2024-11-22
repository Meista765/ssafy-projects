<template>
  <v-container>
    <v-btn :to="{ name: 'CurrencyConverter' }">환율 계산기</v-btn>
    <v-btn :to="{ name: 'findNearestBank' }">가까운 은행 찾기</v-btn>
    <v-btn :to="{ name: 'financialInformation' }">예적금 정보</v-btn>

    <template v-if="authStore.isLogin">
      <v-btn 
        v-if="userId" 
        :to="{ name: 'ProFileView', params: { id: userId }}"
      >
        프로필
      </v-btn>
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
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const authStore = useAuthStore()
const userId = ref(null)

const logOut = function () {
  authStore.logOut()
}

// 로그인한 유저정보 가져오기
const getCurrentUser = async () => {
  try {
    const response = await axios.get(`${authStore.API_URL}/user/`,{
      headers: {
        Authorization: `Token ${authStore.token}`,
      }
    })
    userId.value = response.data.id
  } catch (err) {
    console.log('getCurrentUser', err)
  }
}

// 컴포넌트 마운트 시 현재 사용자 정보 가져오기
onMounted(() => {
  if (authStore.isLogin) {
    getCurrentUser();
  }
});

// authStore.isLogin의 변화를 감지하여 getCurrentUser 호출
watch(() => authStore.isLogin, (newVal) => {
    if (newVal) {
      getCurrentUser();
    } else {
      userId.value = null;
    }
  }
);
</script> 