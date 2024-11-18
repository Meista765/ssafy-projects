from django.db import models

# 정기예금 상품 
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)         # 금융 삼풍 코드
    kor_co_nm = models.TextField()                      # 금융회사명
    fin_prdt_nm = models.TextField()                    # 금융 상품명
    etc_note = models.TextField()                       # 금융 상품 설명
    join_deny = models.IntegerField()                   # 가입 제한
    join_member = models.TextField()                    # 가입대상
    join_way = models.TextField()                       # 가입방법
    spcl_cnd = models.TextField()                       # 우대조건

# 정기예금 상품 옵션
class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='options')
    fin_prdt_cd = models.TextField()                        # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축금리 유형명 
    intr_rate = models.FloatField()                         # 저축금리
    intr_rate2 = models.FloatField()                        # 최고우대금리
    save_trm = models.IntegerField()                        # 저축기간


# 적금 상품 
class SavingsProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)         # 금융 삼풍 코드
    kor_co_nm = models.TextField()                      # 금융회사명
    fin_prdt_nm = models.TextField()                    # 금융 상품명
    etc_note = models.TextField()                       # 금융 상품 설명
    join_deny = models.IntegerField()                   # 가입 제한
    join_member = models.TextField()                    # 가입대상
    join_way = models.TextField()                       # 가입방법
    spcl_cnd = models.TextField()                       # 우대조건

# 적금 상품 옵션
class SavingsOptions(models.Model):
    product = models.ForeignKey(SavingsProducts, on_delete=models.CASCADE, related_name='options')
    fin_prdt_cd = models.TextField()                        # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축금리 유형명 
    intr_rate = models.FloatField()                         # 저축금리
    intr_rate2 = models.FloatField()                        # 최고우대금리
    save_trm = models.IntegerField()                        # 저축기간
    rsrv_type = models.TextField()                          # 적립유형
    rsrv_type_nm = models.TextField()                       # 적립유형 이름
    
