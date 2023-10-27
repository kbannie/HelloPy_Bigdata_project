import pandas as pd
import numpy as np

sc=pd.read_csv('./data/manyToOne.csv')

# '*'를 NaN으로 대체
sc['이동인구(합)'] = sc['이동인구(합)'].replace('*', np.nan)


# '대상연월' 값을 기준으로 데이터를 정렬
sc.sort_values(by='대상연월', inplace=True)

# '대상연월' 값의 범위 확인
unique_months = sc['대상연월'].unique()
num_months = len(unique_months)

# '이동인구(합)' 값을 저장할 리스트 초기화
sum_list = [0.0] * num_months

# 데이터를 순회하며 '이동인구(합)'을 합산
for i in range(num_months):
    month = unique_months[i]
    sum_month = sc.loc[sc['대상연월'] == month, '이동인구(합)'].astype(float).sum()
    sum_list[i] = sum_month

# 결과를 데이터프레임으로 변환
result_df = pd.DataFrame({'대상연월': unique_months, '이동인구(합)': sum_list})

# 결과를 CSV 파일로 저장
result_df.to_csv('./data/sum_list.csv', index=False)
