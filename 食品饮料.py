import akshare as ak
import time
import matplotlib.pyplot as plt

# import matplotlib

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


all = ak.sw_index_daily(index_code='801120', start_date='2018-01-01',end_date='2021-03-15').sort_index(ascending=False)
all['close'] = all['close'].astype(float)
print(all)
all['close'].plot()
# print(ak.sw_index_daily(index_code='801120', start_date='2015-03-14',end_date='2021-03-14')['close'].plot())
plt.show()