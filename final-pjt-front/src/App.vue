<template>
  <nav>
    <router-link :to="{ name: 'exchangeRateCalculator' }">환율 계산기</router-link>
  </nav>

  <div>
    <router-view />
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped></style>
