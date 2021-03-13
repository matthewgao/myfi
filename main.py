import akshare as ak
import time

today = time.time()
date = "20210307"

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

