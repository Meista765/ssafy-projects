<template>
  <ul>
    <li v-for="bank in banks" :key="bank.id">
      {{ bank.name }} - {{ bank.address }}
    </li>
  </ul>
</template>

<script setup>
const props = defineProps({
  banks: {
    type: Array,
    default: () => [],
  },
})
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 10px;
}
</style>
