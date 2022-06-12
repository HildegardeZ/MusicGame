from settings import Settings


class GameFunc:
    def __init__(self):
        self.settings = Settings()
        self.isCombo = True

    def perfect(self):
        """ 音符中心在线1/2半径的同心圆中心点击 """

    def good(self):
        """ 音符中心在判定圈外圈 """

    def bad(self):
        """ 音符中心在判定圈多1/2半径的外圈点击 """

    def bad(self):
        """ 音符中心在 1/4屏幕的剩下所有位置 """
