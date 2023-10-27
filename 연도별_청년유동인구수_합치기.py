import pandas as pd
import os

# CSV 파일이 있는 디렉토리 경로
directory_path = './data/people_num_data'

# 빈 데이터프레임 생성
combined_df = pd.DataFrame()

for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)
        try:
            df = pd.read_csv(file_path, encoding='cp949')
            
            # 원하는 행만 선택 (예: '도착 시군구 코드' 열이 5번째 열에 위치)
            # selected_rows = df[(df.iloc[:, 4] == 11140) & ((df.iloc[:, 6] == 30) | (df.iloc[:, 6] == 20))]
            selected_rows = df[(df['도착 시군구 코드'] == 11110) & ((df['나이'] == 30) | (df['나이'] == 20)|(df['나이'] == 35) | (df['나이'] == 25))]
            combined_df = pd.concat([combined_df, selected_rows], ignore_index=True)
        except UnicodeDecodeError:
            print(f"UnicodeDecodeError: Cannot read {file_path}. Check encoding.")

combined_df.to_csv('./data/manyToOne.csv', index=False)
