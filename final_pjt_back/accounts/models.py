from django.db import models
from django.contrib.auth.models import AbstractUser
from finances.models import DepositProducts, InstallmentProducts

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

    SAVINGS_GOALS_CHOICES = [
        ('0', '~100만원'),
        ('1', '100만원~1000만원'),
        ('2', '1000만원~5000만원'),
        ('3', '5000만원~7000만원'),
        ('4', '7000만원~1억원'),
        ('5', '1억원~'), 
    ]

    # 기본 정보
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    birth_date = models.DateField(null=True)
    age = models.IntegerField(null=True)

    
    # 금융 관련 정보
    investment_style = models.CharField(max_length=20, choices=INVESTMENT_STYLE_CHOICES)
    annual_income = models.CharField(max_length=1, choices=INCOME_CHOICES, null=True)
    savings_goal = models.IntegerField(choices=SAVINGS_GOALS_CHOICES ,null=True)  # 목표 저축액
    
    # 가입한 상품들
    deposit_products = models.ManyToManyField(DepositProducts, related_name='users', blank=True)
    savings_products = models.ManyToManyField(InstallmentProducts, related_name='users', blank=True)