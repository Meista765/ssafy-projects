<template>
  <!-- 검색 폼 -->
  <form @submit.prevent="handleSearch">
    <div class="d-flex flex-column">
      <!-- 광역시/도 선택 -->
      <label for="province">광역시 / 도</label>
      <select v-model="selectedProvince" name="province" id="province">
        <option v-for="(cities, province) in districts" :key="province" :value="province">
          {{ province }}
        </option>
      </select>

      <!-- 시/군/구 선택 -->
      <label for="city">시 / 군 / 구</label>
      <select v-model="selectedCity" name="city" id="city" :disabled="!selectedProvince">
        <option v-for="city in districts[selectedProvince]" :key="city" :value="city">
          {{ city }}
        </option>
      </select>

      <!-- 은행 브랜드 선택 -->
      <label for="brand">은행 브랜드</label>
      <select v-model="selectedBank" name="brand" id="brand">
        <option v-for="bank in banksList.banks" :key="bank" :value="bank">
          {{ bank }}
        </option>
      </select>
      <button type="submit">찾기</button>
    </div>
  </form>
</template>

<script setup>
import districts from '@/assets/district.json'
import banksList from '@/assets/banks-list.json'
import { ref, watch, onMounted } from 'vue'

const emit = defineEmits(['search'])

// 초기값 상수 정의 
const DEFAULT_PROVINCE = Object.keys(districts)[0] // districts의 첫 번째 key(시/도)
const DEFAULT_CITY = districts[DEFAULT_PROVINCE][0] // 첫 번째 시/도의 첫 번째 구/군
const DEFAULT_BANK = banksList.banks[0] // 첫 번째 은행

// 선택된 값을 저장할 반응형 변수들
const selectedProvince = ref(DEFAULT_PROVINCE)
const selectedCity = ref(DEFAULT_CITY)
const selectedBank = ref(DEFAULT_BANK)

// province가 변경될 때 해당 province의 첫 번째 city로 설정
watch(selectedProvince, (newProvince) => {
  selectedCity.value = districts[newProvince][0]
})

// 검색 핸들러
const handleSearch = () => {
  emit('search', {
    province: selectedProvince.value,
    city: selectedCity.value,
    bank: selectedBank.value
  })
}
</script>

<style scoped></style>
