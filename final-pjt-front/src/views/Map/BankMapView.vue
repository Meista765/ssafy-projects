<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h1 class="text-h4 mb-4">가까운 은행 찾기</h1>
      </v-col>
    </v-row>
    <v-row>
      <!-- 필터 섹션 -->
      <v-col cols="12" md="4">
        <v-card>
          <v-card-text>
            <BankFilter @search="handleSearch" />
          </v-card-text>
        </v-card>
      </v-col>
      <!-- 지도 섹션 -->
      <v-col cols="12" md="8">
        <v-card>
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
import { ref } from 'vue'

const searchParams = ref({})

const handleSearch = (params) => {
  searchParams.value = params
}
</script>

<style scoped></style>
