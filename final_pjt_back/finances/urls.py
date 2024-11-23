from django.urls import path
from . import views

urlpatterns = [
    # GET: 정기예금 상품 및 옵션 저장
    path('save-deposits/', views.save_deposits),

    # GET: 적금 상품 및 옵션 저장
    path('save-installments/', views.save_installments),
    
    # GET: 예적금 상품 정보 조회
    path('infos/', views.get_products_infos),

    # POST: 예적금 상품 구독
    path('subscribe/', views.subscribe_financial_product),

    # GET: 상품 상세 정보 조회
    path('infos/<str:product_id>/', views.get_product_detail),
]