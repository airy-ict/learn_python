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

rst="m.kjt.com/product/167244?from=singlemessage&isappinstalled=1"

print(rst.replace("?from=singlemessage&isappinstalled=1",""))
reg=r"[0-9]+(?=[^0-9]*$)"
print(re.findall(reg,"m.kjt.com/registertwo/13873150392?ReturnUrl=http://m.kjt.com/product/1106")[0])