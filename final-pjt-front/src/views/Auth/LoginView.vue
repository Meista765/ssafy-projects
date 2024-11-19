<template>
  <div>
    <h1>LogIn</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password">passoword : </label>
      <input type="password" id="password" v-model.trim="password"><br>

      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';

const store = useAuthStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>

</style>