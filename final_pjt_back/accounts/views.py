from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import UserSerializer
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data)