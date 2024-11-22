<template>
  <v-row class="mb-8">
    <v-col cols="12">
      <v-card class="pa-4">
        <v-row align="center" justify="space-between">
          <v-col cols="auto">
            <h1 class="text-h3 font-weight-bold primary--text">
              커뮤니티
            </h1>
            <div class="text-subtitle-1 text-medium-emphasis mt-1">
              여러분의 금융 이야기를 나눠보세요
            </div>
          </v-col>
          <v-col cols="auto">
            <v-btn
              color="primary"
              size="large"
              prepend-icon="mdi-plus"
              :to="{ name: 'CreateView' }"
              elevation="2"
            >
              새 글 작성
            </v-btn>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
</template> 