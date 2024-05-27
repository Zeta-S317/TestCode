import json

with open('func_data_summary.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# 第一题，获取全部为name和total_time_percentage的数据，包括children里的

all_data = []


def get_children(data):
    select_keys = ["name", "total_time_percentage"]
    if isinstance(data, list):
        for i in data:
            get_children(i)
    elif isinstance(data, dict):
        if "children" in data:
            select_dic = {c_key: data[c_key] for c_key in select_keys}
            all_data.append(select_dic)
            for k in data["children"]:
                get_children(k)
        else:
            select_dic = {c_key: data[c_key] for c_key in select_keys}
            all_data.append(select_dic)


get_children(json_data)

# 控制台输出所有数据，包括children下的,但不包括路径
# print(all_data)
# 控制台输出所有数据，包括children下的,但不包括路径

# 第二题 提取里面的name的值和total_time，同样name的值合并，并且total_time相加

name_list = []  # 合并相同name的值，并且它们的total_time相加


def get_dic_values():
    name_dic = {}

    for i in all_data:
        name_value = i["name"]
        number_value = i["total_time_percentage"]

        if name_value not in name_dic:
            name_dic[name_value] = 0
        name_dic[name_value] += number_value

    name_list.append([{"name": v1, "total_time_percentage": v2} for v1, v2 in name_dic.items()])


get_dic_values()

# 控制台输出提取后的值
# print(name_list)
# 控制台输出提取后的值


# 第三题，带有全部路径的为name和total_time_percentage所有数据
all_data_path = []


#
def get_all_path(data, path=""):
    select_keys = ["name", "total_time_percentage"]
    if isinstance(data, list):
        for i in data:
            print(path)
            get_all_path(i, path)
    elif isinstance(data, dict):
        current_path = path + data["name"]

        if "children" in data:
            full_path = current_path + "/"
            select_dic = {c_key: data[c_key] for c_key in select_keys}
            select_dic["name"] = full_path
            all_data_path.append(select_dic)
            for k in data["children"]:
                get_all_path(k, full_path)
        else:
            select_dic = {c_key: data[c_key] for c_key in select_keys}
            select_dic["name"] = current_path
            all_data_path.append(select_dic)


get_all_path(json_data)

# 控制台输出带路径的全部为name和total_time_percentage数据
# print(all_data_path)
# 控制台输出带路径的全部为name和total_time_percentage数据
