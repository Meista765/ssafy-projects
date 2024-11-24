# Python Standard Library
import requests

# Django
from django.http import JsonResponse
from django.conf import settings

# Django REST Framework
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Local
from .models import (
    DepositOptions,
    DepositProducts,
    InstallmentOptions,
    InstallmentProducts,
)
from .serializers import (
    DepositProductsSerializer,
    DepositOptionsSerializer,
    DepositDetailSerializer,
    InstallmentProductsSerializer,
    InstallmentOptionsSerializer,
    InstallmentDetailSerializer,
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
    url = f"{settings.FINANCE_API_URL}/depositProductsSearch.json"
    
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
    url = f"{settings.FINANCE_API_URL}/installmentProductsSearch.json"
    
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

    # 각각의 시리얼라이저로 데이터 변환
    deposit_data = DepositDetailSerializer(deposit_products, many=True).data
    installment_data = InstallmentDetailSerializer(installment_products, many=True).data

    # 각 데이터에 카테고리와 새로운 pk 추가
    for idx, item in enumerate(deposit_data):
        item['category'] = '예금'
        item['unique_id'] = f'dep_{item["id"]}'  # dep_1, dep_2 형식
    
    for idx, item in enumerate(installment_data):
        item['category'] = '적금'
        item['unique_id'] = f'ins_{item["id"]}'  # ins_1, ins_2 형식

    data = dict()
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


# 예적금 상품 구독
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def subscribe_financial_product(request):
    category = request.data.get("category")
    pk = request.data.get("id")
    
    # 카테고리별 모델과 관계 매핑
    product_map = {
        "dep": (DepositProducts, "deposit_products"),
        "ins": (InstallmentProducts, "installment_products"),
    }
    
    if category not in product_map:
        return JsonResponse({"error": "잘못된 카테고리입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
    try:
        Model, relation_name = product_map[category]
        product = Model.objects.get(pk=pk)
        user_products = getattr(request.user, relation_name)
        
        # 구독 토글
        if user_products.filter(pk=pk).exists():
            user_products.remove(product)
            message = "구독 취소"
        else:
            user_products.add(product)
            message = "구독 완료"
            
        return JsonResponse({"message": message}, status=status.HTTP_200_OK)
        
    except Model.DoesNotExist:
        return JsonResponse({"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_product_detail(request, product_id):
    category = product_id[:3]
    pk = int(product_id.split('_')[1])
    
    try:
        if category == 'dep':
            product = DepositProducts.objects.prefetch_related('options').get(pk=pk)
            serializer = DepositDetailSerializer(product)
        elif category == 'ins':
            product = InstallmentProducts.objects.prefetch_related('options').get(pk=pk)
            serializer = InstallmentDetailSerializer(product)
        else:
            return JsonResponse({'error': '잘못된 카테고리입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = serializer.data
        data['category'] = '��금' if category == 'dep' else '적금'
        data['unique_id'] = product_id
        
        # 구독 여부 확인
        if request.user.is_authenticated:
            if category == 'dep':   
                data['is_subscribed'] = request.user.deposit_products.filter(pk=pk).exists()
            else:
                data['is_subscribed'] = request.user.installment_products.filter(pk=pk).exists()
        
        return Response(data, status=status.HTTP_200_OK)
    except (DepositProducts.DoesNotExist, InstallmentProducts.DoesNotExist):
        return JsonResponse({'error': '상품을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)