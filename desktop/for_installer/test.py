import tkinter as tk
<<<<<<< HEAD
from tkinter import messagebox
import json
# from multiprocessing import Process
import threading
import keyboard
import backtest
import sys
import time
import pyautogui
key = json.load(open("key.json","r",encoding='utf-8'))
a=0
b=1
=======
import json
from multiprocessing import Process
import keyboard
import backtest
import sys

key = json.load(open("key.json","r",encoding='utf-8'))
p1 =0
p2 =0
>>>>>>> 5ea9a83583cfc1db55af33cecc58e1b3db020b69
class Root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("350x350")
        self.configure(bg="#F1DEFF")
        self.canvas = tk.Canvas(self,bg = "#F1DEFF",height = 350,width = 350,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.create_rectangle(215.0,24.0,350.0,204.0,fill="#D9DBFC",outline="")
        # self.canvas.create_rectangle(218.0,210.0,261.0,233.0,fill="#D9DBFC",outline="") #設定
        # self.canvas.create_rectangle(282.0,210.0,325.0,233.0,fill="#D9DBFC",outline="") #確定
        self.canvas.create_rectangle(219.0,319.0,329.0,342.0,fill="#D9DBFC",outline="") #結束
        self.canvas.create_rectangle(20.0,319.0,130.0,342.0,fill="#D9DBFC",outline="") #開始
        # self.canvas.create_rectangle(11.0,28.0,87.0,103.0,fill="#D9DBFC",outline="") #左上
        self.canvas.place(x=0,y=0)
        self.labvar = tk.StringVar(value=key['mode'])    #截圖模式
        self.exitvar = tk.StringVar(value=key['exit'])   #退出模式
        self.printvar = tk.StringVar(value=key['print']) #截圖快照
        self.extraValue = tk.BooleanVar() #Ctrl按鈕
        self.labmodetext = tk.Label(self,textvariable=self.labvar,bg="#D9DBFC").place(x=300,y=50)
        self.labmode = tk.Label(self,text='截圖模式',bg="#D9DBFC").place(x=220,y=50)
        self.exitmode = tk.Label(self,text='退出截圖模式',bg="#D9DBFC").place(x=220,y=100)
        self.exittext = tk.Label(self,textvariable=self.exitvar,bg="#D9DBFC").place(x=300,y=100)
        self.print = tk.Label(self,text='截圖快照',bg="#D9DBFC").place(x=220,y=150)
        self.printtext = tk.Label(self,textvariable=self.printvar,bg="#D9DBFC").place(x=300,y=150)
<<<<<<< HEAD
        self.setbut = tk.Button(self,text='設定',command=self.two,bg="#D9DBFC").place(x=222,y=210)
        self.mybutton2 = tk.Button(self, text='結束',command=self.x,bg="#D9DBFC").place(x=260,y=318)
        self.startbut = tk.Button(self,text='開始',command=self.open,bg="#D9DBFC").place(x=60,y=318)
        self.resizable(False,False)
        self.func = Start()
        self.protocol('WM_DELETE_WINDOW',self.x)
        self.mainloop()
    def x(self):
        if messagebox.askokcancel("Quit","您要離開?"):
            try:
                global b
                b = 0
                self.func.stopfunc()
                self.func.join()
                time.sleep(0.5)
                self.destroy()
                sys.exit()
            except:
                sys.exit()

    def two(self):
        self.twowin = tk.Toplevel()
        self.twowin.geometry("250x250")
        self.twowin.configure(bg="#F1DEFF")
        self.twowin.resizable(False,False)
        self.setbut = tk.Button(self,text='設定',command=self.two,bg="#D9DBFC",state=tk.DISABLED).place(x=222,y=210)
        self.twowinmode = tk.Label(self.twowin,text='截圖模式',bg="#EDD4FF").place(x=20,y=0)
        self.modeentry = tk.Entry(self.twowin,textvariable=self.labvar,width=3)
        self.modeentry.bind("<KeyRelease>", self.print_key)
        self.modeentry.place(x=80,y=0)
        self.exitmode = tk.Label(self.twowin,text='退出截圖模式',bg="#EDD4FF").place(x=0,y=30)
        self.exitentry = tk.Entry(self.twowin,textvariable=self.exitvar,width=3)
        self.exitentry.bind("<KeyRelease>", self.print_key2)
        self.exitentry.place(x=80,y=30)
        self.print = tk.Label(self.twowin,text='截圖快照',bg="#EDD4FF").place(x=20,y=60)
        self.printentry = tk.Entry(self.twowin,textvariable=self.printvar,width=3)
        self.printentry.bind("<KeyRelease>", self.print_key3)
        self.printentry.place(x=80,y=60)
        # self.quitt = tk.Button(self.twowin, text='結束',command=self.twowin.destroy,bg="#EDD4FF").pack(side='bottom')
        self.setting = tk.Button(self.twowin, text='確定',command=self.btt,bg="#EDD4FF").pack(side='bottom')
        self.extra = tk.Checkbutton(self.twowin,text='Ctrl',variable=self.extraValue,bg="#D9DBFC",activebackground="#D9DBFC")
        self.extra.place(x=20,y=148)
        self.extraexplane = tk.Label(self.twowin,text='(僅截圖模式)',bg="#D9DBFC",activebackground="#D9DBFC")
        self.extraexplane.place(x=65,y=150)
        self.mainloop()
    def sett(self):
        self.modeentry = tk.Entry(self.twowin,textvariable=self.labvar,width=3)
        self.modeentry.bind("<KeyRelease>", self.print_key)
        self.modeentry.place(x=80,y=0)
        self.exitentry = tk.Entry(self.twowin,textvariable=self.exitvar,width=3)
        self.exitentry.bind("<KeyRelease>", self.print_key2)
        self.exitentry.place(x=80,y=30)
        self.printentry = tk.Entry(self.twowin,textvariable=self.printvar,width=3)
        self.printentry.bind("<KeyRelease>", self.print_key3)
        self.printentry.place(x=80,y=60)
        # self.confirm = tk.Button(self.twowin,text='確定',command=self.btt,bg="#D9DBFC")
        # self.confirm.place(x=285,y=210)
        self.extra = tk.Checkbutton(self.twowin,text='Ctrl',variable=self.extraValue,bg="#D9DBFC",activebackground="#D9DBFC")
        self.extra.place(x=220,y=178)
        self.extraexplane = tk.Label(self.twowin,text='(僅截圖模式)',bg="#D9DBFC",activebackground="#D9DBFC")
        self.extraexplane.place(x=265,y=180)
=======
        self.setbut = tk.Button(self,text='設定',command=self.sett,bg="#D9DBFC").place(x=222,y=210)
        self.mybutton2 = tk.Button(self, text='結束',command=self.quit,bg="#D9DBFC").place(x=260,y=318)
        self.startbut = tk.Button(self,text='開始',command=self.open,bg="#D9DBFC").place(x=60,y=318)
        self.resizable(False,False)
        self.mainloop()
    def sett(self):
        self.setbut = tk.Button(self,text='設定',command=self.sett,bg="#D9DBFC",state=tk.DISABLED).place(x=222,y=210)
        self.modeentry = tk.Entry(self,textvariable=self.labvar,width=3)
        self.modeentry.bind("<KeyRelease>", self.print_key)
        self.modeentry.place(x=300,y=50)
        self.exitentry = tk.Entry(self,textvariable=self.exitvar,width=3)
        self.exitentry.bind("<KeyRelease>", self.print_key2)
        self.exitentry.place(x=300,y=100)
        self.printentry = tk.Entry(self,textvariable=self.printvar,width=3)
        self.printentry.bind("<KeyRelease>", self.print_key3)
        self.printentry.place(x=300,y=150)
        self.confirm = tk.Button(self,text='確定',command=self.btt,bg="#D9DBFC")
        self.confirm.place(x=285,y=210)
        self.extra = tk.Checkbutton(self,text='Ctrl',variable=self.extraValue,bg="#D9DBFC",activebackground="#D9DBFC")
        self.extra.place(x=220,y=178)
        self.extraexplane = tk.Label(self,text='(僅截圖模式)',bg="#D9DBFC",activebackground="#D9DBFC")
        self.extraexplane.place(x=265,y=180)
        
    def quit(self):
        sys.exit()

>>>>>>> 5ea9a83583cfc1db55af33cecc58e1b3db020b69
    def btt(self):
        key['mode'] = self.labvar.get()
        key['exit'] = self.exitvar.get()
        key['print'] = self.printvar.get()
        self.modeentry.destroy()
        self.exitentry.destroy()
        self.printentry.destroy()
<<<<<<< HEAD
        # self.confirm.place_forget()
        self.extraexplane.place_forget()
        self.setbut = tk.Button(self,text='設定',command=self.two,bg="#D9DBFC").place(x=222,y=210)
=======
        self.confirm.place_forget()
        self.extraexplane.place_forget()
        self.setbut = tk.Button(self,text='設定',command=self.sett,bg="#D9DBFC").place(x=222,y=210)
>>>>>>> 5ea9a83583cfc1db55af33cecc58e1b3db020b69
        self.extraValue.set(self.extraValue.get())
        if self.extraValue.get() == True:
            if not '+' in key['mode']:
                self.labvar.set('ctrl+'+key['mode'])
                key['mode'] = self.labvar.get()
                with open("key.json", 'w',encoding='utf-8') as f:
                    json.dump(key,f)
                    f.close()
            else:
                key['mode'] = self.labvar.get()
                with open("key.json", 'w',encoding='utf-8') as f:
                    json.dump(key,f)
                    f.close()
        else:
            self.labvar.set(key['mode'].replace('ctrl+',''))
            key['mode'] = self.labvar.get()
            with open("key.json", 'w',encoding='utf-8') as f:
                json.dump(key,f)
                f.close()
        self.extra.place_forget()
<<<<<<< HEAD
        self.twowin.destroy()
    def open(self):
        global a
        a=1
        self.setbut = tk.Button(self,text='設定',command=self.two,bg="#D9DBFC",state=tk.DISABLED).place(x=222,y=210)
        self.startbut = tk.Button(self,text='開始',command=self.open,bg="#D9DBFC",state=tk.DISABLED).place(x=60,y=318)
        self.t = threading.Thread(target=self.func.main2)
        self.func.start()
        
=======
    def open(self):
        self.destroy()

>>>>>>> 5ea9a83583cfc1db55af33cecc58e1b3db020b69
    def print_key(self, event):
        keysym,keycode,char = event.keysym, event.keycode, event.char
        self.labvar.set(keysym.lower())
        print("鍵位：{}，ASCII碼：{}，字元：{}".format(keysym,keycode,char))
    def print_key2(self, event):
        keysym = event.keysym
        self.exitvar.set(keysym)
    def print_key3(self, event):
        keysym = event.keysym
        self.printvar.set(keysym)
<<<<<<< HEAD

class Start(threading.Thread):
    def __init__(self):
        self._running_flag = False
        self.stop  = threading.Event()
        threading.Thread.__init__(self,target=self.main2)
    def terminate(self):
        self.stop.set()
    def stopfunc(self):
        self._running_flag = False
    def main2(self):
        try:
            while True :
                self._running_flag = True
                if keyboard.is_pressed(key['mode']):
                    self = backtest.Test()
                    continue
                elif b == 0:
                    self._running_flag = False
                    break
                else:
                    continue
            sys.exit()
            # return Start.main2(self)
        finally:
            self._running_flag = False

if __name__ == '__main__':
    root = Root()
=======
    # def two(self):
    #     self.twowin = tk.Toplevel()
    #     self.twowin.geometry("150x150")
    #     self.twowin.configure(bg="#F1DEFF")
    #     self.twowin.resizable(False,False)
    #     self.twowinmode = tk.Label(self.twowin,text='截圖模式',bg="#EDD4FF").place(x=20,y=0)
    #     self.modelab = tk.Label(self.twowin,text=key['mode'],bg="#EDD4FF").place(x=80,y=0)
    #     self.exitmode = tk.Label(self.twowin,text='退出截圖模式',bg="#EDD4FF").place(x=0,y=30)
    #     self.exitmodelab = tk.Label(self.twowin,text=key['exit'],bg="#EDD4FF").place(x=80,y=30)
    #     self.print = tk.Label(self.twowin,text='截圖快照',bg="#EDD4FF").place(x=20,y=60)
    #     self.printlab = tk.Label(self.twowin,text=key['print'],bg="#EDD4FF").place(x=80,y=60)
    #     self.quitt = tk.Button(self.twowin, text='結束',command=self.quit,bg="#EDD4FF").pack(side='bottom')
        # self.setting = tk.Button(self, text='設定',command=self.main,bg="#EDD4FF").pack(side='bottom')
        self.mainloop()
class Two(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("150x150")
        self.configure(bg="#F1DEFF")
        self.resizable(False,False)
        self.mode = tk.Label(self,text='截圖模式',bg="#EDD4FF").place(x=20,y=0)
        self.modelab = tk.Label(self,text=key['mode'],bg="#EDD4FF").place(x=80,y=0)
        self.exitmode = tk.Label(self,text='退出截圖模式',bg="#EDD4FF").place(x=0,y=30)
        self.exitmodelab = tk.Label(self,text=key['exit'],bg="#EDD4FF").place(x=80,y=30)
        self.print = tk.Label(self,text='截圖快照',bg="#EDD4FF").place(x=20,y=60)
        self.printlab = tk.Label(self,text=key['print'],bg="#EDD4FF").place(x=80,y=60)
        self.quitt = tk.Button(self, text='結束',command=self.quit,bg="#EDD4FF").pack(side='bottom')
        # self.setting = tk.Button(self, text='設定',command=self.main,bg="#EDD4FF").pack(side='bottom')
        self.mainloop()
def main():
    self = Root()

def main2():

    keyboard.wait(key['mode'])
    root = backtest.Test()
    return main2()
def main3():
    root = Two()
if __name__ == '__main__':
    Root()
    p1 = Process(target=main3)
    p2 = Process(target=main2)
    p1.start()
    p2.start()
    p1.join()
    p2.terminate()
    p2.join()
>>>>>>> 5ea9a83583cfc1db55af33cecc58e1b3db020b69
    sys.exit()