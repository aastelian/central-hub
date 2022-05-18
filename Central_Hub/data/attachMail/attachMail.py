import keyboard as kb
import mouse,time

class App:

        
    def open_mail(self):
        print("da")
        kb.send("home")
        time.sleep(1)
        kb.send("r")
        time.sleep(1)
        kb.send("down")
        time.sleep(1)
        kb.send("down")
        time.sleep(1)
        kb.send("enter")
    
    def attach_sign(self):
        mouse.move(748,118,absolute=True,duration=0.4)
        mouse.click("left")
        time.sleep(1)
        for n in range(3):
            kb.send("down")
        kb.send("enter")
        time.sleep(1)
        kb.send("enter")
        
        mouse.move(300,50,absolute=True,duration=0.4)
        mouse.click("left")
        mouse.move(205,76,absolute=True,duration=0.4)
        mouse.click("left")
        mouse.move(100,50,absolute=True,duration=0.4)
        mouse.click("left")
        mouse.move(13,292,absolute=True,duration=0.4)
        mouse.click("left")
        kb.send("ctrl+end")
        mouse.move(676,121,absolute=True,duration=0.4)
        mouse.click("left")
        kb.send("down")
        kb.send("enter")
        
    def attach_documents(self):
        kb.press("alt")
        time.sleep(1)
        kb.send("tab")
        time.sleep(1)
        kb.send("tab")
        time.sleep(1)
        kb.release("alt")
        time.sleep(1)
        kb.send("up")
        time.sleep(1)
        kb.send("ctrl+c")
        time.sleep(1)
        kb.send("alt+tab")
        time.sleep(1)
        kb.send("ctrl+v")
        time.sleep(1)
        kb.send("alt+tab")
        time.sleep(1)
        kb.send("down")
        time.sleep(1)
        kb.send("down")
        time.sleep(1)
        kb.send("ctrl+c")
        time.sleep(1)
        kb.send("alt+tab")
        time.sleep(1)
        kb.send("ctrl+v")
        time.sleep(1)
        
    def delete_documents(self):
        
        time.sleep(1)
        for n in range(3):
            kb.send("home")
            kb.send("r")
            time.sleep(1)
            kb.send("down")
            time.sleep(1)
            kb.send("delete")
            time.sleep(1)
            
    def send_mail(self):
        mouse.move(25,225,absolute=True,duration=0.4)
        mouse.click("left")
        

while True:
    nr = input("Cate reclamatii ai de transmis?: ")
    kb.wait("`")
    for q in range(int(nr)):
        App().open_mail()
        time.sleep(3)
        App().attach_sign()
        time.sleep(3)
        App().attach_documents()
        time.sleep(2)
        App().send_mail()
        time.sleep(3)
        App().delete_documents()
        time.sleep(2)
    

