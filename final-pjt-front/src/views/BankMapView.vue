<template>
  <div>
    <h1>가까운 은행 찾기</h1>
    <BankFilter @filter-change="applyFilter" />
    <KakaoMap :filteredBanks="filteredBanks" />
    <BankList :banks="filteredBanks" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { loadBanks } from '@/api/kakao'

import KakaoMap from '@/components/KakaoMap.vue'
import BankFilter from '@/components/BankFilter.vue'
import BankList from '@/components/BankList.vue'

const banks = ref([]) // 전체 은행 리스트
const filteredBanks = ref([])

onMounted(async () => {
  try {
    banks.value = await loadBanks()
    filteredBanks.value = banks.value
  } catch (error) {
    console.error('Failed to load banks:', error)
    alert('은행 데이터를 불러오는데 실패했습니다. 나중에 다시 시도해주세요.')
  }
})

// // 필터링된 은행 계산
// const filteredBanks = computed(() => {
//   return banks.value.filter((bank) => {
//     const matchRegion =
//       (!filter.value.region || bank.region === filter.value.region) &&
//       (!filter.value.city || bank.city === filter.value.city)
//     const matchBrand = !filter.value.brand || bank.brand === filter.value.brand
//     return matchRegion && matchBrand
//   })
// })
</script>

<style scoped>
h1 {
  text-align: center;
  margin-bottom: 20px;
}
</style>
