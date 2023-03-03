import os.path
import shutil

import yaml
from selenium import webdriver
import time
import json
from zipfile import ZipFile
from bs4 import BeautifulSoup

# word文档解析相关
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

work_path = '/Users/tanglei/Downloads/ceshi'


def getpath(workpath):
    wordlist = os.listdir(workpath)
    target_path_list = []
    for i in wordlist:
        if i.endswith('docx'):
            target_path_list.append(os.path.join(workpath, i))
    return target_path_list


print(getpath(work_path))
main_path = getpath(work_path)[0]
splitext = os.path.splitext(main_path)
zip_path = shutil.copy(main_path, f'{splitext[0]}_new{splitext[1]}')
with ZipFile(zip_path, 'r') as f:
    for file in f.namelist():
        f.extract(file, work_path)

os.remove(zip_path)
pic_path = os.path.join(work_path, 'word/media')
piclist = os.listdir(pic_path)
title_img_path = os.path.join(pic_path, piclist[0])
print(title_img_path)
xml = os.path.join(work_path, 'word/document.xml')
# document = ZipFile(getpath(workpath))
# xml = document.read("word/document.xml")
wordObj = BeautifulSoup(open(xml, encoding='utf-8'), "html.parser")
texts = wordObj.findAll("w:t")
title = texts[0].text
text = ''
for c in texts:
    text = text + c.text
# print(text)
text_list = text.split("。")

# # 小红书自动化相关
driver2 = webdriver.Chrome()
driver2.get("https://creator.xiaohongshu.com/login")
driver2.maximize_window()
if os.path.exists('data.yaml'):

    print('如第一次登录，请在20s内扫码登录！')
    print('如登录过，忽略此信息')
    time.sleep(5)
    getelement = driver2.find_elements(by=By.CLASS_NAME, value='mask')
    if len(getelement) == 0:
        print('此页面没有该元素')
        cookies = driver2.get_cookies()
        with open("data.yaml", "w", encoding="utf-8") as f:
            # 快捷键导包，alt+enter
            # 序列化cookie，存入yaml文件
            yaml.dump(cookies, f)
    else:
        print('使用cookies登录')
        # 读取cookies
        with open("data.yaml", "r", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            # 把cookie传给driver
            driver2.add_cookie(cookie)
        driver2.get("https://creator.xiaohongshu.com/login")
        time.sleep(5)
        # 点击发布笔记按钮
        publish_click = driver2.find_elements(by=By.XPATH, value="//a[@class='btn']")
        publish_click[0].click()
        time.sleep(2)
        # 点击发布图文按钮
        publish_img_click = driver2.find_elements(by=By.XPATH, value="//div[@class='header']/div[@class='tab']")
        publish_img_click[0].click()
        time.sleep(2)
        # 上传图片
        uploading_img = driver2.find_elements(by=By.XPATH, value="//input[@class='upload-input']")
        uploading_img[0].send_keys(title_img_path)
        time.sleep(2)
        # 输入标题
        input_title = driver2.find_elements(By.XPATH, "//input[@class='c-input_inner']")
        input_title[0].send_keys(title)
        time.sleep(2)
        # 输入文本内容
        input_texts = driver2.find_elements(By.ID, "post-textarea")
        for text_li in text_list:
            input_texts[0].send_keys(text_li, Keys.ENTER)
        # time.sleep(4)
        # click_header = driver2.find_elements(By.XPATH, "//div[@class='img-post']/div[@class='header']")
        # click_header[0].click()
        # print(click_header)
        print('内容填写完毕，将在5s后关闭')
        time.sleep(5)
        close_page = driver2.find_elements(By.XPATH, "//button[@class='css-fm44j css-osq2ks dyn']")
        close_page[5].click()

        # ceshi4 = driver2.find_elements(by=By.XPATH, value="//div[@class='wrapper']/div[@class='btn red']")
        # ceshi4[0].click()
        # print(ceshi4)
else:
    print('没有此文件')

# driver.quit()
