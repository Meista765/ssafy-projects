<template>
  <div>
    <h1>게시판 목록</h1>
    <hr>
    <ArtcielListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
    
  </div>
</template>

<script setup>
import ArtcielListItem from './ArtcielListItem.vue';
import { useArticleStore } from '@/stores/article';

const store = useArticleStore()
</script>

<style scoped>

</style>