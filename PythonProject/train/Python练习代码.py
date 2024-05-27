class Test:

    def __init__(self, username, level):
        self.username = username
        self.level = level

    def login(self):  # 打印内容
        print(f"你的昵称是{self.username}，等级是{self.level}")


Test("测试", 100).login()


class Stats:
    id = 0  # 角色Id
    username = ""  # 角色名称
    heath = 100  # 生命值
    speed = 12  # 速度


class CustomRoleAdmin(Stats):

    def __init__(self):
        CustomRoleAdmin.username = "管理员"
        CustomRoleAdmin.speed = 20
        print(f"====你的角色面板====\nID：{CustomRoleAdmin.id}\nUsername：{CustomRoleAdmin.username}\nheath：{CustomRoleAdmin.heath}\nspeed：{CustomRoleAdmin.speed}")


CustomRoleAdmin()
