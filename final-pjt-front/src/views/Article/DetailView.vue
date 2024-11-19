<template>
  <div>
    <h1>게시글 상세</h1>
    {{ article }}
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useArticleStore } from '@/stores/article';
import { useRoute } from 'vue-router';

const route = useRoute()
const articleStore = useArticleStore()
const article = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: `${articleStore.API_URL}/articles/${route.params.id}/`
  })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<style scoped>

</style>