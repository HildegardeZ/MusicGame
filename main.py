import pygame as pg
from settings import Settings
from circle import Circle
import sys
from note import Note
from time import sleep


class RhythmGame:
    def __init__(self):
        """ 初始化 """
        pg.init()
        pg.mixer.init()
        clock = pg.time.Clock()
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.width, self.settings.height), 0, 32)
        self.bg = pg.image.load(self.settings.background)
        pg.display.set_caption(self.settings.caption_name)
        pg.mixer.music.load(self.settings.musicFile)
        pg.mixer.music.play()
        # 创建判定区
        self.circle = Circle(self)
        # 创建音符组
        self.notes = pg.sprite.Group()
        # 判断是否为连击
        self.isCombo = True
        # 判断出界
        self.isHit = False
        # 总分
        self.score = 0
        self.combo = 0

    def create_note(self):
        """ 创建音符并添加到组 """
        # sleep(1.4)
        new_note = Note(self)
        self.notes.add(new_note)
            
    def update_screen(self):
        """ 更新屏幕图像 """
        self.screen.blit(self.bg, (0, 0))
        self.circle.blitme()
        self.create_note()
        for note in self.notes.sprites():
            note.blitme()
        pg.display.update()  # 要刷新才能出现图片

    def run_game(self):
        """ 运行游戏 """
        while True:
            self.update_screen()
            self.check_events()
            self.notes.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # 按键时
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)
        # self.create_note()

    def check_keydown_events(self, event):
        if event.key == pg.K_SPACE:
            self.press()
        # 按 Q 退出游戏
        elif event.key == pg.K_q:
            sys.exit()
            pg.quit()

    def press(self):
        """ 判断note是否在判定圈内并把note从群组删除 """
        for note in self.notes.sprites():
            if pg.sprite.spritecollideany(note, self.circle):
                self.isHit = True
                self.notes.remove(note)
            # 想优化成
            if self.isHit:
                self.score += 200
                self.isCombo = True
                if self.isCombo:
                    self.combo += 1
            else:
                self.combo = 0
                self.isCombo = False
            self.notes.remove(note)
        print('test')

    def check_miss_after(self):
        """ 检查是否有note已经超过了判定区 """
        screen_rect = self.screen.get_rect()
        for note in self.notes.sprites():
            if note.rect.bottom >= screen_rect.bottom:
                self.notes.remove(note)
                break

    def prep_score(self):
        score_str = "{;,}".format(self.score, True)
        return

    def prep_combo(self):
        return


if __name__ == "__main__":
    RG = RhythmGame()
    RG.run_game()
