import tkinter as tk
import pyautogui as pag
import time
import json

key = json.load(open("key.json","r",encoding='utf-8'))
class Test(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.overrideredirect(True)  # 隱藏視窗的標題列
        self.attributes("-alpha", 0.2)
        self.canvas = tk.Canvas(self,width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.change)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.rect = None
        start_x,start_y =None,None
        self.canvas.pack()
        self.bind("<{}>".format(key['exit']),self.quit)
        self.bind("<{}>".format(key['print']),self.screen)
        self.mainloop()
    def on_button_press(self, event):
        # save mouse drag start position
        self.canvas.delete('all')
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(0,0,0,0,outline="blue",fill="#4169E1")          # 畫矩形正方形
        # print('x',self.start_x,self.start_y)
    def change(self,event):
        self.curX, self.curY = (event.x, event.y)
        self.canvas.coords(self.rect,self.start_x, self.start_y, self.curX, self.curY)
        # print(self.curX,'y',self.curY)
    def on_button_release(self,event):
        pass
    def quit(self,event):
        self.destroy()
    def quit_key(self,event):
        self.canvas.destroy()
    def screen(self,event):
        self.destroy()
        time.sleep(0.2)
        print('OK')
        seconds = round(time.time())
        img = pag.screenshot(region=(self.start_x, self.start_y, self.curX-self.start_x, self.curY-self.start_y))
        img.save(str(seconds)+'.jpg')
        # self.destroy()