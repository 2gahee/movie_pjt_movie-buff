from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article

@api_view(["GET", "POST", "OPTIONS"])
@permission_classes([IsAuthenticated])
def article_list(request):
    # if request.method == 'OPTIONS':
    #     return Response(status=200)  # Preflight 요청 성공 처리
    if request.method == "GET":
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=request.user)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    

    
