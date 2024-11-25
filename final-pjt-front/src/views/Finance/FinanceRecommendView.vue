<template>
  <div>
    <h1>추천페이지입니다.</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'; 
import axios from 'axios';


// 변수
const route = useRoute()



const userId = route.params.id

</script>

<style scoped>

</style>