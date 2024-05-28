import time

import uiautomator2 as u2


# d = u2.connect()
# print(d.)
# print(d.app_list())
# d.app_start("com.tencent.mm")  # 打开微信
# d.xpath("//*[@text='微信']").click()
now_time = "当前时间：" + time.strftime("%Y-%m-%d %X", time.localtime())
print(now_time)
# time.sleep(5)
# d.app_stop("com.tencent.mm")

