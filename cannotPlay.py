import os
import time
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class KillGame:
    def __init__(self, list_of_name, workingDay, workingTime):
        self.game_name = list_of_name
        self.workingDay = workingDay
        self.workingTime = workingTime
    
    def warning(self):
        app = QtWidgets.QApplication(sys.argv)
        msg_box = QtWidgets.QMessageBox()
        choice = msg_box.warning(msg_box, "warning", "工作时间里面不可以玩游戏哦！", QtWidgets.QMessageBox.Yes)
        if choice == QtWidgets.QMessageBox.Yes:
            exit(0)
        else:
            exit(1)
        sys.exit(app.exec_())

    def isRunning(self):
        for eachGame in self.game_name:
            try:
                print('tasklist | findstr '+ eachGame)
                process=len(os.popen('tasklist | findstr '+ eachGame).readlines())
                if process >= 1:
                    os.system("taskkill /im " + eachGame + " /f")
                    self.warning()
            except:w
                print(eachGame + " not running")

    def in_working_time(self):
        now = time.localtime()
        today = time.strftime("%A",now)
        hours = int(time.strftime("%H", now))
        if today in self.workingDay:
            for each_pare in self.workingTime:
                print(each_pare)
                if hours >= each_pare[0] and hours <= each_pare[1]:
                    # in working hour
                    print("inside")
                    self.isRunning()



if __name__ == "__main__":
    game_name = ["dontstarve_steam.exe"]
    BlockGame = "D:\\dontPlay\\blockgame.txt"
    WorkingDay = "D:\\dontPlay\\WorkingDay.txt"
    WorkingTime = "D:\\dontPlay\\WorkingTime.txt"
    wd_list = []
    wt_list_tmp = []
    
    with open(BlockGame, 'r') as bg:
        for line in bg:
            game_name.append(line.split(','))

    with open(WorkingDay, 'r') as wd:
        for line in wd:
            wd_list.append(line.strip(','))

    with open(WorkingTime, 'r') as wt:
        for line in wt:
            wt_list_tmp=line.split(',')
    
    wt_list = []
    tmp = []
    i=0
    for each in wt_list_tmp:
        if i == 0:
            i = i + 1
            tmp.append(int(each))
        else:
            tmp.append(int(each))
            wt_list.append(tmp.copy())
            tmp.clear()
            i = 0

    print(wd_list)
    print(wt_list)
    killgame = KillGame(game_name, wd_list, wt_list)

    while True:
        killgame.in_working_time()
        time.sleep(10)
        
    