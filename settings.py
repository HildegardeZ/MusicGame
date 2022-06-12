import pygame as pg
import time as t


class Settings:
    def __init__(self):
        self.musicFile = "music/Brain Power.mp3"  # 曲目
        self.background = "img/background.png"  # 背景
        self.width = 1000
        self.height = 600
        self.caption_name = 'musicgame'
        # self.keyFile = "music/keytone.mp3"  # 按键音效
        self.isKeyOn = False  # 默认不开启按键音

        # 前后调整按键出现时间
        self.judgeTime = 0  # 默认一开始不调整
        self.gap = 0.1  # 0.1秒一个跨度

        # 符号
        self.noteImg = "img/note.png"

        # 速度
        self.speed = 20

        # 判定区
        self.circleImg = "img/circle.png"
