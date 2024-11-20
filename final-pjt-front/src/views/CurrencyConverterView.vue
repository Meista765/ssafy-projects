<template>
  <div>
    <h1>환율계산기</h1>
    <div>
      <select
        name="currency-selection"
        id="currency-selection"
        v-model="selectedCurrency"
        @change="handleSelection"
      >
        <option
          v-for="exchangeRate in store.exchangeRates"
          :key="exchangeRate.cur_unit"
          :value="exchangeRate"
        >
          {{ exchangeRate.cur_nm }} ({{ exchangeRate.cur_unit }})
        </option>
      </select>
      <input
        type="number"
        name="target-currency"
        id="target-currency"
        v-model.number="targetCurrency"
        @input="onInputTargetCurrency"
      />
      <span>{{ selectedCurrency?.cur_unit }}</span>
    </div>
    <div>
      <input
        type="number"
        name="krw-currency"
        id="krw-currency"
        v-model.number="krwCurrency"
        @input="onInputKrwCurrency"
      />
      <span>₩</span>
    </div>
    <p>* 엔화, 인도네시아 루피아는 100 단위, 나머지는 모두 1 단위</p>
  </div>
</template>

<script setup>
import { useExchangeRateStore } from '@/stores/exchangeRate'
import { ref, computed, watch, onMounted } from 'vue'
import {} from 'vue-router'

// ===== 내장 모듈 =====
const store = useExchangeRateStore()

// ===== 변수 =====
const selectedCurrency = ref(null) // 현재 선택된 옵션
const targetCurrency = ref(0) // 대상 통화의 값
const krwCurrency = ref(0) // 원화의 값

// ===== computed 변수 =====
const dealBas = computed(() => {
  return selectedCurrency.value?.kftc_deal_bas_r || 1
})

// ===== 이벤트 핸들러 =====
const onInputTargetCurrency = () => {
  krwCurrency.value = targetCurrency.value * dealBas.value
}

const onInputKrwCurrency = () => {
  targetCurrency.value = krwCurrency.value / dealBas.value
}

// ===== 함수 =====
const handleSelection = () => {
  console.log(`Selected value: ${selectedCurrency.value?.cur_nm}`)
  console.log(`Deal base rate: ${dealBas.value}`)
}

// ===== 와쳐 =====
watch(
  /**
   * 기본 선택 옵션을 미국 달러로 변경하며 빈 선택지를 없앰
   */
  () => store.exchangeRates,
  (newRates) => {
    if (newRates.length > 0 && !selectedCurrency.value) {
      selectedCurrency.value = newRates.find(
        (rate) => rate.cur_nm === '미국 달러'
      )
    }
  },
  { immediate: true }
)

// API에서 데이터 수집
onMounted(async () => {
  try {
    await store.getExchangeRate() // 데이터를 Prefetch
  } catch (error) {
    console.error('환율 데이터를 가져오는 중 에러 발생:', error)
  }
})
</script>

<style scoped></style>
