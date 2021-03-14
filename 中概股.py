import akshare as ak
import time
import matplotlib.pyplot as plt

# import matplotlib

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


all = ak.stock_us_zh_spot()
all['最新价'] = all['最新价'].astype(float)
all['成交量'] = all['成交量'].astype(float)
# print(all.sort_values(by=['最新价'],ascending=False).head(50))
print(all.sort_values(by=['成交量'],ascending=False).head(50))
# print(ak.stock_us_zh_spot())