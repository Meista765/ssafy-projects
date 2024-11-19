from rest_framework import serializers
from .models import Article,Comment

# 게시글 조회
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')

# 게시글 생성
class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('user', 'content',)

    # # 역참조 데이터 override
    comment = CommentDetailSerializer(read_only=True, many=True)
    comment_count = serializers.IntegerField(source='comment.count', read_only=True)
    like_count = serializers.IntegerField(source='like_articles.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        

# 댓글 생성
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article')
