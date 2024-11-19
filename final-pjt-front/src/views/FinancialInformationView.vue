<template>
  <v-app>
    <v-container>
      <v-data-table
        :headers="headers"
        :items="tableData"
        sort-by="kor_co_nm"
        class="elevation-1"
      >
        <template #item="{ item }">
          <tr>
            <td>{{ item.dcls_month }}</td>
            <td>{{ item.kor_co_nm }}</td>
            <td>{{ item.fin_prdt_nm }}</td>
            <td>{{ item.intr_rate_6 }}</td>
            <td>{{ item.intr_rate_12 }}</td>
            <td>{{ item.intr_rate_24 }}</td>
            <td>{{ item.intr_rate_36 }}</td>
          </tr>
        </template>
      </v-data-table>
    </v-container>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import { createVuetify } from 'vuetify'
import 'vuetify/styles'

// Vuetify 인스턴스를 생성합니다
const vuetify = createVuetify()

// JSON 데이터 로드
const rawData = require('@/assets/response.json').data

// 데이터 변환 로직
const transformData = (data) =>
  data.map((item) => {
    const findRate = (term) => {
      const option = item.options.find((opt) => opt.save_trm === term)
      return option && option.intr_rate !== '-1' ? option.intr_rate : '-'
    }

    return {
      dcls_month: item.dcls_month,
      kor_co_nm: item.kor_co_nm,
      fin_prdt_nm: item.fin_prdt_nm,
      intr_rate_6: findRate(6),
      intr_rate_12: findRate(12),
      intr_rate_24: findRate(24),
      intr_rate_36: findRate(36),
    }
  })

const tableData = ref(transformData(rawData))

const headers = ref([
  { text: '공시 제출월', value: 'dcls_month' },
  { text: '금융회사 명', value: 'kor_co_nm' },
  { text: '상품 명', value: 'fin_prdt_nm' },
  {
    text: '저축기간 별 금리',
    align: 'start',
    sortable: false,
    children: [
      { text: '6개월', value: 'intr_rate_6', sortable: true },
      { text: '12개월', value: 'intr_rate_12', sortable: true },
      { text: '24개월', value: 'intr_rate_24', sortable: true },
      { text: '36개월', value: 'intr_rate_36', sortable: true },
    ],
  },
])
</script>

<style scoped>
.v-data-table th {
  font-weight: bold;
}
</style>
