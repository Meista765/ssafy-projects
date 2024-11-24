from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
# Create your views here.

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
        serializer = UserSerializer(user)
        return Response(serializer.data)
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