import pandas as pd


sc = pd.read_csv('./data/people_num_data/생활이동_자치구_2023.08_19시.csv', encoding='cp949')
row = len(sc)

sc['이동인구(합)'] = sc['이동인구(합)'].replace('*', float('nan'))

# 노원구 청년층 이동인구 합산
sum1 = 0
for i in range(row):
    if sc.loc[i, '도착 시군구 코드'] == 11110 and (
            sc.loc[i, '나이'] == 30 or sc.loc[i, '나이'] == 20 or sc.loc[i, '나이'] == 35 or sc.loc[i, '나이'] == 25):
        if pd.notna(sc.loc[i, '이동인구(합)']):
            sum1 += float(sc.loc[i, '이동인구(합)'])

# 노원구 노년층 이동인구 합산
sum2 = 0
for i in range(row):
    if sc.loc[i, '도착 시군구 코드'] == 11110 and (
            sc.loc[i, '나이'] == 50 or sc.loc[i, '나이'] == 60 or sc.loc[i, '나이'] == 55 or sc.loc[i, '나이'] == 65):
        if pd.notna(sc.loc[i, '이동인구(합)']):
            sum2 += float(sc.loc[i, '이동인구(합)'])

# 마포구 청년층 이동인구 합산
sum3 = 0
for i in range(row):
    if sc.loc[i, '도착 시군구 코드'] == 11140 and (
            sc.loc[i, '나이'] == 30 or sc.loc[i, '나이'] == 20 or sc.loc[i, '나이'] == 35 or sc.loc[i, '나이'] == 25):
        if pd.notna(sc.loc[i, '이동인구(합)']):
            sum3 += float(sc.loc[i, '이동인구(합)'])

# 마포구 노년층 이동인구 합산
sum4 = 0
for i in range(row):
    if sc.loc[i, '도착 시군구 코드'] == 11140 and (
            sc.loc[i, '나이'] == 50 or sc.loc[i, '나이'] == 60 or sc.loc[i, '나이'] == 55 or sc.loc[i, '나이'] == 65):
        if pd.notna(sc.loc[i, '이동인구(합)']):
            sum4 += float(sc.loc[i, '이동인구(합)'])

# 새로운 데이터프레임 생성
data = {'지역': ['노원구', '노원구', '마포구', '마포구'],
        '나이': ['20-30대','50-60대','20-30대','50-60대'],
        '이동인구(합)': [sum1, sum2, sum3, sum4]}
sc_new = pd.DataFrame(data)

# CSV 파일로 저장
sc_new.to_csv('C:/nowon/Data/sc_new.csv', index=False)

print(sc_new)
