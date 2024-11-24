from rest_framework import serializers
from .models import Article, Comment
from django.conf import settings
from django.contrib.auth import get_user_model



# 게시글 조회
class ArticleListSerializer(serializers.ModelSerializer):    
    class CustomUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('first_name','last_name')

    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ("id", "title", "content",'created_at','user')


# 댓글 상세
class CommentDetailSerializer(serializers.ModelSerializer):
    # 댓글 작성자 id 추가
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    # 댓글 작성자의 username 추가
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ("content", "username", "updated_at", "user_id", "id",)


# 게시글 상세 조회
class ArticleDetailSerializer(serializers.ModelSerializer):

    comment = CommentDetailSerializer(read_only=True, many=True)
    username = serializers.CharField(source="user.username", read_only=True)
    comment_count = serializers.IntegerField(source="comment.count", read_only=True)
    like_count = serializers.IntegerField(source="like_articles.count", read_only=True)

    class Meta:
        model = Article
        fields = "__all__"


# 게시글 생성
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("user", "like_users")


# 댓글 생성
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = (
            "user",
            "article",
        )
