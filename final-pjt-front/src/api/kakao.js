import axios from 'axios'

const KAKAO_REST_API_KEY = '1648197d9faa32d265464414e7218dc4'

const kakaoApi = axios.create({
  baseURL: 'https://dapi.kakao.com/v2/local/search',
  headers: {
    Authorization: `KakaoAK ${KAKAO_REST_API_KEY}`,
  },
})

// 은행 리스트 검색
async function fetchAllBanks() {
  const results = []
  let page = 1
  const maxResultsPerPage = 15 // Kakao API 한 페이지 최대 아이템 수

  while (true) {
    try {
      const response = await kakaoApi.get('/keyword.json', {
        params: {
          query: '은행',
          category_group_code: 'BK9',
          size: maxResultsPerPage,
          page,
        },
      })
      console.log(response)

      const data = response.data.documents
      const meta = response.data.meta

      // 현재 페이지 결과 추가
      results.push(...data)
      console.log(`Fetched page ${page}, items: ${data.length}`)

      // 다음 페이지가 없으면 종료
      if (meta.is_end) break

      page++
    } catch (error) {
      console.error(`Failed to fetch page ${page}:`, error.message)
      break
    }
  }
  return results
}

// 은행 데이터 로드
export async function loadBanks() {
  const cachedBanks = localStorage.getItem('banks')
  if (cachedBanks) {
    // 로컬스토리지에서 데이터 가져오기
    return JSON.parse(cachedBanks)
  } else {
    // REST API로 은행 데이터 가져오기
    const banks = await fetchAllBanks()
    localStorage.setItem('banks', JSON.stringify(banks)) // 로컬스토리지에 저장
    return banks
  }
}
