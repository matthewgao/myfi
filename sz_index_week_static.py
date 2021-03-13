import akshare as ak
import time

# 统计一个星期 每天涨跌的概率
from datetime import datetime
all = ak.stock_zh_index_daily(symbol='sz399001')
# print(all)
mon_p_c = 0
mon_n_c = 0

tue_p_c = 0
tue_n_c = 0

wen_p_c = 0
wen_n_c = 0

thru_p_c = 0
thru_n_c = 0

fri_p_c = 0
fri_n_c = 0

# month
m1_p_c = 0
m1_n_c = 0
m2_p_c = 0
m2_n_c = 0
m3_p_c = 0
m3_n_c = 0
m4_p_c = 0
m4_n_c = 0
m5_p_c = 0
m5_n_c = 0
m6_p_c = 0
m6_n_c = 0
m7_p_c = 0
m7_n_c = 0
m8_p_c = 0
m8_n_c = 0
m9_p_c = 0
m9_n_c = 0
m10_p_c = 0
m10_n_c = 0
m11_p_c = 0
m11_n_c = 0
m12_p_c = 0
m12_n_c = 0

for index, row in all.iterrows():
    # print(index)
    # break
    # if 'Name' not in row:
    #     continue
    date = index
    diff = row['close'] - row['open']
    week = date.to_pydatetime().date().weekday()
    # print(week)
    if week == 0:
        if diff > 0:
            mon_p_c = mon_p_c + 1
        else:
            mon_n_c = mon_n_c + 1
    
    if week == 1:
        if diff > 0:
            tue_p_c = tue_p_c + 1
        else:
            tue_n_c = tue_n_c + 1

    if week == 2:
        if diff > 0:
            wen_p_c = wen_p_c + 1
        else:
            wen_n_c = wen_n_c + 1

    if week == 3:
        if diff > 0:
            thru_p_c = thru_p_c + 1
        else:
            thru_n_c = thru_n_c + 1

    if week == 4:
        if diff > 0:
            fri_p_c = fri_p_c + 1
        else:
            fri_n_c = fri_n_c + 1
    month = date.to_pydatetime().date().month
    if month == 1:
        if diff > 0:
            m1_p_c = m1_p_c + 1
        else:
            m1_n_c = m1_n_c + 1
    if month == 2:
        if diff > 0:
            m2_p_c = m2_p_c + 1
        else:
            m2_n_c = m2_n_c + 1
    if month == 3:
        if diff > 0:
            m3_p_c = m3_p_c + 1
        else:
            m3_n_c = m3_n_c + 1
    if month == 4:
        if diff > 0:
            m4_p_c = m4_p_c + 1
        else:
            m4_n_c = m4_n_c + 1
    if month == 5:
        if diff > 0:
            m5_p_c = m5_p_c + 1
        else:
            m5_n_c = m5_n_c + 1
    if month == 6:
        if diff > 0:
            m6_p_c = m6_p_c + 1
        else:
            m6_n_c = m6_n_c + 1
    if month == 7:
        if diff > 0:
            m7_p_c = m7_p_c + 1
        else:
            m7_n_c = m7_n_c + 1
    if month == 8:
        if diff > 0:
            m8_p_c = m8_p_c + 1
        else:
            m8_n_c = m8_n_c + 1
    if month == 9:
        if diff > 0:
            m9_p_c = m9_p_c + 1
        else:
            m9_n_c = m9_n_c + 1
    if month == 10:
        if diff > 0:
            m10_p_c = m10_p_c + 1
        else:
            m10_n_c = m10_n_c + 1
    if month == 11:
        if diff > 0:
            m11_p_c = m11_p_c + 1
        else:
            m11_n_c = m11_n_c + 1
    if month == 12:
        if diff > 0:
            m12_p_c = m12_p_c + 1
        else:
            m12_n_c = m12_n_c + 1


# Mon P 710, N 727, R 0.4940848990953375
# Tue P 791, N 679, R 0.5380952380952381
# Wen P 745, N 728, R 0.5057705363204344
# Thru P 688, N 778, R 0.4693042291950887
# Fri P 779, N 671, R 0.5372413793103449
print("Mon P {}, N {}, R {}".format(mon_p_c, mon_n_c, mon_p_c/(mon_p_c+mon_n_c)))
print("Tue P {}, N {}, R {}".format(tue_p_c, tue_n_c, tue_p_c/(tue_p_c+tue_n_c)))
print("Wen P {}, N {}, R {}".format(wen_p_c, wen_n_c, wen_p_c/(wen_p_c+wen_n_c)))
print("Thru P {}, N {}, R {}".format(thru_p_c, thru_n_c, thru_p_c/(thru_p_c+thru_n_c)))
print("Fri P {}, N {}, R {}".format(fri_p_c, fri_n_c, fri_p_c/(fri_p_c+fri_n_c)))
print("M1 P {}, N {}, R {}".format(m1_p_c, m1_n_c, m1_p_c/(m1_p_c+m1_n_c)))
print("M2 P {}, N {}, R {}".format(m2_p_c, m2_n_c, m2_p_c/(m2_p_c+m2_n_c)))
print("M3 P {}, N {}, R {}".format(m3_p_c, m3_n_c, m3_p_c/(m3_p_c+m3_n_c)))
print("M4 P {}, N {}, R {}".format(m4_p_c, m4_n_c, m4_p_c/(m4_p_c+m4_n_c)))
print("M5 P {}, N {}, R {}".format(m5_p_c, m5_n_c, m5_p_c/(m5_p_c+m5_n_c)))
print("M6 P {}, N {}, R {}".format(m6_p_c, m6_n_c, m6_p_c/(m6_p_c+m6_n_c)))
print("M7 P {}, N {}, R {}".format(m7_p_c, m7_n_c, m7_p_c/(m7_p_c+m7_n_c)))
print("M8 P {}, N {}, R {}".format(m8_p_c, m8_n_c, m8_p_c/(m8_p_c+m8_n_c)))
print("M9 P {}, N {}, R {}".format(m9_p_c, m9_n_c, m9_p_c/(m9_p_c+m9_n_c)))
print("M10 P {}, N {}, R {}".format(m10_p_c, m10_n_c, m10_p_c/(m10_p_c+m10_n_c)))
print("M11 P {}, N {}, R {}".format(m11_p_c, m11_n_c, m11_p_c/(m11_p_c+m11_n_c)))
print("M12 P {}, N {}, R {}".format(m12_p_c, m12_n_c, m12_p_c/(m12_p_c+m12_n_c)))

# M1 P 299, N 267, R 0.5282685512367491
# M2 P 254, N 204, R 0.5545851528384279
# M3 P 333, N 318, R 0.511520737327189
# M4 P 319, N 298, R 0.5170178282009724
# M5 P 298, N 292, R 0.5050847457627119
# M6 P 297, N 327, R 0.47596153846153844
# M7 P 351, N 314, R 0.5278195488721804
# M8 P 331, N 331, R 0.5
# M9 P 305, N 317, R 0.4903536977491961
# M10 P 270, N 269, R 0.5009276437847866
# M11 P 325, N 316, R 0.5070202808112324
# M12 P 331, N 330, R 0.5007564296520424