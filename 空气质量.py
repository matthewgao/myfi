import akshare as ak
import time
import matplotlib.pyplot as plt

# import matplotlib

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


all = ak.air_quality_hist(city='上海',start_date='2015-03-14',end_date='2021-03-14')
all['aqi'] = all['aqi'].astype(float)
all['pm2_5'] = all['pm2_5'].astype(float)
all['pm2_5'].plot()

all = ak.air_quality_hist(city='三亚',start_date='2015-03-14',end_date='2021-03-14')
all['aqi'] = all['aqi'].astype(float)
all['pm2_5'] = all['pm2_5'].astype(float)
all['pm2_5'].plot()
# print(ak.air_quality_hist(city='杭州',start_date='2015-03-14',end_date='2021-03-14')['aqi'].plot())
plt.show()