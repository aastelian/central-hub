import tkinter,subprocess, os
from config.definitions import ROOT_DIR, NETWORK_DIR


class Hub:
    def __init__(self):
        
        
        self.rootPath = ROOT_DIR
        
        

    def openSendComplaints(self):
        
        subprocess.Popen(os.path.join(self.rootPath, "Scriere_Reclamatii.bat"))
        
        self.topWindow.destroy()
      
    def openRegisterComplaint(self):
        subprocess.Popen(os.path.join(self.rootPath,"complaintRegistration.pyw"), shell = True)
        self.topWindow.destroy()
        
    def createHub(self):
    
        myFont = ("Castellar",11,"bold")
        self.topWindow = tkinter.Tk()
        self.topWindow.title("Meniul Principal")
        self.topWindow.geometry("745x70+400+400")
        self.topWindow.config(bg="light blue")
        
        myLabel = tkinter.Label(self.topWindow, text = "Alege unul dintre modulele de mai jos:",font=myFont,bg="light blue")
        myLabel.grid(row = 0, column = 0,columnspan=2)
        
        self.sendButton = tkinter.Button(self.topWindow, text = "Modulul Transmitere Reclamatii", command = lambda : self.openSendComplaints(), bg = "light green",font=myFont)
        self.sendButton.grid(row = 1,column = 0)
        
        self.registerButton = tkinter.Button(self.topWindow, text = "Modulul Inregistrare Reclamatii", command = lambda : self.openRegisterComplaint(), bg = "light green",font=myFont)
        self.registerButton.grid(row = 1, column = 1)
        
        self.topWindow.mainloop()
        
myObj = Hub()
myObj.createHub()