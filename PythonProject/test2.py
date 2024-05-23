import json

# 假设你的JSON数据存储在一个文件中，文件名为 data.json
with open('func_data_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

A =[{"self_time": 2220.8094799999994, "name": "PlayerLoop", "total_time": 298504.70992, "avg_total_time": 99.10514937583001, "calls": 3012, "gc_mem": 66502.0986328125
     , "gt_10ms": 3012, "max_total_time": 5370.848, "calls_pre_frame": 1.0, "total_time_percentage": 100.0}]


list = []
# for i in data:
#     for j in range(len(i["children"]) - 1):
#         # try:
#         #     print(len(i["children"][j]["children"]))
#         # except:
#         #     pass
#         if "children" in i["children"][j]:
#             # print(f"{j}行有")
#             print(len(i["children"][j]["children"]))

def getdata():
    print(data[0])


getdata()
print(list)

# for k in data[0]:
#     if "children" == k:
#         pass
#     else:
#         list.append({k:v})




# key = ["self_time", "name", "total_time", "avg_total_time", "calls", "gc_mem",
#        "gt_10ms", "max_total_time", "calls_pre_frame", "total_time_percentage",]

key = "total_time_percentage"

# take_key_values(key, data)