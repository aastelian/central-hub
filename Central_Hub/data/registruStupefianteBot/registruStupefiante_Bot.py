import keyboard as kb
import mouse as ms
import time
import pyperclip as pc
import tkinter as tk

class App:

    def __init__(self):
        self.s=0
        ws = tk.Tk()
        l = tk.Label(ws, text = """Selecteaza celula <Nr doc PHL> de la intrarea anterioara
si apasa <ctrl+alt> pt folosirea bot-ului""")
        l.pack()
        
        kb.add_hotkey("ctrl+\\",self.start)


        kb.add_hotkey("ctrl+alt",self.start_color)
        
        b = tk.Button(ws, text = "Exit", command = lambda c=ws: self.exit_app(root=c))
        b.pack()
        
        ws.mainloop()
        
    def exit_app(self,root):
        root.destroy()

    def start(self):
        
        time.sleep(0.5)
        kb.send("ctrl+c")
        time.sleep(1)
        kb.send("alt+tab")
        time.sleep(1)
        ms.move(1020,450,duration=0.2)
        ms.click("left")
        time.sleep(0.5)
        kb.send("ctrl+a")
        time.sleep(0.5)
        kb.send("ctrl+v")
        time.sleep(0.5)
        kb.send("enter")
        self.s=1
        
    def start_2(self):
        time.sleep(0.4)
        kb.send("alt+tab")
        time.sleep(0.5)
        kb.send("shift+space")
        time.sleep(0.4)
        ms.move(315,115,duration=0)
        time.sleep(0.1)
        ms.click("left")
        time.sleep(0.2)
        kb.send("down")
        time.sleep(0.3)
        kb.send("shift+space")
        self.s=0

    def start_3(self):
        
        time.sleep(0.2)
        kb.send("left")
        time.sleep(0.2)
        kb.send("right")
        time.sleep(0.3)
        kb.send("f2")
        time.sleep(0.2)
        kb.send("ctrl+a")
        time.sleep(0.2)
        kb.send("ctrl+c")
        
        time.sleep(0.2)
        control = pc.paste()
        time.sleep(0.2)
        kb.send("esc")
        if control != 0 and control != "0":
            self.start()
        else:
            
            time.sleep(0.3)
            kb.send("shift+space")
            ms.move(315,115,duration=0)
            time.sleep(0.1)
            ms.click("left")
            time.sleep(0.2)
            kb.send("down")
            time.sleep(0.3)
            kb.send("shift+space")
            self.s=0
            
        
       
        
        
        
        

    def start_color(self):
        if self.s == 1:
            self.start_2()
        elif self.s == 0:
            self.start_3()
        
App()


    