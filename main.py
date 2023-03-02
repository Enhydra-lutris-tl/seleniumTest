import os.path
import shutil

import yaml
from selenium import webdriver
import time
import json
from zipfile import ZipFile
from bs4 import BeautifulSoup

# word文档解析相关
from selenium.webdriver.common.by import By

workpath = '/Users/tanglei/Downloads/'


def getpath(workpath):
    wordlist = os.listdir(workpath)
    for i in wordlist:
        if i.endswith('docx'):
            targetpath = os.path.join(workpath, i)
    return targetpath


splitext = os.path.splitext(getpath(workpath))
zip_path = shutil.copy(getpath(workpath), f'{splitext[0]}_new{splitext[1]}')
with ZipFile(zip_path, 'r') as f:
    for file in f.namelist():
        f.extract(file, workpath)

os.remove(zip_path)
pic_path = os.path.join(workpath, 'word/media')
piclist = os.listdir(pic_path)
print(piclist)

xml = os.path.join(workpath, 'word/document.xml')
# document = ZipFile(getpath(workpath))
# xml = document.read("word/document.xml")
wordObj = BeautifulSoup(open(xml, encoding='utf-8'), "html.parser")
texts = wordObj.findAll("w:t")
for text in texts:
    print(text.text)

# 小红书自动化相关
driver2 = webdriver.Chrome()
driver2.get("https://creator.xiaohongshu.com/login")
if os.path.exists('data.yaml'):

    print('如第一次登录，请在20s内扫码登录！')
    print('如登录过，忽略此信息')
    time.sleep(15)
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
        ceshi = driver2.find_elements(by=By.XPATH, value="//a[@class='btn']")
        ceshi[0].click()
        time.sleep(2)
        ceshi2 = driver2.find_elements(by=By.XPATH, value="//div[@class='header']/div[@class='tab']")
        ceshi2[0].click()
        print(ceshi2)

else:
    print('没有此文件')

# driver.quit()
