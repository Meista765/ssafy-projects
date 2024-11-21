<template>
  <div>
    <h1>게시판</h1>
    <hr>
    <ArticleList/>
    <RouterLink :to="{ name: 'CreateView' }">게시글 생성</RouterLink>
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleComponent/ArticleList.vue';
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/article';
import { RouterLink } from 'vue-router';

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>

</style>