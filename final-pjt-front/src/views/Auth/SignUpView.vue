<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card class="elevation-12 pa-6">
          <v-card-title class="text-h4 text-center mb-4">
            회원가입
          </v-card-title>
          
          <v-form @submit.prevent="signUp">
            <v-text-field
              v-model="username"
              label="id"
              prepend-inner-icon="mdi-account"
              variant="outlined"
              required
              :rules="[v => !!v || 'id 입력해주세요']"
            ></v-text-field>

            <v-text-field
              v-model="password1"
              label="비밀번호"
              prepend-inner-icon="mdi-lock"
              :type="showPassword1 ? 'text' : 'password'"
              :append-inner-icon="showPassword1 ? 'mdi-eye' : 'mdi-eye-off'"
              variant="outlined"
              required
              :rules="[v => !!v || '비밀번호를 입력해주세요']"
              @click:append-inner="showPassword1 = !showPassword1"
            ></v-text-field>

            <v-text-field
              v-model="password2"
              label="비밀번호 확인"
              prepend-inner-icon="mdi-lock-check"
              :type="showPassword2 ? 'text' : 'password'"
              :append-inner-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
              variant="outlined"
              required
              :rules="[
                v => !!v || '비밀번호를 다시 입력해주세요',
                v => v === password1 || '비밀번호가 일치하지 않습니다'
              ]"
              @click:append-inner="showPassword2 = !showPassword2"
            ></v-text-field>

            <v-row>
              <v-col col="6">
                <v-text-field
                v-model="last_name"
                label="성"
                prepend-inner-icon=""
                variant="outlined"
                required
                :rules="[ v=> !!v || '성을 입력해주세요']"
                ></v-text-field>
              </v-col>
              <v-col col="6">
                <v-text-field
                  v-model="first_name"
                  label="이름"
                  prepend-inner-icon=""
                  variant="outlined"
                  required
                  :rules="[ v=> !!v || '이름을 입력해주세요']"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-select
              v-model="gender"
              :items="genderOptions"
              item-title="text"
              item-value="value"
              label="성별"
              prepend-inner-icon="mdi-gender-male-female"
              variant="outlined"
              required
              :rules="[v => !!v || '성별을 선택해주세요']"
            ></v-select>

            <v-row>
              <v-col cols="4">
                <v-select
                  v-model="birthYear"
                  :items="yearOptions"
                  label="년"
                  variant="outlined"
                  required
                  :rules="[v => !!v || '년도를 선택해주세요']"
                ></v-select>
              </v-col>
              <v-col cols="4">
                <v-select
                  v-model="birthMonth"
                  :items="monthOptions"
                  label="월"
                  variant="outlined"
                  required
                  :rules="[v => !!v || '월을 선택해주세요']"
                ></v-select>
              </v-col>
              <v-col cols="4">
                <v-select
                  v-model="birthDay"
                  :items="dayOptions"
                  label="일"
                  variant="outlined"
                  required
                  :rules="[v => !!v || '일을 선택해주세요']"
                ></v-select>
              </v-col>
            </v-row>

            <!-- 투자 성향 -->
            <v-select
              v-model="investmentType"
              :items="investmentTypeOptions"
              item-title="text"
              item-value="value"
              label="투자 성향"
              prepend-inner-icon="mdi-finance"
              variant="outlined"
              required
              :rules="[v => !!v || '투자 성향을 선택해주세요']"
            >
            </v-select>

            <!--연소득-->
            <v-select
              v-model="annualIncome"
              :items="annualIncomeOptions"
              item-title="text"
              item-value="value"
              label="연소득"
              prepend-inner-icon="mdi-currency-krw"
              variant="outlined"
              required
              :rules="[v => !!v || '연소득을 선택해주세요']"
            >
            </v-select>

            <!--목표 저축액-->
            <v-select
              v-model="savingsGoal"
              :items="savingsGoalOptions"
              item-title="text"
              item-value="value"
              label="목표 저축액"
              prepend-inner-icon="mdi-target"
              variant="outlined"
              required
              :rules="[v => !!v || '목표 저축액을 선택해주세요']"
            >
            </v-select>
            <v-btn
              type="submit"
              color="primary"
              block
              size="large"
              class="mt-4"
            >
              회원가입
            </v-btn>

            <v-row class="mt-4">
              <v-col class="text-center">
                이미 계정이 있으신가요?
                <router-link to="/login" class="text-decoration-none">
                  로그인하기
                </router-link>
              </v-col>
            </v-row>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useAuthStore } from '@/stores/auth'

// 변수

// 기본 정보
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const showPassword1 = ref(false)
const showPassword2 = ref(false)


// 성별 정보
const gender = ref(null)
const genderOptions = [
  { text: '남성', value: 'M' },
  { text: '여성', value: 'F' },
]

// 이름 정보
const first_name = ref(null)
const last_name = ref(null)

/// 생년월일 정보
const birthYear = ref(null)
const birthMonth = ref(null)
const birthDay = ref(null)

const currentYear = new Date().getFullYear()
const yearOptions = []
for (let y = currentYear; y >= 1900; y--) {
  yearOptions.push(y)
}

// 투자 성향 정보
const investmentType = ref(null)
const investmentTypeOptions = [
  {text: '안정형', value: 'conservative'},
  {text: '중립형', value: 'moderate'},
  {text: '공격형', value: 'aggresive'},

]

// 연소득 정보
const annualIncome = ref(null)
const annualIncomeOptions = [
  { text: '~2000만원', value: '0'},
  { text: '2000만원~3500만원', value: '1'},
  { text: '3500만원~5000만원', value: '2'},
  { text: '5000만원~7000만원', value: '3'},
  { text: '7000만원~1억원', value: '4'},
  { text: '1억원~', value: '5'},
]

// 목표 저축액
const savingsGoal = ref(null)
const savingsGoalOptions = [
  { text: '~100만원', value: '0' },
  { text: '100만원~1000만원', value: '1' },
  { text: '1000만원~5000만원', value: '2' },
  { text: '5000만원~7000만원', value: '3' },
  { text: '7000만원~1억원', value: '4' },
  { text: '1억원~', value: '5' },
]

const monthOptions = Array.from({ length: 12 }, (v, k) => k + 1)

const dayOptions = ref([])

watch([birthYear, birthMonth], () => {
  if (birthYear.value && birthMonth.value) {
    const daysInMonth = new Date(birthYear.value, birthMonth.value, 0).getDate()
    dayOptions.value = Array.from({ length: daysInMonth }, (v, k) => k + 1)
  } else {
    dayOptions.value = []
  }
})


// 생년월일 조합
const birthDate = computed(() => {
  if (birthYear.value && birthMonth.value && birthDay.value) {
    const month = birthMonth.value.toString().padStart(2, '0')
    const day = birthDay.value.toString().padStart(2, '0')
    return `${birthYear.value}-${month}-${day}`
  }
  return null
})

const store = useAuthStore()
const age = computed(() => {
  if (birthDate.value) {
    const today = new Date()
    const birthDateObj = new Date(birthDate.value)
    let age = today.getFullYear() - birthDateObj.getFullYear()
    const monthDiff = today.getMonth() - birthDateObj.getMonth()
    if (
      monthDiff < 0 ||
      (monthDiff === 0 && today.getDate() < birthDateObj.getDate())
    ) {
      age--
    }
    return age
  }
  return null
})
const signUp = async function () {
  try {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      first_name: first_name.value,
      last_name: last_name.value,
      gender: gender.value,
      birth_date:birthDate.value,
      age: age.value,
      investment_style: investmentType.value,
      annual_income: annualIncome.value,
      savings_goal: savingsGoal.value
    }
    await store.signUp(payload)
  } catch (error) {
    console.error('회원가입 실패:', error)
    alert('회원가입에 실패했습니다. 다시 시도해주세요.')
  }
}
</script>

<style scoped>

</style>