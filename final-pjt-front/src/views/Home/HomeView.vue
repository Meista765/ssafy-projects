<template>
  <v-container class="d-flex flex-column">
    <!-- 환영 메시지 -->
    <ViewTitle title="Finders에 오신 것을 환영합니다" subtitle="모든 금융 서비스를 한 곳에서 편리하게 이용하세요"/>

    <!-- 카드 목록 -->
    <v-row class="flex-grow-1 align-center" gap="16">
      <!-- 카드 1 -->
      <v-col cols="12" sm="6" md="3" class="d-flex">
        <v-card to="/currency-converter" class="flex-grow-1 d-flex flex-column align-center justify-center card-custom">
          <v-icon size="64" color="primary" class="mb-4">mdi-currency-usd</v-icon>
          <h2 class="text-h6">환율 계산기</h2>
          <p class="text-caption text-center">실시간 환율 정보 확인</p>
        </v-card>
      </v-col>

      <!-- 카드 2 -->
      <v-col cols="12" sm="6" md="3" class="d-flex">
        <v-card to="/find-nearest-bank" class="flex-grow-1 d-flex flex-column align-center justify-center card-custom">
          <v-icon size="64" color="primary" class="mb-4">mdi-map-marker</v-icon>
          <h2 class="text-h6">가까운 은행 찾기</h2>
          <p class="text-caption text-center">주변 은행 위치 확인</p>
        </v-card>
      </v-col>

      <!-- 카드 3 -->
      <v-col cols="12" sm="6" md="3" class="d-flex">
        <v-card to="/financial-product" class="flex-grow-1 d-flex flex-column align-center justify-center card-custom">
          <v-icon size="64" color="primary" class="mb-4">mdi-bank</v-icon>
          <h2 class="text-h6">금융상품 정보</h2>
          <p class="text-caption text-center">다양한 금융상품 비교</p>
        </v-card>
      </v-col>

      <!-- 카드 4 -->
      <v-col cols="12" sm="6" md="3" class="d-flex">
        <v-card to="/articles" class="flex-grow-1 d-flex flex-column align-center justify-center card-custom">
          <v-icon size="64" color="primary" class="mb-4">mdi-forum</v-icon>
          <h2 class="text-h6">커뮤니티</h2>
          <p class="text-caption text-center">금융 정보 공유</p>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import '@mdi/font/css/materialdesignicons.css'
import ViewTitle from '@/components/common/ViewTitle.vue';
</script>

<style scoped>
.finders-shadow {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.v-container {
  /* 최대 너비를 설정하여 너무 넓어지는 것을 방지 */
  max-width: 1200px;
  margin: 0 auto; /* 중앙 정렬 */
  padding: 16px; /* 필요 시 패딩 추가 */
}

.v-row {
  /* 카드 목록을 중앙에 배치 */
  display: flex;
  flex-wrap: wrap;
}

.card-custom {
  /* 카드의 최소 높이를 설정 */
  min-height: 300px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.card-custom:hover {
  transform: translateY(-5px);
  box-shadow: 6px 6px 20px rgba(0, 0, 0, 0.2);
}

@media (min-width: 960px) {
  .v-container {
    height: auto; /* fill-height 대신 자동 높이 */
  }
}
</style>
