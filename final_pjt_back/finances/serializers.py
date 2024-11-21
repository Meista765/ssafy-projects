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

# 통합 시리얼라이저 구성
class OptionSerializer(serializers.Serializer):
    save_trm = serializers.IntegerField()
    intr_rate = serializers.DecimalField(max_digits=4, decimal_places=2)

class CombinedProductSerializer(serializers.Serializer):
    category = serializers.CharField()
    dcls_month = serializers.CharField()
    kor_co_nm = serializers.CharField()
    fin_prdt_nm = serializers.CharField()
    options = OptionSerializer(many=True)

    def to_representation(self, instance):
        """
        Serializer에서 기본으로 제공하는 to_reprsentation 메소드를 오버라이드
        """
        # 변수 초기화
        category = None
        options = []
        
        if isinstance(instance, DepositProducts):
            category = '예금'
            options = DepositOptions.objects.filter(product=instance)
        elif isinstance(instance, InstallmentProducts):
            category = '적금'
            options = InstallmentOptions.objects.filter(product=instance)

        return {
            'category': category,
            'dcls_month': instance.dcls_month,
            'kor_co_nm': instance.kor_co_nm,
            'fin_prdt_nm': instance.fin_prdt_nm,
            'options': OptionSerializer(options, many=True).data,
        }
