# 표준 라이브러리
import requests

# Django & DRF
from django.http import JsonResponse
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view

# Local imports
from .models import (
    DepositOptions,
    DepositProducts,
    InstallmentOptions,
    InstallmentProducts,
)
from .serializers import (
    CombinedProductSerializer,
    DepositOptionsSerializer,
    DepositProductsSerializer,
    InstallmentOptionsSerializer,
    InstallmentProductsSerializer,
)

# API_KEY 환경변수에서 가져오기
API_KEY = settings.FINLIFE_API_KEY


# API를 활용해 데이터 수집
# 정기 예금 상품
@api_view(["GET"])
def save_deposits(request):
    params = {
        "auth": API_KEY,
        "topFinGrpNo": "020000",
        "pageNo": 1,
    }
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
    
    response = requests.get(url, params=params).json()
    result = response.get("result")
    
    if not result:
        return JsonResponse({"error": "API 응답에 result가 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
    baseList = result.get("baseList", [])
    optionList = result.get("optionList", [])
    
    if not baseList or not optionList:
        return JsonResponse({"error": "데이터가 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
    # 상품 정보 저장
    for base in baseList:
        if DepositProducts.objects.filter(
            dcls_month=base.get("dcls_month"),
            fin_co_no=base.get("fin_co_no"),
            fin_prdt_cd=base.get("fin_prdt_cd"),
        ).exists():
            continue

        serializer = DepositProductsSerializer(data=base)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 옵션 정보 저장
    for option in optionList:
        if DepositOptions.objects.filter(
            dcls_month=option.get("dcls_month"),
            fin_co_no=option.get("fin_co_no"),
            fin_prdt_cd=option.get("fin_prdt_cd"),
            intr_rate_type=option.get("intr_rate_type"),
            save_trm=option.get("save_trm"),
        ).exists():
            continue

        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid():
            product = DepositProducts.objects.get(
                dcls_month=option.get("dcls_month"),
                fin_co_no=option.get("fin_co_no"),
                fin_prdt_cd=option.get("fin_prdt_cd"),
            )
            serializer.save(product=product)

    return JsonResponse({
        "category": "예금",
        "prdt_count": DepositProducts.objects.count(),
        "opt_count": DepositOptions.objects.count(),
    }, status=status.HTTP_200_OK)


# 정기 적금 상품
@api_view(["GET"])
def save_installments(request):
    params = {
        "auth": API_KEY,
        "topFinGrpNo": "020000",
        "pageNo": 1,
    }
    url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json"
    
    response = requests.get(url, params=params).json()
    result = response.get("result")
    
    if not result:
        return JsonResponse({"error": "API 응답에 result가 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
    baseList = result.get("baseList", [])
    optionList = result.get("optionList", [])
    
    if not baseList or not optionList:
        return JsonResponse({"error": "데이터가 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
    # 상품 정보 저장
    for base in baseList:
        if InstallmentProducts.objects.filter(
            dcls_month=base.get("dcls_month"),
            fin_co_no=base.get("fin_co_no"),
            fin_prdt_cd=base.get("fin_prdt_cd"),
        ).exists():
            continue

        serializer = InstallmentProductsSerializer(data=base)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 옵션 정보 저장
    for option in optionList:
        if InstallmentOptions.objects.filter(
            dcls_month=option.get("dcls_month"),
            fin_co_no=option.get("fin_co_no"),
            fin_prdt_cd=option.get("fin_prdt_cd"),
            intr_rate_type=option.get("intr_rate_type"),
            save_trm=option.get("save_trm"),
        ).exists():
            continue

        serializer = InstallmentOptionsSerializer(data=option)
        if serializer.is_valid():
            product = InstallmentProducts.objects.get(
                dcls_month=option.get("dcls_month"),
                fin_co_no=option.get("fin_co_no"),
                fin_prdt_cd=option.get("fin_prdt_cd"),
            )
            serializer.save(product=product)

    return JsonResponse({
        "category": "적금",
        "prdt_count": InstallmentProducts.objects.count(),
        "opt_count": InstallmentOptions.objects.count(),
    }, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_products_infos(request):
    # 예/적금 데이터 쿼리, FK로 연결된 옵션 데이터도 prefetch
    deposit_products = DepositProducts.objects.prefetch_related("options").all()
    installment_products = InstallmentProducts.objects.prefetch_related("options").all()

    deposit_data = CombinedProductSerializer(deposit_products, many=True).data
    installment_data = CombinedProductSerializer(installment_products, many=True).data

    data = dict()
    status_info = None

    if deposit_data or installment_data:
        data["status"] = "success"
        data["prdt_data"] = deposit_data + installment_data
        status_info = status.HTTP_200_OK
    else:
        data["status"] = "error"
        data["prdt_data"] = []
        data["message"] = "DB에 데이터가 없습니다."
        status_info = status.HTTP_404_NOT_FOUND

    return JsonResponse(data=data, status=status_info)
