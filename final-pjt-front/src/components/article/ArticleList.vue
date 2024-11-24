<template>
  <v-row>
    <v-col cols="12">
      <v-card elevation="3">
        <v-card-text class="pa-0">
          <v-table hover>
            <thead>
              <tr>
                <th class="text-center" width="80">번호</th>
                <th class="text-left">제목</th>
                <th class="text-center" width="120">작성자</th>
                <th class="text-center" width="150">작성일</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(article, index) in articles"
                :key="article.id"
                @click="$emit('article-click', article.id)"
                class="article-row"
              >
                <td class="text-center">{{ articles.length - index }}</td>
                <td>
                  <div class="d-flex align-center">
                    <span class="text-subtitle-1">{{ article.title }}</span>
                    <v-chip
                      v-if="isNewArticle(article.created_at)"
                      color="error"
                      size="x-small"
                      class="ml-2"
                    >
                      NEW
                    </v-chip>
                  </div>
                </td>
                <td class="text-center">{{ article.user.last_name+article.user.first_name }}</td>
                <td class="text-center">{{ article.created_at.slice(0,10) }}</td>
              </tr>
            </tbody>
          </v-table>
          
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>


  
</template>

<script setup>
defineProps({
  articles: {
    type: Array,
    required: true
  }
})


const isNewArticle = (dateString) => {
  const articleDate = new Date(dateString)
  const now = new Date()
  const diffTime = now - articleDate
  const diffHours = diffTime / (1000 * 60 * 60)
  return diffHours <= 24
}
</script>

<style scoped>
.article-row {
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.article-row:hover {
  background-color: var(--v-hover-base, #f5f5f5) !important;
}

.v-table {
  border-radius: 8px;
}

.v-table thead tr th {
  font-size: 0.95rem;
  font-weight: 600;
  background-color: #f8f9fa;
  text-transform: none;
  letter-spacing: 0;
}

.v-table tbody tr td {
  padding: 12px 16px;
}
</style> 