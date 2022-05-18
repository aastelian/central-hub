import tkinter
import subprocess, os
from config.definitions import ROOT_DIR, NETWORK_DIR


class Main:
    def __init__(self):
        
        
        self.rootPath = ROOT_DIR
        

    def openMainFile(self):
        subprocess.Popen(os.path.join(self.rootPath,"registruToJson.pyw"), shell = True)
        subprocess.Popen(os.path.join(self.rootPath,"jsonToComplaint_aastelian.pyw"), shell = True)
        
        self.topWindow.destroy()
        
    def closeMainFile(self):
        self.topWindow.destroy()

    def createWindow(self):
        myFont = ("Castellar",12,"bold")
        self.topWindow = tkinter.Tk()
        self.topWindow.title("Meniul Principal")
        self.topWindow.geometry("300x300+500+300")

        self.myButton = tkinter.Button(self.topWindow, text = "Refresh", command = lambda : self.openMainFile())
        self.myButton.place(x = 30, y = 20)
        self.myButton.config(font = myFont)
        self.myExitButton = tkinter.Button(self.topWindow, text = "Exit", command = lambda : self.closeMainFile())
        self.myExitButton.place(x = 100, y = 20)
        self.myExitButton.config(font = myFont)

        self.topWindow.mainloop()
        

    
