# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

# Local
from .models import Article, Comment
from .serializers import (
    ArticleListSerializer,
    ArticleSerializer,
    ArticleDetailSerializer,
    CommentSerializer
)


# 게시글 전체 조회 및 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(
                {'detail': '게시글을 작성하려면 로그인이 필요합니다.'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# GET: 게시글 상세 조회
# DELETE: 게시글 삭제
# PUT: 게시글 수정 
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_detail(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        print(request.user)
        print('=======')
        print(article.user)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 댓글 수정 및 삭제
@api_view(['DELETE','PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)