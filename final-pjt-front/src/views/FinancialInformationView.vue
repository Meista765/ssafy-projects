<template>
  <div class="container mt-4">
    <h2 class="text-center">금융 정보</h2>
    <table class="table table-bordered table-striped mt-4">
      <thead>
        <tr>
          <th>공시 제출월</th>
          <th>금융회사 명</th>
          <th>상품 명</th>
          <th colspan="4" class="text-center">저축기간 별 금리</th>
        </tr>
        <tr>
          <th></th>
          <th></th>
          <th></th>
          <th @click="sortBy('6')">6개월</th>
          <th @click="sortBy('12')">12개월</th>
          <th @click="sortBy('24')">24개월</th>
          <th @click="sortBy('36')">36개월</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(product, index) in sortedProducts" :key="index">
          <td>{{ product.dcls_month || '-' }}</td>
          <td>{{ product.kor_co_nm || '-' }}</td>
          <td>{{ product.fin_prdt_nm || '-' }}</td>
          <td>{{ getInterestRate(product.options, 6) }}</td>
          <td>{{ getInterestRate(product.options, 12) }}</td>
          <td>{{ getInterestRate(product.options, 24) }}</td>
          <td>{{ getInterestRate(product.options, 36) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue';
import { useFinanceStore } from '@/stores/financialProduct';

const store = useFinanceStore();

// Fetch financial products on mount
store.getExchangeRate();

const sortColumn = ref(null);
const sortDirection = ref(0); // 0: no sort, 1: ascending, -1: descending

const sortedProducts = computed(() => {
  if (!sortColumn.value) return store.financialProducts;

  return [...store.financialProducts].sort((a, b) => {
    const rateA = getInterestRate(a.options, sortColumn.value, true);
    const rateB = getInterestRate(b.options, sortColumn.value, true);

    // Handle '-' values: they always go to the end
    if (rateA === '-') return sortDirection.value;
    if (rateB === '-') return -sortDirection.value;

    return (rateA - rateB) * sortDirection.value;
  });
});

// Get interest rate based on saving term
function getInterestRate(options, term, raw = false) {
  const option = options?.find(opt => opt.save_trm == term);
  const rate = option?.intr_rate ?? -1;
  if (raw) return rate === -1 ? '-' : rate;
  return rate === -1 ? '-' : `${rate}%`;
}

// Toggle sorting on column
function sortBy(term) {
  if (sortColumn.value === term) {
    sortDirection.value = sortDirection.value === 1 ? -1 : (sortDirection.value === -1 ? 0 : 1);
  } else {
    sortColumn.value = term;
    sortDirection.value = 1; // Default to ascending
  }
}
</script>

<style scoped>
.table th {
  cursor: pointer;
}

.table th:hover {
  background-color: #f8f9fa;
}
</style>
