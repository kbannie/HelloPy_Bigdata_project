import pandas as pd
import matplotlib.pyplot as plt

sc=pd.read_csv('C:/nowon/Data/sc_new.csv')

#figure창 한글깨짐 해결
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


nowon_sc=sc.head(2)

values = nowon_sc['이동인구(합)']
labels = nowon_sc['나이']

colors = ['#5371F3', '#7BC0D7']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.title('노원구 연령대별 유동인구 비율')
plt.show()



mapo_sc=sc.tail(2)

values2 = mapo_sc['이동인구(합)']
labels2 = mapo_sc['나이']

colors = ['#5371F3', '#7BC0D7']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(values2, labels=labels2, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.title('마포구 연령대별 유동인구 비율')
plt.show()
