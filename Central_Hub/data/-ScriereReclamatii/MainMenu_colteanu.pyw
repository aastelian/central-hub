import tkinter
import subprocess, os


class Main:

    def __init__(self):
        file = open("root_path.txt","r")
        self.rootPath_copy = file.readline()
        
        self.rootPath = self.rootPath_copy.replace("\n","")
        file.close()

    def openMainFile(self):
        subprocess.Popen(os.path.join(self.rootPath,"-ScriereReclamatii/registruToJson.pyw"), shell = True)
        subprocess.Popen(os.path.join(self.rootPath,"-ScriereReclamatii/jsonToComplaint_colteanu.pyw"), shell = True)
        
        self.topWindow.destroy()
        
    def closeMainFile(self):
        self.topWindow.destroy()

    def createWindow(self):
        self.topWindow = tkinter.Tk()
        self.topWindow.title("Meniul Principal")
        self.topWindow.geometry("300x300")

        self.myButton = tkinter.Button(self.topWindow, text = "Refresh", command = lambda : self.openMainFile())
        self.myButton.place(x = 30, y = 20)
        self.myExitButton = tkinter.Button(self.topWindow, text = "Exit", command = lambda : self.closeMainFile())
        self.myExitButton.place(x = 100, y = 20)

        self.topWindow.mainloop()
    
