import requests
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (DepositOptions, DepositProducts, 
                     InstallmentOptions, InstallmentProducts)
from .serializers import (CombinedProductSerializer, 
                          DepositOptionsSerializer,
                          DepositProductsSerializer,
                          InstallmentOptionsSerializer,
                          InstallmentProductsSerializer)

API_KEY = "cf2af1fd5c5757c7329be2745173eb9e"


# API를 활용해 데이터 수집
# 정기 예금 상품
@api_view(["GET"])
def save_deposits(request):
    # 데이터 가져오기
    params = {
        "auth": API_KEY,
        "topFinGrpNo": "020000",
        "pageNo": 1,
    }
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
    response = requests.get(url, params=params).json()
    baseList = response.get("result").get("baseList")
    optionList = response.get("result").get("optionList")

    # 원하는 필드 추출(product)
    for base in baseList:
        dcls_month      = base.get("dcls_month")
        fin_co_no       = base.get("fin_co_no")
        fin_prdt_cd     = base.get("fin_prdt_cd")
        kor_co_nm       = base.get("kor_co_nm")
        fin_prdt_nm     = base.get("fin_prdt_nm")
        join_way        = base.get("join_way")
        mtrt_int        = base.get("mtrt_int")
        spcl_cnd        = base.get("spcl_cnd")
        join_deny       = base.get("join_deny")
        join_member     = base.get("join_member")
        etc_note        = base.get("etc_note")
        max_limit       = base.get("max_limit") if base.get("max_limit") is not None else -1
        dcls_strt_day   = base.get("dcls_strt_day")
        dcls_end_day    = base.get("dcls_end_day")
        fin_co_subm_day	= base.get("fin_co_subm_day")

        if DepositProducts.objects.filter(
            dcls_month=dcls_month,
            fin_co_no=fin_co_no,
            fin_prdt_cd=fin_prdt_cd,
        ).exists():
            continue

        save_base_data = {
            "dcls_month"      : dcls_month,
            "fin_co_no"       : fin_co_no,
            "fin_prdt_cd"     : fin_prdt_cd,
            "kor_co_nm"       : kor_co_nm,
            "fin_prdt_nm"     : fin_prdt_nm,
            "join_way"        : join_way,
            "mtrt_int"        : mtrt_int,
            "spcl_cnd"        : spcl_cnd,
            "join_deny"       : join_deny,
            "join_member"     : join_member,
            "etc_note"        : etc_note,
            "max_limit"       : max_limit,
            "dcls_strt_day"   : dcls_strt_day,
            "dcls_end_day"    : dcls_end_day,
            "fin_co_subm_day" : fin_co_subm_day,
        }

        serializer = DepositProductsSerializer(data=save_base_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 원하는 필드 추출(option)
    for option in optionList:
        dcls_month        = option.get("dcls_month")
        fin_co_no         = option.get("fin_co_no")
        fin_prdt_cd       = option.get("fin_prdt_cd")
        intr_rate_type    = option.get("intr_rate_type")
        intr_rate_type_nm = option.get("intr_rate_type_nm")
        save_trm          = option.get("save_trm")
        intr_rate         = option.get("intr_rate") if option.get("intr_rate") is not None else -1
        intr_rate2        = option.get("intr_rate2") if option.get("intr_rate2") is not None else -1

        if DepositOptions.objects.filter(
            dcls_month=dcls_month,
            fin_co_no=fin_co_no,
            fin_prdt_cd=fin_prdt_cd,
            intr_rate_type=intr_rate_type,
            save_trm=save_trm,
        ).exists():
            continue

        save_option_data = {
            "dcls_month"        : dcls_month,
            "fin_co_no"         : fin_co_no,
            "fin_prdt_cd"       : fin_prdt_cd,
            "intr_rate_type"    : intr_rate_type,
            "intr_rate_type_nm" : intr_rate_type_nm,
            "save_trm"          : save_trm,
            "intr_rate"         : intr_rate,
            "intr_rate2"        : intr_rate2,
        }

        serializer = DepositOptionsSerializer(data=save_option_data)
        if serializer.is_valid():
            product = DepositProducts.objects.get(
                dcls_month=dcls_month,
                fin_co_no=fin_co_no,
                fin_prdt_cd=fin_prdt_cd,
            )
            serializer.save(product=product)
    
    rtn_data = {
        "category": "예금",
        "prdt_count": DepositProducts.objects.count(),
        "opt_count": DepositOptions.objects.count(),
    }
    
    return JsonResponse(data=rtn_data, status=status.HTTP_200_OK)

# 정기 적금 상품
@api_view(["GET"])
def save_installments(request):
    # 데이터 가져오기
    params = {
        "auth": API_KEY,
        "topFinGrpNo": "020000",
        "pageNo": 1,
    }
    url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json"
    response = requests.get(url, params=params).json()
    baseList = response.get("result").get("baseList")
    optionList = response.get("result").get("optionList")

    for base in baseList:
        dcls_month      = base.get("dcls_month")
        fin_co_no       = base.get("fin_co_no")
        fin_prdt_cd     = base.get("fin_prdt_cd")
        kor_co_nm       = base.get("kor_co_nm")
        fin_prdt_nm     = base.get("fin_prdt_nm")
        join_way        = base.get("join_way")
        mtrt_int        = base.get("mtrt_int")
        spcl_cnd        = base.get("spcl_cnd")
        join_deny       = base.get("join_deny")
        join_member     = base.get("join_member")
        etc_note        = base.get("etc_note")
        max_limit       = base.get("max_limit") if base.get("max_limit") is not None else -1
        dcls_strt_day   = base.get("dcls_strt_day")
        dcls_end_day    = base.get("dcls_end_day")
        fin_co_subm_day	= base.get("fin_co_subm_day")

        if InstallmentProducts.objects.filter(
            dcls_month=dcls_month,
            fin_co_no=fin_co_no,
            fin_prdt_cd=fin_prdt_cd,
        ).exists():
            continue

        save_base_data = {
            "dcls_month"      : dcls_month,
            "fin_co_no"       : fin_co_no,
            "fin_prdt_cd"     : fin_prdt_cd,
            "kor_co_nm"       : kor_co_nm,
            "fin_prdt_nm"     : fin_prdt_nm,
            "join_way"        : join_way,
            "mtrt_int"        : mtrt_int,
            "spcl_cnd"        : spcl_cnd,
            "join_deny"       : join_deny,
            "join_member"     : join_member,
            "etc_note"        : etc_note,
            "max_limit"       : max_limit,
            "dcls_strt_day"   : dcls_strt_day,
            "dcls_end_day"    : dcls_end_day,
            "fin_co_subm_day" : fin_co_subm_day,
        }

        serializer = InstallmentProductsSerializer(data=save_base_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 원하는 필드 추출(option)
    for option in optionList:
        dcls_month        = option.get("dcls_month")
        fin_co_no         = option.get("fin_co_no")
        fin_prdt_cd       = option.get("fin_prdt_cd")
        intr_rate_type    = option.get("intr_rate_type")
        intr_rate_type_nm = option.get("intr_rate_type_nm")
        rsrv_type         = option.get("rsrv_type")
        rsrv_type_nm      = option.get("rsrv_type_nm")
        save_trm          = option.get("save_trm")
        intr_rate         = option.get("intr_rate") if option.get("intr_rate") is not None else -1
        intr_rate2        = option.get("intr_rate2") if option.get("intr_rate2") is not None else -1

        if InstallmentOptions.objects.filter(
            dcls_month=dcls_month,
            fin_co_no=fin_co_no,
            fin_prdt_cd=fin_prdt_cd,
            intr_rate_type=intr_rate_type,
            save_trm=save_trm,
        ).exists():
            continue

        save_option_data = {
            "dcls_month"        : dcls_month,
            "fin_co_no"         : fin_co_no,
            "fin_prdt_cd"       : fin_prdt_cd,
            "intr_rate_type"    : intr_rate_type,
            "intr_rate_type_nm" : intr_rate_type_nm,
            "rsrv_type"         : rsrv_type,
            "rsrv_type_nm"      : rsrv_type_nm,
            "save_trm"          : save_trm,
            "intr_rate"         : intr_rate,
            "intr_rate2"        : intr_rate2,
        }

        serializer = InstallmentOptionsSerializer(data=save_option_data)
        if serializer.is_valid():
            product = InstallmentProducts.objects.get(
                dcls_month=dcls_month,
                fin_co_no=fin_co_no,
                fin_prdt_cd=fin_prdt_cd,
            )
            serializer.save(product=product)

    rtn_data = {
        "category": "적금",
        "prdt_count": InstallmentProducts.objects.count(),
        "opt_count": InstallmentOptions.objects.count(),
    }
    
    return JsonResponse(data=rtn_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_products_infos(request):
    # 예/적금 데이터 쿼리, FK로 연결된 옵션 데이터도 prefetch
    deposit_products = DepositProducts.objects.prefetch_related('options').all()
    installment_products = InstallmentProducts.objects.prefetch_related('options').all()
    
    deposit_data = CombinedProductSerializer(deposit_products, many=True).data
    installment_data = CombinedProductSerializer(installment_products, many=True).data

    data = dict()
    status_info = None
    
    if deposit_data or installment_data:
        data['status'] = 'success'
        data['prdt_data'] = deposit_data + installment_data
        status_info = status.HTTP_200_OK
    else:
        data['status'] = 'error'
        data['prdt_data'] = []
        data['message'] = 'DB에 데이터가 없습니다.'
        status_info = status.HTTP_404_NOT_FOUND
    
    return JsonResponse(data=data, status=status_info)    
    