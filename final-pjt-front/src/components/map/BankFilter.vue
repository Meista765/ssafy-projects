<template>
  <form @submit.prevent="handleSearch">
    <v-container>
      <!-- 광역시/도 선택 -->
      <v-select
        v-model="selectedProvince"
        :items="Object.keys(districts)"
        label="광역시 / 도"
        variant="outlined"
        density="comfortable"
        class="mb-4"
        bg-color="surface"
      ></v-select>

      <!-- 시/군/구 선택 -->
      <v-select
        v-model="selectedCity"
        :items="districts[selectedProvince]"
        label="시 / 군 / 구"
        variant="outlined"
        density="comfortable"
        class="mb-4"
        :disabled="!selectedProvince"
        bg-color="surface"
      ></v-select>

      <!-- 은행 브랜드 선택 -->
      <v-select
        v-model="selectedBank"
        :items="banksList.banks"
        label="은행 브랜드"
        variant="outlined"
        density="comfortable"
        class="mb-4"
        bg-color="surface"
      ></v-select>

      <v-btn
        type="submit"
        color="primary"
        block
        class="mt-2"
        :elevation="2"
      >
        찾기
      </v-btn>
    </v-container>
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
