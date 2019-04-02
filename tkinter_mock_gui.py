import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(500, 150))
        self.master.title("Check Files")

        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1,)
        self.btnBrowse1.grid(row =0, column=0,padx=(10,0), pady=(30,0), sticky=W)
        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1,)
        self.btnBrowse2.grid(row =1, column=0,padx=(10,0), pady=(10,0), sticky=W)
        self.btnCheck = Button(self.master, text="Check for files...",width=12, height=2)
        self.btnCheck.grid(row =2, column=0,padx=(10,0), pady=(10,0), sticky=W)
        self.btnCheck = Button(self.master, text="Check for files...",width=12, height=2)
        self.btnCheck.grid(row =2, column=0,padx=(10,0), pady=(10,0), sticky=W)
        self.btnClose = Button(self.master, text="Close Program",width=12, height=2)
        self.btnClose.grid(row =2, column=2, sticky=E)

        self.txtBox1 = Entry(self.master, text="", font=12, width=40)
        self.txtBox1.grid(row=0, column=1, columnspan=2,padx=(25,0), pady=(30,0))
        self.txtBox2 = Entry(self.master, text="", font=12, width=40)
        self.txtBox2.grid(row=1, column=1, columnspan=2,padx=(25,0), pady=(10,0))




if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
