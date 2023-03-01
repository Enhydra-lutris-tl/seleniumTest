import os.path

import yaml
from selenium import webdriver
import time
import json
if os.path.exists('data.yaml'):
    driver2 = webdriver.Chrome()
    driver2.get("https://creator.xiaohongshu.com/login")
    # 读取cookies
    with open("data.yaml", "r", encoding="utf-8") as f:
        cookies = yaml.safe_load(f)
    for cookie in cookies:
        # 把cookie传给driver
        driver2.add_cookie(cookie)
    driver2.get("https://creator.xiaohongshu.com/login")
else:
    print(22222)
# driver = webdriver.Chrome()
# loginUrl = 'https://creator.xiaohongshu.com/login'
# driver.get(loginUrl)
# time.sleep(20)
# print('登陆成功！！！')
# cookies = driver.get_cookies()
# print(cookies)
#
# with open("data.yaml", "w", encoding="utf-8") as f:
#     # 快捷键导包，alt+enter
#     # 序列化cookie，存入yaml文件
#     yaml.dump(cookies, f)
#
#


# driver.quit()
