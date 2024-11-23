<template>
  <v-container v-if="financeStore.selectedProduct">
    <v-card>
      <div class="d-flex align-center justify-space-between px-4">
        <div>
          <v-card-title>{{
            financeStore.selectedProduct.fin_prdt_nm
          }}</v-card-title>
          <v-card-subtitle>{{
            financeStore.selectedProduct.kor_co_nm
          }}</v-card-subtitle>
        </div>
        <v-btn
          v-if="authStore.isLogin"
          :color="isSubscribed ? 'error' : 'primary'"
          @click="handleSubscribe"
        >
          {{ isSubscribed ? '상품 해지' : '상품 가입' }}
        </v-btn>
      </div>

      <v-card-text>
        <v-list>
          <v-list-item
            v-for="(value, key, index) in processedProduct"
            :key="key"
          >
            <v-list-item-title
              ><strong>{{ index + 1 }}. {{ key }}</strong></v-list-item-title
            >
            <v-list-item-subtitle>{{ value }}</v-list-item-subtitle>
          </v-list-item>
        </v-list>
        <v-list>
          <v-list-item>
            <v-list-item-title
              ><strong>10. 가입 기간별 금리</strong></v-list-item-title
            >
            <BarChart :chartData="interestInfo" />
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import axios from 'axios'

import { computed, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'

import { useAuthStore } from '@/stores/auth'
import { useFinanceStore } from '@/stores/financialProduct'

import BarChart from '@/components/finance/BarChart.vue'  // 추가

const route = useRoute()
const financeStore = useFinanceStore()
const authStore = useAuthStore()

const BACKEND_SERVER_URL = import.meta.env.VITE_BACKEND_SERVER_URL

// 구독 상태를 로컬 ref로 관리
const isSubscribed = ref(null)

// 데이터 가공
const processedProduct = computed(() => {
  // 선택된 상품 정보
  const product = financeStore.selectedProduct

  // 상품 내 속성 정보
  const baseInfo = {
    '공시 제출월': product.dcls_month,
    '가입 방법': product.join_way,
    '가입 제한':
      product.join_deny === 1
        ? '제한 없음'
        : product.join_deny === 2
        ? '서민 전용'
        : product.join_deny === 3
        ? '일부 제한'
        : '',

    '가입 대상': product.join_member,
    '최고 한도': product.max_limit === null ? '없음' : product.max_limit,

    '만기 후 이자율': product.mtrt_int,
    우대조건: product.spcl_cnd,
    '기타 유의사항': product.etc_note,

    '금리 유형': product.option?.[0]?.intr_rate_type_nm || '없음',
  }
  return baseInfo
})

// 금리 정보
const interestInfo = computed(() => {
  const product = financeStore.selectedProduct
  const terms = new Array()

  // 옵션에서 각 기간별 금리 정보 추출
  product.options?.forEach((opt) => {
    terms.push({
      save_trm: opt.save_trm, // 저축 기간
      intr_rate: opt.intr_rate, // 저축 금리
      intr_rate2: opt.intr_rate2, // 최고 우대금리
    })
  })

  return terms
})

// 가입하기 버튼 클릭 핸들러 추가
const handleSubscribe = async () => {
  const authStore = useAuthStore()
  const product = financeStore.selectedProduct

  await axios({
    method: 'post',
    url: `${BACKEND_SERVER_URL}/finances/subscribe/`,
    data: {
      category: product.unique_id.slice(0, 3),
      id: product.id,
    },
    headers: {
      Authorization: `Token ${authStore.token}`,
    },
  })
    .then((res) => {
      console.log(res)
      // 로컬 상태만 토글
      isSubscribed.value = !isSubscribed.value
    })
    .catch((error) => {
      console.error(error)
    })
}

// 초기 마운트 시 구독 상태 설정
onMounted(async () => {
  const productUniqueId = route.params.productUniqueId
  await financeStore.getProductDetailFromServer(productUniqueId)
    .then(() => {
      isSubscribed.value = financeStore.selectedProduct?.is_subscribed || false
    })
})
</script>
