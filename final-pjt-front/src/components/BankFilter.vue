<template>
  <div>
    <select v-model="region" @change="updateFilter">
      <option value="">광역시/도</option>
      <option v-for="r in regions" :key="r" :value="r">{{ r }}</option>
    </select>
    <select v-model="city" @change="updateFilter">
      <option value="">시/군/구</option>
      <option v-for="c in cities" :key="c" :value="c">{{ c }}</option>
    </select>
    <select v-model="brand" @change="updateFilter">
      <option value="">은행 브랜드</option>
      <option v-for="b in brands" :key="b" :value="b">{{ b }}</option>
    </select>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const regions = ['서울특별시', '경기도', '부산광역시'] // 예시 데이터
const cities = ['강남구', '중구', '서구'] // 예시 데이터
const brands = ['국민은행', '우리은행', '하나은행'] // 예시 데이터

const region = ref('')
const city = ref('')
const brand = ref('')

const emit = defineEmits(['filter-change'])

// 필터 변경 이벤트
function updateFilter() {
  emit('filter-change', {
    region: region.value,
    city: city.value,
    brand: brand.value,
  })
}
</script>

<style scoped>
select {
  margin: 0 10px;
}
</style>
