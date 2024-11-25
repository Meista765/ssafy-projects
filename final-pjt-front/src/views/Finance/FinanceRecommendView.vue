<template>
  <v-container v-if="userInfo?.user" class="pa-4">
    <v-row justify="center">
      <v-col cols="12" md="8">
        <!-- 사용자 환영 카드 -->
        <v-card class="mb-5" elevation="2">
          <v-card-title class="headline">
            {{ userInfo.user.last_name + userInfo.user.first_name }}님과 유사한 회원들이 가입한 상품은 무엇일까요?
          </v-card-title>
          <v-card-subtitle>
            해당 서비스를 받기 위해 간단한 질문에 응답해주세요.
          </v-card-subtitle>
        </v-card>

        <!-- 사용자 입력 폼 카드 -->
        <v-card class="mb-5" elevation="2">
          <v-card-text>
            <v-form @submit.prevent="handleSubmit">
              <v-row>
                <v-col cols="12">
                  <!-- 주 은행 선택 -->
                  <v-select
                    v-model="form.mainbank"
                    :items="bankList"
                    label="주 은행"
                    required
                    :rules="[v => !!v || '주 은행을 선택해주세요']"
                    outlined
                    dense
                  ></v-select>
                </v-col>

                <v-col cols="12" sm="6">
                  <!-- 예금 상품 수 입력 -->
                  <v-text-field
                    v-model.number="form.deposit_cnt"
                    label="현재 가입한 예금 상품 수"
                    type="number"
                    required
                    min="0"
                    :rules="[v => v >= 0 || '예금 상품 수는 0 이상이어야 합니다']"
                    outlined
                    dense
                  ></v-text-field>
                </v-col>

                <v-col cols="12" sm="6">
                  <!-- 적금 상품 수 입력 -->
                  <v-text-field
                    v-model.number="form.savings_cnt"
                    label="현재 가입한 적금 상품 수"
                    type="number"
                    required
                    min="0"
                    :rules="[v => v >= 0 || '적금 상품 수는 0 이상이어야 합니다']"
                    outlined
                    dense
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-row justify="center" class="mt-4">
                <v-btn type="submit" color="primary" :loading="loading" large>
                  <v-icon left>mdi-bank</v-icon>
                  추천 받기
                </v-btn>
              </v-row>
            </v-form>
          </v-card-text>
        </v-card>

        <!-- 추천 상품 표시 카드 -->
        <v-card v-if="recommendProducts" class="mb-5" elevation="2">
          <v-card-title class="headline">
            {{ userInfo.user.last_name + userInfo.user.first_name }}님과 유사한 회원들은 이런 상품을 가입했습니다.
          </v-card-title>
          <v-card-text>
            <v-expansion-panels>
              <v-expansion-panel v-for="(user, key) in recommendProducts" :key="key">
                <v-expansion-panel-title class="bg-grey-lighten-4">
                  <v-row align="center">
                    <v-col cols="10">
                      <strong>{{ user.last_name }}** 님의 추천</strong> (성별: {{ user.gender }}, 나이 {{ user.age }})
                    </v-col>
                  </v-row>
                </v-expansion-panel-title>

                <v-divider class="border-opacity-100"></v-divider>
                <v-expansion-panel-text>
                  <!-- 예금 상품 -->
                  <v-list-subheader class="mt-3">
                    <v-icon left color="primary">mdi-wallet-plus</v-icon>
                    <span>예금 상품</span>
                  </v-list-subheader>
                  <v-list dense>
                    <v-list-item 
                    v-for="product in user.depositproducts" 
                    :key="product.id"
                    :to="{ name: 'FinancialProductDetail', params: { productUniqueId: product.id }}">
                      <div class="grid grid-cols-1">
                        <div class="text-body-1 font-medium">
                          {{ product.fin_prdt_nm }}
                        </div>
                        <div class="text-body-2 text-secondary">
                          {{ product.kor_co_nm }}
                        </div>
                      </div>
                    </v-list-item>
                  </v-list>

                  <v-divider class="border-opacity-75"></v-divider>

                  <!-- 적금 상품 -->
                  <v-list-subheader>
                    <v-icon left color="secondary">mdi-piggy-bank</v-icon>
                    <span>적금 상품</span>
                  </v-list-subheader>
                  <v-list dense>
                    <v-list-item 
                    v-for="product in user.savingsproducts" 
                    :key="product.id"
                    :to="{ name: 'FinancialProductDetail', params: { productUniqueId: product.id }}">
                      <div class="grid grid-cols-1">
                        <div class="text-body-1 font-medium">
                          {{ product.fin_prdt_nm }}
                        </div>
                        <div class="text-body-2 text-secondary">
                          {{ product.kor_co_nm }}
                        </div>
                      </div>
                    </v-list-item>
                  </v-list>
                </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-card-text>
        </v-card>

        <!-- 에러 메시지 표시 -->
        <v-alert v-if="error" type="error" class="mb-5" elevation="2">
          <v-icon left>mdi-alert-circle</v-icon>
          {{ error }}
        </v-alert>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';


// 은행 리스트 정의
const bankList = [
  '우리은행',
  '한국스탠다드차타드은행',
  '아이엠뱅크',
  '부산은행',
  '광주은행',
  '제주은행',
  '전북은행',
  '경남은행',
  '중소기업은행',
  '한국산업은행',
  '국민은행',
  '신한은행',
  '농협은행주식회사',
  '하나은행',
  '주식회사 케이뱅크',
  '수협은행',
  '주식회사 카카오뱅크',
  '토스뱅크 주식회사'
];

// 변수 정의
const route = useRoute();
const authStore = useAuthStore();
const router = useRouter()
const userId = route.params.id;

const recommendProducts = ref(null);
const error = ref(null);
const loading = ref(false);

// 사용자 정보 반응형 데이터
const userInfo = computed(() => authStore.userInfo);

// 폼 데이터
const form = ref({
  mainbank: '',
  deposit_cnt: 0,
  savings_cnt: 0,
});
//  
// const handleRowClick = (event, product) => {
//   router.push({
//     name: 'FinancialProductDetail',
//     params: { productUniqueId: product.item.unique_id }
//   })
// }
// 추천 상품 가져오기 함수
const getRecommendProducts = async () => {
  loading.value = true;
  error.value = null;

  try {
    const response = await axios.post(
      `${authStore.BACKEND_SERVER_URL}/finances/recommend-finance/${userId}/`,
      {
        mainbank: form.value.mainbank,
        deposit_cnt: form.value.deposit_cnt,
        savings_cnt: form.value.savings_cnt,
      }
    );

    recommendProducts.value = response.data;
    console.log('추천 정보 조회 성공', response.data);
  } catch (err) {
    console.error('추천 정보 조회 실패', err);
    error.value = '추천 정보를 불러오는 데 실패했습니다. 다시 시도해주세요.';
  } finally {
    loading.value = false;
  }
};

// 사용자 정보 가져오기
const getUserInfo = function () {
  authStore.getUserInfo(userId);
  console.log(authStore.userInfo);
};

// 폼 제출 핸들러
const handleSubmit = () => {
  // 입력 값 검증 (필요 시 추가)
  getRecommendProducts();
};

onMounted(getUserInfo);
</script>

<style scoped>
.text-center {
  text-align: center;
}
.mb-2 {
  margin-bottom: 0.5rem;
}
.mb-5 {
  margin-bottom: 2rem;
}
.mt-3 {
  margin-top: 1rem;
}
.mt-4 {
  margin-top: 1.5rem;
}
</style>
