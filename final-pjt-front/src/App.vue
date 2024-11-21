<template>
  <div>
    <nav v-if="authStore.isLogin">
      <router-link :to="{ name: 'CurrencyConverter' }">환율 계산기</router-link> |
      <router-link :to="{ name: 'ArticleView' }">게시판</router-link> |
      <router-link v-if="userId" :to="{ name: 'ProFileView', params: { id: userId }}">프로필</router-link>

      <form @submit.prevent="logOut">
        <input type="submit" value="로그아웃"> | 
      </form>
    </nav>
    
    <nav v-else>
      <router-link :to="{ name: 'CurrencyConverter' }">환율 계산기</router-link> |
      <router-link :to="{ name: 'findNearestBank' }">가까운 은행 찾기</router-link> |
      <router-link :to="{ name: 'SignUpView' }">회원가입</router-link> |
      <router-link :to="{ name: 'LoginView' }">로그인</router-link> |
      <router-link :to="{ name: 'ArticleView' }">게시판</router-link> 
    </nav>
  </div>

  <div>
    <router-view />
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useAuthStore } from './stores/auth';
import { ref, onMounted, computed, watch } from 'vue';
import axios from 'axios';

// 변수
const authStore = useAuthStore()
const userId = ref(null)

// 액션
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
    // console.log('getCurrentuser', response)
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

const isUserIdAvailable = computed(() => {
  return userId.value !== null && userId.value !== undefined;
});
</script>

<style scoped></style>
