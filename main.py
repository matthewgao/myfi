import akshare as ak
import time
import matplotlib.pyplot as plt

# import matplotlib
# https://www.akshare.xyz/zh_CN/latest/tutorial.html

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


today = time.time()
date = "20210307"

# 财报发布日期, xxxx-03-31, xxxx-06-30, xxxx-09-30, xxxx-12-31

# print(ak.news_cctv(date=date).get(["date", "title"]).head(20))
# print(ak.news_cctv.__doc__)

# print(ak.movie_boxoffice_realtime())
# print(ak.stock_report_fund_hold_detail(symbol="001387", date='2021-12-31').sort_values(by=['占总股本比例'],ascending=False).head(10))

#机构持股详情
# print(ak.stock_institute_hold_detail.__doc__)
# stock_institute_hold_detail

# print(ak.fund_em_open_fund_rank.__doc__)
# print(ak.fund_em_open_fund_rank(symbol="全部").sort_values(by=['近1年'],ascending=False).head(10))
# print(ak.fund_em_open_fund_rank(symbol="全部").sort_values(by=['近1周'],ascending=False).head(10))
# print(ak.fund_em_open_fund_rank(symbol="全部").sort_values(by=['近1月'],ascending=False).head(10))

# 存款准备金率
# print(ak.macro_china_reserve_requirement_ratio())

# 社会消费品零售总额
# print(ak.macro_china_consumer_goods_retail().head(142))

# "stock_market_fund_flow"  # 大盘资金流
# print(ak.stock_market_fund_flow())


 # 微博舆情报告
#  "stock_js_weibo_report"  # 微博舆情报告
# print(ak.stock_js_weibo_report(time_period="1周"))
# print(ak.stock_institute_recommend())
# print(ak.stock_zh_index_daily(symbol='sz399001'))

# print(ak.bond_investing_global(country='美国',index_name='美国10年期国债', end_date='2021-03-14'))
# ak.bond_investing_global(country='美国',index_name='美国10年期国债', start_date='2019-03-14',end_date='2021-03-14')['收盘'].plot()

# plt.show()
# time.sleep(10000)

# print(ak.stock_us_zh_spot().sort_values(by=['成交量'],ascending=False).head(50))
# print(ak.stock_us_zh_spot().sort_values(by=['最新价'],ascending=True).head(50))
# all = ak.stock_us_zh_spot()
# all['最新价'] = all['最新价'].astype(float)
# all['成交量'] = all['成交量'].astype(float)
# # print(all.sort_values(by=['最新价'],ascending=False).head(50))
# print(all.sort_values(by=['成交量'],ascending=False).head(50))
# print(ak.stock_us_zh_spot())
# all = ak.sw_index_daily(index_code='801120', start_date='2018-01-01',end_date='2021-03-15').sort_index(ascending=False)
# all['close'] = all['close'].astype(float)
# print(all)
# all['close'].plot()
# # print(ak.sw_index_daily(index_code='801120', start_date='2015-03-14',end_date='2021-03-14')['close'].plot())
# plt.show()


# # print(ak.air_quality_watch_point(city='杭州',start_date='2015-03-14',end_date='2021-03-14'))
# all = ak.air_quality_hist(city='上海',start_date='2015-03-14',end_date='2021-03-14')
# all['aqi'] = all['aqi'].astype(float)
# all['pm2_5'] = all['pm2_5'].astype(float)
# all['pm2_5'].plot()

# all = ak.air_quality_hist(city='三亚',start_date='2015-03-14',end_date='2021-03-14')
# all['aqi'] = all['aqi'].astype(float)
# all['pm2_5'] = all['pm2_5'].astype(float)
# all['pm2_5'].plot()
# # print(ak.air_quality_hist(city='杭州',start_date='2015-03-14',end_date='2021-03-14')['aqi'].plot())
# plt.show()
all = ak.fund_em_open_fund_daily().sort_values(by=['日增长率'],ascending=False).head(100)
print(all)
all.to_excel('Result.xls')