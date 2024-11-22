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
              label="사용자 이름"
              prepend-inner-icon="mdi-account"
              variant="outlined"
              required
              :rules="[v => !!v || '사용자 이름을 입력해주세요']"
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
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const showPassword1 = ref(false)
const showPassword2 = ref(false)

const store = useAuthStore()

const signUp = async function () {
  try {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
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