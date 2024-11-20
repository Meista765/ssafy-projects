<template>
  <div>
    <h1>게시글 상세</h1>
    <hr>
    <div v-if="article && Object.keys(article).length > 0">
      <h2>제목 : {{ article.title }}</h2>
      <p>작성자 : {{ article.username }}</p>
      <p>내용 : {{ article.content }}</p>
      <hr>
      <h3>댓글 창</h3>
      <p>댓글 수 : {{ article.comment_count }}</p>
      
      <div v-if="article.comment.length > 0">
        <ul>
          <li v-for="com in article.comment">
            {{ com.username }}: {{ com.content }}
          </li>
        </ul>
      </div>
      <div v-else>
        <p>아직 댓글이 없습니다.</p>
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
import { useRoute } from 'vue-router';

// 상태 관리
const route = useRoute();
const articleStore = useArticleStore();
const article = ref({}); // 빈 객체로 초기화

// 데이터 로드 함수
const getArticle = () => {
  axios({
    method: 'get',
    url: `${articleStore.API_URL}/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data;
    })
    .catch((err) => {
      console.error("Failed to get article:", err);
    });
};


onMounted(getArticle);
watch(() => route.params.id, getArticle);
</script>
