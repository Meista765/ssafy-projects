<template>
  <div>
    <h1>게시글 상세</h1>
    <hr>

    <div v-if="article && Object.keys(article).length > 0">
      <h2>제목 : {{ article.title }}</h2>
      <p>작성자 : {{ article.username }}</p>
      <p v-if="!isEditingArticle">{{ article.content }}</p>

      <!-- 게시글 수정 -->
      <div v-else>
        <textarea v-model.trim="updatedArticleContent"></textarea>
        <button @click="updateArticle(article.id)">수정 완료</button>
        <button @click="cancelArticleEdit">취소</button>
      </div>

      <!-- 게시글 버튼 -->
      <div v-if="article.user === userId && !isEditingArticle">
        <button @click="startEditingArticle">수정하기</button>
        <button @click="deleteArticle(article.id)">삭제하기</button>
      </div>
      
      <hr>

      <!-- 댓글 섹션 -->
      <h2>댓글 창</h2>
      <p>댓글 수: {{ article.comment_count }}</p>

      <!-- 댓글 리스트 -->
      <ul v-if="article.comment.length > 0">
        <li v-for="com in article.comment" :key="com.id">
          <div v-if="editingCommentId !== com.id">
            <p>{{ com.username }}: {{ com.content }}</p>
            <!-- 댓글 버튼 -->
            <div v-if="com.user_id === userId">
              <button @click="startEditingComment(com.id, com.content)">수정하기</button>
              <button @click="deleteComment(com.id)">삭제하기</button>
            </div>
          </div>
          <!-- 댓글 수정 -->
          <div v-else>
            <textarea v-model="updatedCommentContent"></textarea>
            <button @click="updateComment(com.id)">수정 완료</button>
            <button @click="cancelCommentEdit">취소</button>
          </div>
        </li>
      </ul>
      <div v-else>
        <p>아직 댓글이 없습니다.</p>
      </div>
      
      <div> 
        <h3>댓글을 작성해주세요</h3>
        <form @submit.prevent="createComment">
          <label for="content">작성란</label> <br>
          <textarea id="content" v-model.trim="content"></textarea>
          <input type="submit" value="댓글 생성">
        </form>
      
      </div>


    </div>
    
    <div v-else>
      <p>로딩 중...</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';
import { useArticleStore } from '@/stores/article';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
// 상태 관리
const route = useRoute();
const router = useRouter()
const articleStore = useArticleStore();
const authStore = useAuthStore()

const article = ref({});
const content = ref(null)
const userId = ref(null)

const isEditingArticle = ref(false)       // 수정 중인 확인하는 변수
const editingCommentId = ref('')      
const updatedArticleContent = ref('')
const updatedCommentContent = ref('')

// 로그인 유저 정보 조회
const getCurrentUser = function () {
  axios({
    method:'get',
    url: `${articleStore.API_URL}/user/`,
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  })
    .then((res) => {
      console.log(res.data)
      userId.value = res.data.id
    })
    .catch((err) => {
      console.log(err)
    })
}

// 상세 게시글 조회 함수
const getArticle = () => {
  axios({
    method: 'get',
    url: `${articleStore.API_URL}/articles/${route.params.id}/`
  })
    .then((res) => {
      console.log(res.data)
      article.value = res.data;
    })
    .catch((err) => {
      console.error("Failed to get article:", err);
    });
};

// 게시글 삭제 함수
const deleteArticle = function (articleId) {
  axios({
    method:'delete',
    url: `${articleStore.API_URL}/articles/${articleId}/`,
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  })
    .then((res) => {
      console.log('게시글 삭제 성공', res)
      router.push({ name: 'ArticleView'})  // 나중에 메인 페이지 생기면 수정
    })
    .catch((err) => {
      console.log(err)
    })
  
}

// 게시글 수정
const startEditingArticle = function () {
  isEditingArticle.value = true
  updatedArticleContent.value = article.value.content
}

const cancelArticleEdit = function () {
  isEditingArticle.value = false
  updatedArticleContent.value = ''
}

const updateArticle = function (articleId) {
  axios({
    method: 'put',
    url: `${articleStore.API_URL}/articles/${articleId}/`,
    data: {content: updatedArticleContent.value},
    headers: {Authorization: `Token ${authStore.token}`}
  })
    .then((res) => {
      getArticle()
      isEditingArticle.value = false
    })
    .catch((err) => {
      console.log(err)
    })
}


// 댓글 생성 
const createComment = function () {
  axios({
    method:'post',
    url: `${articleStore.API_URL}/articles/${route.params.id}/comments/`,
    data:{
      content:content.value
    },
    headers:{
      Authorization: `Token ${authStore.token}`
    }
  })
    .then((res) => {
      console.log(res)
      getArticle()
      content.value = null
    })
    .catch((err) => {
      console.log(err)
    })
}




// 댓글 삭제 함수
const deleteComment = function (commentId) {
  axios({
    method:'delete',
    url: `${articleStore.API_URL}/articles/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  })
    .then((res) => {
      console.log('댓글 삭제 성공',res)
      getArticle()
    })
    .catch((err) => {
      console.log(commentId)
      console.log(err)
    })
}

// 댓글 수정 함수
const startEditingComment = function (commentId, currentContent) {
  editingCommentId.value = commentId
  updatedCommentContent.value = currentContent
}

const cancelCommentEdit = function () {
  editingCommentId.value = null
  updatedCommentContent.value = ''
}

const updateComment = function (commentId) {
  axios({
    method: 'put',
    url: `${articleStore.API_URL}/articles/comments/${commentId}/`,
    data: {
      content: updatedCommentContent.value
    },
    headers: {Authorization: `Token ${authStore.token}`}
  })
    .then((res) => {
      getArticle()
      editingCommentId.value = null
      updatedCommentContent.value = ''
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
}

onMounted(getArticle);
onMounted(getCurrentUser)
watch(() => route.params.id, getArticle);

</script>