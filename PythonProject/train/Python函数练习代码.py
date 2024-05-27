list_data = ["hello"]


def change_info(data):
    data.append("你好")
    return data


change_info(list_data)

print(list_data)


def print_info(arg1, *test):
    print(arg1)
    for var in test:
        print(var)
    return


# print_info(10)
print_info(30, 40, 50)
