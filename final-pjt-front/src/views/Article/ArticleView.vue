<template>
  <v-container class="py-8">
    <ArticleHeader />
    <ArticleList 
      :articles="store.articles"
      @article-click="navigateToDetail"
    />
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useRouter } from 'vue-router'
import ArticleHeader from '@/components/article/ArticleHeader.vue'
import ArticleList from '@/components/article/ArticleList.vue'

const store = useArticleStore()
const router = useRouter()

onMounted(() => {
  store.getArticles()
})

const navigateToDetail = (id) => {
  router.push({ name: 'DetailView', params: { id } })
}
</script>