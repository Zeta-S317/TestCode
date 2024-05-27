list_data = ["hello"]


def change_info(data):
    data.append("你好")
    return data


change_info(list_data)

print(list_data)
