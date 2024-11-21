from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_user),                           # 현재 유저 정보 조회
    path('detail/<int:user_pk>/', views.detail_user)        # 회원 탈퇴
]
