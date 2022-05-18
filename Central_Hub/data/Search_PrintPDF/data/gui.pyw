import tkinter
from mainScript import MainClass
from tkinter import messagebox
import subprocess, os

class guiClass(MainClass):

    def go_func(self):
        
        clients = self.clientEntry.get()
        
        if self.search_func(clients) == 0:
            messagebox.showinfo("Atentie!", f"Clientul {clients} nu a fost gasit in fisierul PDF")
        else:
            self.defaultValue = tkinter.StringVar()
            self.defaultValue.set("Alege clientul dorit")
            self.clientMenu = tkinter.OptionMenu(self.mainWindow, self.defaultValue, *self.client_list, command = self.print_func)
            self.clientMenu.grid(row = 3,column=0)
            
    def open_rename(self):
        subprocess.Popen("C:/Users/andrei.astelian/Desktop/Central_Hub/data/Search_PrintPDF/1_rename.bat", shell = True)
        
    def open_del(self):
        subprocess.Popen("C:/Users/andrei.astelian/Desktop/Central_Hub/data/Search_PrintPDF/2_del.bat", shell = True)
        
    def main_func(self):
    
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("Search&PrintPDF")
        self.mainWindow.geometry("400x400")
        
        self.clientLabel = tkinter.Label(self.mainWindow, text = "Introdu clientul dorit:")
        self.clientLabel.grid(row=0, column=0)

        self.clientEntry = tkinter.Entry(self.mainWindow, width = 40)
        self.clientEntry.grid(row=1,column=0)
        
        self.button = tkinter.Button(self.mainWindow, text = "Cauta", command = self.go_func)
        self.button.grid(row=2,column=0)
        
        self.buttonRename = tkinter.Button(self.mainWindow, text = "1.Rename PDF to <0.pdf>", command = self.open_rename)
        self.buttonRename.place(x=10,y=180)
        
        self.buttonDel = tkinter.Button(self.mainWindow, text = "2.Delete files", command = self.open_del)
        self.buttonDel.place(x=220,y=180)
        
        self.mainWindow.mainloop()
        
guiClass().main_func()