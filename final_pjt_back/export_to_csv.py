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



def depositproduct_export():
    # QuerySet 가져오기
    queryset = DepositProducts.objects.all().values()
    df = pd.DataFrame(queryset)

    # CSV 파일로 저장
    df.to_csv(file_path +'/depositproducts.csv', index=False, encoding='utf-8')
    print("depositproducts CSV 파일 생성 완료")


# installmentproducts
def installmentproducts_export():
    # QuerySet 가져오기
    queryset = InstallmentProducts.objects.all().values()
    df = pd.DataFrame(queryset)

    # CSV 파일로 저장
    df.to_csv(file_path+'/installmentproducts.csv', index=False, encoding='utf-8')
    print("depositproducts CSV 파일 생성 완료")



# USER
from django.contrib.auth import get_user_model

User = get_user_model()

def user_export():
    queryset = User.objects.all().values()
    df = pd.DataFrame(queryset)

    # CSV 파일로 저장
    df.to_csv(file_path+'/users.csv', index=False, encoding='utf-8')
    print("depositproducts CSV 파일 생성 완료")

if __name__ == "__main__":
    depositproduct_export()
    installmentproducts_export()
    user_export