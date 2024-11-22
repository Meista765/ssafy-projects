<template>
  <Bar :data="chartData" :options="chartOptions" />
</template>

<script setup>
import { ref, reactive } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

const props = defineProps({
  chartData: {
    type: Object,
    required: true
  }
})

const chartData = reactive({
  labels: props.chartData.map(item => `${item.save_trm}개월`),
  datasets: [
    {
      label: '저축 금리',
      backgroundColor: '#f87979',
      data: props.chartData.map(item => item.intr_rate)
    },
    {
      label: '최고 우대금리',
      backgroundColor: '#7979f8',
      data: props.chartData.map(item => item.intr_rate2)
    }
  ]
})

const chartOptions = ref({
  responsive: true,
  scales: {
    y: {
      beginAtZero: true
    }
  }
})
</script> 