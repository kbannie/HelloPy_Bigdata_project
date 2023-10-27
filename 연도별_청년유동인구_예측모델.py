import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#figure창 한글깨짐 해결
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

sc = pd.read_csv('./data/sum_list.csv')

data = {'X': sc['대상연월'], 'y': sc['이동인구(합)']}

data_df = pd.DataFrame(data)

# 선형 회귀 모델 학습
X = data_df[['X']]
y = data_df['y']
lr = LinearRegression()
lr.fit(X, y)

def predict_population(year, month):
    # 입력된 연도와 월로 예측
    prediction = lr.predict(np.array([[year * 100 + month]]))
    return prediction[0]

predictions = [predict_population(2024, 1), predict_population(2025, 1), predict_population(2026, 1),predict_population(2027, 1),predict_population(2028, 1)]

plt.figure(figsize=(12, 6))
plt.scatter(data_df['X'], data_df['y'], color='#7BC0D7', label='실제 데이터')
plt.scatter([202401, 202501, 202601,202701, 202801], predictions, color='#5371F3', label='예측값', marker='o', s=100)

#plt.title('청년 이동인구 예측')
plt.xlabel('연도별 1월기준 예측값')
plt.ylabel('이동인구(합)')
plt.legend()
plt.grid(True)
plt.show()