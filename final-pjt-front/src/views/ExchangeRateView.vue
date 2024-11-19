<template>
  <div>
    환율 계산기
  </div>
</template>

<script setup>
import { useExchangeRateStore } from '@/stores/exchangeRate';

const store = useExchangeRateStore()

store.getExchangeRate()

</script>

<style scoped>

</style>