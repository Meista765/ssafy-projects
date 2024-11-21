<template>
  <div>
    <h1>글 작성하기</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model.trim="title">
      </div>

      <div>
        <label for="content">내용 : </label>
        <textarea id="content" v-model.trim="content"></textarea>
      </div>

      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/article';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import axios from 'axios';

const title = ref(null)
const content = ref(null)
const router = useRouter()
const articleStore = useArticleStore()
const authStore = useAuthStore()

const createArticle = function () {
  axios({
    method:'post',
    url:`${articleStore.API_URL}/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  })
    .then((res) => {
      console.log(res.data)
      router.push({name:'ArticleView'})
    })
    .catch((err) => {
      console.log(err)
    })
}


</script>

<style scoped>

</style>