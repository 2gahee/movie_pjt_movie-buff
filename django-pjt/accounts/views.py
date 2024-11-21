from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from .serializers import CustomRegisterSerializer
from movies.models import UserMovie

# from .forms import CustomUserCreationForm

@api_view(['POST'])
@permission_classes(['AllowAny'])
def signup(request):
    serializer = CustomRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Signup successful!'}, status=201)
    return Response(serializer.errors, status=400)
