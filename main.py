# _*_ coding:UTF-8 _*_
import pyautogui
import time
import sys


def clickSecKill(gTime):
    print("ready to Kill..")
    while True:
        now=time.time()
        if(now>gTime):
            print("Kill now...")
            try100()
            print("Kill end...")

#点他100次
def try100():
    for i in range(0,100):
        pyautogui.click()
        time.sleep(1*0.001)
    sys.exit()

if __name__ == '__main__':
    clickSecKill(1514124000.0) #  左侧时间为2017-12-24 22:00:00


