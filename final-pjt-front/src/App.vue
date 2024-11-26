<template>
  <v-app>
    <v-app-bar>
      <TheNavigation />
    </v-app-bar>

    <v-main class="bg-grey-lighten-4">
      <router-view />
    </v-main>

    <TheFooter />
    <ChatBot />
  </v-app>
</template>


<script setup>
import TheNavigation from '@/components/common/Navigation.vue'
import TheFooter from '@/components/common/Footer.vue'
import ChatBot from '@/components/common/ChatBot.vue';
</script>

<style scoped></style>
