<template>
  <v-container v-if="financeStore.selectedProduct">
    <v-card>
      <v-card-title>{{ financeStore.selectedProduct.fin_prdt_nm }}</v-card-title>
      <v-card-subtitle>{{ financeStore.selectedProduct.kor_co_nm }}</v-card-subtitle>

      <v-card-text>
        <v-list>
          <v-list-item v-for="(value, key) in processedProduct" :key="key">
            <v-list-item-title>{{ key }}</v-list-item-title>
            <v-list-item-content>{{ value }}</v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useFinanceStore } from '@/stores/financialProduct'
import { useRoute } from 'vue-router'

const route = useRoute()
const financeStore = useFinanceStore()

// 데이터 가공
const processedProduct = computed(() => {
  // 선택된 상품 정보
  const product = financeStore.selectedProduct

  // 상품 내 속성 정보
  const baseInfo = {
    '공시 제출월': product.dcls_month,
    '가입 방법': product.join_way,
    '가입 제한': product.join_deny === 1 ? '제한 없음' :
      product.join_deny === 2 ? '서민 전용' :
        product.join_deny === 3 ? '일부 제한' : '',

    '가입 대상': product.join_member,
    '최고 한도': product.max_limit === null ? '없음' : product.max_limit,

    '만기 후 이자율': product.mtrt_int,
    '우대조건': product.spcl_cnd,
    '기타 유의사항': product.etc_note,

    '금리 유형': product.option?.[0]?.intr_rate_type_nm || '없음',
    '금리 정보': new Array(),
  }

  // 옵션에서 각 기간별 금리 정보 추출
  product.options?.forEach(opt => {
    baseInfo['금리 정보'].push({
      save_trm: opt.save_trm,     // 저축 기간  
      intr_rate: opt.intr_rate,   // 저축 금리
      intr_rate2: opt.intr_rate2, // 최고 우대금리
    })
  })

  return baseInfo
})

onMounted(() => {
  const productUniqueId = route.params.productUniqueId
  financeStore.getProductDetail(productUniqueId)
  console.log(financeStore.selectedProduct)
})
</script>