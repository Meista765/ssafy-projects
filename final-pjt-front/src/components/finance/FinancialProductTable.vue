<template>
  <v-data-table
    :headers="headers"
    :items="processedProducts"
    :sort-by="sortBy"
    :sort-desc="sortDesc"
    class="elevation-1"
  >
    <template v-slot:item.dcls_month="{ item }">
      {{ formatMonth(item.dcls_month) }}
    </template>
  </v-data-table>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useFinanceStore } from '@/stores/financialProduct'

const financeStore = useFinanceStore()

// 테이블 헤더 정의
const headers = [
  { title: '공시 제출월', key: 'dcls_month', sortable: true },
  { title: '금융회사', key: 'kor_co_nm', sortable: true },
  { title: '상품명', key: 'fin_prdt_nm', sortable: true },
  { title: '6개월 금리', key: 'intr_rate_6', sortable: true },
  { title: '12개월 금리', key: 'intr_rate_12', sortable: true },
  { title: '24개월 금리', key: 'intr_rate_24', sortable: true },
  { title: '36개월 금리', key: 'intr_rate_36', sortable: true },
]

// 정렬 상태 관리
const sortBy = ref([])
const sortDesc = ref([])

// 날짜 포맷팅 함수
const formatMonth = (value) => {
  if (!value) return ''
  return `${value.slice(0, 4)}년 ${value.slice(4)}월`
}

// 데이터 가공
const processedProducts = computed(() => {
  return financeStore.financialProducts.map(product => {
    // 기본 상품 정보
    const baseInfo = {
      dcls_month: product.dcls_month,
      kor_co_nm: product.kor_co_nm,
      fin_prdt_nm: product.fin_prdt_nm,
      intr_rate_6: '-',
      intr_rate_12: '-',
      intr_rate_24: '-',
      intr_rate_36: '-'
    }

    // 옵션에서 각 기간별 금리 정보 추출
    product.options?.forEach(opt => {
      switch(opt.save_trm) {
        case 6:
          baseInfo.intr_rate_6 = opt.intr_rate
          break
        case 12:
          baseInfo.intr_rate_12 = opt.intr_rate
          break
        case 24:
          baseInfo.intr_rate_24 = opt.intr_rate
          break
        case 36:
          baseInfo.intr_rate_36 = opt.intr_rate
          break
      }
    })

    return baseInfo
  })
})
</script>