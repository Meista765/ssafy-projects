<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <h1 class="text-h4 mb-6">환율계산기</h1>
        
        <v-card class="pa-4">
          <v-row>
            <v-col cols="12">
              <v-select
                v-model="selectedCurrency"
                :items="store.exchangeRates"
                item-title="cur_nm"
                item-value="cur_unit"
                label="통화 선택"
                @update:model-value="handleSelection"
                return-object
              ></v-select>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model.number="targetCurrency"
                :label="`금액 (${selectedCurrency?.cur_unit || ''})`"
                type="number"
                @input="onInputTargetCurrency"
                variant="outlined"
                density="comfortable"
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model.number="krwCurrency"
                label="원화 (₩)"
                type="number"
                @input="onInputKrwCurrency"
                variant="outlined"
                density="comfortable"
              ></v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12">
              <v-alert
                type="info"
                variant="tonal"
                density="comfortable"
              >
                * 엔화, 인도네시아 루피아는 100 단위, 나머지는 모두 1 단위
              </v-alert>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
