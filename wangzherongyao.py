import win32api
import win32gui
import win32con
import time


class WangzherongyaoGame:

    def __init__(self):
        self.hwnd = win32gui.FindWindow(win32con.NULL, '腾讯手游助手【极速傲引擎】')
        self.left, self.top, self.right, self.bottom = win32gui.GetWindowRect(self.hwnd)
        self.sonHwnd = win32gui.FindWindowEx(self.hwnd, 0, "AEngineRenderWindowClass", None)
        self.sonLeft, self.sonTop, self.sonRight, self.sonBottom = win32gui.GetWindowRect(self.sonHwnd)
        self.offsetTop = self.sonTop - self.top
        self.offsetLeft = self.sonLeft - self.left
        self.width = self.sonRight - self.sonLeft
        self.height = self.sonBottom - self.sonTop

    def show(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(self.hwnd)

    def getPixelColor(self, xy):
        color = win32gui.GetPixel(win32gui.GetWindowDC(self.hwnd), xy[0] + self.offsetLeft, xy[1] + self.offsetTop)
        return color % 256, color // 256 % 256, color // 256 // 256

    def click(self, xy):
        long_position = win32api.MAKELONG(xy[0], xy[1])
        print(win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position))
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)


if __name__ == '__main__':

    xys = [(100, 100),(200, 200),(300, 300),(400, 400),(805, 530), (805, 540), (805, 550), (805, 560), (805, 527), (805, 485), (774, 400), (1000, 87)]
    autoBtnXy = (957, 22)
    autoBtnColor = (175, 192, 201)

    game = WangzherongyaoGame()
    game.show()
    print(game.getPixelColor(autoBtnXy))

    while True:
        if game.getPixelColor(autoBtnXy) == autoBtnColor:
            print(456)
            game.click(autoBtnXy)
        for xy in xys:
            print(xy)
            game.click(xy)
        time.sleep(0.3)
