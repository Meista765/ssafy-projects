<template>
  <v-container class="fill-height">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6" class="text-center">
        <v-card class="pa-8">
          <v-card-title class="text-h2 font-weight-bold mb-6">
            404
          </v-card-title>
          
          <v-card-subtitle class="text-h5 mb-6">
            페이지를 찾을 수 없습니다
          </v-card-subtitle>
          
          <v-card-text class="text-body-1 mb-6">
            요청하신 페이지가 존재하지 않거나 이동되었을 수 있습니다.
          </v-card-text>
          
          <v-btn
            color="primary"
            size="large"
            :to="{ name: 'HomeView' }"
            prepend-icon="mdi-home"
          >
            홈으로 돌아가기
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
// No additional script needed
</script>