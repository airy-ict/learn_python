# -*- coding utf-8 -*-

import numpy as np
import pandas as pd
import os
import re
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups')


def read_order(path):
    # ./data_sql/orderdata/
    files = os.listdir(path)
    frames = []
    for f in files:
        name = path + f
        df = pd.read_csv(name, encoding="utf-8")
        frames.append(df)
    # 数据合并
    result = pd.concat(frames)
    return result


def read_visit(path):
    # ./data_sql/orderdata/
    files = os.listdir(path)
    frames = []
    for f in files:
        name = path + f
        df = pd.read_csv(name, encoding="utf-8")
        frames.append(df)
    # 数据合并
    result = pd.concat(frames)
    return result


if __name__ == '__main__':

    # 订单数据
    dfp = read_order("./data_sql/orderdata/")
    # 浏览数据
    dfv = read_visit("./data_sql/visitdata/")
    #查找某个用户的数据
    user_data = dfp[(dfp.customerSysNo == 664196)]
    user_visit = dfv[(dfv.customerSysNo == 664196)]

    setdata = user_visit[user_visit.url.str.contains(
        "^(?!.*(pre|search|list|arrivenotice)).*$", flags=re.I)]
    # print(setdata)
    # 商品的编号
    upid = user_data["productSysNo"].unique()
    # pro_data= user_data.groupby(["productSysNo","status"]).groups
    dic_product = []
    for p in upid:
        # 某个商品的订单数据
        pdata = user_data[(user_data.productSysNo == p)]
        buy_count = 0.0
        for (customerSysNo, status, productSysNo,
             quantity) in pdata.itertuples(index=False):
            if status == -1 or status == -4 or status == 6 or status == 65:
                buy_count += quantity * 0.3
            else:
                buy_count += quantity * 0.5
        # 某个商品的购买评分
        # print(p, count)
        # 浏览的数据
        view_count = 0.00
        for (customerSysNo, userId, url, quantity) in setdata.itertuples(
                index=False):
            str_len = len(re.findall("\d+", url, re.IGNORECASE))
            productsysNo = 0
            if str_len > 0:
                productsysNo = str(re.findall("\d+", url)[str_len - 1])
            if str(p) == productsysNo:
                view_count += quantity + 0.01
            else:
                view_count = 0.01
                if (productsysNo, view_count) not in dic_product:
                    s=[x for (dp,dr) in dic_product if str(dp)==str(productsysNo)]
                    if len(s)==0:
                        dic_product.append((productsysNo, view_count))
        
        dic_product.append((productsysNo, (buy_count + view_count)))

    print(dic_product)