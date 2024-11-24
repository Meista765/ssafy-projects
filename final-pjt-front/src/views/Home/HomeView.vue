<template>
  <v-container class="fill-height">
    <v-row class="text-center mb-8">
      <v-col>
        <h1 class="text-h3 font-weight-bold mb-4">금융 서비스에 오신 것을 환영합니다</h1>
        <p class="text-subtitle-1">모든 금융 서비스를 한 곳에서 편리하게 이용하세요</p>
      </v-col>
    </v-row>

    <v-row class="flex-grow-1 align-center">
      <v-col cols="12" sm="6" md="3" class="d-flex">
        <v-card to="/currency-converter" class="flex-grow-1 d-flex flex-column align-center justify-center">
          <v-icon size="64" color="primary" class="mb-4">mdi-currency-usd</v-icon>
          <h2 class="text-h6">환율 계산기</h2>
          <p class="text-caption text-center">실시간 환율 정보 확인</p>
        </v-card>
      </v-col>

      <v-col cols="12" sm="6" md="3" class="d-flex">
        <v-card to="/find-nearest-bank" class="flex-grow-1 d-flex flex-column align-center justify-center">
          <v-icon size="64" color="primary" class="mb-4">mdi-map-marker</v-icon>
          <h2 class="text-h6">가까운 은행 찾기</h2>
          <p class="text-caption text-center">주변 은행 위치 확인</p>
        </v-card>
      </v-col>

      <v-col cols="12" sm="6" md="3" class="d-flex">
        <v-card to="/financial-product" class="flex-grow-1 d-flex flex-column align-center justify-center">
          <v-icon size="64" color="primary" class="mb-4">mdi-bank</v-icon>
          <h2 class="text-h6">금융상품 정보</h2>
          <p class="text-caption text-center">다양한 금융상품 비교</p>
        </v-card>
      </v-col>

      <v-col cols="12" sm="6" md="3" class="d-flex">
        <v-card to="/article" class="flex-grow-1 d-flex flex-column align-center justify-center">
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
</script>

<style scoped>
.v-card {
  transition: transform 0.2s;
  cursor: pointer;
  min-height: 250px;
}

.v-card:hover {
  transform: translateY(-5px);
}

@media (min-width: 960px) {
  .v-container {
    height: calc(100vh - 144px); /* 앱바(64px)와 푸터(80px) 높이를 제외 */
  }
}
</style>