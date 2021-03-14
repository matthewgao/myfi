import akshare as ak
import time
import matplotlib.pyplot as plt

# import matplotlib

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

ak.bond_investing_global(country='美国',index_name='美国10年期国债', start_date='2000-03-14',end_date='2021-03-14')['收盘'].plot()
ak.bond_investing_global(country='美国',index_name='美国10年期国债', start_date='2020-03-14',end_date='2021-03-14')['收盘'].plot()

plt.show()
# time.sleep(10000)