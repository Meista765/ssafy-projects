<template>
  <v-container class="mt-5" fluid>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title>
            <span class="text-h5">회원정보 수정</span>
          </v-card-title>

          <v-divider></v-divider>

          <v-card-text>
            <v-form ref="form" v-model="isValid" lazy-validation>
              <!-- 이름 -->
              <v-text-field
                v-model="first_name"
                label="이름"
                :rules="[rules.required]"
                required
              ></v-text-field>

              <v-text-field
                v-model="last_name"
                label="성"
                :rules="[rules.required]"
                required
              ></v-text-field>

              <!-- 투자 성향 -->
              <v-select
                v-model="investment_style"
                :items="investmentStyleOptions"
                item-title="text"
                item-value="value"
                label="투자 성향"
                :rules="[rules.required]"
                required
              ></v-select>

              <!-- 연소득 -->
              <v-select
                v-model="annual_income"
                :items="annualIncomeOptions"
                item-title="text"
                item-value="value"
                label="연소득"
              ></v-select>

              <!-- 목표 저축액 -->
              <v-select
                v-model="savings_goal"
                :items="savingsGoalOptions"
                item-title="text"
                item-value="value"
                label="목표 저축액"
              ></v-select>

              <!-- 저장 버튼 -->
              <v-btn
                :disabled="!isValid || isSubmitting"
                color="primary"
                @click="updateUserInfo"
              >
                저장
                <v-progress-circular
                  v-if="isSubmitting"
                  indeterminate
                  size="20"
                  color="white"
                  class="ml-2"
                ></v-progress-circular>
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter, useRoute } from 'vue-router';

// 변수
const authStore = useAuthStore();
const router = useRouter();
const route = useRoute()
const userId = route.params.id
const userInfo = ref(null)

const isValid = ref(false);
const isSubmitting = ref(false);



// 옵션 데이터
const investmentStyleOptions = [
  { text: '안정형', value: 'conservative' },
  { text: '중립형', value: 'moderate' },
  { text: '공격형', value: 'aggressive' },
];

const annualIncomeOptions = [
  { text: '~2000만원', value: '0' },
  { text: '2000만원~3500만원', value: '1' },
  { text: '3500만원~5000만원', value: '2' },
  { text: '5000만원~7000만원', value: '3' },
  { text: '7000만원~1억원', value: '4' },
  { text: '1억원~', value: '5' },
];

const savingsGoalOptions = [
  { text: '~100만원', value: '0' },
  { text: '100만원~1000만원', value: '1' },
  { text: '1000만원~5000만원', value: '2' },
  { text: '5000만원~7000만원', value: '3' },
  { text: '7000만원~1억원', value: '4' },
  { text: '1억원~', value: '5' },
];


// 유효성 검사 규칙
const rules = {
  required: (value) => !!value || '필수 입력 항목입니다.',
};

// 사용자 정보 반응형 데이터
const first_name = ref(null)
const last_name = ref(null)
const investment_style = ref(null)
const annual_income = ref(null)
const savings_goal = ref(null)

// 사용자 정보 비동기로 가져오기
const getUserInfo = async () => {
    try {
      const res = await axios.get(`${authStore.BACKEND_SERVER_URL}/user/detail/${userId}/`, {
        headers: {
          Authorization: `Token ${authStore.token}`
        }
      })
      console.log('User Info:', res.data)
      userInfo.value = res.data
      first_name.value = userInfo.value.user.first_name
      last_name.value = userInfo.value.user.last_name
      investment_style.value = userInfo.value.user.investment_style
      annual_income.value = userInfo.value.user.annual_income
      savings_goal.value = userInfo.value.user.savings_goal
      console.log(userInfo.value)
    } catch (err) {
      console.error('Failed to get user info:', err)
    }
  }



// 회원 정보 업데이트
const updateUserInfo = function () {
  axios({
    method: 'put',
    url: `${authStore.BACKEND_SERVER_URL}/user/detail/${userId}/`,
    data: {
      first_name:first_name.value,
      last_name:last_name.value,
      investment_style:investment_style.value,
      annual_income: annual_income.value,
      savings_goal:savings_goal.value
    },
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  })
    .then((res) => {
      console.log('회원가입 성공',res)
      router.push({ name: 'ProFileView', params:{ id: userId}})
    })
    .catch((err) => {
      console.log(err)
    })
}


// 초기 로딩
onMounted(getUserInfo);
</script>

<style scoped>
.v-card {
  padding: 20px;
}
.headline {
  font-weight: bold;
}
</style>
