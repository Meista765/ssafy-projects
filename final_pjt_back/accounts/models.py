from django.db import models
from django.contrib.auth.models import AbstractUser
from finances.models import DepositProducts, SavingsProducts

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
    ]
    
    INVESTMENT_STYLE_CHOICES = [
        ('conservative', '안정형'),
        ('moderate', '중립형'),
        ('aggressive', '공격형'),
    ]

    INCOME_CHOICES = [
        ('0', '~2000만원'),
        ('1', '2000만원~3500만원'),
        ('2', '3500만원~5000만원'),
        ('3', '5000만원~7000만원'),
        ('4', '7000만원~1억원'),
        ('5', '1억원~'),
    ]

    # 기본 정보
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=15, null=True)
    
    # 금융 관련 정보
    investment_style = models.CharField(max_length=20, choices=INVESTMENT_STYLE_CHOICES, null=True)
    annual_income = models.CharField(max_length=1, choices=INCOME_CHOICES, null=True)
    savings_goal = models.IntegerField(null=True)  # 목표 저축액
    
    # 가입한 상품들
    deposit_products = models.ManyToManyField(DepositProducts, related_name='users', blank=True)
    savings_products = models.ManyToManyField(SavingsProducts, related_name='users', blank=True)
    
    # 선호도/관심사
    preferred_bank = models.CharField(max_length=100, null=True)  # 선호 은행
    preferred_saving_period = models.IntegerField(null=True)  # 선호 저축 기간(개월)
    is_mortgage_needed = models.BooleanField(default=False)  # 주택담보대출 필요 여부