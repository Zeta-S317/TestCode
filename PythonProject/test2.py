import json



with open('func_data_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

a = [{"self_time": 2220.8094799999994, "name": "PlayerLoop", "total_time": 298504.70992,
      "avg_total_time": 99.10514937583001, "calls": 3012, "gc_mem": 66502.0986328125
         , "gt_10ms": 3012, "max_total_time": 5370.848, "calls_pre_frame": 1.0, "total_time_percentage": 100.0}]

# select_keys = ["self_time", "name", "total_time", "avg_total_time", "calls", "gc_mem",
#        "gt_10ms", "max_total_time", "calls_pre_frame", "total_time_percentage"]

select_keys = ["name", "total_time_percentage"]

list_box = []

def Get_children(list_data):
    if isinstance(list_data, list):
        for i in list_data:
            Get_children(i)
    elif isinstance(list_data, dict):
        if "children" in list_data:
            select_dic = {c_key: list_data[c_key] for c_key in select_keys}
            list_box.append(select_dic)
            for k in list_data["children"]:
                Get_children(k)
        else:
            select_dic = {c_key: list_data[c_key] for c_key in select_keys}
            list_box.append(select_dic)

Get_children(data)



test_dic = []
time = False

def test2():
    # 初始化一个空字典用于累加
    name_dic = {}

    # 遍历 list_box，然后存放
    for i in list_box:
        v1 = i["name"]
        v2 = i["total_time_percentage"]

        if v1 not in name_dic:
            name_dic[v1] = 0
        name_dic[v1] += v2

    # 将累加结果转换为所需的列表形式
    result_list = [{"name": v1, "total_time_percentage": v2} for v1, v2 in
                   name_dic.items()]

    # print(result_list)


test2()




list_box2 = []

#
def test3(list_data, path=""):
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
            for k in list_data["children"]:
                test3(k, full_path)
        else:
            # 没有子节点时，不添加斜杠
            select_dic = {c_key: list_data[c_key] for c_key in select_keys}
            select_dic["name"] = current_path
            list_box2.append(select_dic)

test3(data)

print(list_box2)


