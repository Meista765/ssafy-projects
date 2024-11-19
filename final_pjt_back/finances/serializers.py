from rest_framework import serializers
from .models import DepositOptions, DepositProducts, InstallmentOptions, InstallmentProducts

# 정기 예금 저장
class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

# 정기 예금 상품 옵션 저장
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

# 적금 상품 저장
class InstallmentProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentProducts
        fields = '__all__'

# 적금 상품 옵션 저장
class SavingsOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentOptions
        fields = '__all__'
        read_only_fields = ('product',)
