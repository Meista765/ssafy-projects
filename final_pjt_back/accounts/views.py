# Django
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Local
from .serializers import UserSerializer
from finances.serializers import DepositDetailSerializer, InstallmentDetailSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    

@api_view(['GET','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def detail_user(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        deposit_serializer = DepositDetailSerializer(user.deposit_products.all(), many=True)
        savings_serializer = InstallmentDetailSerializer(user.savings_products.all(), many=True)
        data = {
            'user': user_serializer.data,
            'deposit': deposit_serializer.data,
            'installments': savings_serializer.data,
        }
        return JsonResponse(data)

    elif request.method == 'DELETE':
        if request.user.pk != user.pk:
            return Response({'msg': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    elif request.method == 'PUT':
        if request.user.pk != user.pk:
            return Response({'msg': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)