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
                :items="currencyItems"
                item-title="name"
                item-value="ticker"
                label="통화 선택"
                @update:model-value="onInputForeignCurrency"
                return-object
              ></v-select>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model.number="foreignCurrency"
                :label="`금액 (${selectedCurrency?.symbol || ''})`"
                type="number"
                @input="onInputForeignCurrency"
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
              <v-alert type="info" variant="tonal" density="comfortable">
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
import axios from 'axios'
import { ref, computed, onMounted } from 'vue'
import currencyMap from '@/assets/currency-map.json'

const EXCHANGE_RATE_API_KEY = import.meta.env.VITE_EXCHANGE_RATE_API_KEY
const EXCHANGE_RATE_SERVER_URL = import.meta.env.VITE_EXCHANGE_RATE_SERVER_URL
const baseCurrency = 'KRW'

const selectedCurrency = ref(null) // 현재 선택된 통화
const foreignCurrency = ref(0) // 대상 통화의 값
const krwCurrency = ref(0) // 원화의 값
const conversionRates = ref(null) // 환율 데이터

const currencyItems = computed(() => {
  return Object.entries(currencyMap).map(([ticker, [name, symbol]]) => ({
    ticker,
    name,
    symbol,
  }))
})

const rate = computed(() => {
  return conversionRates.value[selectedCurrency.value?.ticker]
})

const onInputForeignCurrency = () => {
  krwCurrency.value = Math.round(foreignCurrency.value / rate.value)
}

const onInputKrwCurrency = () => {
  foreignCurrency.value = Math.round(krwCurrency.value * rate.value)
}

onMounted(async () => {
  await axios({
    method: 'get',
    url: `${EXCHANGE_RATE_SERVER_URL}/${EXCHANGE_RATE_API_KEY}/latest/${baseCurrency}`,
  })
    .then((response) => {
      conversionRates.value = response.data.conversion_rates
    })
    .then(() => {
      selectedCurrency.value = currencyItems.value.find(
        (currency) => currency.ticker === 'USD'
      )
    })
    .catch((error) => {
      console.error('환율 데이터를 가져오는 중 에러 발생:', error)
    })
})
</script>

<style scoped></style>
