from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

@api_view(["GET", "POST", "OPTIONS"])
@permission_classes([IsAuthenticated])
def article_list(request):
    # if request.method == 'OPTIONS':
    #     return Response(status=200)  # Preflight 요청 성공 처리
    if request.method == "GET":
        title_query = request.GET.get('title', '')
        username_query = request.GET.get('username', '')
        content_query = request.GET.get('content', '')
        if title_query:
            articles = Article.objects.filter(title__icontains=title_query)
        elif username_query:
            articles = Article.objects.filter(user__username__icontains=username_query)
        elif content_query:
            articles = Article.objects.filter(content__icontains=content_query)
        else:  # 검색 조건이 없으면 전체 리스트 반환
            articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "DELETE", "PUT"])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated]) 
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated]) 
def comment_detail(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # elif request.method == "PUT":
    #     serializer = CommentSerializer(comment, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)