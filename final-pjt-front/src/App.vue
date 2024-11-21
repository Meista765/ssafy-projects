<template>
  <div>
    <nav v-if="authStore.isLogin">
      <form @submit.prevent="logOut">
        <router-link :to="{ name: 'CurrencyConverter' }">환율 계산기</router-link> |

        <input type="submit" value="로그아웃"> | 
        <router-link :to="{ name: 'ArticleView' }">게시판</router-link> 
      </form>
    </nav>
    
    <nav v-else>
      <router-link :to="{ name: 'CurrencyConverter' }">환율 계산기</router-link> |
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

const authStore = useAuthStore()

const logOut = function () {
  authStore.logOut()
}

</script>

<style scoped></style>
