from django.db import models
from django.db.models import Q

# 가입제한 옵션
DENY_NO_RESTRICTION = 1           # 제한없음
DENY_COMMON_PEOPLE_EXCLUSIVE = 2  # 서민전용
DENY_PARTIAL_RESTRICTION = 3      # 일부제한

# 정기예금 상품 
class DepositProducts(models.Model):
    dcls_month      = models.TextField()             # 공시 제출월 [YYYYMM]
    fin_co_no       = models.TextField()             # 금융회사 코드
    fin_prdt_cd     = models.TextField(unique=True)  # 금융상품 코드
    kor_co_nm       = models.TextField()             # 금융회사 명
    fin_prdt_nm     = models.TextField()             # 금융 상품명
    join_way        = models.TextField()             # 가입 방법
    mtrt_int        = models.TextField()             # 만기 후 이자율
    spcl_cnd        = models.TextField()             # 우대조건
    join_deny       = models.IntegerField()          # 가입 제한
    join_member     = models.TextField()             # 가입대상
    etc_note        = models.TextField()             # 기타 유의사항
    max_limit       = models.IntegerField()          # 최고한도
    dcls_strt_day   = models.TextField()             # 공시 시작일
    dcls_end_day    = models.TextField(null=True)    # 공시 종료일
    fin_co_subm_day	= models.TextField()             # 금융회사 제출일 [YYYYMMDDHH24MI]
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['dcls_month', 'fin_co_no', 'fin_prdt_cd'], name='deposit_product_primary_key'
            ),
            # 가입제한 : 1 ~ 3
            models.CheckConstraint(
                check=Q(join_deny__gte=1) & Q(join_deny__lte=3),
                name='product_join_deny_range_1_to_3'
            ),
        ]
    
    
# 정기예금 상품 옵션
class DepositOptions(models.Model):
    # FK: product -> option
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='options')
    dcls_month        = models.TextField()     # 공시 제출월 [YYYYMM]
    fin_co_no         = models.TextField()     # 금융회사 코드
    fin_prdt_cd       = models.TextField()     # 금융상품 코드
    intr_rate_type    = models.TextField()     # 저축 금리 유형 
    intr_rate_type_nm = models.TextField()     # 저축 금리 유형명
    save_trm          = models.IntegerField()  # 저축 기간 [단위: 개월]
    # 저축 금리 [소수점 2자리]
    intr_rate         = models.DecimalField(max_digits=4, decimal_places=2)
    # 최고 우대금리 [소수점 2자리]
    intr_rate2        = models.DecimalField(max_digits=4, decimal_places=2)


# 적금 상품 
class InstallmentProducts(models.Model):
    dcls_month      = models.TextField()             # 공시 제출월 [YYYYMM]
    fin_co_no       = models.TextField()             # 금융회사 코드
    fin_prdt_cd     = models.TextField(unique=True)  # 금융상품 코드
    kor_co_nm       = models.TextField()             # 금융회사 명
    fin_prdt_nm     = models.TextField()             # 금융 상품명
    join_way        = models.TextField()             # 가입 방법
    mtrt_int        = models.TextField()             # 만기 후 이자율
    spcl_cnd        = models.TextField()             # 우대조건
    join_deny       = models.IntegerField()          # 가입 제한
    join_member     = models.TextField()             # 가입대상
    etc_note        = models.TextField()             # 기타 유의사항
    max_limit       = models.IntegerField()          # 최고한도
    dcls_strt_day   = models.TextField()             # 공시 시작일
    dcls_end_day    = models.TextField(null=True)    # 공시 종료일
    fin_co_subm_day	= models.TextField()             # 금융회사 제출일 [YYYYMMDDHH24MI]
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['dcls_month', 'fin_co_no', 'fin_prdt_cd'], name='saving_product_primary_key'
            ),
            # 가입제한 : 1 ~ 3
            models.CheckConstraint(
                check=Q(join_deny__gte=1) & Q(join_deny__lte=3),
                name='saving_join_deny_range_1_to_3'
            ),
        ]

# 적금 상품 옵션
class InstallmentOptions(models.Model):
    # FK: product -> option
    product = models.ForeignKey(InstallmentProducts, on_delete=models.CASCADE, related_name='options')
    dcls_month        = models.TextField()     # 공시 제출월 [YYYYMM]
    fin_co_no         = models.TextField()     # 금융회사 코드
    fin_prdt_cd       = models.TextField()     # 금융상품 코드
    intr_rate_type    = models.TextField()     # 저축 금리 유형 
    intr_rate_type_nm = models.TextField()     # 저축 금리 유형명
    rsrv_type         = models.TextField()     # 적립유형
    rsrv_type_nm      = models.TextField()     # 적립유형 이름
    save_trm          = models.IntegerField()  # 저축 기간 [단위: 개월]
    # 저축 금리 [소수점 2자리]
    intr_rate         = models.DecimalField(max_digits=4, decimal_places=2)
    # 최고 우대금리 [소수점 2자리]
    intr_rate2        = models.DecimalField(max_digits=4, decimal_places=2)