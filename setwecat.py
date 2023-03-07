import pyautogui
import pyperclip
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# def main():
#     pyautogui.PAUSE = 0
#
#     icon_position = pyautogui.Point(x=148, y=879)  # 任务栏图标位置
#     entry_position = pyautogui.Point(x=174, y=751)  # 输入框位置
#
#     pyautogui.moveTo(icon_position, duration=1)  # duration为执行时长，可选
#     pyautogui.click(icon_position)
#     pyautogui.moveTo(entry_position, duration=0.7)
#     pyautogui.click(entry_position)
#     pyperclip.copy("快去睡觉")
#     pyautogui.hotkey("ctrl", "v")
#     pyautogui.press("enter")
#     pyperclip.copy("笨猪")
#     pyautogui.hotkey("ctrl", "v")
#     pyautogui.press("enter")
#
#
# scheduler = BlockingScheduler()  # 实例化
# scheduler.add_job(main, "date", run_date=datetime(2021, 8, 18, 24, 00, 00))  # 添加任务
# scheduler.start()

print(pyautogui.position())


def main():
    pyautogui.PAUSE = 1
    icon_click = pyautogui.Point(x=589, y=1017)
    input_click = pyautogui.Point(x=1242, y=838)
    pyautogui.moveTo(icon_click, duration=1)
    pyautogui.click(icon_click)
    pyautogui.moveTo(input_click, duration=1)
    pyautogui.click(input_click)
    pyperclip.copy("真是服了你这个老六了！[自动发送]")
    pyautogui.hotkey('command', 'v')
    pyautogui.press('enter')
    print("任务结束")


# scheduler = BlockingScheduler()  # 实例化一个调度器
# scheduler.add_job(main, "date", run_date=datetime(2023, 3, 6, 11, 23, 00))  # 添加任务
# scheduler.start()
