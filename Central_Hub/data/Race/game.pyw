import tkinter as tk
from pil import ImageTk, Image

class gameClass:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Race Game")
        self.root.state("zoomed")
        
        self.pic = Image.open("bg.jpg")
        self.myCanv = tk.Canvas(self.root,width = 1920, height = 500,highlightthickness=0)
        self.myCanv.place(x=0,y=0)
        self.background = ImageTk.PhotoImage(self.pic)
        self.i=1531
        self.myCanv.create_image(self.i,164,image=self.background)
        self.speed=0
        self.car_height=228
        self.car_original = Image.open("car.png")
        self.car_resized = self.car_original.resize((100,50))
        self.car=ImageTk.PhotoImage(self.car_resized)
        self.carImage = self.myCanv.create_image(960,228,image=self.car)
        self.myCanv.bind("<Up>",lambda event:self.jumpB())
        self.myCanv.focus_set()
        self.plusButton = tk.Button(self.root,text="Increase speed by 1",command=lambda:self.increase())
        self.plusButton.place(x=800,y=550)
        
        self.minusButton = tk.Button(self.root,text="Decrease speed by 1",command=lambda:self.decrease())
        self.minusButton.place(x=1000,y=550)
        
        self.fullStopButton = tk.Button(self.root,text="STOP",command=lambda:self.fullStop(),bg="red")
        self.fullStopButton.place(x=940,y=650)
        
        self.jumpButton = tk.Button(self.root,text="Jump",command=lambda:self.jumpB())
        self.jumpButton.place(x=940,y=700)
        
        self.jump_not_done = True
        
        self.run()
        
        self.root.mainloop()
        
    def jumpB(self):
        if self.car_height <=228 and self.jump_not_done == True and self.car_height > 190:
            self.car_height -= 2
            
            self.root.after(10,self.jumpB)
        elif self.car_height == 190 and self.jump_not_done == True:
            self.jump_not_done = False
            
            self.root.after(10,self.jumpB)
            
        elif self.jump_not_done == False and self.car_height < 228:
            self.car_height += 2
            
            self.root.after(10,self.jumpB)
        elif self.car_height == 228:
            
            self.jump_not_done = True
        
    def jump(self,event):
        
        self.car_height = 200
        
        
    def increase(self):
        self.speed += 1
        
    def decrease(self):
        if self.speed >0:
            self.speed -= 1
            
    def fullStop(self):
        self.speed=0
        
    def run(self):
        self.myCanv.destroy()
        self.i -= self.speed
        
        if self.i >778:
            self.myCanv = tk.Canvas(self.root,width = 1920, height = 500,highlightthickness=0)
            self.myCanv.place(x=0,y=0)
            self.myCanv.create_image(self.i,164,image=self.background)
            self.carImage=self.myCanv.create_image(960,self.car_height,image=self.car)
            
            self.myCanv.bind("<Up>",lambda event:self.jumpB())
            self.myCanv.focus_set()
            
            self.root.after(10,self.run)
        elif self.i<=778:
            self.i=1531
            self.myCanv = tk.Canvas(self.root,width = 1920, height = 500,highlightthickness=0)
            self.myCanv.place(x=0,y=0)
            self.myCanv.create_image(self.i,164,image=self.background)
            self.carImage=self.myCanv.create_image(960,self.car_height,image=self.car)
            
            self.myCanv.bind("<Up>",lambda event:self.jumpB())
            self.myCanv.focus_set()
            self.root.after(10,self.run)
        
obj=gameClass()