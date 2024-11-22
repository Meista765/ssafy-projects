<template>
  <v-container>
    <h2 class="mb-5">금융상품 정보</h2>
    <FinancialProductTable />
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { useFinanceStore } from '@/stores/financialProduct'
import FinancialProductTable from '@/components/finance/FinancialProductTable.vue'

const financeStore = useFinanceStore()

onMounted(() => {
  financeStore.getFinancialProducts()
})
</script> 