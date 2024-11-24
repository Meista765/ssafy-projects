<template>
  <v-container>
    <FinancialProductFilter 
      :products="financeStore.financialProducts"
      @update:filters="updateFilters"
      @update:selectedTerm="updateSelectedTerm"
    />
    
    <FinancialProductTable 
      :filters="filters"
      :selectedTerm="selectedTerm"
    />
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useFinanceStore } from '@/stores/financialProduct'
import FinancialProductFilter from '@/components/finance/FinancialProductFilter.vue'
import FinancialProductTable from '@/components/finance/FinancialProductTable.vue'

const financeStore = useFinanceStore()
const filters = ref({
  bank: null,
  term: null,
  category: null
})
const selectedTerm = ref(null)

const updateFilters = (newFilters) => {
  filters.value = newFilters
}

const updateSelectedTerm = (term) => {
  selectedTerm.value = term
}

// 컴포넌트 마운트 시 상품 데이터 로드
financeStore.getFinancialProducts()
</script> 