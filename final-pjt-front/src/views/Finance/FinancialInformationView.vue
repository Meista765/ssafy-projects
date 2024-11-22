<template>
  <v-container>
    <v-card class="mt-4 pa-4">
      <v-card-title class="text-h4 text-center mb-4">
        금융 정보
      </v-card-title>

      <v-data-table
        :headers="headers"
        :items="store.financialProducts"
        :sort-by="[{ key: 'rate6', order: 'desc' }]"
        density="comfortable"
        hover
        class="elevation-1"
      >
        <template v-slot:item="{ item }">
          <tr>
            <td>{{ item.dcls_month || '-' }}</td>
            <td>{{ item.kor_co_nm || '-' }}</td>
            <td>{{ item.fin_prdt_nm || '-' }}</td>
            <td class="text-center">{{ getInterestRate(item.options, 6) }}</td>
            <td class="text-center">{{ getInterestRate(item.options, 12) }}</td>
            <td class="text-center">{{ getInterestRate(item.options, 24) }}</td>
            <td class="text-center">{{ getInterestRate(item.options, 36) }}</td>
          </tr>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import { useFinanceStore } from '@/stores/financialProduct';

const store = useFinanceStore();

// Fetch financial products on mount
store.getExchangeRate();

const headers = [
  { 
    title: '공시 제출월',
    key: 'dcls_month',
    align: 'start',
    sortable: true,
    width: '15%',
  },
  {
    title: '금융회사',
    key: 'kor_co_nm',
    align: 'start',
    sortable: true,
    width: '15%',
  },
  {
    title: '상품명',
    key: 'fin_prdt_nm',
    align: 'start',
    sortable: true,
    width: '25%',
  },
  {
    title: '6개월',
    key: 'rate6',
    align: 'center',
    sortable: true,
    width: '11.25%',
  },
  {
    title: '12개월',
    key: 'rate12',
    align: 'center',
    sortable: true,
    width: '11.25%',
  },
  {
    title: '24개월',
    key: 'rate24',
    align: 'center',
    sortable: true,
    width: '11.25%',
  },
  {
    title: '36개월',
    key: 'rate36',
    align: 'center',
    sortable: true,
    width: '11.25%',
  },
];

// Get interest rate based on saving term
function getInterestRate(options, term) {
  const option = options?.find(opt => opt.save_trm == term);
  const rate = option?.intr_rate ?? -1;
  return rate === -1 ? '-' : `${rate}%`;
}
</script>

<style scoped>
:deep(.v-data-table-header) {
  background-color: rgb(var(--v-theme-primary));
}

:deep(.v-data-table-header th) {
  color: white !important;
  font-size: 1.1rem !important;
  font-weight: bold !important;
}
</style>
