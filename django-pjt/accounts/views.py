from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from .serializers import CustomRegisterSerializer
from movies.models import UserMovie
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

# from .forms import CustomUserCreationForm

@api_view(['POST'])
@permission_classes(['AllowAny'])
def signup(request):
    serializer = CustomRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Signup successful!'}, status=201)
    return Response(serializer.errors, status=400)


# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status

class Profile(APIView):
    # 올바른 permission_classes 설정
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def get(self, request):
        user = request.user
        data = {
            "username": user.username,
            "nickname": user.nickname,
            "email": user.email,
            "password": "******",
        }
        return Response(data, status=status.HTTP_200_OK)

# 회원정보 수정
class ProfileUpdate(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def put(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # 입력값 가져오기
        nickname = data.get('nickname', user.nickname)
        current_password = data.get('current_password')
        new_password = data.get('new_password')

        # 닉네임 업데이트
        user.nickname = nickname

        # 비밀번호 확인 및 업데이트
        if current_password and new_password:
            if not user.check_password(current_password):
                return JsonResponse({
                    'success': False,
                    'errors': {'current_password': '현재 비밀번호가 올바르지 않습니다.'}
                }, status=400)
            
            if len(new_password) < 8:
                return JsonResponse({
                    'success': False,
                    'errors': {'new_password': '비밀번호는 8자 이상이어야 합니다.'}
                }, status=400)
            
            user.password = make_password(new_password)

        # 저장
        user.save()

        return JsonResponse({
            'success': True,
            'message': '프로필이 성공적으로 업데이트되었습니다.'
        }, status=200)
