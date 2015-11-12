__author__ = 'Zero'

import threading
import tkinter

def resize(ev=None):
    lable.config( font=('Tempus Sans ITC', scale.get()))

top = tkinter.Tk()
lable = tkinter.Label(top, text="Test", font=('Tempus Sans ITC', 12))
lable.pack()

scale = tkinter.Scale(top, from_ = 10, to_ = 40, orient = tkinter.HORIZONTAL, command = resize)
scale.set(12)
scale.pack(fill = tkinter.X, expand = 1)

btn = tkinter.Button(top, text = 'Quit', command = top.quit,  bg="red", fg = 'blue')
btn.pack(fill=tkinter.X, expand = 1)
top.mainloop()

#这两个是python中的可变参数。*args表示任何多个无名参数，它是一个tuple；
# **kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前，
# 像foo(a=1, b='2', c=3, a', 1, None, )这样调用的话，会提示语法错误“SyntaxError: non-keyword arg after keyword arg”
class LThread(threading.Thread):
    def __int__(self, func, args, name = ''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.res = self.func(*self.args)

    def getResult(self):
        return self.res



