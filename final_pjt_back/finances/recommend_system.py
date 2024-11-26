import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def change_investment_style(x):
    if x == 'moderate':
        return 0
    elif x == 'aggressive':
        return 1
    else:
        return 2

def change_gender(x):
    if x == 'M':
        return 0
    else:
        return 1

def change_mainbank(x):
    if x == '중소기업은행':
        return 0
    elif x == '농협은행주식회사':
        return 1
    elif x == '부산은행':
        return 2
    elif x == '경남은행':
        return 3
    elif x == '수협은행':
        return 4
    elif x == '한국스탠다드차타드은행':
        return 5
    elif x == '광주은행':
        return 6
    elif x == '국민은행':
        return 7
    elif x == '제주은행':
        return 8
    elif x == '아이엠뱅크':
        return 9
    elif x == '토스뱅크 주식회사':
        return 10
    elif x == '한국산업은행':
        return 11
    elif x == '주식회사 케이뱅크':
        return 12
    elif x == '전북은행':
        return 13
    elif x == '신한은행':
        return 14
    elif x == '우리은행':
        return 15
    elif x == '하나은행':
        return 16
    else:
        return 17
    
def recommend_system(data):
    user_id = data['user_id']
    new_data = pd.DataFrame([data])
    new_data['investment_style'] = new_data['investment_style'].apply(change_investment_style)
    new_data['gender'] = new_data['gender'].apply(change_gender)
    new_data['주거래은행'] = new_data['주거래은행'].apply(change_mainbank)


    file_path = './data/'
    features = pd.read_csv(file_path + 'features.csv')

    df = pd.concat([features, new_data]) 
    df.set_index('user_id', inplace=True)
    user_sim = cosine_similarity(df, df)
    user_sim = pd.DataFrame(user_sim, df.index, df.index)
    # print(user_sim)
    # print(user_sim[user_id])
    return list(user_sim[user_id].sort_values(ascending=False)[1:4].reset_index().user_id)


