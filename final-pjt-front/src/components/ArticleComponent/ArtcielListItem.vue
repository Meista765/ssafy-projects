<template>
  <div>
    <h2>제목 : {{ article.title }}</h2>
    <p>내용 : {{ article.content }}</p>
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
      자세히 보기
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
const props = defineProps({
  article:Object
})
</script>

<style scoped>

</style>