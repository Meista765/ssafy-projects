<template>
  <v-container>
    <v-card class="mx-auto mt-6">
      <v-card-title class="text-h4 pa-4">
        {{ store.article?.title }}
      </v-card-title>

      <v-card-subtitle class="pa-4">
        <v-row no-gutters align="center">
          <v-col cols="auto" class="mr-4">
            <v-icon icon="mdi-account" class="mr-1"></v-icon>
            {{ store.article?.user }}
          </v-col>
          <v-col cols="auto">
            <v-icon icon="mdi-clock-outline" class="mr-1"></v-icon>
            {{ formatDate(store.article?.created_at) }}
          </v-col>
        </v-row>
      </v-card-subtitle>

      <v-divider></v-divider>

      <v-card-text class="pa-4 text-body-1">
        {{ store.article?.content }}
      </v-card-text>

      <v-card-actions class="pa-4">
        <v-spacer></v-spacer>
        <v-btn
          color="primary"
          variant="outlined"
          @click="router.push({ name: 'ArticleView' })"
        >
          목록으로
        </v-btn>
        <v-btn
          v-if="isAuthor"
          color="error"
          class="ml-2"
          @click="deleteArticle"
        >
          삭제
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup>
import { onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/article';
import { useAuthStore } from '@/stores/auth';

const route = useRoute()
const router = useRouter()
const store = useArticleStore()
const authStore = useAuthStore()

const isAuthor = computed(() => {
  return store.article?.user === authStore.currentUser
})

onMounted(() => {
  store.getArticle(route.params.id)
})

const deleteArticle = async () => {
  if (confirm('정말 삭제하시겠습니까?')) {
    await store.deleteArticle(route.params.id)
    router.push({ name: 'ArticleView' })
  }
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>