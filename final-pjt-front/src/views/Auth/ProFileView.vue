<template>
  <div v-if="userInfo">
    <h1>{{ userInfo.username }}님의 프로필 페이지</h1>
    <button @click="signOut">
      회원탈퇴
    </button>
  </div>
  <div v-else>
    <p>사용자 정보를 불러오는 중...</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted,computed } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRoute } from 'vue-router';

// 변수
const authStore = useAuthStore()
const route = useRoute()
const userId = route.params.id



// 액션

// 사용자 정보 가져오기
const getUserInfo = function () {
  authStore.getUserInfo(userId)
  console.log(authStore.userInfo)
}

const signOut = function () {
  if (confirm('진짜 탈퇴할거임?')) {
    authStore.signOut(userId)
  }
}
const userInfo = computed(() => authStore.userInfo);
onMounted(getUserInfo)
</script>

<style scoped>

</style>