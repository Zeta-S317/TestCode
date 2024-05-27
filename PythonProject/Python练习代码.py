int_number = 10
float_number = 20.5
str_text = "hello world"



list_box = [1,2,["list嵌套", "test"],4,"5"]
list_box.append("新增内容")
list_box.pop(2)
del list_box[1]

_text = [1,2,3] *5
a = 10
b = 10

_text.sort(reverse=True)

TEST = 123


class Test:

    def __init__(self,username,level):
        self.username = username
        self.level = level

    def logout(self): # 打印内容
        print(f"你的昵称是{self.username}，等级是{self.level}")


targe1 = Test("测试", 100).logout() # 实例化对象

class stats:
    id = 0 # 角色Id
    username = "" # 角色名称
    heath = 100 # 生命值
    speed = 12 # 速度

class role1(stats):
    
    def __init__(self):
        role1.username = "管理员"
        role1.speed = 20
        print(f"ID：{role1.id}\nUsername：{role1.username}\nheath：{role1.heath}\nspeed：{role1.speed}")

role1()

sum = lambda a,b: a + b
print(sum(1,2))