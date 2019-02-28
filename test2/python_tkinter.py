# Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用,使用Tkinter进行GUI编程
# Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
# Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。

from tkinter import *
import tkinter.messagebox as tkMessagebox


class Application(Frame):
    """pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
        """

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

        # self.helloLabel = Label(self, text='Hello world')
        # self.helloLabel.pack()
        # self.quitButton = Button(self, text='Quit', command=self.quit)
        # self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessagebox.showinfo('Message', 'Hello,%s' % name)


app = Application()
# 设置窗口标题:
app.master.title('Hello world')
# 主消息循环:
app.mainloop()


