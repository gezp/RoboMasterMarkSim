# -*- coding: utf-8 -*-
########################################################################
#Copyright(c)     UESTC ROBOMASTERS2018      MarkSim Code for robot
#ALL RIGHTS RESERVED
#@file:marksim.py
#@brief: nothing
#@vesion 1.0
#@author: csm,gezp
#@email: 448554615@qq.com,1350824033@qq.com
#@date: 18-7-9
#######################################################################
import sys
import random
import pyaudio
import numpy as np
import time
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TestWindow(QWidget):
    def __init__(self):
        super(TestWindow,self).__init__()
        self.imgLabels=[];
        self.imgs=[]
        self.rand9nums=[]
        self.initUI()
        self.model=0
        self.active=0;
        self.starttime=time.time()
        self.endtime=time.time()

    def initUI(self):
        #self.setWindowTitle("big mark")
        self.grid = QGridLayout(self)
        self.setWindowTitle('main')
        for i in range(0,9):
            label = QLabel()
            self.grid.addWidget(label,(i-i%3)/3,i%3)
            self.imgLabels.append(label)
        self.initLabel();
        #设置水平间距
        self.grid.setHorizontalSpacing(100);
        #设置垂直间距
        self.grid.setVerticalSpacing(60);
        #设置外间距
        self.grid.setContentsMargins(10, 10,10, 10);
        self.setStyleSheet("background-color: black");
        self.setLayout(self.grid)
        self.setFocusPolicy(Qt.ClickFocus);
        self.timer = QTimer(self);
        self.timer.timeout.connect(self.onTimerOut)
        self.startFlag=False

        #audio
        self.CHUNK = 512
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 48000
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=self.CHUNK)
        self.flag=False
        self.monitorFlag=False
        self.m=0
        #audio timer
        self.monitorTimer = QTimer(self);
        self.monitorTimer.timeout.connect(self.onMonitor)

    def clean(self):
        for i in range(0,9):
            imgpath="./0.jpg"
            img=QImage(imgpath) 
            img =img.scaledToHeight(180)
            self.imgLabels[i].setPixmap(QPixmap.fromImage(img))     
            self.imgLabels[i].setScaledContents(True)     

    def initLabel(self):
        for i in range(0,9):
            imgpath="./0.jpg"
            self.rand9nums.append(i+1)
            img=QImage(imgpath)
            img =img.scaledToHeight(180)
            self.imgs.append(img)
        for i in range(0,9):
            self.imgLabels[i].setPixmap(QPixmap.fromImage(self.imgs[i]))
            self.imgLabels[i].setScaledContents(True)

    def update9Img(self):
        if(self.active==0):
            self.clean()
        elif(self.model==0):
            random.shuffle(self.rand9nums)
            for i in range(0,9):
                imgpath="./SmallMarkImg/"+str(self.rand9nums[i])+"/"+str(random.randint(1,95))+".png"
                img=QImage(imgpath) 
                img =img.scaledToHeight(180)
                self.imgLabels[i].setPixmap(QPixmap.fromImage(img))     
                self.imgLabels[i].setScaledContents(True)
        else:
            random.shuffle(self.rand9nums)
            for i in range(0,9):
                imgpath="./BigMarkImg/"+str(self.rand9nums[i])+".png"
                img=QImage(imgpath)
                img=img.scaledToHeight(180)
                self.imgLabels[i].setPixmap(QPixmap.fromImage(img))
                self.imgLabels[i].setScaledContents(True)   

    def onTimerOut(self):
        self.update9Img();

    def mousePressEvent(self,event):
        if(self.model==0):
            self.model=1;
        else:
            self.model=0;
        
    def mouseDoubleClickEvent(self,event):
        if(self.isFullScreen()):
            self.showNormal()
        else:
            self.showFullScreen()

    def keyPressEvent(self, event):  
        if event.key() == Qt.Key_Escape:  
            self.close()  
        elif event.key() == Qt.Key_M:
            self.showFullScreen()
        elif event.key() == Qt.Key_A:
            if(self.startFlag==False):
                self.timer.start(1300)
                self.startFlag=True
                print("start monitor")
                self.monitorTimer.start(5)
                self.starttime=time.time()
                #self.update9Img() 

    def onMonitor(self):
        frames = []
        for i in range(0, 1):
            data = self.stream.read(self.CHUNK)
            frames.append(data)
        audio_data = np.fromstring(data, dtype=np.short)
        temp = np.max(audio_data)

        if ((temp > 30000)&(self.monitorFlag==False)):
            self.monitorFlag=True
            self.m=self.m+1
            self.timer.start(1300)
            self.active=1;
            self.update9Img() 
            self.starttime=time.time()
            print ("检测到信号"+":"+str(self.m))
            print ('当前阈值：'+str(temp))
        if ((self.monitorFlag==True)&(temp<10000)):
            self.monitorFlag=False

        self.endtime=time.time()
        proctime=self.endtime-self.starttime
        if proctime>4.5:
            if self.active==1:
                self.active=0
                self.update9Img()      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestWindow()
    ex.show()
    sys.exit(app.exec_()) 


