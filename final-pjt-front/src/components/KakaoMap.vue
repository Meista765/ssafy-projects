<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script setup>
import { onMounted, watch } from 'vue'

const KAKAO_MAP_API_KEY = '1b598c82f60237435951d1359f5902fe'

const props = defineProps({
  filteredBanks: {
    type: Array,
    default: () => [],
  },
})

let map = null
let markers = []

// Kakao Map API 로드 함수
function loadKakaoMap(initMap) {
  const script = document.createElement('script')
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${KAKAO_MAP_API_KEY}&autoload=false`
  script.onload = () => {
    window.kakao.maps.load(() => {
      initMap()
    })
  }
  document.head.appendChild(script)
}

// Kakao Map 초기화 함수
function initMap() {
  const container = document.getElementById('map') // 지도를 표시할 div
  const options = {
    center: new kakao.maps.LatLng(37.5665, 126.978), // 서울 중심좌표
    level: 3, // 지도 확대 레벨
  }

  // 지도 생성
  map = new kakao.maps.Map(container, options)
}

// 마커 생성
function createMarkers(banks) {
  // 기존 마커 제거
  markers.forEach(marker => marker.setMap(null))
  markers = []

  banks.forEach(bank => {
    const marker = new kakao.maps.Marker({
      position: new kakao.maps.LatLng(bank.lat, bank.lng),
    })
    marker.setMap(map)
    markers.push(marker)
  })
}

// 필터링된 은행 데이터 변경 감지
watch(
  () => props.filteredBanks,
  (newBanks) => {
    createMarkers(newBanks)
  },
  { immediate: true }
)

onMounted(() => {
  loadKakaoMap(initMap)
})
</script>

<style scoped>
/* 지도 컨테이너 스타일 */
#map {
  width: 100%;
  height: 400px;
  border: 1px solid #ddd;
}
</style>
