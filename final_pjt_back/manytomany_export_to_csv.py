import csv
import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt_back.settings")
django.setup() 

# 저장할 CSV 파일 경로
file_path = os.path.join(os.getcwd(),'data')

if not os.path.exists(file_path):
    os.makedirs(file_path)

# depostiproduct
from finances.models import DepositProducts, InstallmentProducts

# 중간 테이블 모델 가져오기
deposit_through_model = DepositProducts.users.through
savings_through_model = InstallmentProducts.users.through
# 중간 테이블의 모든 데이터 가져오기


def user_deposit_products():
    queryset = deposit_through_model.objects.all()
    data = []
    for query in queryset:
        data.append({
            'id': query.id,
            'user_id': query.user_id,
            'deposit_id': query.depositproducts_id
        })

    # CSV 파일로 저장
    df = pd.DataFrame(data)
    df.to_csv(file_path+'/user_deposit.csv', index=False, encoding='utf-8')
    print("user_depoist CSV 파일 생성 완료")


def user_savings_products():
    queryset = savings_through_model.objects.all()
    data = []
    for query in queryset:
        data.append({
            'id': query.id,
            'user_id': query.user_id,
            'savings_id': query.installmentproducts_id
        })

    # CSV 파일로 저장
    df = pd.DataFrame(data)
    df.to_csv(file_path+'/user_savings.csv', index=False, encoding='utf-8')
    print("user_savings CSV 파일 생성 완료")


if __name__ == "__main__":
    user_deposit_products()
    user_savings_products()