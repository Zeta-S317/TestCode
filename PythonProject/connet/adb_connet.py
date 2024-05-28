import uiautomator2 as u2

d = u2.connect()


# print(d.)
# print(d.app_list())
# d.app_start("com.tencent.mm")  # 打开微信
# d.xpath("//*[@text='微信']").click()
# now_time = "当前时间：" + time.strftime("%Y-%m-%d %X", time.localtime())
# print(now_time)
# time.sleep(5)
# d.app_stop("com.tencent.mm")


# import uiautomator2 as u2
#
#
# d = u2.connect()
# for i in d.app_list():
#     if i == "com.ss.android.ugc.aweme":
#         print("找到抖音，开始启动")
#         d.app_start("com.ss.android.ugc.aweme")
#         break

class DouYinTest:
    def __init__(self, timecount, input_info):
        self.timecount = timecount
        self.input_info = input_info
    def star_and_sub(self):
        d.click() # 点赞
        d.click() # 点关注

    def send_info(self):
        d.send_keys(self.input_info, clear=True)
        # 等待2秒后打开评论区
        # 填写评论
    def down_scr(self):
        d.down


if __name__ == "__main__":
    DouYinTest(3, "测试")
