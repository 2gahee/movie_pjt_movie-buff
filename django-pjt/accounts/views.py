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

# from .forms import CustomUserCreationForm

@api_view(['POST'])
@permission_classes(['AllowAny'])
def signup(request):
    serializer = CustomRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Signup successful!'}, status=201)
    return Response(serializer.errors, status=400)


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class Profile(APIView):
    # 올바른 permission_classes 설정
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def get(self, request):
        user = request.user
        data = {
            "username": user.username,
            "nickname": user.nickname,
            "email": user.email,
        }
        return Response(data)

    def put(self, request):
        user = request.user
        data = request.data
        
        # 수정할 필드 가져오기
        username = data.get('username', user.username)
        nickname = data.get('nickname', user.nickname)
        email = data.get('email', user.email)
        password = data.get('password', None)

        # 사용자 정보 업데이트
        user.username = username
        user.nickname = nickname
        user.email = email

        # 비밀번호가 변경된 경우에는 반드시 해싱하여 저장
        if password:
            user.set_password(password)  # 비밀번호는 set_password로 설정해야 해싱됨
        user.save()

        # 업데이트된 사용자 정보 반환
        updated_data = {
            "username": user.username,
            "nickname": user.nickname,
            "email": user.email,
            "password": user.password
        }

        return Response(updated_data, status=status.HTTP_200_OK)

