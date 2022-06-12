import pygame as pg


class Circle:
    def __init__(self, RhythmGame):
        self.screen = RhythmGame.screen
        self.settings = RhythmGame.settings
        # 加载飞机图像并获取外接矩形,飞机放在屏幕底部中央
        self.image = pg.image.load(self.settings.circleImg)
        self.rect = self.image.get_rect()
        self.screen_rect = RhythmGame.screen.get_rect()
        self.rect.center = self.screen_rect.center
        # 因为速度值可能有小数，借助x改编rect的x值，解决左右移动速度不均的问题

    def blitme(self):
        """ 指定位置绘制判定区 """
        self.screen.blit(self.image, self.rect)
