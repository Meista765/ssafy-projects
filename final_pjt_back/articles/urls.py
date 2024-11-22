from django.urls import path
from . import views

urlpatterns = [
    # 게시글 조회 및 생성
    path('', views.article_list),

    # GET: 게시글 상세 조회
    # DELETE: 게시글 삭제
    # PUT: 게시글 수정 
    path('<int:article_pk>/', views.article_detail),

    # 댓글 생성
    path('<int:article_pk>/comments/', views.comment_create),

    # 댓글 수정 및 삭제
    path('comments/<int:comment_pk>/', views.comment_detail)
]