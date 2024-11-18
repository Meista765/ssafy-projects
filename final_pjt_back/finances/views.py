import requests
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import DepositProducts, DepositOptions, SavingsOptions, SavingsProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingsOptionSerializer, SavingsProductsSerializer


API_KEY = "cf2af1fd5c5757c7329be2745173eb9e"

# API를 활용해 데이터 수집
# 정기 예금 상품
@api_view(['GET'])
def save_deposit_products(request):
    # 데이터 가져오기 
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo':1,
    }
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    response = requests.get(url,params=params).json()
    baseList = response.get('result').get('baseList')
    optionList = response.get('result').get('optionList')

    # 원하는 필드 추출(product)
    count = 0
    for base in baseList:
        fin_prdt_cd = base.get('fin_prdt_cd')
        kor_co_nm = base.get('kor_co_nm')
        fin_prdt_nm = base.get('fin_prdt_nm')
        etc_note = base.get('etc_note')
        join_deny = base.get('join_deny')
        join_member = base.get('join_member')
        join_way = base.get('join_way')
        spcl_cnd = base.get('spcl_cnd')

        if DepositProducts.objects.filter(
            fin_prdt_cd=fin_prdt_cd, kor_co_nm=kor_co_nm, fin_prdt_nm=fin_prdt_nm, etc_note=etc_note,
            join_deny=join_deny, join_member=join_member, join_way=join_way, spcl_cnd=spcl_cnd
        ).exists():
            continue

        save_base_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }

        serializer = DepositProductsSerializer(data=save_base_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            

    

    # 원하는 필드 추출(option)
    for option in optionList:
        fin_prdt_cd = option.get('fin_prdt_cd')
        intr_rate_type_nm = option.get('intr_rate_type_nm')
        intr_rate = option.get('intr_rate') if option.get('intr_rate') != None else -1 
        intr_rate2 = option.get('intr_rate2') if option.get('intr_rate2') != None else -1
        save_trm = option.get('save_trm')



        if DepositOptions.objects.filter(
            fin_prdt_cd=fin_prdt_cd, intr_rate_type_nm=intr_rate_type_nm, intr_rate=intr_rate,
            intr_rate2=intr_rate2, save_trm=save_trm
        ).exists():
            continue

        save_option_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,

        }

        serializer = DepositOptionsSerializer(data=save_option_data)
        if serializer.is_valid():
            product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            serializer.save(product=product)
            count+=1

        
    return JsonResponse({'message':'저장 성공', 'count':count})


# 정기 적금 상품
@api_view(['GET'])
def save_savings_products(request):
    # 데이터 가져오기 
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo':1,
    }
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
    response = requests.get(url,params=params).json()
    baseList = response.get('result').get('baseList')
    optionList = response.get('result').get('optionList')


    count = 0
    for base in baseList:
        fin_prdt_cd = base.get('fin_prdt_cd')
        kor_co_nm = base.get('kor_co_nm')
        fin_prdt_nm = base.get('fin_prdt_nm')
        etc_note = base.get('etc_note')
        join_deny = base.get('join_deny')
        join_member = base.get('join_member')
        join_way = base.get('join_way')
        spcl_cnd = base.get('spcl_cnd')

        if SavingsProducts.objects.filter(
            fin_prdt_cd=fin_prdt_cd, kor_co_nm=kor_co_nm, fin_prdt_nm=fin_prdt_nm, etc_note=etc_note,
            join_deny=join_deny, join_member=join_member, join_way=join_way, spcl_cnd=spcl_cnd
        ).exists():
            continue

        save_base_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }

        serializer = SavingsProductsSerializer(data=save_base_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            

    

    # 원하는 필드 추출(option)
    for option in optionList:
        fin_prdt_cd = option.get('fin_prdt_cd')
        intr_rate_type_nm = option.get('intr_rate_type_nm')
        intr_rate = option.get('intr_rate') if option.get('intr_rate') != None else -1 
        intr_rate2 = option.get('intr_rate2') if option.get('intr_rate2') != None else -1
        save_trm = option.get('save_trm')
        rsrv_type = option.get('rsrv_type')                         
        rsrv_type_nm = option.get('rsrv_type_nm')


        if SavingsOptions.objects.filter(
            fin_prdt_cd=fin_prdt_cd, intr_rate_type_nm=intr_rate_type_nm, intr_rate=intr_rate,
            intr_rate2=intr_rate2, save_trm=save_trm, rsrv_type=rsrv_type, rsrv_type_nm=rsrv_type_nm
        ).exists():
            continue

        save_option_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
            'rsrv_type':rsrv_type,
            'rsrv_type_nm':rsrv_type_nm
        }

        serializer = SavingsOptionSerializer(data=save_option_data)
        if serializer.is_valid():
            product = SavingsProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            serializer.save(product=product)
            count+=1

        
    return JsonResponse({'message':'저장 성공', 'count':count})