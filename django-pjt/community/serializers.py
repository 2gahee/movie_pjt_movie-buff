from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):
    class ArticleUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = UserModel
            fields = ('username',)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    user = ArticleUserSerializer(read_only=True)
    comment_count = serializers.SerializerMethodField()
    def get_comment_count(self, obj):
        return Comment.objects.filter(article=obj).count()
    class LikeUserSerializer(serializers.ModelSerializer):
        likes_count = serializers.SerializerMethodField()
        class Meta:
            model = UserModel
            fields = ('username','likes_count',)
        def get_likes_count(self, obj):
            return obj.like_users.count()
    class Meta:
        model = Article
        fields = '__all__'
        extra_fields = ['comment_count']

class ArticleSerializer(serializers.ModelSerializer):
    class ArticleUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = UserModel
            fields = ('username',)
    user = ArticleUserSerializer(read_only=True)
    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = UserModel
            fields = ('username',)
    like_users = LikeUserSerializer(many=True, read_only=True)

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class CommentDetailSerializer(serializers.ModelSerializer):
        created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
        class CommentUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = UserModel
                fields = ('username',)
        user = CommentUserSerializer(read_only=True)
        class Meta:
            model = Comment
            fields = '__all__'
    
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):
    class CommentUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = UserModel
            fields = ('username',)
    user = CommentUserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)