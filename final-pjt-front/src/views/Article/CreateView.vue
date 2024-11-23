<template>
  <v-container class="py-8">
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card class="pa-6">
          <h1 class="text-h4 mb-6 text-center">글 작성하기</h1>
          
          <v-form @submit.prevent="createArticle">
            <v-text-field
              v-model="title"
              label="제목"
              variant="outlined"
              :rules="[v => !!v || '제목을 입력해주세요']"
              required
            ></v-text-field>

            <v-textarea
              v-model="content"
              label="내용"
              variant="outlined"
              :rules="[v => !!v || '내용을 입력해주세요']"
              required
              rows="10"
              class="mt-4"
            ></v-textarea>

            <v-row class="mt-4" justify="center">
              <v-col cols="auto">
                <v-btn
                  type="submit"
                  color="primary"
                  size="large"
                  prepend-icon="mdi-send"
                >
                  작성완료
                </v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import axios from 'axios'

const title = ref('')
const content = ref('')
const router = useRouter()
const articleStore = useArticleStore()
const authStore = useAuthStore()

const createArticle = function () {
  if (!title.value || !content.value) {
    return
  }

  axios({
    method: 'post',
    url: `${articleStore.BACKEND_SERVER_URL}/articles/`,
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
      router.push({name: 'ArticleView'})
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>