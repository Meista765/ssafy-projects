<template>
  <v-container>
    <v-card class="mx-auto mt-6">
      <v-card-title class="text-h4 pa-4">
        {{ articleStore.article?.title }}
      </v-card-title>

      <v-card-subtitle class="pa-4">
        <v-row no-gutters align="center" justify="space-between">
          <v-row no-gutters align="center">
            <v-col cols="auto">
              <div class="mr-3">
                <v-icon icon="mdi-account" class="mr-1"></v-icon>
                <span class="mr-3">
                  {{ articleStore.article?.username }}
                </span>
                <v-icon icon="mdi-clock-outline" class="mr-1"></v-icon>
                <span class="mr-3">
                  {{ formatDate(articleStore.article?.created_at) }}
                </span>
              </div>
            </v-col>
          </v-row>

          <v-col cols="auto" v-if="isAuthor">
            <v-btn
              color="primary"
              variant="text"
              density="comfortable"
              @click="startEditingArticle"
            >
              수정
            </v-btn>
            <v-btn
              color="error"
              variant="text"
              density="comfortable"
              @click="deleteArticle"
            >
              삭제
            </v-btn>
          </v-col>
        </v-row>
      </v-card-subtitle>

      <v-divider></v-divider>

      <v-card-text class="pa-4 text-body-1">
        <div v-if="!isEditingArticle">
          {{ articleStore.article?.content }}
        </div>
        <div v-else>
          <v-textarea
            v-model.trim="updatedArticleContent"
            label="내용"
            rows="5"
          ></v-textarea>
        </div>
      </v-card-text>

      <v-card-actions class="pa-4">
        <v-spacer></v-spacer>
        <div v-if="!isEditingArticle">
          <v-btn
            color="primary"
            variant="outlined"
            @click="router.push({ name: 'ArticleView' })"
          >
            목록으로
          </v-btn>
        </div>
        <div v-else>
          <v-btn
            color="primary"
            variant="outlined"
            @click="updateArticle(articleStore.article.id)"
          >
            수정
          </v-btn>
          <v-btn color="grey" class="ml-2" @click="cancelArticleEdit">
            취소
          </v-btn>
        </div>
      </v-card-actions>
    </v-card>

    <v-card class="mt-6">
      <v-card-title class="text-h5">댓글 창</v-card-title>
      <v-card-subtitle
        >댓글 수: {{ articleStore.article?.comment_count }}</v-card-subtitle
      >

      <v-card-text>
        <v-list v-if="articleStore.article?.comment?.length > 0">
          <template
            v-for="(com, index) in articleStore.article.comment"
            :key="com.id"
          >
            <v-list-item
              :class="index % 2 === 0 ? 'bg-grey-lighten-4' : ''"
              rounded="lg"
              class="mb-2"
            >
              <div class="d-flex justify-space-between align-center w-100">
                <div class="flex-grow-1">
                  <div v-if="editingCommentId !== com.id">
                    <div class="text-body-1">{{ com.content }}</div>
                    <div class="text-caption text-grey">{{ com.username }}</div>
                  </div>
                  <div v-else class="w-100">
                    <v-textarea
                      v-model="updatedCommentContent"
                      label="댓글 수정"
                      rows="2"
                      variant="outlined"
                      density="comfortable"
                      class="mt-2 mb-2"
                      hide-details
                    ></v-textarea>
                  </div>
                </div>

                <div class="ml-4">
                  <template
                    v-if="com.user_id === userId && editingCommentId !== com.id"
                  >
                    <v-btn
                      variant="text"
                      density="comfortable"
                      color="primary"
                      @click="startEditingComment(com.id, com.content)"
                    >
                      수정
                    </v-btn>
                    <v-btn
                      variant="text"
                      density="comfortable"
                      color="error"
                      @click="deleteComment(com.id)"
                    >
                      삭제
                    </v-btn>
                  </template>
                  <template v-if="editingCommentId === com.id">
                    <v-btn
                      variant="text"
                      density="comfortable"
                      color="primary"
                      @click="updateComment(com.id)"
                    >
                      완료
                    </v-btn>
                    <v-btn
                      variant="text"
                      density="comfortable"
                      color="error"
                      @click="cancelCommentEdit"
                    >
                      취소
                    </v-btn>
                  </template>
                </div>
              </div>
            </v-list-item>
            <v-divider
              v-if="index !== articleStore.article.comment.length - 1"
              class="my-2"
            ></v-divider>
          </template>
        </v-list>
        <div v-else>
          <p>아직 댓글이 없습니다.</p>
        </div>
      </v-card-text>

      <v-card-actions v-if="!editingCommentId">
        <v-form @submit.prevent="createComment" class="w-100 pa-3">
          <v-textarea
            v-model.trim="content"
            label="댓글을 작성해주세요"
            rows="2"
            variant="outlined"
            density="comfortable"
            required
          ></v-textarea>
          <div class="d-flex justify-end">
            <v-btn type="submit" color="primary" class="mt-2">
              댓글 생성
            </v-btn>
          </div>
        </v-form>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup>
import axios from 'axios'
import { onMounted, computed, watch, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import { useAuthStore } from '@/stores/auth'

// 변수
const route = useRoute()
const router = useRouter()
const articleStore = useArticleStore()
const authStore = useAuthStore()
const userId = ref(null)

const content = ref('')
const isEditingArticle = ref(false) // 수정 중인 확인하는 변수
const editingCommentId = ref('')
const updatedArticleContent = ref('')
const updatedCommentContent = ref('')
const isAuthor = computed(() => {
  return articleStore.article?.user === userId.value
})

// 함수

// 로그인 유저 정보 조회
const getCurrentUser = async function () {
  try {
    const res = await axios({
      method: 'get',
      url: `${authStore.BACKEND_SERVER_URL}/user/`,
      headers: {
        Authorization: `Token ${authStore.token}`,
      },
    })
    console.log(res)
    userId.value = res.data.id
  } catch (error) {
    console.error('사용자 정보 조회 실패:', error)
  }
}

// 게시글 수정
const startEditingArticle = function () {
  isEditingArticle.value = true
  updatedArticleContent.value = articleStore.article.content
}

const cancelArticleEdit = function () {
  isEditingArticle.value = false
  updatedArticleContent.value = ''
}

const updateArticle = async function (articleId) {
  try {
    await axios({
      method: 'put',
      url: `${articleStore.BACKEND_SERVER_URL}/articles/${articleId}/`,
      data: { content: updatedArticleContent.value },
      headers: { Authorization: `Token ${authStore.token}` },
    })
    await articleStore.getArticle(route.params.id)
    isEditingArticle.value = false
  } catch (error) {
    console.error('게시글 수정 실패:', error)
  }
}

const deleteArticle = async () => {
  if (confirm('정말 삭제하시겠습니까?')) {
    await articleStore.deleteArticle(route.params.id)
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
    minute: '2-digit',
  })
}

// 댓글

// 댓글 생성
const createComment = async () => {
  try {
    await axios({
      method: 'post',
      url: `${articleStore.BACKEND_SERVER_URL}/articles/${route.params.id}/comments/`,
      data: { content: content.value },
      headers: { Authorization: `Token ${authStore.token}` },
    })
    await articleStore.getArticle(route.params.id)
    content.value = ''
  } catch (error) {
    console.error('댓글 생성 실패:', error)
  }
}

// 댓글 수정 시작
const startEditingComment = (commentId, currentContent) => {
  editingCommentId.value = commentId
  updatedCommentContent.value = currentContent
}

// 댓글 수정 취소
const cancelCommentEdit = () => {
  editingCommentId.value = null
  updatedCommentContent.value = ''
}

// 댓글 업데이트
const updateComment = async (commentId) => {
  try {
    await axios({
      method: 'put',
      url: `${articleStore.BACKEND_SERVER_URL}/articles/comments/${commentId}/`,
      data: { content: updatedCommentContent.value },
      headers: { Authorization: `Token ${authStore.token}` },
    })
    await articleStore.getArticle(route.params.id)
    editingCommentId.value = null
    updatedCommentContent.value = ''
  } catch (error) {
    console.error('댓글 수정 실패:', error)
  }
}

// 댓글 삭제
const deleteComment = async (commentId) => {
  if (!confirm('댓글을 삭제하시겠습니까?')) return

  try {
    await axios({
      method: 'delete',
      url: `${articleStore.BACKEND_SERVER_URL}/articles/comments/${commentId}/`,
      headers: { Authorization: `Token ${authStore.token}` },
    })
    await articleStore.getArticle(route.params.id)
  } catch (error) {
    console.error('댓글 삭제 실패:', error)
  }
}

onMounted(() => {
  articleStore.getArticle(route.params.id)
})

onMounted(getCurrentUser)

// watch(() => route.params.id, articleStore.getArticle(route.params.id))
</script>
