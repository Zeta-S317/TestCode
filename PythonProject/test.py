def outtest(info):
    if info == "hello world":
        assert(1 > 2)
    else:
        print(info)

info = input("请输入内容:")
outtest(info)