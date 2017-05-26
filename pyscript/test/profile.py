from time import time
import re

t = time()
data = [
    'a', 'b', 'is', 'python', 'jason', 'hello', 'hill', 'with', 'phone',
    'test', 'dfdf', 'apple', 'pddf', 'ind', 'basic', 'none', 'baecr', 'var',
    'bana', 'dd', 'wrd'
]

# dicr=[{dic[id]:({dp:dr})}  for (id,p,r) in users for (did,dp,dr) in users if id==did]
# print(dic)

# new_data=[]
# [new_data.append(u) for x in data if len(x)>3]
# print(new_data)
# words=["com.kjt.app/product_detail/101034","pre.kjt.com/product/101034","kjt.com/product_list/101034"
# ,"www.kjt.com/product/search/101034"]

# s=[x for x in words if len(re.findall(r"^\\(pre|search|list)",x))==0]
# print(s)


def set_data(data: list):
    """
        数据去重
        :param data: 
        :return: list
        """
    new_list = []
    if data is None or len(data) == 0:
        return new_list
    # 先排序
    data = [x for x in data if len(x) > 0]
    sort_data = sorted(data, key=lambda x: x[1])
    # 商品编号分组
    group_data = groupby(data, key=lambda x: x[1])
    indexes = []
    for n in group_data:
        indexes.append(str(n[0]))
    # 合并商品编号重复的数据
    for sysno in indexes:
        count = 0.0
        for d in sort_data:
            if str(sysno) == str(d[1]):
                count += d[1]
        new_list.append((data[0][0], sysno, count))
    return new_list


rst = "m.kjt.com/product/167244?from=singlemessage&isappinstalled=1"

print(rst.replace("?from=singlemessage&isappinstalled=1", ""))
reg = r"[0-9]+(?=[^0-9]*$)"
rt = re.findall(
    reg, "m.kjt.com/registertwo/sd?ReturnUrl=http://m.kjt.com/product/10002")
print(len(rt))

lc1 = [(1001, 2), (1002, 3), (1003, 3)]
lc2 = [(1001, 0.1), (1003, 0.2), (1006, 0.3), (1005, 0.2)]

lc1.extend(lc2)
print(lc1)
s=[(z,y,1)for  (z,y) in lc2]
print(s)


