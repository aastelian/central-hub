import tkinter, subprocess
from pil import ImageTk, Image
from config.definitions import ROOT_DIR
import os

class Main():

    def func(self,param):
        if param == "Registru reclamatii":
            subprocess.Popen("X:/Registru reclamatii calitate final.xls", shell = True)
            self.default_value.set("Reclamatii")
        elif param == "Aplicatie reclamatii":
            subprocess.Popen(os.path.join(ROOT_DIR,"data/-ScriereReclamatii/RECLAMATII.bat"), shell = True)
            self.default_value.set("Reclamatii")
        elif param == "Proces verbal de neconformitate":
            subprocess.Popen(os.path.join(ROOT_DIR,"data/Proces_verbal_de_constatare_draft.docx"), shell = True)
            self.default_value.set("Reclamatii")
        elif param == "F/ RECLAMATIE":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openRECLAMATIE.bat"), shell = True)
            self.default_value.set("Reclamatii")
        elif param == "F/ -_RECLAMATII":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/open-_RECLAMATII.bat"), shell = True)
            self.default_value.set("Reclamatii")
        elif param == "F/ REGISTRU RECLAMATII VECHI":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openRegistruReclamatiiVechi.bat"), shell = True)
            self.default_value.set("Reclamatii")
        elif param == "F/ PV DISTRUGERE":
            subprocess.Popen(os.path.join(ROOT_DIR,"data/generateDestroyedReport/start.lnk"),shell = True)
            self.misc_default_value.set("Diverse")
        elif param == "Brave":
            subprocess.Popen("C:/Users/andrei.astelian/Desktop/AA/1.Brave.lnk", shell = True)
            self.misc_default_value.set("Diverse")
        elif param == "Game":
            subprocess.Popen(os.path.join(ROOT_DIR,"data/Race/game.pyw"),shell=True)
            self.misc_default_value.set("Diverse")
        elif param == "Pharmalog":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openPharmalog.bat"), shell = True)
            self.misc_default_value.set("Diverse")
        elif param == "F/ PRINTARE INSTIINTARI OFFLINE":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openPrintareInstiintariOffline.bat"),shell = True)
            self.recall_default_value.set("Retrageri")
        
        elif param == "Cros Logistic":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openCROS.bat"), shell = True)
            self.misc_default_value.set("Diverse")
        elif param == "F/ WALLPAPER":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openWallpaper.bat"),shell = True)
            self.misc_default_value.set("Diverse")
        elif param == "Apelare":
            subprocess.Popen(os.path.join(ROOT_DIR,"data/apelare/botApelare.py"),shell=True)
            self.misc_default_value.set("Diverse")
            
        elif param == "F/ Rapoarte":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openRAPOARTE.bat"),shell = True)
            self.recall_default_value.set("Retrageri")
        elif param == "F/ RETRAGERI":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openRETRAGERI.bat"), shell = True)
            self.recall_default_value.set("Retrageri")
        elif param == "F/ SEARCH&PRINT PDF":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openSearch_PrintPDF.bat"),shell = True)
            subprocess.Popen(os.path.join(ROOT_DIR,"data/Search_PrintPDF/data/start.bat"),shell = True)
            self.recall_default_value.set("Retrageri")
        elif param == "Printare Instiintari Offline":
            subprocess.Popen(os.path.join(ROOT_DIR,"r/openPrintOfflineNotifications.bat"),shell = True)
            subprocess.Popen(os.path.join(ROOT_DIR,"data/PrintOfflineNotifications/data/start.bat"), shell = True)
            self.recall_default_value.set("Retrageri")
            
    def destroyWindow(self):
        self.mainWindow.destroy()
    
    def mainFunc(self):
    
        myFont = ("Castellar","10")
        myFont_2 = ("Castellar","12","bold")

        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("500x300+1400+10")
        self.mainWindow.title("Hub Principal")
        
        myImage = ImageTk.PhotoImage(Image.open("background.jpg"))
        myCanvas = tkinter.Canvas(self.mainWindow,width=500,height=300)
        myCanvas.place(x=0,y=0)
        myCanvas.create_image(250,150,image=myImage)
        myCanvas.config(border=0,highlightthickness=0)
        
        
        # self.main_canvas = tkinter.Canvas(self.mainWindow, width = 200, height = 200)
        # self.main_canvas.place(x=10,y=190)
        # self.logo = ImageTk.PhotoImage(Image.open(os.path.join(ROOT_DIR,"r/logo.bmp")))
        # self.main_canvas.create_image(60,50, image = self.logo)
        self.nameLabel = tkinter.Label(text = "by Andrei Astelian",font=myFont,bg="light green")
        self.nameLabel.place(x=0, y = 280)
        

        self.complaint_dd_list = ["Registru reclamatii","Aplicatie reclamatii", "Proces verbal de neconformitate", "F/ RECLAMATIE", "F/ -_RECLAMATII","F/ REGISTRU RECLAMATII VECHI"]
        self.default_value = tkinter.StringVar()
        self.default_value.set("Reclamatii")
        
        self.complaint_dd_menu = tkinter.OptionMenu(self.mainWindow, self.default_value, *self.complaint_dd_list, command=self.func)
        self.complaint_dd_menu.config(bg = "light green",font=myFont_2,fg="red3",highlightthickness=0)
        self.complaint_dd_menu.grid(row=0,column=0)
        menu_1 = self.mainWindow.nametowidget(self.complaint_dd_menu.menuname)
        menu_1.config(font=myFont_2)
        
        
        
        self.misc_dd_list = ["Brave","Pharmalog","Cros Logistic","F/ PV DISTRUGERE","F/ WALLPAPER", "Apelare", "Game"]
        self.misc_default_value = tkinter.StringVar()
        self.misc_default_value.set("Diverse")
        self.misc_dd_menu = tkinter.OptionMenu(self.mainWindow, self.misc_default_value, *self.misc_dd_list, command = self.func)
        self.misc_dd_menu.config(bg = "light green",font=myFont_2,fg="red3",highlightthickness=0)
        self.misc_dd_menu.grid(row=0,column=1)
        menu_2 = self.mainWindow.nametowidget(self.misc_dd_menu.menuname)
        menu_2.config(font=myFont_2)        
        
        
        self.recall_dd_list = ["Printare Instiintari Offline","F/ Rapoarte","F/ RETRAGERI","F/ PRINTARE INSTIINTARI OFFLINE","F/ SEARCH&PRINT PDF"]
        self.recall_default_value = tkinter.StringVar()
        self.recall_default_value.set("Retrageri")
        self.recall_dd_menu = tkinter.OptionMenu(self.mainWindow, self.recall_default_value, *self.recall_dd_list, command = self.func)
        self.recall_dd_menu.config(bg = "light green",font=myFont_2,fg="red3",highlightthickness=0)
        self.recall_dd_menu.grid(row=0,column=2)
        menu_3 = self.mainWindow.nametowidget(self.recall_dd_menu.menuname)
        menu_3.config(font=myFont_2)
        
        
        
        self.exit_button = tkinter.Button(self.mainWindow, text = "EXIT", command = self.destroyWindow, bg = "red",font=myFont_2,highlightthickness=0)
        self.exit_button.place(x=420,y=250)

        self.mainWindow.mainloop()
        
myMainObject = Main()
myMainObject.mainFunc()