import tkinter as tk
import keyboard as kb
import time
from tkinter import messagebox
import mouse

class guiClass:
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("300x200")
        self.b=tk.Button(self.root,text="Activeaza programul",command=lambda:self.enterApelare(),bg="light blue")
        self.b.pack()
        
        
        self.infoLabel=tk.Label(self.root,text="""Dupa apasarea butonului <Activeaza programul> 
        si selectarea ferestrei PHL, 
        apasa <`> - tilda pentru a porni bot-ul""")
        self.infoLabel.pack()
        self.root.mainloop()
        
    def enterApelare(self):
        kb.wait("`")
        mouse.move(416,35,absolute=True,duration=0.01)
        mouse.click("left")
        mouse.move(436,57,absolute=True,duration=0.2)
        mouse.move(614,58,absolute=True,duration=0.5)
        mouse.click("left")
        time.sleep(3)
        kb.send("enter")
        time.sleep(3)
        mouse.move(984,666,absolute=True,duration=0.05)
        mouse.click("left")
        time.sleep(1)
        kb.write("009")
        mouse.move(1450,835,absolute=True,duration=0.1)
        mouse.click("left")
        time.sleep(1)
        messagebox.showinfo("Atentie!","Introdu numarul de apelari si apoi apasa pe <tilda>")
        time.sleep(1)
        
        self.eLabel=tk.Label(self.root,text="Nr de apelari:")
        self.eLabel.pack()
        self.e=tk.Entry(self.root,width=10)
        self.e.pack()
        
        kb.add_hotkey("`",self.printA,args=())
        
        self.printA()
        
    def printA(self):
        a=0
        q=1
        

        a=self.e.get()
        self.e.delete(0,"end")
        
        try:
            for n in range(int(a)):
                
                time.sleep(8)
                kb.send("F8")
                time.sleep(10)
                for n in range(2):
                    mouse.move(900,400,absolute=True,duration=0.2)
                    mouse.click("left")
                    time.sleep(2)
                    kb.send("F9")
                    time.sleep(4)
                    kb.send("enter")
                    time.sleep(3)
                    kb.send("enter")
                    time.sleep(4)
                
                
                kb.send("esc")
                time.sleep(5)
        except ValueError:
            messagebox.showinfo("Atentie!","Nr de apelari trebuie sa fie un numar intreg!")
        
obj=guiClass()

