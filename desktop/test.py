import tkinter as tk
import pyautogui as pag
import time
import keyboard
import backtest
from multiprocessing import Process

class Root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("200x200")
        self.configure(bg="gray")
        self.mybutton1 = tk.Button(self, text='開始',command=self.new_win_button)
        self.mybutton2 = tk.Button(self, text='結束',command=self.quit)
        # self.mybutton3 = tk.Button(self, text='測試',command=self.new_win_button)
        # self.mybutton4 = tk.Button(self, text='測試',command=self.new_win_button)
        self.bind('<Control-z>',self.new_win_keyboard)
        self.bind('<F2>',self.quit_keyboard)
        self.mybutton1.pack() 
        self.mybutton2.pack()
        # self.mybutton3.pack()
        # self.mybutton4.pack()
    def new_win_button(self):
        self.top = tk.Toplevel()
        self.top.overrideredirect(True)  # 隱藏視窗的標題列
        self.top.attributes("-alpha", 0.2)
        self.canvas = tk.Canvas(self.top,width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.change)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.rect = None
        start_x,start_y =None,None
        self.canvas.pack()
        self.top.bind('<F2>',self.quit_keyboard)
        self.top.bind('<F5>',self.screen)
    def new_win_keyboard(self,event):
        self.top = tk.Toplevel()
        self.top.overrideredirect(True)  # 隱藏視窗的標題列
        self.top.attributes("-alpha", 0.2)
        self.canvas = tk.Canvas(self.top,width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.change)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.rect = None
        start_x,start_y =None,None
        self.canvas.pack()
        self.top.bind('<F2>',self.quit_keyboard)
        self.top.bind('<F5>',self.screen)
        # self.canvas.bind("<ButtonPress-1>", self.quit_key)
    def on_button_press(self, event):
        # save mouse drag start position
        self.canvas.delete('all')
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(0,0,0,0,outline="blue",fill='yellow')          # 畫矩形正方形
        # print('x',self.start_x,self.start_y)
    def change(self,event):
        self.curX, self.curY = (event.x, event.y)
        self.canvas.coords(self.rect,self.start_x, self.start_y, self.curX, self.curY)
        # print(self.curX,'y',self.curY)
    def on_button_release(self,event):
        pass

    def quit(self):
        self.destroy()
    def quit_keyboard(self,event):
        self.top.destroy()
    def quit_key(self,event):
        self.canvas.destroy()
    def screen(self,event):
        self.top.destroy()
        time.sleep(0.2)
        print('OK')
        seconds = round(time.time())
        img = pag.screenshot(region=(self.start_x, self.start_y, self.curX-self.start_x, self.curY-self.start_y))
        img.save(str(seconds)+'.jpg')

def main():
    root = Root()
    root.mainloop()
def main2():
    qaz = 0
    while qaz < 1231323211651564641:
        qaz +=1
        if keyboard.read_key() == 'f8':
            rb = backtest.Test()
            rb.mainloop
def main3():
    p1 = Process(target=main)
    p1.start()

    p2 = Process(target=main2)
    
    p2.start()

if __name__ == '__main__':
    main3()