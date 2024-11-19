import requests

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def get_and_response_exchange_rates(request):
    external_api_url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON" # 외부 API 엔드포인트
    authkey = "6N3X7TgXvz1cD1f9i6sxIHeuTKFH611J"                                         # API 인증키 <- 향후 숨김처리 필요
    # 필요한 쿼리 파라미터
    params = {
        "authkey": authkey,  # 인증키: OpenAPI 신청시 발급된 인증키
        "data": "AP01",      # 검색요청API타입: AP01 : 환율, AP02 : 대출금리, AP03 : 국제금리
    }

    try:
        # GET 요청에 params 추가
        response = requests.get(external_api_url, params=params, timeout=10)
        response.raise_for_status()  # 상태 코드 체크 (200 OK 이외의 response에 대해 에러 발생)

        # 외부 API에서 반환된 JSON 데이터
        exchange_rates_data = response.json()

        # 응답 데이터 구성
        data = {
            "status": "success",
            "exchange_rates_data": exchange_rates_data,  # 외부 API 데이터 포함
        }

    except requests.exceptions.RequestException as e:
        # 에러 처리
        data = {
            "status": "error",
            "message": str(e),
        }

    # JSON 응답 반환
    return JsonResponse(data)
