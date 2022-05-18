import tkinter, xlrd, xlwt, xlutils.copy
from tkinter import messagebox
import os
from tkinter.ttk import *
import subprocess
from config.definitions import ROOT_DIR, NETWORK_DIR
from pil import ImageTk, Image

class Complaint:

    def __init__(self):
        
        
        self.rootPath = NETWORK_DIR
        
        
        self.product = ""
        self.batchExpiry = ""
        self.complaint = ""
        self.client = ""
        self.supplier = ""
        self.complaintNumber = ""
        self.complaintDate = ""
        self.n = ""
        self.m = ""
        self.exit = 0
        self.clientResolution = ""
        self.productType = ""
        self.colectare = ""
        self.q = 1
        
        
    def exitAttention(self):
        self.attentionFrame.destroy()
        
    def attentionCommand(self):
        self.attentionFrame = tkinter.Tk()
        self.attentionFrame.geometry("360x120+500+400")
        self.attentionFrame.title("Atentie!")
        self.attentionText = tkinter.Text(self.attentionFrame, width = 41, height = 3)
        self.attentionText.grid(row = 1,column = 0)
        self.attentionLabel = tkinter.Label(self.attentionFrame, text = "Nu uita sa creezi in MS Outlook folderul")
        self.attentionLabel.grid(row = 0, column = 0)
        self.data = f"{self.complaintNumber-1}_{self.product}"
        self.attentionText.insert(tkinter.END,self.data)
        self.okButton = tkinter.Button(self.attentionFrame, text = "Ok", command = lambda : self.exitAttention())
        self.okButton.grid(row = 2, column = 0)
        self.attentionFrame.mainloop()
        
    def startComplaintRegistration(self):
    
        self.product = self.productEntry.get()
        self.batchExpiry = self.batchEntry.get() + "/" + self.expiryEntry.get()
        self.quantity = self.quantityEntry.get()
        self.complaint = self.complaintEntry.get()
        try:
            
            self.client = self.clientBoxValue.get()+" - "+ self.colectare + self.clientEntry.get()
        except:
            messagebox.showinfo("Atentie!","Nu ai selectat corect clientul")
            self.restartRegistration()
        self.supplier = self.optionSet.get()
        self.clientResolution = self.statusValue.get()
        self.productType = self.defaultValue.get()
    
        complaintRegister = xlrd.open_workbook(os.path.join(self.rootPath,"reclamatii_de_adaugat.xls"))
    
        complaintRegister_copy = xlutils.copy.copy(complaintRegister)
        sheet_copy = complaintRegister_copy.get_sheet(0)
        
        yes_no = 0
        
        if os.path.exists(os.path.join(self.rootPath,f"-_RECLAMATII/{self.complaintNumber}")) == False:
            os.makedirs(os.path.join(self.rootPath,f"-_RECLAMATII/{self.complaintNumber}"))
        else:
            messagebox.showinfo("Atentie!",f"Folderul pentru reclamatia {self.complaintNumber} exista! Se va trece la numarul {str(int(self.complaintNumber) +1)}")
            yes_no = 1 
            
        if yes_no == 0:
            for x in range(13):
                if x == 0:
                    value = self.complaintNumber
                elif x == 1:
                    value = self.complaintDate
                elif x == 2:
                    value = self.product
                elif x == 3:
                    value = self.batchExpiry
                elif x == 4:
                    value = self.quantity
                elif x == 5:
                    value = self.complaint
                elif x == 6:
                    value = self.client
                elif x == 7:
                    value = self.supplier
                elif x in [8,9,11]:
                    value = ""
                elif x == 10:
                    value = self.clientResolution
                elif x == 12:
                    value = self.productType
                sheet_copy.write(self.m,x,value)
                
            complaintRegister_copy.save(os.path.join(self.rootPath,"reclamatii_de_adaugat.xls"))
            self.productEntry.delete(0, "end")
            self.batchEntry.delete(0, "end")
            self.expiryEntry.delete(0, "end")
            self.quantityEntry.delete(0, "end")
            self.complaintEntry.delete(0, "end")
            self.clientEntry.delete(0, "end")
            self.clientStatusEntry.current(0)
            self.defaultValue.set("")
            self.supplierEntry.current(0)
            self.clientBoxValue.set("Selecteaza filiala")
            try:
                self.clientEntry.destroy()
                self.clientYesLabel.destroy()
            except:
                pass
            self.clientLabel.grid(row = 5, column = 0)
            self.clientLabelYesNo = tkinter.Label(self.mainWindow, text = "Colectare: ",highlightthickness=0)
            self.clientLabelYesNo.grid(row = 5, column = 2)
            self.clientYesButton = tkinter.Button(self.mainWindow, text = "Da", command = lambda : self.labelYesPrint(),highlightthickness=0)
            self.clientYesButton.grid(row = 5, column = 3)
            self.clientNoButton = tkinter.Button(self.mainWindow, text = "Nu", command = lambda : self.labelNoPrint(),highlightthickness=0)
            self.clientNoButton.grid(row = 5, column = 4)
            self.m +=1
            self.complaintNumber +=1
            self.mainWindow.title(f"Formular Inregistrare Reclamatia {self.complaintNumber} - {self.complaintDate}")
            self.attentionCommand()
        else:    
            self.complaintNumber +=1
            
            
            
            self.mainWindow.title(f"Formular Inregistrare Reclamatia {self.complaintNumber} - {self.complaintDate}")
        
        
        
        
        
        
    def exitApp(self):
    
        complaintToBeInsertedExcel = xlrd.open_workbook(os.path.join(self.rootPath,"reclamatii_de_adaugat.xls"))
        sheetToBeInsertedExcel = complaintToBeInsertedExcel.sheet_by_index(0)
        try:
            if sheetToBeInsertedExcel.cell_value(0,0) != "":
                subprocess.Popen(os.path.join(self.rootPath,"reclamatii_de_adaugat.xls"), shell = True)
                subprocess.Popen(os.path.join(self.rootPath,"Registru reclamatii calitate final.xls"), shell = True)
                self.mainWindow.destroy()
        except IndexError:
            self.mainWindow.destroy()
        
        

    def readComplaintRegister(self):
    
        complaintRegister = xlrd.open_workbook(os.path.join(self.rootPath,"Registru reclamatii calitate final.xls"))
        sheet = complaintRegister.sheet_by_index(0)
        
        complaintToBeInsertedExcel = xlrd.open_workbook(os.path.join(self.rootPath,"reclamatii_de_adaugat.xls"))
        sheetToBeInsertedExcel = complaintToBeInsertedExcel.sheet_by_index(0)
        
        skip = 0
        self.m = 0
        
        try:
            while skip == 0:
            
                if sheetToBeInsertedExcel.cell_value(self.m,0) == "":
                    skip = 1
                    self.m -= 1
                self.m += 1
                 
        except IndexError:
            pass
                
        
        skip = 0
        self.n = 1000
        
        try:
            while skip == 0:
                
                

                if sheet.cell_value(self.n,0) == "":
                    skip = 1
                    self.n -= 1
                    
                self.n += 1
        except IndexError:
            pass
                
           
        
        self.complaintNumber = int(sheet.cell_value(self.n-1,0)) + 1
        
    def labelYesPrint(self):
        self.clientLabelYesNo.destroy()
        self.clientYesButton.destroy()
        self.clientNoButton.destroy()
        self.clientYesLabel = tkinter.Label(self.mainWindow, text = "colectare")
        self.clientYesLabel.grid(row = 5, column = 3)
        self.clientEntry = tkinter.Entry(self.mainWindow)
        self.colectare = "colectare"
        
    def labelNoPrint(self):
        self.clientLabelYesNo.destroy()
        self.clientYesButton.destroy()
        self.clientNoButton.destroy()
        self.clientEntry = tkinter.Entry(self.mainWindow, width = 28)
        self.clientEntry.grid(row = 5, column = 2)
        self.colectare = ""
        
    def restartRegistration(self):
        self.mainWindow.destroy()
        self.q = 0
        self.openMainWindow()
        
    def copyData(self):
        subprocess.Popen(os.path.join(self.rootPath,"reclamatii_de_adaugat.xls"), shell = True)
        subprocess.Popen(os.path.join(self.rootPath,"Registru reclamatii calitate final.xls"), shell = True)
        
        messagebox.showinfo("Atentie!", "Dupa copierea noilor date in Registru apasa pe butonul albastru 'Refresh'")

    def openMainWindow(self):
        if self.q == 1:
            self.date = str(self.default_day.get())+"."+str(self.default_month.get())+"."+str(self.default_year.get())
    
            if self.date == "":
                messagebox.showinfo("Atentie!", """Nu ai trecut nicio data.
Scrie data in format zz.ll.aaaa""")
            elif (len(self.date) == 10 and (self.date[2] != "." or self.date[5] != ".")):
                messagebox.showinfo("Atentie!", "Formatul datei trebuie sa fie zz.ll.aaaa")
            elif len(self.date) != 10:
                messagebox.showinfo("Atentie!", "Formatul datei trebuie sa fie zz.ll.aaaa")
            else:
            
                self.complaintDate = self.date
                self.dateWindow.destroy()
                
                
                self.mainWindow = tkinter.Tk()
                self.mainWindow.geometry("600x400+500+300")
                self.mainWindow.title(f"Formular Inregistrare Reclamatia {self.complaintNumber} - {self.complaintDate}")
                
                
                self.myCanvas = tkinter.Canvas(self.mainWindow,width=600,height = 400, border=0,highlightthickness=0)
                self.myCanvas.place(x=0,y=0)
                
                the_image = Image.open("wallpaper.jpg")
                the_image_resized = the_image.resize((1200,800))
                
                myImage = ImageTk.PhotoImage(the_image_resized)
                self.myCanvas.create_image(0,0,image=myImage)
            
                
                self.productLabel = tkinter.Label(self.mainWindow, text = "Produs:")
                self.productLabel.grid(row = 0, column = 0)
                
                self.productEntry = tkinter.Entry(self.mainWindow, width = 28)
                self.productEntry.grid(row = 0, column = 1)
                
                self.batchLabel = tkinter.Label(self.mainWindow, text = "Lot:")
                self.batchLabel.grid(row = 1, column = 0)
                
                self.batchEntry = tkinter.Entry(self.mainWindow, width = 28)
                self.batchEntry.grid(row = 1, column = 1)
                
                self.expiryLabel = tkinter.Label(self.mainWindow, text = "Data de expirare (zz.ll.aaaa):")
                self.expiryLabel.grid(row = 2, column = 0)
                
                self.expiryEntry = tkinter.Entry(self.mainWindow, width = 28)
                self.expiryEntry.grid(row = 2, column = 1)
                
                self.quantityLabel = tkinter.Label(self.mainWindow, text = "Cantitate:")
                self.quantityLabel.grid(row = 3, column = 0)
                
                self.quantityEntry = tkinter.Entry(self.mainWindow, width = 28)
                self.quantityEntry.grid(row = 3, column = 1)
                
                self.complaintLabel = tkinter.Label(self.mainWindow, text = "Motiv reclamatie:")
                self.complaintLabel.grid(row = 4, column = 0)
                
                self.complaintEntry = tkinter.Entry(self.mainWindow, width = 28)
                self.complaintEntry.grid(row = 4, column = 1)
                
                self.clientLabel = tkinter.Label(self.mainWindow, text = "Client:")
                self.clientLabel.grid(row = 5, column = 0)
                
                clientBoxList = ["depozit central", "filiala  Brasov", "filiala Constanta", "filiala Cluj", "filiala Craiova", "filiala Galati", "filiala Iasi", "filiala Oradea", "filiala Sibiu", "filiala Timisoara"]
                self.clientBoxValue = tkinter.StringVar()
                self.clientBoxValue.set(".Selecteaza filiala.")
                self.clientBox = tkinter.OptionMenu(self.mainWindow, self.clientBoxValue, *clientBoxList)
                self.clientBox.grid(row = 5, column = 1)
                bold_font = ("Times New Roman",12,"bold")
                self.clientBox.config(bg = "light green",border=0,font=bold_font,highlightthickness=0)
                
                self.clientLabelYesNo = tkinter.Label(self.mainWindow, text = "Colectare: ",highlightthickness=0)
                self.clientLabelYesNo.grid(row = 5, column = 2)
                
                self.clientYesButton = tkinter.Button(self.mainWindow, text = "Da", command = lambda : self.labelYesPrint(),highlightthickness=0)
                self.clientYesButton.grid(row = 5, column = 3)
                self.clientNoButton = tkinter.Button(self.mainWindow, text = "Nu", command = lambda : self.labelNoPrint(),highlightthickness=0)
                self.clientNoButton.grid(row = 5, column = 4)
                
                
                
                self.supplierLabel = tkinter.Label(self.mainWindow, text = "Furnizor:")
                self.supplierLabel.grid(row = 6, column = 0)
                
                
                self.supplierList2 = [".Selecteaza furnizorul.","PERRIGO ROMANIA SRL","LABORMED PHARMA TRADING","EL PHARMA ROMANIA SRL.","OPELLA HEALTCHARE ROMANIA","ABBVIE LOGISTICS B.V.","ABBVIE TRADING S.R.L","AC HELCOR PHARMA SRL BAIA MARE","MYOSOTIS FARM S.R.L.","ACCORD HEALTHCARE POLSKA SP ZOO","AFLOFARM ROMANIA SRL","ALCON ROMANIA SRL","ADDENDA PHARMACEUTICALS SRL","ALFASIGMA SPA","ALVOGEN ROMANIA SRL","MYOSOTIS FARM S.R.L.","AMBROSIA BIOSCIENCE SRL","AMD NOBEL PHARMACEUTICAL SRL","AMGEN ROMANIA SRL","ANGELINI PHARMACEUTICALS ROMANIA SRL","ANTIBIOTICE SA IASI","S.C. ALLOGA LOGISTICS ROMANIA S.R.L.","ASTELLAS PHARMA BULGARIA","ASTELLAS PHARMA d.o.o","ASTRAZENECA AB","AUROBINDO PHARMA ROMANIA SRL","BAYER SRL","BAYER SRL","MYOSOTIS FARM S.R.L.","SC ELMAFARM TRADING SRL","ELI LILLY EXPORT SA","PFIZER ROMANIA SRL","SANOFI ROMANIA SRL","BERES PHARMACEUTICALS PRIVATE LIMITED COMPANY BUDAPEST SUCURSALA","BERLIN - CHEMEIE A.MENARINI DISTRIBUTION ROMANIA SRL","BERLIN CHEMIE","NAOS SKIN CARE ROMANIA SRL","2A FARM Srl","BIOFARM S.A.- BUCURESTI","MYOSOTIS FARM S.R.L.","BIOGALENICA PROJECT  CONSULTING","AICORE LLP","BIONORICA AG","SC ELMAFARM TRADING SRL","BOEHRINGER INGELHEIM RCV GMBH  CO KG  VIENA SUC. BUCURESTI","S.C. BOIRON RO SRL BUCURESTI","SC ELMAFARM TRADING SRL","BRISTOL-MYERS SQUIBB ROMANIA SRL","CELLTECH PHARMA SRL","2A FARM Srl","CILAG GmbH INTERNATIONAL","MYOSOTIS FARM S.R.L.","SC ELMAFARM TRADING SRL","AMRING FARMA SRL","CO CO CONSUMER 2002 SRL","DESITIN ARZNEIMITTEL GMBH","DIRECT PHARMA LOGISTICS SRL","DR PHYTO SRL","DR. REDDY'S LABORATORIES ROMANIA SRL","DR.REDDY'S LABORATORIES SA (DRL SA)","JIMCO FARM SRL BUCURESTI","EGIS ROMPHARMA SRL","MYOSOTIS FARM S.R.L.","ELI LILLY EXPORT SA","EVER NEURO PHARMA GMBH","MEMOMIND GMBH","EWOPHARMA  AG","MYOSOTIS FARM S.R.L.","SC ROCHE ROMANIA SRL","S.C. NATURPHARMA PRODUCTS RO S.R.L.","FRESENIUS KABI ROMANIA SRL","2A FARM Srl","GEDEON RICHTER ROMANIA SA","MYOSOTIS FARM S.R.L.","FARMACEUTICA REMEDIA DISTRIBUTION   LOGISTICS SRL","ROMASTRU TRADING SRL","GLAXO SMITHKLINE SRL","MYOSOTIS FARM S.R.L.","GLAXO SMITHKLINE SRL","GLAXOSMITHKLINE CONSUMER HEALTHCARE SRL","PFIZER ROMANIA SRL","GLENMARK PHARMACEUTICALS SRL","GOOD DAYS THERAPY SRL","GREENKO SOLUTIONS RO SRL","2A FARM Srl","GTS SOLUTION SRL","PM INNOVATION LABORATORIES LTD","HEALTH ADVISORS SRL","HEATON k.s.","HOFIGAL S.A.EXPORT IMPORT","HYLLAN PHARMA S.R.L.","PRISUM INTERNATIONAL TRADING CO. S.R.L.","INOCARE PHARM SRL","IPSEN PHARMA","IPSEN PHARMA ROMANIA SRL","PHARMAPLUS - WAREHOUSE SRL","FARMACEUTICA REMEDIA DISTRIBUTION   LOGISTICS SRL","JOHNSON & JOHNSON ROMANIA SRL","2A FARM Srl","KRKA d.d.","MYOSOTIS FARM S.R.L.","SC ELMAFARM TRADING SRL","LABORATOIRE INNOTECH INTERNATIONAL","LABORATOIRES DIEPHARMEX SA","LABORATOIRES THEA PHARMA SRL","CORE INVEST HEALTH SRL","LAROPHARM SRL","ADVANTAGE MEDIA","SERMEDIC SRL BUCURESTI","SC TRUSTMED SRL","NOVA FARM SRL","SAGA SANATATE SRL","MAGISTRA C C PHARMA SRL","MYOSOTIS FARM S.R.L.","2A FARM Srl","MAGNAPHARM MARKETING AND SALES ROMANIA SRL","MYOSOTIS FARM S.R.L.","SC A&D PHARMA MARKETING & SALES SERVICES SRL","TEVA PHARMACEUTICALS SRL","MANGESIUS TRADING SRL","MBA PHARMA INOVATION","MCM KLOSTERFRAU VERTRIEBSGESELLSCHAFT MBH","MEDIMOW CENTER","MEDOCHEMIE ROMANIA SRL","CHIMIMPORTEXPORT-PLURIMEX S.R.L.","MERCK SHARP & DOHME B.V.","MONTAVIT GesmbH","MONTEFARMACO OTC SPA","BGP PRODUCTS OPERATIONS GmbH","BGP PRODUCTS SRL","NEED FARM","NOVARTIS PHARMA SERVICES ROMANIA SRL","NOVO NORDISK A/S","NOVO NORDISK FARMA SRL","NOVOLINE PHARM SRL","NYRVUSANO PHARMACEUTICALS SRL","OCTAPHARMA AG","MYOSOTIS FARM S.R.L.","SC ELMAFARM TRADING SRL","SC HIPOCRATE 2000 SRL","OVERLAND SRL","PAUL HARTMANN SRL","PFIZER ROMANIA SRL","PHARCO IMPEX 93 SRL","PHOENIX LEKARENSKY VELKOOBCHOD S.R.O.","PM INNOVATION LABORATORIES LTD","POLISANO PHARMACEUTICALS S.A.","QUEISSER PHARMA SRL","RECKITT BENCKISER ROMANIA","RECORDATI ROMANIA SRL","ORGANIC LINNEA","PHARMAFARM SA","SC ROCHE ROMANIA SRL","ROMPHARM COMPANY SRL","ROWA WAGNER GMBH & CO.KG","S.C PHARMA PROMOTION S.R.L","S.C. AMNIOCEN DISTRIBUTIE S.R.L.","S.C. NATURPHARMA PRODUCTS RO S.R.L.","YORK FARM SRL","MYOSOTIS FARM S.R.L.","SANDOZ SRL","SANOFI ROMANIA SRL","SANOFI ROMANIA SRL","SANTEN OY","SARANTIS ROMANIA SA","SC ALLERGAN SRL","MYOSOTIS FARM S.R.L.","SC FITERMAN DISTRIBUTION SRL","SC GLOBAL TREAT SRL","SC IME-DC DIABET SRL","INNER BIOMED SRL","SC MEBRA SRL","SC MEDIMOW PROMO CENTER SRL","SC PHARMA BRANDS SRL","SC SANIENCE SRL","SC SPD STAR SRL","SC SYNERGA PHARMACEUTICALS SRL","SC ZENTIVA SA","SECOM HEALTHCARE SRL","SELF CARE MEDICAL S.R.L.","MERCK ROMANIA SRL","SESDERMA LABORATORY SRL","OFTAFARMA ROMANIA SRL","SINTOFARM BUCURESTI","POLI GENERIKA SRL","BIESSEN PHARMA S.R.L.","SC SOFARFARM SRL","SOLACIUM PHARMA S.R.L.","SOLARTIUM GROUP","BIOSOOFT COMPANY SRL","SC CEUMED SRL","STADA M&D SRL","ASCENDIS WELLNESS SRL","TAKEDA PHARMACEUTICALS S.R.L.","TEOFARMA SRL Pharma GmbH","MYOSOTIS FARM S.R.L.","TERAPIA S.A. CLUJ-NAPOCA","MAGNAPHARM MARKETING AND SALES ROMANIA SRL","MYOSOTIS FARM S.R.L.","TEVA PHARMACEUTICALS SRL","CHIESI PHARMACEUTICALS GMBH","TRIDENT PHARMA SRL","UCB PHARMA ROMANIA SRL","UNICOMS CORP. ROMANIA SRL","UNIMED PHARMA - SLOVACIA","BAUSCH HEALTH POLAND SP. Z O.O.","VALEANT PHARMA POLAND SP ZOO","MYOSOTIS FARM S.R.L.","VEDRA INTERNATIONAL","SC VIFOR PHARMA ROMANIA SRL","VIM SPECTRUM SRL","PRISUM INTERNATIONAL TRADING CO. S.R.L.","VIVA PHARMA DISTRIBUTION SRL","2A FARM Srl","MYOSOTIS FARM S.R.L.","WALMARK ROMANIA SRL","WESTWOOD - INTRAFIN SA","2A FARM Srl","MYOSOTIS FARM S.R.L.","WORWAG PHARMA GMBH & CO.KG","WORWAG PHARMA ROMANIA SRL","ZDROVIT ROMANIA SRL","S.C. ZENYTH PHARMACEUTICALS S.R.L.","ORIGIN PHARMA DISTRIBUTION SRL","PHARMING TECHNOLOGIES B.V.","DDS DIAGNOSTIC SRL","ORGANON PHARMA B.V."]
                            
                self.supplierList = list(dict.fromkeys(self.supplierList2))
                self.supplierList.sort()
                
                
                self.optionSet = tkinter.StringVar()
                
                
                self.supplierEntry = tkinter.ttk.Combobox(self.mainWindow, textvariable = self.optionSet, width = 28)
                self.supplierEntry.grid(row = 6, column = 1)
                self.supplierEntry["values"] = tuple(self.supplierList)
                self.supplierEntry.current(0)
                
                self.clientStatusLabel = tkinter.Label(self.mainWindow, text = "Rezolutie client:")
                self.clientStatusLabel.grid(row = 7, column = 0)
                
                
                self.statusValue = tkinter.StringVar()
                self.clientStatusEntry = tkinter.ttk.Combobox(self.mainWindow, textvariable = self.statusValue, width = 28)
                self.clientStatusEntry.grid(row = 7, column = 1)
                self.clientStatusEntry["values"] = (".Selecteaza rezolutia pt client.","-","retur client aprobat")
                self.clientStatusEntry.current(0)
                
                type = ["RX","O","SA","C","P","DM"]
                self.defaultValue = tkinter.StringVar()
                self.defaultValue.set("Tip produs")
                
                self.productTypeEntry = tkinter.OptionMenu(self.mainWindow, self.defaultValue, *type)
                self.productTypeEntry.grid(row = 8, column = 1)
                self.productTypeEntry.config(bg="light green",border=0,font=bold_font,highlightthickness=0)
                
                self.productTypeLabel = tkinter.Label(self.mainWindow, text = "Tip Produs (RX, O, C, P, SA, DM):")
                self.productTypeLabel.grid(row = 8, column = 0)
                
                self.registerButton = tkinter.Button(self.mainWindow, text = "Inregistreaza reclamatia", bg = "light green",command = lambda : self.startComplaintRegistration() )
                self.registerButton.grid(row = 9, column = 0)
                
                self.exitButton = tkinter.Button(self.mainWindow, text = "Exit", bg = "red" ,command = lambda : self.exitApp() )
                self.exitButton.grid(row = 9, column = 1)
                
                self.copyButton = tkinter.Button(self.mainWindow, text = "Copiaza datele", bg = "yellow",command = lambda : self.copyData())
                self.copyButton.grid(row = 10, column = 1)
                
                self.restartButton = tkinter.Button(self.mainWindow, text = "Reseteaza", command = lambda : self.restartRegistration())
                self.restartButton.grid(row = 10, column = 0)
                
                self.refreshButton = tkinter.Button(self.mainWindow, text = "Refresh", bg = "light blue",command = lambda : self.readComplaintRegister())
                self.refreshButton.grid(row = 11, column = 0)
                
                
                
                self.mainWindow.mainloop()
        else:
            self.mainWindow = tkinter.Tk()
            self.mainWindow.geometry("600x400+500+300")
            self.mainWindow.title(f"Formular Inregistrare Reclamatia {self.complaintNumber} - {self.complaintDate}")
            self.myCanvas = tkinter.Canvas(self.mainWindow,width=600,height = 400, border=0,highlightthickness=0)
            self.myCanvas.place(x=0,y=0)
            
            the_image = Image.open("wallpaper.jpg")
            the_image_resized = the_image.resize((1200,800))
            
            myImage = ImageTk.PhotoImage(the_image_resized)
            self.myCanvas.create_image(0,0,image=myImage)
            
            self.productLabel = tkinter.Label(self.mainWindow, text = "Produs:")
            self.productLabel.grid(row = 0, column = 0)
            
            self.productEntry = tkinter.Entry(self.mainWindow, width = 28)
            self.productEntry.grid(row = 0, column = 1)
            
            self.batchLabel = tkinter.Label(self.mainWindow, text = "Lot:")
            self.batchLabel.grid(row = 1, column = 0)
            
            self.batchEntry = tkinter.Entry(self.mainWindow, width = 28)
            self.batchEntry.grid(row = 1, column = 1)
            
            self.expiryLabel = tkinter.Label(self.mainWindow, text = "Data de expirare:")
            self.expiryLabel.grid(row = 2, column = 0)
            
            self.expiryEntry = tkinter.Entry(self.mainWindow, width = 28)
            self.expiryEntry.grid(row = 2, column = 1)
            
            self.quantityLabel = tkinter.Label(self.mainWindow, text = "Cantitate:")
            self.quantityLabel.grid(row = 3, column = 0)
            
            self.quantityEntry = tkinter.Entry(self.mainWindow, width = 28)
            self.quantityEntry.grid(row = 3, column = 1)
            
            self.complaintLabel = tkinter.Label(self.mainWindow, text = "Motiv reclamatie:")
            self.complaintLabel.grid(row = 4, column = 0)
            
            self.complaintEntry = tkinter.Entry(self.mainWindow, width = 28)
            self.complaintEntry.grid(row = 4, column = 1)
            
            self.clientLabel = tkinter.Label(self.mainWindow, text = "Client:")
            self.clientLabel.grid(row = 5, column = 0)
            
            clientBoxList = ["depozit central", "filiala  Brasov", "filiala Constanta", "filiala Cluj", "filiala Craiova", "filiala Galati", "filiala Iasi", "filiala Oradea", "filiala Sibiu", "filiala Timisoara"]
            self.clientBoxValue = tkinter.StringVar()
            self.clientBoxValue.set("Selecteaza filiala")
            self.clientBox = tkinter.OptionMenu(self.mainWindow, self.clientBoxValue, *clientBoxList)
            self.clientBox.grid(row = 5, column = 1)
            self.clientBox.config(bg = "light green",border=0,font=bold_font,highlightthickness=0)
            
            self.clientLabelYesNo = tkinter.Label(self.mainWindow, text = "Colectare: ",highlightthickness=0)
            self.clientLabelYesNo.grid(row = 5, column = 2)
            
            self.clientYesButton = tkinter.Button(self.mainWindow, text = "Da", command = lambda : self.labelYesPrint(),highlightthickness=0)
            self.clientYesButton.grid(row = 5, column = 3)
            self.clientNoButton = tkinter.Button(self.mainWindow, text = "Nu", command = lambda : self.labelNoPrint(),highlightthickness=0)
            self.clientNoButton.grid(row = 5, column = 4)
            
            
            
            self.supplierLabel = tkinter.Label(self.mainWindow, text = "Furnizor:")
            self.supplierLabel.grid(row = 6, column = 0)
            
            
            self.supplierList2 = [".Selecteaza furnizorul.","PERRIGO ROMANIA SRL","LABORMED PHARMA TRADING","EL PHARMA ROMANIA SRL.","OPELLA HEALTCHARE ROMANIA","ABBVIE LOGISTICS B.V.","ABBVIE TRADING S.R.L","AC HELCOR PHARMA SRL BAIA MARE","MYOSOTIS FARM S.R.L.","ACCORD HEALTHCARE POLSKA SP ZOO","AFLOFARM ROMANIA SRL","ALCON ROMANIA SRL","ADDENDA PHARMACEUTICALS SRL","ALFASIGMA SPA","ALVOGEN ROMANIA SRL","MYOSOTIS FARM S.R.L.","AMBROSIA BIOSCIENCE SRL","AMD NOBEL PHARMACEUTICAL SRL","AMGEN ROMANIA SRL","ANGELINI PHARMACEUTICALS ROMANIA SRL","ANTIBIOTICE SA IASI","S.C. ALLOGA LOGISTICS ROMANIA S.R.L.","ASTELLAS PHARMA BULGARIA","ASTELLAS PHARMA d.o.o","ASTRAZENECA AB","AUROBINDO PHARMA ROMANIA SRL","BAYER SRL","BAYER SRL","MYOSOTIS FARM S.R.L.","SC ELMAFARM TRADING SRL","ELI LILLY EXPORT SA","PFIZER ROMANIA SRL","SANOFI ROMANIA SRL","BERES PHARMACEUTICALS PRIVATE LIMITED COMPANY BUDAPEST SUCURSALA","BERLIN - CHEMEIE A.MENARINI DISTRIBUTION ROMANIA SRL","BERLIN CHEMIE","NAOS SKIN CARE ROMANIA SRL","2A FARM Srl","BIOFARM S.A.- BUCURESTI","MYOSOTIS FARM S.R.L.","BIOGALENICA PROJECT  CONSULTING","AICORE LLP","BIONORICA AG","SC ELMAFARM TRADING SRL","BOEHRINGER INGELHEIM RCV GMBH  CO KG  VIENA SUC. BUCURESTI","S.C. BOIRON RO SRL BUCURESTI","SC ELMAFARM TRADING SRL","BRISTOL-MYERS SQUIBB ROMANIA SRL","CELLTECH PHARMA SRL","2A FARM Srl","CILAG GmbH INTERNATIONAL","MYOSOTIS FARM S.R.L.","SC ELMAFARM TRADING SRL","AMRING FARMA SRL","CO CO CONSUMER 2002 SRL","DESITIN ARZNEIMITTEL GMBH","DIRECT PHARMA LOGISTICS SRL","DR PHYTO SRL","DR. REDDY'S LABORATORIES ROMANIA SRL","DR.REDDY'S LABORATORIES SA (DRL SA)","JIMCO FARM SRL BUCURESTI","EGIS ROMPHARMA SRL","MYOSOTIS FARM S.R.L.","ELI LILLY EXPORT SA","EVER NEURO PHARMA GMBH","MEMOMIND GMBH","EWOPHARMA  AG","MYOSOTIS FARM S.R.L.","SC ROCHE ROMANIA SRL","S.C. NATURPHARMA PRODUCTS RO S.R.L.","FRESENIUS KABI ROMANIA SRL","2A FARM Srl","GEDEON RICHTER ROMANIA SA","MYOSOTIS FARM S.R.L.","FARMACEUTICA REMEDIA DISTRIBUTION   LOGISTICS SRL","ROMASTRU TRADING SRL","GLAXO SMITHKLINE SRL","MYOSOTIS FARM S.R.L.","GLAXO SMITHKLINE SRL","GLAXOSMITHKLINE CONSUMER HEALTHCARE SRL","PFIZER ROMANIA SRL","GLENMARK PHARMACEUTICALS SRL","GOOD DAYS THERAPY SRL","GREENKO SOLUTIONS RO SRL","2A FARM Srl","GTS SOLUTION SRL","PM INNOVATION LABORATORIES LTD","HEALTH ADVISORS SRL","HEATON k.s.","HOFIGAL S.A.EXPORT IMPORT","HYLLAN PHARMA S.R.L.","PRISUM INTERNATIONAL TRADING CO. S.R.L.","INOCARE PHARM SRL","IPSEN PHARMA","IPSEN PHARMA ROMANIA SRL","PHARMAPLUS - WAREHOUSE SRL","FARMACEUTICA REMEDIA DISTRIBUTION   LOGISTICS SRL","JOHNSON & JOHNSON ROMANIA SRL","2A FARM Srl","KRKA d.d.","MYOSOTIS FARM S.R.L.","SC ELMAFARM TRADING SRL","LABORATOIRE INNOTECH INTERNATIONAL","LABORATOIRES DIEPHARMEX SA","LABORATOIRES THEA PHARMA SRL","CORE INVEST HEALTH SRL","LAROPHARM SRL","ADVANTAGE MEDIA","SERMEDIC SRL BUCURESTI","SC TRUSTMED SRL","NOVA FARM SRL","SAGA SANATATE SRL","MAGISTRA C C PHARMA SRL","MYOSOTIS FARM S.R.L.","2A FARM Srl","MAGNAPHARM MARKETING AND SALES ROMANIA SRL","MYOSOTIS FARM S.R.L.","SC A&D PHARMA MARKETING & SALES SERVICES SRL","TEVA PHARMACEUTICALS SRL","MANGESIUS TRADING SRL","MBA PHARMA INOVATION","MCM KLOSTERFRAU VERTRIEBSGESELLSCHAFT MBH","MEDIMOW CENTER","MEDOCHEMIE ROMANIA SRL","CHIMIMPORTEXPORT-PLURIMEX S.R.L.","MERCK SHARP & DOHME B.V.","MONTAVIT GesmbH","MONTEFARMACO OTC SPA","BGP PRODUCTS OPERATIONS GmbH","BGP PRODUCTS SRL","NEED FARM","NOVARTIS PHARMA SERVICES ROMANIA SRL","NOVO NORDISK A/S","NOVO NORDISK FARMA SRL","NOVOLINE PHARM SRL","NYRVUSANO PHARMACEUTICALS SRL","OCTAPHARMA AG","MYOSOTIS FARM S.R.L.","SC ELMAFARM TRADING SRL","SC HIPOCRATE 2000 SRL","OVERLAND SRL","PAUL HARTMANN SRL","PFIZER ROMANIA SRL","PHARCO IMPEX 93 SRL","PHOENIX LEKARENSKY VELKOOBCHOD S.R.O.","PM INNOVATION LABORATORIES LTD","POLISANO PHARMACEUTICALS S.A.","QUEISSER PHARMA SRL","RECKITT BENCKISER ROMANIA","RECORDATI ROMANIA SRL","ORGANIC LINNEA","PHARMAFARM SA","SC ROCHE ROMANIA SRL","ROMPHARM COMPANY SRL","ROWA WAGNER GMBH & CO.KG","S.C PHARMA PROMOTION S.R.L","S.C. AMNIOCEN DISTRIBUTIE S.R.L.","S.C. NATURPHARMA PRODUCTS RO S.R.L.","YORK FARM SRL","MYOSOTIS FARM S.R.L.","SANDOZ SRL","SANOFI ROMANIA SRL","SANOFI ROMANIA SRL","SANTEN OY","SARANTIS ROMANIA SA","SC ALLERGAN SRL","MYOSOTIS FARM S.R.L.","SC FITERMAN DISTRIBUTION SRL","SC GLOBAL TREAT SRL","SC IME-DC DIABET SRL","INNER BIOMED SRL","SC MEBRA SRL","SC MEDIMOW PROMO CENTER SRL","SC PHARMA BRANDS SRL","SC SANIENCE SRL","SC SPD STAR SRL","SC SYNERGA PHARMACEUTICALS SRL","SC ZENTIVA SA","SECOM HEALTHCARE SRL","SELF CARE MEDICAL S.R.L.","MERCK ROMANIA SRL","SESDERMA LABORATORY SRL","OFTAFARMA ROMANIA SRL","SINTOFARM BUCURESTI","POLI GENERIKA SRL","BIESSEN PHARMA S.R.L.","SC SOFARFARM SRL","SOLACIUM PHARMA S.R.L.","SOLARTIUM GROUP","BIOSOOFT COMPANY SRL","SC CEUMED SRL","STADA M&D SRL","ASCENDIS WELLNESS SRL","TAKEDA PHARMACEUTICALS S.R.L.","TEOFARMA SRL Pharma GmbH","MYOSOTIS FARM S.R.L.","TERAPIA S.A. CLUJ-NAPOCA","MAGNAPHARM MARKETING AND SALES ROMANIA SRL","MYOSOTIS FARM S.R.L.","TEVA PHARMACEUTICALS SRL","CHIESI PHARMACEUTICALS GMBH","TRIDENT PHARMA SRL","UCB PHARMA ROMANIA SRL","UNICOMS CORP. ROMANIA SRL","UNIMED PHARMA - SLOVACIA","BAUSCH HEALTH POLAND SP. Z O.O.","VALEANT PHARMA POLAND SP ZOO","MYOSOTIS FARM S.R.L.","VEDRA INTERNATIONAL","SC VIFOR PHARMA ROMANIA SRL","VIM SPECTRUM SRL","PRISUM INTERNATIONAL TRADING CO. S.R.L.","VIVA PHARMA DISTRIBUTION SRL","2A FARM Srl","MYOSOTIS FARM S.R.L.","WALMARK ROMANIA SRL","WESTWOOD - INTRAFIN SA","2A FARM Srl","MYOSOTIS FARM S.R.L.","WORWAG PHARMA GMBH & CO.KG","WORWAG PHARMA ROMANIA SRL","ZDROVIT ROMANIA SRL","S.C. ZENYTH PHARMACEUTICALS S.R.L.","ORIGIN PHARMA DISTRIBUTION SRL","PHARMING TECHNOLOGIES B.V.","DDS DIAGNOSTIC SRL","ORGANON PHARMA B.V."]
                        
            self.supplierList = list(dict.fromkeys(self.supplierList2))
            self.supplierList.sort()
            
            
            self.optionSet = tkinter.StringVar()
            
            
            self.supplierEntry = tkinter.ttk.Combobox(self.mainWindow, textvariable = self.optionSet, width = 28)
            self.supplierEntry.grid(row = 6, column = 1)
            self.supplierEntry["values"] = tuple(self.supplierList)
            self.supplierEntry.current(0)
            
            self.clientStatusLabel = tkinter.Label(self.mainWindow, text = "Rezolutie client:")
            self.clientStatusLabel.grid(row = 7, column = 0)
            
            
            self.statusValue = tkinter.StringVar()
            self.clientStatusEntry = tkinter.ttk.Combobox(self.mainWindow, textvariable = self.statusValue, width = 28)
            self.clientStatusEntry.grid(row = 7, column = 1)
            self.clientStatusEntry["values"] = ("","-","retur client aprobat")
            self.clientStatusEntry.current(0)
            
            type = ["RX","O","SA","C","P","DM"]
            self.defaultValue = tkinter.StringVar()
            self.defaultValue.set("Tip produs")
            
            self.productTypeEntry = tkinter.OptionMenu(self.mainWindow, self.defaultValue, *type)
            self.productTypeEntry.grid(row = 8, column = 1)
            self.productTypeEntry.config(bg="light green",border=0,font=bold_font,highlightthickness=0)
            
            self.productTypeLabel = tkinter.Label(self.mainWindow, text = "Tip Produs (RX, O, C, P, SA, DM):")
            self.productTypeLabel.grid(row = 8, column = 0)
            
            self.registerButton = tkinter.Button(self.mainWindow, text = "Inregistreaza reclamatia", bg = "light green",command = lambda : self.startComplaintRegistration() )
            self.registerButton.grid(row = 9, column = 0)
            
            self.exitButton = tkinter.Button(self.mainWindow, text = "Exit", bg = "red",command = lambda : self.exitApp() )
            self.exitButton.grid(row = 9, column = 1)
            
            self.copyButton = tkinter.Button(self.mainWindow, text = "Copiaza datele", bg = "yellow", command = lambda : self.copyData())
            self.copyButton.grid(row = 10, column = 1)
            
            self.restartButton = tkinter.Button(self.mainWindow, text = "Reseteaza", command = lambda : self.restartRegistration())
            self.restartButton.grid(row = 10, column = 0)
            
            self.refreshButton = tkinter.Button(self.mainWindow, text = "Refresh", bg = "light blue",command = lambda : self.readComplaintRegister())
            self.refreshButton.grid(row = 11, column = 0)
            
            self.mainWindow.mainloop()
        
    
    def createDateWindow(self):
        self.readComplaintRegister()
        self.dateWindow = tkinter.Tk()
        self.dateWindow.title("Introducere reclamatii")
        self.dateWindow.geometry("450x50+600+400")
        self.dateWindow.config(bg="light blue")
        
        self.dateLabel = tkinter.Label(self.dateWindow, text = "Data inregistrarii reclamatiei:",bg="light blue")
        self.dateLabel.grid(row = 0,column = 0)
        
        self.default_day = tkinter.StringVar()
        self.default_day.set("Zi")
        
        day_list =[]
        for i in range(1,32):
            if i <=9:
                day_list.append("0"+str(i))
            else:
                day_list.append(str(i))
            
        self.default_month = tkinter.StringVar()
        self.default_month.set("Luna")
        
        month_list = []
        for i in range(1,13):
            if i<=9:
                month_list.append("0"+str(i))
            else:
                month_list.append(str(i))
            
        self.default_year = tkinter.StringVar()
        self.default_year.set("An")
        
        year_list = []
        for i in range(2020,2025):
            year_list.append(str(i))
        
        self.dayMenu = tkinter.OptionMenu(self.dateWindow,self.default_day, *day_list)
        self.dayMenu.grid(row = 0, column = 1)
        self.dayMenu.config(bg="red",border=0,activebackground = "light green")
        self.monthMenu = tkinter.OptionMenu(self.dateWindow,self.default_month, *month_list)
        self.monthMenu.grid(row=0,column=2)
        self.monthMenu.config(bg="red",border=0,activebackground = "light green")
        self.yearMenu = tkinter.OptionMenu(self.dateWindow,self.default_year,*year_list)
        self.yearMenu.grid(row=0,column=3)
        self.yearMenu.config(bg="red",border=0,activebackground = "light green")
        
        # self.dayMenu.bind("<LEAVE>",self.on_leave)
        # self.monthMenu.bind("<LEAVE>",self.on_leave)
        # self.yearMenu.bind("<LEAVE>",self.on_leave)
        
        # self.dateEntry = tkinter.Entry(self.dateWindow)
        # self.dateEntry.grid(row = 0, column = 1)
        
        self.myButton = tkinter.Button(self.dateWindow, text = "Inregistreaza", command = lambda : self.openMainWindow(), bg = "light green" )
        self.myButton.grid(row = 0, column = 4)
        
        self.dateWindow.mainloop()
        
    # def on_leave(self,event):
        # self.dayMenu
        
    
myObj = Complaint()
myObj.createDateWindow()    
    