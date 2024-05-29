import time

import uiautomator2 as u2

start_time = time.time()


def get_now_time():
    now_time = time.strftime("%Y-%m-%d %X ", time.localtime())
    return now_time


class DouYinTest:
    def __init__(self, like=False, comment=False, sub=False, input_info="", timecount=0):
        self.input_info = input_info
        self.d = u2.connect()

        self.like = like
        self.comment = comment
        self.sub = sub

        self.douyin = self.d.app_current()
        if self.douyin["package"] == "com.ss.android.ugc.aweme":
            print(get_now_time() + "抖音正在运行，为防止抖音卡住其他页面，重启抖音")
            self.d.app_stop("com.ss.android.ugc.aweme")
            self.d.app_start("com.ss.android.ugc.aweme")
            self.d.wait_activity("com.ss.android.ugc.aweme", 15)
        else:
            self.d.app_start("com.ss.android.ugc.aweme")
            print(get_now_time() + "抖音未运行，正在启动抖音")
            self.d.wait_activity("com.ss.android.ugc.aweme", 15)

        self.error = get_now_time() + "当前应用不是抖音，终止程序！"

        i = 0
        while i < timecount:
            i += 1
            self.video = get_now_time() + f"第{i}个视频："
            self.douyin = self.d.app_current()
            if self.douyin["package"] == "com.ss.android.ugc.aweme":
                print(self.video + "初始化")
                self.d.wait_activity("com.ss.android.ugc.aweme", 15)
                self.__like()
            else:
                print(self.error)
                break

    def __like(self):
        self.douyin = self.d.app_current()
        if self.douyin["package"] == "com.ss.android.ugc.aweme":
            if self.like:
                if self.d.xpath("//*[@resource-id='com.ss.android.ugc.aweme:id/eun'"
                                "]/android.widget.ImageView[1]").exists:
                    self.d.xpath("//*[@resource-id='com.ss.android.ugc.aweme:id/eun'"
                                 "]/android.widget.ImageView[1]").click()  # 点赞
                    print(self.video + "已点赞")
                    self.__send_info()
                else:
                    print(self.video + "找不到点赞图标")
                    self.__send_info()
            else:
                self.__send_info()
        else:
            return 0

    def __sub(self):
        self.douyin = self.d.app_current()
        if self.douyin["package"] == "com.ss.android.ugc.aweme":
            if self.sub:
                if self.d(resourceId="com.ss.android.ugc.aweme:id/ht8").exists:
                    self.d(resourceId="com.ss.android.ugc.aweme:id/ht8").click()
                    print(self.video + "已订阅")
                    self.__down_scr()
                else:
                    print(self.video + "找不到订阅图标，已经订阅？")
                    self.__down_scr()
            else:
                self.__down_scr()
        else:
            return 0

    def __send_info(self):
        self.douyin = self.d.app_current()
        if self.douyin["package"] == "com.ss.android.ugc.aweme":
            if self.comment:
                if self.d(resourceId="com.ss.android.ugc.aweme:id/c8g").exists:
                    print(self.video + "正在执行评论")
                    time.sleep(0.5)
                    self.d(resourceId="com.ss.android.ugc.aweme:id/c8g").click(timeout=5)  # 打开评论区
                    time.sleep(1)
                    self.d(resourceId="com.ss.android.ugc.aweme:id/c67").click(timeout=5)  # 点击评论窗口
                    self.d.send_keys(self.input_info, clear=True)
                    time.sleep(0.5)
                    self.d.press("back")
                    self.d.press("back")
                    self.d.press("back")
                    print(self.video + "评论完成")
                    self.__sub()
                else:
                    print(self.video + "找不到评论图标，跳过直播")
                    self.__sub()
            else:
                self.__sub()
        else:
            return 0

    def __down_scr(self):
        self.douyin = self.d.app_current()

        if self.douyin["package"] == "com.ss.android.ugc.aweme":
            self.d.swipe_ext("up", scale=1)
        else:
            return 0


if __name__ == "__main__":
    DouYinTest(True, True, True, "Hello World", 100)
    end_time = time.time()
    print(f"程序已结束，用时：{round(end_time - start_time, 1)}秒")

"""
是否点赞，是否评论，是否订阅，重复几次？

"""
