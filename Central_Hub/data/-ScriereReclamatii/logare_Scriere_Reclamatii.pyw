import tkinter
import tkinter.messagebox
import subprocess
import time
import os
from config.definitions import ROOT_DIR, NETWORK_DIR



class App:

    # def checkUserName(self):
        
        # userName = self.myEntry.get()
        # password = self.myEntry2.get()
        # if userName == "aastelian" and password == "andrei05":
            # subprocess.Popen(os.path.join(self.rootPath,"-ScriereReclamatii/start_aastelian.pyw"), shell = True)
            
            # self.topWindow.destroy()
        # elif userName == "colteanu" and password == "sara2007":
            # subprocess.Popen(os.path.join(self.rootPath,"-ScriereReclamatii/start_colteanu.pyw"), shell = True)
            
            # self.topWindow.destroy()
        # else:
            # tkinter.messagebox.showinfo("Logare", "Nume utilizator sau parola incorecte!")
            
        # if os.path.exists(os.path.join(self.rootPath,"-ScriereReclamatii/MailReclamatii/resources")) == False:
            # os.makedirs(os.path.join(self.rootPath,"-ScriereReclamatii/MailReclamatii/resources"))
            
    def openApp(self,index):
        if index == 1:
            subprocess.Popen(os.path.join(self.rootPath,"start_aastelian.pyw"), shell = True)
            self.topWindow.destroy()
        elif index == 2:
            subprocess.Popen(os.path.join(self.rootPath,"start_colteanu.pyw"), shell = True)
            self.topWindow.destroy()

    def __init__(self,root):
        
        
        myFont = ("Castellar",12,"bold")
        
        self.rootPath = ROOT_DIR
        
    
        self.topWindow = root
        self.topWindow.title("Scriere Reclamatii - logare")
        self.topWindow.geometry("400x200+500+300")
        # self.myLabel = tkinter.Label(self.topWindow, text = "User name: ")
        # self.myLabel.place(x = 50, y = 10)
        # self.myEntry = tkinter.Entry(self.topWindow)
        # self.myEntry.place(x = 130, y = 10)
        
        
        # self.myLabel2 = tkinter.Label(self.topWindow, text = "Password: ")
        # self.myLabel2.place(x = 50, y = 50)
        # self.myEntry2 = tkinter.Entry(self.topWindow, show = "*")
        # self.myEntry2.place(x = 130, y = 50)
        self.label = tkinter.Label(self.topWindow, text = "Selecteaza un utilizator:")
        self.label.place(relx = 0.3, rely = 0.05)   
        self.andreiButton = tkinter.Button(self.topWindow, text = "Andrei", command = lambda : self.openApp(1),font=myFont,bg="light green")
        self.andreiButton.place(relx = 0.2, rely = 0.2)
        
        self.cosminButton = tkinter.Button(self.topWindow, text = "Cosmin", command = lambda : self.openApp(2),font=myFont,bg="light blue")
        self.cosminButton.place(relx = 0.6, rely = 0.2)
        
        
        #self.myButton = tkinter.Button(self.topWindow, text = "Inregistrare", command = lambda : self.checkUserName() ).place(x = 130, y = 100)
        
        self.topWindow.mainloop()
        
root = tkinter.Tk()
App(root)
root.mainloop()