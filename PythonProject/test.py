def outtest(info):
    if info == "hello world":
        print("你不能hello world")
    else:
        print(info)

info = input("请输入内容:")
outtest(info)