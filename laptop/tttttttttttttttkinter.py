import tkinter as tk
from tkinter.constants import NO  # 使用Tkinter前需要先匯入
from PIL import Image, ImageTk
# 第1步，例項化object，建立視窗window
class Winn(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        # self.overrideredirect(True)
        # 第2步，給視窗的視覺化起名字
        self.title('My Window')

        # 第3步，設定視窗的大小(長 * 寬)
        self.geometry('{}x{}'.format(300,300))  # 這裡的乘是小x
        # self.attributes("-alpha", 0.2)
        self.attributes("-toolwindow", True)
        # 第4步，在圖形介面上建立 500 * 200 大小的畫布並放置各種元素
        button = tk.Button(self,text='start',command=self.win).pack()
        self.bind('<F1>',self.quit)
    def win(self):
        self.top = tk.Toplevel()
        self.x = self.y = 0
        self.top.overrideredirect(True)
        # 第2步，給視窗的視覺化起名字
        self.top.title('My Window')

        # 第3步，設定視窗的大小(長 * 寬)
        self.top.geometry('{}x{}'.format(self.winfo_screenwidth(),self.winfo_screenheight()))  # 這裡的乘是小x
        self.top.attributes("-alpha", 0.2)
        self.top.attributes("-toolwindow", True)
        # self.bind('<F3>',self.cv)

    # def cv(self,event):
        
        self.canvas = tk.Canvas(self.top,width=self.winfo_screenwidth(), height=self.winfo_screenheight(),bg='grey')
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.change)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.rect = None
        start_x,start_y =None,None

        self.canvas.bind("<F2>", self.cv_quit)
        self.canvas.pack()
        self.bind('<F3>',self.quit)
    def quit(self,event):
        # global self
        self.destroy()
    # 第6步，觸發函式，用來一定指定圖形
    def moveit(self):
        self.canvas.move(self.rect, 2, 2) # 移動正方形rect（也可以改成其他圖形名字用以移動一起圖形、元素），按每次（x=2, y=2）步長進行移動
    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(330, 30, 330, 30,fill='#FFFFCC')          # 畫矩形正方形
    def change(self,event):
        curX, curY = (event.x, event.y)
        self.canvas.coords(self.rect,self.start_x, self.start_y, curX, curY)
    def on_button_release(self,event):
        pass
    def cv_quit(self,event):
        self.top.destroy()
    # 第5步，定義一個按鈕用來移動指定圖形的在畫布上的位置
    
    # 第7步，主視窗迴圈顯示

if __name__ == '__main__':
    window = Winn()
    window.mainloop()