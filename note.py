import pygame as pg
from pygame.sprite import Sprite


class Note(Sprite):
    def __init__(self, RhythmGame):
        super().__init__()
        self.screen = RhythmGame.screen
        self.settings = RhythmGame.settings
        # 加载note图像并获取外接矩形
        self.image = pg.image.load(self.settings.noteImg)
        self.rect = self.image.get_rect()
        # note从屏幕上方顶部开始移动
        self.screen_rect = RhythmGame.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """ 向下移动 """
        self.y += self.settings.speed
        self.rect.y = self.y

    def blitme(self):
        """ 指定位置绘制note """
        self.screen.blit(self.image, self.rect)
