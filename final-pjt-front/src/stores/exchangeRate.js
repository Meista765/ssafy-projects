import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeRateStore = defineStore(
  'exchangeRate',
  () => {
    const API_KEY = '6N3X7TgXvz1cD1f9i6sxIHeuTKFH611J'
    const exchangeRates = ref([])

    // create URL
    const url = new URL(
      'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    )
    url.searchParams.append('authkey', API_KEY) // 인증키: OpenAPI 신청시 발급된 인증키
    url.searchParams.append('data', 'AP01')     // 검색요청API타입: AP01 : 환율, AP02 : 대출금리, AP03 : 국제금리
    // url.searchParams.append('searchdata', [값]) // 검색요청날짜: ex) 2015-01-01, 20150101, (DEFAULT)현재일
    

    const getExchangeRate = () => {
      axios
        .get(url.toString())
        .then(res => {
          exchangeRates.value = res.data
          console.log(exchangeRates);
          
        })
        .catch((err) => console.log(err))
    }

    return { getExchangeRate }
  },
  { persist: true }
)
