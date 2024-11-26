<template>
  <v-container v-if="userInfo?.user" fluid>
    <ViewTitle 
      title="프로필" 
      subtitle="회원님의 상세 정보를 확인하세요"
    />
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="text-center">
            <v-avatar size="100">
              <v-icon size="150">mdi-account-circle</v-icon>
            </v-avatar>
          </v-card-title>

          <v-card-subtitle class="text-center mb-4">
            {{ userInfo.user.last_name }}{{ userInfo.user.first_name }}
          </v-card-subtitle>

          <v-divider></v-divider>

          <v-list density="compact" id="user-info-list">
            <v-list-item
              prependIcon="mdi-gender-male-female"
              color="primary"
            >
              <v-list-item-title>성별</v-list-item-title>
              <v-list-item-text>{{ genderDisplay }}</v-list-item-text>
            </v-list-item>

            <v-divider></v-divider>

            <v-list-item
              prependIcon="mdi-calendar"
              color="primary"
            >
              <v-list-item-title>생년월일</v-list-item-title>
              <v-list-item-text>{{ userInfo.user.birth_date }}</v-list-item-text>
            </v-list-item>

            <v-divider></v-divider>

            <v-list-item
              prependIcon="mdi-human-male-female"
              color="primary"
            >
              <v-list-item-title>나이</v-list-item-title>
              <v-list-item-text>{{ userInfo.user.age }}세</v-list-item-text>
            </v-list-item>

            <v-divider></v-divider>

            <v-list-item
              prependIcon="mdi-finance"
              color="primary"
            >
              <v-list-item-title>투자 성향</v-list-item-title>
              <v-list-item-text>{{ investmentStyleDisplay }}</v-list-item-text>
            </v-list-item>

            <v-divider></v-divider>

            <v-list-item
              prependIcon="mdi-currency-krw"
              color="primary"
            >
              <v-list-item-title>연소득</v-list-item-title>
              <v-list-item-text>{{ annualIncomeDisplay }}</v-list-item-text>
            </v-list-item>

            <v-divider></v-divider>

            <v-list-item
              prependIcon="mdi-target"
              color="primary"
            >
              <v-list-item-title>목표 저축액</v-list-item-title>
              <v-list-item-text>{{ savingsGoalDisplay }}</v-list-item-text>
            </v-list-item>

            <v-divider></v-divider>

            <v-list-item
              prependIcon="mdi-piggy-bank-outline"
              color="primary"
              class="py-2"
            >
              <v-list-item-title>가입한 예금 상품</v-list-item-title>
              <template v-if="userInfo.deposit.length > 0">
                <div v-for="deposit in userInfo.deposit" :key="deposit.id">
                  <v-btn
                    variant="text"
                    class="pa-0"
                    :to="{ name: 'FinancialProductDetail', params: { productUniqueId: 'dep_' + deposit.id } }"
                  >
                    {{ deposit.fin_prdt_nm }}
                  </v-btn>
                </div>
              </template>
              <v-list-item-text v-else>
                아직 가입한 예금 상품이 없습니다.
              </v-list-item-text>
            </v-list-item>

            <v-divider></v-divider>

            <v-list-item
              prependIcon="mdi-piggy-bank"
              color="primary"
            >
              <v-list-item-title>가입한 적금 상품</v-list-item-title>
              <template v-if="userInfo.installments.length > 0">
                <div v-for="installments in userInfo.installments" :key="installments.id">
                  <v-btn
                    variant="text"
                    class="pa-0"
                    :to="{ name: 'FinancialProductDetail', params: { productUniqueId: 'ins_' + installments.id } }"
                  >
                    {{ installments.fin_prdt_nm }}
                  </v-btn>
                </div>
              </template>
              <v-list-item-text v-else>
                아직 가입한 적금 상품이 없습니다.
              </v-list-item-text>
            </v-list-item>
          </v-list>

          <v-divider></v-divider>

          <v-card-actions class="justify-end">
            <v-btn color="red" dark @click="confirmSignOut">
              <v-icon left>mdi-account-remove</v-icon>
              회원탈퇴
            </v-btn>
            <v-btn color="primary" @click="changeUserInfo">
              <v-icon left>mdi-account-convert</v-icon>
              정보수정
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <!-- 탈퇴 확인 다이얼로그 -->
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="headline">회원탈퇴 확인</v-card-title>
        <v-card-text>
          정말로 회원탈퇴를 진행하시겠습니까? 탈퇴하시면 모든 데이터가 삭제되며 복구가 불가능합니다.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey" text @click="dialog = false">취소</v-btn>
          <v-btn color="red" dark @click="signOut">탈퇴하기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
  <v-container v-else class="mt-5" fluid>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-text class="text-center">
            데이터를 불러오는 중...
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';

import { useAuthStore } from '@/stores/auth';
import { useRoute, useRouter } from 'vue-router';

import ViewTitle from '@/components/common/ViewTitle.vue'

// 변수
const authStore = useAuthStore();
const route = useRoute();
const router = useRouter();
const userId = route.params.id;

// 다이얼로그 제어
const dialog = ref(false);

// 액션

// 사용자 정보 가져오기
const getUserInfo = function () {
  authStore.getUserInfo(userId);
  console.log(authStore.userInfo);
};

// 회원탈퇴 확인
const confirmSignOut = function () {
  dialog.value = true;
};

// 사용자 정보 반응형 데이터
const userInfo = computed(() => authStore.userInfo);

// 선택지 값 변환
const genderDisplay = computed(() => {
  if (!userInfo.value.user.gender) return '정보 없음';
  return userInfo.value.user.gender === 'M' ? '남성' : '여성';
});

const investmentStyleDisplay = computed(() => {
  switch (userInfo.value.user.investment_style) {
    case 'conservative':
      return '안정형';
    case 'moderate':
      return '중립형';
    case 'aggressive':
      return '공격형';
    default:
      return '정보 없음';
  }
});

const annualIncomeDisplay = computed(() => {
  const mapping = {
    '0': '~2000만원',
    '1': '2000만원~3500만원',
    '2': '3500만원~5000만원',
    '3': '5000만원~7000만원',
    '4': '7000만원~1억원',
    '5': '1억원~',
  };
  return mapping[userInfo.value.user.annual_income] || '정보 없음';
});

const savingsGoalDisplay = computed(() => {
  const mapping = {
    '0': '~100만원',
    '1': '100만원~1000만원',
    '2': '1000만원~5000만원',
    '3': '5000만원~7000만원',
    '4': '7000만원~1억원',
    '5': '1억원~',
  };
  return mapping[userInfo.value.user.savings_goal] || '정보 없음';
});


// 회원탈퇴 액션
const signOut = function () {
  authStore.signOut(userId)
    .then(() => {
      dialog.value = false;
      router.push('/'); // 탈퇴 후 홈으로 이동
      alert('회원탈퇴가 완료되었습니다.');
    })
    .catch((error) => {
      console.error('회원탈퇴 실패:', error);
      alert('회원탈퇴에 실패했습니다. 다시 시도해주세요.');
    });
};


// 회원정보 변경 액션
const changeUserInfo = function () {
  router.push({ name: 'ChangeUserInfoView', params: { id: route.params.id } })
}
// 라이프사이클 훅
onMounted(getUserInfo)
</script>

<style scoped>
.v-card {
  padding: 20px;
}

.headline {
  font-weight: bold;
}

#user-info-list {
  padding: 0
}

#user-info-list .v-list-item {
  padding: 0.5rem
}

#user-info-list .v-list-item-title {
  font-weight: bold;
}
</style>
