<template>
  <div>
    <div id="map" class="map-container"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import siGunGu from '@/assets/si-gun-gu.json'

const props = defineProps({
  searchParams: {
    type: Object,
    required: true,
    default: () => ({})
  }
})

const map = ref(null)
const polygon = ref(null)
const markers = ref([])
const openInfowindow = ref(null)

// 카카오맵 API 로드
const loadKakaoMapScript = () => {
  return new Promise((resolve) => {
    if (window.kakao && window.kakao.maps) {
      resolve()
      return
    }

    const script = document.createElement('script')
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${import.meta.env.VITE_KAKAO_MAP_API_KEY}&libraries=services&autoload=false`
    script.onload = () => {
      window.kakao.maps.load(() => {
        resolve()
      })
    }
    document.head.appendChild(script)
  })
}

// 지도 초기화
onMounted(async () => {
  await loadKakaoMapScript()
  const container = document.getElementById('map')
  const options = {
    center: new window.kakao.maps.LatLng(36.2683, 127.6358),
    level: 13
  }
  map.value = new window.kakao.maps.Map(container, options)
})

// 검색 파라미터 변경 감지
watch(() => props.searchParams, async (newParams) => {
  if (!newParams || !newParams.city) return

  // 기존 폴리곤과 마커 제거
  clearOverlays()

  // 시/군/구 영역 폴리곤 표시
  const cityFeature = siGunGu.features.find(
    feature => feature.properties.SIG_KOR_NM === newParams.city
  )

  if (cityFeature) {
    drawPolygon(cityFeature.geometry.coordinates[0])
    searchBanks(newParams)
  }
}, { deep: true })

// 폴리곤 그리기
const drawPolygon = (coordinates) => {
  const path = coordinates.map(coord => 
    new window.kakao.maps.LatLng(coord[1], coord[0])
  )

  polygon.value = new window.kakao.maps.Polygon({
    path: path,
    strokeWeight: 2,
    strokeColor: '#004c80',
    strokeOpacity: 0.8,
    fillColor: '#fff',
    fillOpacity: 0.3
  })

  polygon.value.setMap(map.value)

  // 폴리곤 영역으로 지도 이동
  const bounds = new window.kakao.maps.LatLngBounds()
  path.forEach(point => bounds.extend(point))
  map.value.setBounds(bounds)
}

// 은행 검색
const searchBanks = async (params) => {
  const ps = new window.kakao.maps.services.Places()
  
  const searchOptions = {
    location: map.value.getCenter(),
    bounds: map.value.getBounds(),
    category_group_code: 'BK9'
  }

  ps.keywordSearch(`${params.bank}`, (data, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      // ATM, 365 키워드 제외
      const filteredData = data.filter(place => 
        !place.place_name.includes('ATM') && 
        !place.place_name.includes('365') &&
        place.category_group_code === 'BK9'
      )

      // 마커 생성
      filteredData.forEach(place => {
        const marker = new window.kakao.maps.Marker({
          position: new window.kakao.maps.LatLng(place.y, place.x),
          map: map.value
        })

        // 인포윈도우 생성
        const infowindow = new window.kakao.maps.InfoWindow({
          content: `<div style="padding:5px;font-size:12px;">${place.place_name}</div>`
        })

        // 마커 클릭 이벤트
        window.kakao.maps.event.addListener(marker, 'click', () => {
          // 이미 열린 인포윈도우가 있다면 닫기
          if (openInfowindow.value) {
            openInfowindow.value.close()
          }
          // 현재 클릭한 마커의 인포윈도우 열기
          infowindow.open(map.value, marker)
          // 현재 열린 인포윈도우 저장
          openInfowindow.value = infowindow
        })

        markers.value.push({ marker, infowindow })
      })
    }
  }, searchOptions)
}

// 오버레이 초기화
const clearOverlays = () => {
  if (polygon.value) {
    polygon.value.setMap(null)
  }
  // 열린 인포윈도우가 있다면 닫기
  if (openInfowindow.value) {
    openInfowindow.value.close()
    openInfowindow.value = null
  }
  markers.value.forEach(({ marker, infowindow }) => {
    marker.setMap(null)
    infowindow.close()
  })
  markers.value = []
}
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 700px;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>