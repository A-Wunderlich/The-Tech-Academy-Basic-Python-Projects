from tkinter import filedialog
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 150))
        self.master.title("File Path")


        self.btnBrowse = Button(self.master, text="Browse", width=10, height=2, command=self.getFolder)
        self.btnBrowse.grid(row =0, column=0,sticky=NW)
        self.txtFName = Entry(self.master, text='', font = ('Helvetica', 12), width=70,)
        self.txtFName.grid(row=1, column=0)

        

    def getFolder(self):
        fn = filedialog.askdirectory()
        self.txtFName.insert(END, fn)
        
        


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
