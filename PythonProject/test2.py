import json
import pickle

# 假设你的JSON数据存储在一个文件中，文件名为 data.json
with open('func_data_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

a = [{"self_time": 2220.8094799999994, "name": "PlayerLoop", "total_time": 298504.70992,
      "avg_total_time": 99.10514937583001, "calls": 3012, "gc_mem": 66502.0986328125
         , "gt_10ms": 3012, "max_total_time": 5370.848, "calls_pre_frame": 1.0, "total_time_percentage": 100.0}]

# select_keys = ["self_time", "name", "total_time", "avg_total_time", "calls", "gc_mem",
#        "gt_10ms", "max_total_time", "calls_pre_frame", "total_time_percentage"]

select_keys = ["name", "total_time_percentage"]

list_box = []

def test(list_data):
    if isinstance(list_data, list):
        for i in list_data:
            test(i)
    elif isinstance(list_data, dict):
        if "children" in list_data:
            select_dic = {c_key: list_data[c_key] for c_key in select_keys}
            list_box.append(select_dic)
            for k in list_data["children"]:
                test(k)
        else:
            select_dic = {c_key: list_data[c_key] for c_key in select_keys}
            list_box.append(select_dic)


test(data)
# print(list_box)


test_dic = []
time = False

pass

def test2():
    # 初始化一个空字典用于累加 total_time_percentage
    name_dic = {}

    # 遍历 list_box，累加 total_time_percentage
    for i in list_box:
        name = i["name"]
        total_time_percentage = i["total_time_percentage"]

        if name not in name_dic:
            name_dic[name] = 0
        name_dic[name] += total_time_percentage

    # 将累加结果转换为所需的列表形式
    result_list = [{"name": name, "total_time_percentage": total_time_percentage} for name, total_time_percentage in
                   name_dic.items()]

    # print(result_list)


test2()




list_box2 = []
storage = []

#
def test3(list_data, path=""):
    count = 0
    if isinstance(list_data, list):
        for i in list_data:
            test3(i, path)
    elif isinstance(list_data, dict):
        # 构建当前路径
        current_path = path + list_data["name"]

        if "children" in list_data:
            # 有子节点时，路径后面添加斜杠
            full_path = current_path + "/"
            select_dic = {c_key: list_data[c_key] for c_key in select_keys}
            select_dic["name"] = full_path
            list_box2.append(select_dic)
            count += 1
            for k in list_data["children"]:
                test3(k, full_path)
        else:
            # 没有子节点时，不添加斜杠
            select_dic = {c_key: list_data[c_key] for c_key in select_keys}
            select_dic["name"] = current_path
            list_box2.append(select_dic)

# 调用函数示例
test3(data)

print(list_box2)

#
#
#
#
# test3(data)
# print(list_box2)

