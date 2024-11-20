<template>
  <nav>
    <router-link :to="{ name: 'currencyConverter' }">환율 계산기</router-link>
    <span> | </span>
    <router-link :to="{ name: 'financialInformation' }">금융 정보</router-link>
  </nav>

  <div>
    <router-view />
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped></style>
