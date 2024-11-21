"""
URL configuration for final_pjt_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # GET: 정기예금 상품 및 옵션 저장
    path('save-deposits/', views.save_deposits),

    # GET: 적금 상품 및 옵션 저장
    path('save-installments/', views.save_installments),
    
    # GET: 적금 상품 및 옵션 저장
    path('get_products_infos/', views.get_products_infos),

]