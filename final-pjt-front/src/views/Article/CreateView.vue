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
import { ref, onMounted } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import axios from 'axios'

const title = ref('')
const content = ref('')
const router = useRouter()
const articleStore = useArticleStore()
const authStore = useAuthStore()

// 로그인 상태 확인
onMounted(() => {
  if (!authStore.isLogin) {
    alert('로그인이 필요한 서비스입니다.')
    router.push({ name: 'LoginView' })
  }
})

const createArticle = async function () {
  if (!title.value || !content.value) return
  
  if (!authStore.isLogin) {
    alert('로그인이 필요한 서비스입니다.')
    router.push({ name: 'LoginView' })
    return
  }

  try {
    await axios({
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
    router.push({name: 'ArticleView'})
  } catch (error) {
    console.error('게시글 생성 실패:', error)
    if (error.response?.status === 401) {
      alert('로그인이 필요한 서비스입니다.')
      router.push({ name: 'LoginView' })
    } else {
      alert('게시글 작성에 실패했습니다.')
    }
  }
}
</script>

<style scoped>

</style>