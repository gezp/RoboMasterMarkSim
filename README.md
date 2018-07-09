# MarkSim

## 一、简要说明

本神符模拟器针对robmaster2018而设计，尽可能的模拟官方效果而不需要太多其他硬件费用。一台笔记本电脑加一个显示器，以及一块透明挡板，即可实现官方神符效果（不包括数码管）。本程序的特色是通过__笔记本电脑的麦克风__实现实现__子弹打击屏幕的感应__功能（通过子弹打击屏幕的巨大声音实现）。

__特性：__

* 实现打击屏幕启动，4.5无打击进入待机界面。


* 1.3秒定时切换一张图，如果有子弹打击，通过屏幕感应，立即切换。
* 随时可切换大小符模式

## 二、详细使用

### a.运行环境

* ubuntu16.04+python3

__依赖:__ (python3)

* PyQt5 , pyaudio , numpy

依赖安装方式：

```bash
sudo apt-get update
sudo apt-get install python3-numpy
sudo apt-get install python3-pyqt5  #图形界面依赖
sudo apt-get install python3-pyaudio #麦克风使用依赖
```

### b.使用

__step1.启动__

```bash
python3 marksim.py
```

__step2.全屏切换:__

* 双击窗口，或者按'm'进入全屏

__step3.启动声音监听:__

* 按键盘'a'

__step４.切换大小符模式:__

* 右键单击窗口

__step5.外接显示器：__

* 将笔记本外接大显示器显示即可
* __笔记本需要放置在屏幕旁边__。(以感应子弹打击屏幕时的声音，实现实时切换屏幕)。

## 三、版权及许可证

__联系__

uestc robomaster2018

* csm  448554615@qq.com

- gezp 1350824033@qq.com

__开源许可证__

MarkSim is provided under the __GPL-v3__