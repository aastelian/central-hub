import tkinter
from mainScript import MainClass

class guiClass(MainClass):
    
    def mainApp(self):
    
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("500x500")
        self.mainWindow.title("Printare Instiintari Offline")
        self.printLabel = tkinter.Label(self.mainWindow,text = "Asigura-te ca ai fisierele 0.xls, 1.xls si 0.pdf in folderul principal")
        self.printLabel.grid(row=0,column=0)
        self.actionButton = tkinter.Button(self.mainWindow, text = "Start", command = self.mainClassApp)
        self.actionButton.grid(row=1,column =0)
        self.renameButton = tkinter.Button(self.mainWindow, text = "Redenumeste fisierele sursa", command = self.rename)
        self.renameButton.grid(row=1, column = 1)
        self.deleteButton = tkinter.Button(self.mainWindow, text = "Delete files", command = self.deleteB)
        self.deleteButton.grid(row=2,column=1)
        self.label1 = tkinter.Label(self.mainWindow, text = "0.xls = Raportul de vanzari")
        self.label1.grid(row=2,column=0)
        self.label2 = tkinter.Label(self.mainWindow, text = "1.xls = Raportul cu statusul instiintarilor online")
        self.label2.grid(row=3,column=0)
        self.label3 = tkinter.Label(self.mainWindow, text = "0.pdf = Fisierul pdf cu instiintari de retragere")
        self.label3.grid(row=4,column=0)
        self.mainWindow.mainloop()
    
guiClass().mainApp()
