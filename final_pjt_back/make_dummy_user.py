import random
import os
import django
from django.conf import settings
from tqdm import tqdm
import json
import datetime
# Django 설정 모듈 지정 (프로젝트에 맞게 조정)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt_back.settings")
django.setup()

from accounts.models import User
from finances.models import DepositProducts, InstallmentProducts

# 한글 이름 생성 샘플
last_name_samples = "김이박최정강조윤장임신유한오서전황원문양손배백류허표차변민명심"
first_name_samples = "민윤효세경예지도하주채현지승영진희솔빛다정아라봄가을빛"
first_name_samples2 = "준우원호후서연아은진수혁영경환인석범찬기원민채영담율리빈채"

def random_last_name():
    """랜덤한 유저 이름 생성"""
    return random.choice(last_name_samples)

def random_fist_name():
    return random.choice(first_name_samples) + random.choice(first_name_samples2)

def random_birth_date():
    '''1970년 부터 2005년 사이의 랜덤 생년월일 생성'''
    start_date = datetime.datetime(1970, 1, 1)
    end_date = datetime.datetime(2005, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + datetime.timedelta(days=random_days)).date()

def random_age(birth_date):
    '''birth_data에 맞춰 age생성'''
    today = datetime.datetime.today()
    age = today.year - birth_date.year
    return age

# 사용자 수
USER_COUNT = 10000

# JSON 저장 위치
save_dir = 'accounts/fixtures/accounts/user_data.json'
os.makedirs(os.path.dirname(save_dir), exist_ok=True)

# DepositProducts 및 InstallmentProducts 데이터 가져오기
deposits = list(DepositProducts.objects.all())
savings = list(InstallmentProducts.objects.all())

if not deposits or not savings:
    raise ValueError("DepositProducts 또는 InstallmentProducts에 데이터가 존재하지 않습니다. 먼저 데이터를 로드하세요.")

user_data = []

# 사용자 데이터 생성
for i in tqdm(range(1, USER_COUNT + 1), desc="Generating user data"):
    username = f"testuser{i}"
    first_name = random_fist_name()
    last_name = random_last_name()
    email = f"testuser{i}@example.com"  # 유니크한 이메일
    birth_date = random_birth_date()
    age = random_age(birth_date)
    investment_style = random.choice(['conservative', 'moderate', 'aggressive'])
    annual_income = random.choice(['0', '1', '2', '3', '4', '5'])
    savings_goal = random.choice(['0', '1', '2', '3', '4', '5'])
    gender = random.choice(['M', 'F'])
    num_deposit = random.randint(1, 6)
    num_savings = random.randint(1, 6)
    user = {
        "model": "accounts.User",
        "pk": i,
        "fields": {
            "username": username,
            "first_name": first_name,
            'last_name': last_name,
            "email": email,
            "birth_date":birth_date.strftime('%Y-%m-%d'),
            # "password": make_password('rewq1234'),  # 해싱된 비밀번호
            "gender": gender,
            "age": age,
            "investment_style": investment_style,
            "annual_income": annual_income,
            "savings_goal": savings_goal,
            # ManyToMany 관계 설정
            "deposit_products": [deposit.pk for deposit in random.sample(deposits, num_deposit)],
            "savings_products": [saving.pk for saving in random.sample(savings, num_savings)]
        }
    }
    user_data.append(user)

# JSON 데이터 저장
with open(save_dir, 'w', encoding="utf-8") as f:
    json.dump(user_data, f, ensure_ascii=False, indent=4)

print(f"데이터 생성 완료 / 저장 위치: {save_dir}")