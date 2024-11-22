from rest_framework import serializers
from .models import DepositOptions, DepositProducts, InstallmentOptions, InstallmentProducts

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

class InstallmentProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentProducts
        fields = '__all__'

class InstallmentOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentOptions
        fields = '__all__'
        read_only_fields = ('product',)

# 예금 상세 정보 시리얼라이저
class DepositDetailSerializer(serializers.ModelSerializer):
    options = DepositOptionsSerializer(many=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'

# 적금 상세 정보 시리얼라이저   
class InstallmentDetailSerializer(serializers.ModelSerializer):
    options = InstallmentOptionsSerializer(many=True)

    class Meta:
        model = InstallmentProducts
        fields = '__all__'

