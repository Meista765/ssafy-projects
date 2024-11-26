<template>
  <v-container fluid>
    <ViewTitle title="가까운 은행 찾기" subtitle="내 주변 은행을 쉽고 빠르게 찾아보세요" />
    <v-row>
      <!-- 필터 섹션 -->
      <v-col cols="12" md="4">
        <v-card elevation="2">
          <v-card-text>
            <BankFilter @search="handleSearch" />
          </v-card-text>
        </v-card>
      </v-col>
      <!-- 지도 섹션 -->
      <v-col cols="12" md="8">
        <v-card elevation="2">
          <v-card-text>
            <KakaoMap :searchParams="searchParams" />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import KakaoMap from '@/components/map/KakaoMap.vue'
import BankFilter from '@/components/map/BankFilter.vue'
import ViewTitle from '@/components/common/ViewTitle.vue'

import { ref } from 'vue'

const searchParams = ref({})

const handleSearch = (params) => {
  searchParams.value = params
}
</script>

<style scoped>
.title-wrapper {
  padding: 2rem 0;
}

.subtitle {
  margin-top: 8px;
}
</style>
