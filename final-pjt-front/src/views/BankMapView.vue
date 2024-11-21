<template>
  <div>
    <p>가까운 은행 찾기</p>
    <BankFilter @search="handleSearch" />
    <KakaoMap :searchParams="searchParams" />
  </div>
</template>

<script setup>
import KakaoMap from '@/components/KakaoMap.vue'
import BankFilter from '@/components/BankFilter.vue'
import { ref } from 'vue'

const searchParams = ref({})

const handleSearch = (params) => {
  searchParams.value = params
}
</script>

<style scoped></style>
