from django.db import models
from django.db.models import Q

# ==========================================================
# 상수 정의
# ==========================================================
class JoinDenyChoices(models.IntegerChoices):
    NO_RESTRICTION = 1, '제한없음'
    COMMON_PEOPLE_EXCLUSIVE = 2, '서민전용'
    PARTIAL_RESTRICTION = 3, '일부제한'


# ==========================================================
# 정기예금 상품
# ==========================================================
class DepositProducts(models.Model):
    # 상품 기본 정보
    fin_prdt_cd = models.TextField(unique=True)  # 금융상품 코드
    fin_co_no = models.TextField()               # 금융회사 코드
    kor_co_nm = models.TextField()               # 금융회사 명
    fin_prdt_nm = models.TextField()             # 금융 상품명
    
    # 가입 관련 정보
    join_way = models.TextField()                # 가입 방법
    join_deny = models.IntegerField(             # 가입 제한
        choices=JoinDenyChoices.choices,
        default=JoinDenyChoices.NO_RESTRICTION,
    )
    join_member = models.TextField()             # 가입대상
    max_limit = models.IntegerField(null=True)   # 최고한도
    
    # 상품 조건 정보
    mtrt_int = models.TextField()                # 만기 후 이자율
    spcl_cnd = models.TextField()                # 우대조건
    etc_note = models.TextField()                # 기타 유의사항
    
    # 공시 관련 정보
    dcls_month = models.TextField()              # 공시 제출월 [YYYYMM]
    dcls_strt_day = models.TextField()           # 공시 시작일
    dcls_end_day = models.TextField(null=True)   # 공시 종료일
    fin_co_subm_day = models.TextField()         # 금융회사 제출일 [YYYYMMDDHH24MI]

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["dcls_month", "fin_co_no", "fin_prdt_cd"],
                name="deposit_product_primary_key",
            ),
            models.CheckConstraint(
                check=Q(join_deny__gte=1) & Q(join_deny__lte=3),
                name="product_join_deny_range_1_to_3",
            ),
        ]
    
    # def __str__(self):
    #     return str(self.kor_co_nm)

# ==========================================================
# 정기예금 상품 옵션
# ==========================================================
class DepositOptions(models.Model):
    # 관계 설정
    product = models.ForeignKey(
        DepositProducts, 
        on_delete=models.CASCADE, 
        related_name="options"
    )
    
    # 상품 식별 정보
    dcls_month = models.TextField()              # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField()               # 금융회사 코드
    fin_prdt_cd = models.TextField()             # 금융상품 코드
    
    # 금리 관련 정보
    intr_rate_type = models.TextField()          # 저축 금리 유형
    intr_rate_type_nm = models.TextField()       # 저축 금리 유형명
    save_trm = models.IntegerField()             # 저축 기간 [단위: 개월]
    intr_rate = models.DecimalField(             # 저축 금리 [소수점 2자리]
        max_digits=4, 
        decimal_places=2, 
        null=True
    )
    intr_rate2 = models.DecimalField(            # 최고 우대금리 [소수점 2자리]
        max_digits=4, 
        decimal_places=2, 
        null=True
    )


# ==========================================================
# 적금 상품
# ==========================================================
class InstallmentProducts(models.Model):
    # 상품 기본 정보
    fin_prdt_cd = models.TextField(unique=True)  # 금융상품 코드
    fin_co_no = models.TextField()               # 금융회사 코드
    kor_co_nm = models.TextField()               # 금융회사 명
    fin_prdt_nm = models.TextField()             # 금융 상품명
    
    # 가입 관련 정보
    join_way = models.TextField()                # 가입 방법
    join_deny = models.IntegerField(             # 가입 제한
        choices=JoinDenyChoices.choices,
        default=JoinDenyChoices.NO_RESTRICTION,
    )
    join_member = models.TextField()             # 가입대상
    max_limit = models.IntegerField(null=True)   # 최고한도
    
    # 상품 조건 정보
    mtrt_int = models.TextField()                # 만기 후 이자율
    spcl_cnd = models.TextField()                # 우대조건
    etc_note = models.TextField()                # 기타 유의사항
    
    # 공시 관련 정보
    dcls_month = models.TextField()              # 공시 제출월 [YYYYMM]
    dcls_strt_day = models.TextField()           # 공시 시작일
    dcls_end_day = models.TextField(null=True)   # 공시 종료일
    fin_co_subm_day = models.TextField()         # 금융회사 제출일 [YYYYMMDDHH24MI]

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["dcls_month", "fin_co_no", "fin_prdt_cd"],
                name="saving_product_primary_key",
            ),
            models.CheckConstraint(
                check=Q(join_deny__gte=1) & Q(join_deny__lte=3),
                name="saving_join_deny_range_1_to_3",
            ),
        ]


# ==========================================================
# 적금 상품 옵션
# ==========================================================
class InstallmentOptions(models.Model):
    # 관계 설정
    product = models.ForeignKey(
        InstallmentProducts, 
        on_delete=models.CASCADE, 
        related_name="options"
    )
    
    # 상품 식별 정보
    dcls_month = models.TextField()              # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField()               # 금융회사 코드
    fin_prdt_cd = models.TextField()             # 금융상품 코드
    
    # 금리 관련 정보
    intr_rate_type = models.TextField()          # 저축 금리 유형
    intr_rate_type_nm = models.TextField()       # 저축 금리 유형명
    rsrv_type = models.TextField()               # 적립유형
    rsrv_type_nm = models.TextField()            # 적립유형 이름
    save_trm = models.IntegerField()             # 저축 기간 [단위: 개월]
    intr_rate = models.DecimalField(             # 저축 금리 [소수점 2자리]
        max_digits=4, 
        decimal_places=2, 
        null=True
    )
    intr_rate2 = models.DecimalField(            # 최고 우대금리 [소수점 2자리]
        max_digits=4, 
        decimal_places=2, 
        null=True
    )
