import json
import email.message
import email.generator
import os
import xlrd, xlwt, xlutils.copy
import pil
import pil.Image
from win32com import client
import time
import tkinter
from MainMenu_aastelian import Main
import os
from config.definitions import ROOT_DIR, NETWORK_DIR
from datetime import date



rootPath = NETWORK_DIR



rootPath_local = ROOT_DIR



def generateComplaintDoc(textToPv,complaint_number,date,supplier):
    wb = xlwt.Workbook()
    
    sheet1 = wb.add_sheet(f"Reclamatie {complaint_number}")
    
    sheet1.write(8,0,f"Nr. {complaint_number}")
    sheet1.write(8,8,f"Data: {date}")
    
    sheet1.insert_bitmap(os.path.join(rootPath_local,"logo_solo.bmp"), 0,7)
    sheet1.insert_bitmap(os.path.join(rootPath_local,"signature_solo.bmp"), 50,6)
    
    title_style = xlwt.XFStyle()
    title_font = xlwt.Font()
    title_font.bold = True
    title_style.font = title_font
    sheet1.write(12,2,"PROCES VERBAL DE CONSTATARE NECONFORMITATE", title_style)
    
    for y in range(len(textToPv.split("\n"))):
        sheet1.write(y+17,1,textToPv.split("\n")[y])
    
    if os.path.exists(os.path.join(rootPath_local, f"MailReclamatii/resources")) == False:
        os.makedirs(os.path.join(rootPath_local, f"MailReclamatii/resources"))
    
    wb.save(os.path.join(rootPath_local,f"MailReclamatii/resources/pv - {supplier} - {complaint_number} - {date}.xls"))
    
    excel = client.Dispatch("Excel.Application")
    sheets = excel.Workbooks.Open(os.path.join(rootPath_local,f"MailReclamatii/resources/pv - {supplier} - {complaint_number} - {date}.xls"))
    work_sheets = sheets.Worksheets[0]
    
    supplier_copy = supplier.replace(" ","_")
    
    work_sheets.ExportAsFixedFormat(0, os.path.join(rootPath_local,f"MailReclamatii/pv-{supplier_copy}-{complaint_number}-{date}.pdf"))
    if os.path.exists(os.path.join(rootPath,f"-_RECLAMATII/{complaint_number}")) == False:
        os.makedirs(os.path.join(rootPath,f"-_RECLAMATII/{complaint_number}"))
    work_sheets.ExportAsFixedFormat(0, os.path.join(rootPath,f"-_RECLAMATII/{complaint_number}/pv-{supplier_copy}-{complaint_number}-{date}.pdf"))
    sheets.Close()
   
    
    

def generateExcel(complaints,ans,date):
    
    wb = xlwt.Workbook()
    top_style = xlwt.XFStyle()
    top_pattern = xlwt.Pattern()
    top_pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    top_pattern.pattern_fore_colour = 5
    top_font = xlwt.Font()
    top_font.bold = True
    top_alignment = xlwt.Alignment()
    top_alignment.horz = 0x02
    top_alignment.wrap = 1
    top_borders = xlwt.Borders()
    top_borders.left = top_borders.right = top_borders.top = top_borders.bottom = 1
        
    
    top_style.borders = top_borders
    top_style.alignment = top_alignment
    top_style.pattern = top_pattern
    top_style.font = top_font
    sheet1 = wb.add_sheet("Centralizator", top_style)
    sheet1.col(0).width = 5*256
    sheet1.col(1).width = sheet1.col(5).width =30*256
    sheet1.col(2).width = sheet1.col(3).width = 15*256
    sheet1.col(4).width = 10*256
    
    sheet1.write(0,0,"Nr. Crt.", top_style)
    sheet1.write(0,1,"Nume produs", top_style)
    sheet1.write(0,2,"Expirare", top_style)
    sheet1.write(0,3,"Lot", top_style)
    sheet1.write(0,4,"Cantitate",top_style)
    sheet1.write(0,5,"Reclamatie", top_style)
    k = 1
    
    central_style = xlwt.XFStyle()
    
    central_borders = xlwt.Borders()
    central_borders.left = central_borders.right = central_borders.top = central_borders.bottom = 1
    
    central_alignment = xlwt.Alignment()
    central_alignment.wrap = 1
    
    central_style.borders = central_borders
    central_style.alignment = central_alignment
    
    product_list = []
    
    for n in complaints:
        if complaints[n]["product"] not in product_list:
            product_list.append(complaints[n]["product"])
            
    product_list.sort()    
    
    for product in product_list:
        
        for n in complaints:
            
            if complaints[n]["supplier"] == ans and complaints[n]["product"] == product:
                
                sheet1.write(k,0,n,central_style)
                sheet1.write(k,1,complaints[n]["product"],central_style)
                if len(complaints[n]["batch"].split("/")) == 2:
                
                    expiry = complaints[n]["batch"].split("/")[1]
                else:
                    expiry = "-"
                batch = complaints[n]["batch"].split("/")[0]
                sheet1.write(k,2,expiry,central_style)
                sheet1.write(k,3,batch,central_style)
                if float(complaints[n]["quantity"]) % 1 == 0:
                    complaints[n]["quantity"] = int(complaints[n]["quantity"])
                else:
                    complaints[n]["quantity"] = float(complaints[n]["quantity"])
                sheet1.write(k,4,complaints[n]["quantity"],central_style)
                sheet1.write(k,5,complaints[n]["reason"],central_style)
                k += 1
                
                
    wb_pv = xlwt.Workbook()
    sheet1_pv = wb_pv.add_sheet("Proces Verbal")
    
    sheet1_pv.insert_bitmap(os.path.join(rootPath_local,"logo.bmp"), 0,4)
    sheet1_pv.insert_bitmap(os.path.join(rootPath_local,"signature.bmp"), 44,4)
    sheet1_pv.write(40,4,"Intocmit")
    sheet1_pv.write(41,4,"Inlocuitor Persoana Responsabila")
    sheet1_pv.write(42,4,"Astelian Andrei")
    
    complaint_numbers = []
    for n in complaints:
        complaint_numbers.append(n)
        
    complaint_numbers_string = ""
    for n in range(len(complaint_numbers)):
        if complaints[complaint_numbers[n]]["supplier"] == ans:
            if n == len(complaint_numbers)-1:
                complaint_numbers_string += complaint_numbers[n]
            else:
                complaint_numbers_string += complaint_numbers[n] + ", "
    #sheet1_pv.write(7,0,f"Nr.: {complaint_numbers_string}")
    date_style = xlwt.XFStyle()
    date_alignment = xlwt.Alignment()
    date_alignment.horz = date_alignment.HORZ_RIGHT
    date_style.alignment = date_alignment
    sheet1_pv.write(7,5, "Data: "+date, date_style)
    
    title_style = xlwt.XFStyle()
    title_font = xlwt.Font()
    title_font.bold = True
    title_alignement = xlwt.Alignment()
    title_alignement.horz = title_alignement.HORZ_CENTER
    title_style.font = title_font
    title_style.alignment = title_alignement
    sheet1_pv.write(12,2,"PROCES VERBAL DE CONSTATARE NECONFORMITATE", title_style)
    
    top_style = xlwt.XFStyle()
    top_pattern = xlwt.Pattern()
    top_pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    top_pattern.pattern_fore_colour = 5
    top_font = xlwt.Font()
    top_font.bold = True
    top_alignment = xlwt.Alignment()
    top_alignment.horz = 0x02
    top_alignment.wrap = 1
    top_borders = xlwt.Borders()
    top_borders.left = top_borders.right = top_borders.top = top_borders.bottom = 1
        
    
    top_style.borders = top_borders
    top_style.alignment = top_alignment
    top_style.pattern = top_pattern
    top_style.font = top_font
    
    p = 0
    
    sheet1_pv.col(p).width = 5*256
    sheet1_pv.col(p+1).width = 28*256
    sheet1_pv.col(p+5).width = 21*256
    sheet1_pv.col(p+2).width = 13*256
    sheet1_pv.col(p+3).width = 13*256
    sheet1_pv.col(p+4).width = 10*256
    
    sheet1_pv.write(16,0,"""     Au fost constatate urmatoarele neconformitati calitative:""")
    
    sheet1_pv.write(18,p,"Nr. Crt.",top_style)
    sheet1_pv.write(18,p+1,"Nume produs", top_style)
    sheet1_pv.write(18,p+2,"Expirare", top_style)
    sheet1_pv.write(18,p+3,"Lot", top_style)
    sheet1_pv.write(18,p+4,"Cantitate",top_style)
    sheet1_pv.write(18,p+5,"Reclamatie", top_style)
    k = 19
    
    central_style = xlwt.XFStyle()
    
    central_borders = xlwt.Borders()
    central_borders.left = central_borders.right = central_borders.top = central_borders.bottom = 1
    
    central_alignment = xlwt.Alignment()
    central_alignment.wrap = 1
    
    central_style.borders = central_borders
    central_style.alignment = central_alignment
    
    middle_style = xlwt.XFStyle()
    
    middle_alignment = xlwt.Alignment()
    middle_alignment.horz = 0x02
    
    middle_style.borders = central_borders
    
    middle_style.alignment = middle_alignment
    
    product_list = []
    
    for n in complaints:
        if complaints[n]["product"] not in product_list:
            product_list.append(complaints[n]["product"])
            
    product_list.sort()    
    criteria_number = []
    
    for product in product_list:
        
        for n in complaints:
            
            if complaints[n]["supplier"] == ans and complaints[n]["product"] == product:
                
                sheet1_pv.write(k,p,str(n),central_style)
                criteria_number.append(int(n))
                sheet1_pv.write(k,p+1,complaints[n]["product"],central_style)
                if len(complaints[n]["batch"].split("/")) == 2:
                
                    expiry = complaints[n]["batch"].split("/")[1]
                else:
                    expiry = "-"
                batch = complaints[n]["batch"].split("/")[0]
                sheet1_pv.write(k,p+2,expiry,middle_style)
                sheet1_pv.write(k,p+3,batch,middle_style)
                if float(complaints[n]["quantity"]) % 1 == 0:
                    complaints[n]["quantity"] = int(complaints[n]["quantity"])
                else:
                    complaints[n]["quantity"] = float(complaints[n]["quantity"])
                sheet1_pv.write(k,p+4,complaints[n]["quantity"],middle_style)
                sheet1_pv.write(k,p+5,complaints[n]["reason"],central_style)
                k += 1
    if os.path.exists(os.path.join(rootPath_local, f"MailReclamatii/resources")) == False:
        os.makedirs(os.path.join(rootPath_local, f"MailReclamatii/resources"))
    
    wb.save(os.path.join(rootPath_local,f"MailReclamatii/{ans} - {date}.xls"))
    wb_pv.save(os.path.join(rootPath_local,f"MailReclamatii/resources/pv - {ans} - {date}.xls"))
    
    excel = client.Dispatch("Excel.Application")
    sheets = excel.Workbooks.Open(os.path.join(rootPath_local,f"MailReclamatii/resources/pv - {ans} - {date}.xls"))
    work_sheet = sheets.Worksheets[0]
    
    ans_copy = ans.replace(" ","_")
    
    work_sheet.ExportAsFixedFormat(0,os.path.join(rootPath_local,f"MailReclamatii/pv-{ans_copy}-{date}.pdf"))
    
    for n in criteria_number:
        
    
        if os.path.exists(os.path.join(rootPath,f"-_RECLAMATII/{n}")) == False:
            os.makedirs(os.path.join(rootPath,f"-_RECLAMATII/{n}"))
        work_sheet.ExportAsFixedFormat(0,os.path.join(rootPath,f"-_RECLAMATII/{n}/pv-{ans_copy}-{date}.pdf"))
    
    sheets.Close()
    
    
def readFromJson(file_name):
    file = open(file_name,"r")
    dictionary = json.load(file)
    file.close()
    return dictionary
    


class App:
    
    def __init__(self):
        self.supplier = ""
        self.answer = ""
        file = open("root_path.txt","r")
        self.rootPath_copy = file.readline()
        
        self.rootPath = self.rootPath_copy.replace("\n","")
        file.close()

    def soloChoise(self):
        
        self.answer = 1
        self.doneLabel = tkinter.Label(self.topWindow, text = "Inchide pentru a continua").grid(row = 5, column = 0)
        
        self.topWindow.destroy()
        
    def supplierChoise(self):
        
        self.answer = 2
        self.doneLabel = tkinter.Label(self.topWindow, text = "Inchide pentru a continua").grid(row = 5, column = 0)
        
        self.topWindow.destroy()
        
        
    def buttonClick(self,c):
        
        self.supplier = c
        self.topWindow2.destroy()
        
    def createWindow2(self,list_1):
        
        
        self.topWindow2 = tkinter.Tk()
        self.topWindow2.title("Furnizori")
        self.topWindow2.geometry("300x600+500+200")
        
        self.supplierLabel = tkinter.Label(self.topWindow2, text = "Alege unul dintre furnizorii de mai jos:").grid(row = 0 , column = 0)
        n = 0
        for n in range(0,len(list_1)):
            self.myButton = tkinter.Button(self.topWindow2, text = f"{list_1[n]}", command = lambda c=list_1[n] : self.buttonClick(c))
            self.myButton.grid(row = n+1, column = 0)
        self.exitButton = tkinter.Button(self.topWindow2, text = "Exit", command = lambda : self.topWindow2.destroy())
        self.exitButton.grid(row = n+2, column = 0)
        self.topWindow2.mainloop()
        

    # def readEntry(self):
    
        # global date
        

        # date = self.dateEntry.get()
        
        # #self.doneLabel = tkinter.Label(self.topWindow, text = "Inchide pentru a continua").grid(row = 1, column = 0)
        # self.choiceLabel = tkinter.Label(self.topWindow, text = "Alege modul in care doresti sa generezi reclamatiile:").grid(row = 3, column = 0)
        # self.soloButton = tkinter.Button(self.topWindow, text = "1. Individual", command = lambda : self.soloChoise() )
        # self.soloButton.grid(row = 4, column = 0)
        # self.supplierButton = tkinter.Button(self.topWindow, text = "2. Pe furnizor", command = lambda : self.supplierChoise() )
        # self.supplierButton.grid(row = 4, column = 1)
        
        
    
    def createWindow(self):
        
        global date
        
        dateObj = date.today()
        date = dateObj.strftime("%d/%m/%Y")
        date = date.replace("/",".")

        self.topWindow = tkinter.Tk()
        self.topWindow.title("Meniul Principal")
        self.topWindow.geometry("340x200+600+300")
        
        
        self.choiceLabel = tkinter.Label(self.topWindow, text = "Alege modul in care doresti sa generezi reclamatiile:").grid(row = 3, column = 0)
        self.soloButton = tkinter.Button(self.topWindow, text = "1. Individual", command = lambda : self.soloChoise() )
        self.soloButton.place(x = 40, y = 30)
        self.supplierButton = tkinter.Button(self.topWindow, text = "2. Pe furnizor", command = lambda : self.supplierChoise() )
        self.supplierButton.place(x = 170, y = 30)
        self.topWindow.mainloop()
        
        
        # self.entryLabel = tkinter.Label(self.topWindow, text = "Data: ").grid(row = 0, column = 0)
        
        # self.dateEntry = tkinter.Entry(self.topWindow)
        # self.dateEntry.grid(row = 0, column = 1)
        
        # self.myButton = tkinter.Button(self.topWindow, text = "Inregistreaza", command = lambda : self.readEntry()).grid(row = 0, column = 2)
        # self.topWindow.mainloop()
        
        

    
if __name__ == "__main__":

    
    dictionary = readFromJson("registru.json")
    file_no = 0
    myObj = App()
    
    myObj.createWindow()
    answer = myObj.answer
        
    
        
    # while ans not in [1,2]:
        # try:
            # ans = int(input("Genereaza reclamatia:\n(1) individual\n(2) pe furnizor\n"))
            # if ans is int and ans not in [1,2]:
                # print("Raspunsul trebuie sa fie 1 sau 2")
        # except ValueError:
            # print("Raspunsul trebuie sa fie 1 sau 2")
            
    if answer == 1:
    
        for n in dictionary:
            
            eml = email.message.EmailMessage()
                    
            if dictionary[n][2] == "1" or dictionary[n][1] == 1 and dictionary[n][6] == "$":
            
                textToBeSent = """Buna ziua,
            
A fost reclamata o buc. {} neconforma calitativ.
            
Produs: {}
Lot/bbd: {}
Cantitate: {}
Motiv: {}

Multumesc,

Andrei Astelian
Farmacist - Inlocuitor Persoana Responsabila
 
Farmexim S.A.
Str. Malul Rosu nr. 4
077015, Balotesti, Jud. Ilfov
Telefon 0213.086.920
Interior 5720
andrei.astelian@farmexim.ro
www.farmexim.ro
""".format(dictionary[n][0],dictionary[n][0],dictionary[n][1],dictionary[n][2],dictionary[n][3])
                
                eml.set_content(textToBeSent)
                eml["Subject"] = f"neconformitate - {dictionary[n][5]} - {date} - viciu ascuns"
                
                eml["To"] = "neconformitati@farmexim.ro"
                eml["Cc"] = "cosmin.olteanu@farmexim.ro;simona.dumitriu@farmexim.ro;nuti.mladin@farmexim.ro"
                
                textToPv = f"""A fost reclamata o buc. {dictionary[n][0]} 
neconforma calitativ.\n\n
            
Produs: {dictionary[n][0]}\n
Lot/bbd: {dictionary[n][1]}\n
Cantitate: {dictionary[n][2]}\n
Motiv: {dictionary[n][3]}\n"""
                
            elif dictionary[n][2] != "1" or dictionary[n][1] != 1 and dictionary[n][6] == "$":
                textToBeSent = """Buna ziua,
            
Au fost reclamate {} buc. {} neconforme calitativ.

Produs: {}
Lot/bbd: {}
Cantitate: {}
Motiv: {}

Multumesc,

Andrei Astelian
Farmacist - Inlocuitor Persoana Responsabila
 
Farmexim S.A.
Str. Malul Rosu nr. 4
077015, Balotesti, Jud. Ilfov
Telefon 0213.086.920
Interior 5720
andrei.astelian@farmexim.ro
www.farmexim.ro""".format(dictionary[n][2],dictionary[n][0],dictionary[n][0],dictionary[n][1],dictionary[n][2],dictionary[n][3])
            
                eml.set_content(textToBeSent)
                eml["Subject"] = f"neconformitate - {dictionary[n][5]} - {date} - viciu ascuns"
                eml["To"] = "neconformitati@farmexim.ro"
                eml["Cc"] = "cosmin.olteanu@farmexim.ro;simona.dumitriu@farmexim.ro;nuti.mladin@farmexim.ro"
                
                textToPv = f"""Au fost reclamate {dictionary[n][2]} buc. {dictionary[n][0]}
neconforme calitativ.\n\n

Produs: {dictionary[n][0]}\n
Lot/bbd: {dictionary[n][1]}\n
Cantitate: {dictionary[n][2]}\n
Motiv: {dictionary[n][3]}\n"""
            
            pathToSave = os.path.join(rootPath_local,"MailReclamatii/")
            fileName = "{}.eml".format(n)    
            fullFileName = os.path.join(pathToSave,fileName)
            file = open(fullFileName,"w")
            gen = email.generator.Generator(file)
            gen.flatten(eml)
            file.close()
            
            complaint_number = n
            supplier = dictionary[n][5]
            
            generateComplaintDoc(textToPv,complaint_number,date,supplier)
            
    elif answer == 2:
    
    
    
        # print("Furnizori de ales: ",end="")
        list_1 = []
        for n in dictionary:
            if dictionary[n][5] not in list_1:
                list_1.append(dictionary[n][5])
                
        list_1.sort()
        
        
        myObj.createWindow2(list_1)
        
        #print(list_1)
        # ans = 0
        # while ans not in list_1:
        
            # ans_2 = input("Alege furnizor: ")
            # ans = ans_2.upper()
            # if ans not in list_1:
                # print("Furnizorul tastat nu este valid. Scrie cu atentie numele complet")
        
        complaints = {}
        ans = myObj.supplier
        
        if ans !="":
        
            for n in dictionary:
                aux_dic = {}
                for m in range(len(dictionary[n])):
                    if m == 0:
                        aux_dic["product"] = dictionary[n][m]
                    if m == 1:
                        aux_dic["batch"] = dictionary[n][m]
                    if m == 2:
                        aux_dic["quantity"] = dictionary[n][m]
                    if m == 3:
                        aux_dic["reason"] = dictionary[n][m]
                    if m == 4:
                        aux_dic["client"] = dictionary[n][m]
                    if m == 5:
                        aux_dic["supplier"] = dictionary[n][m]
                    if m == 6:
                        aux_dic["status"] = dictionary[n][m]
                complaints[n] = aux_dic
            
            quantity_sum = 0
            
            complaints_copy = complaints
            complaints_2 = complaints
            
            
            
            for s in complaints:
                if complaints[s]["supplier"] == ans:
                    quantity_sum += float(complaints[s]["quantity"])
            
            file = open(os.path.join(rootPath_local,"complaints.txt"),"w")
            
            product_list = []
            
            for n in complaints:
                if complaints[n]["product"] not in product_list:
                    product_list.append(complaints[n]["product"])
                
            product_list.sort()
            
            for product in product_list:
            
                for n in list(complaints_copy):
                
                    try:
                    
                        n_product = complaints_copy[n]["product"]
                        n_reason = complaints_copy[n]["reason"]
                        k = n
                        
                        if complaints_copy[n]["supplier"] == ans and complaints_copy[n]["product"] == product:
                            batch_string = ""
                            quantity_string = ""
                            sum_of_quantity = 0
                            for m in list(complaints):
                                if n_product == complaints[m]["product"]:
                                    if n_reason == complaints[m]["reason"]:
                                        batch_string += complaints[m]["batch"] + " // "
                                        quantity_string += complaints[m]["quantity"] + " // "
                                        sum_of_quantity += float(complaints[m]["quantity"])
                                        del complaints_copy[m]
                                        
                            if sum_of_quantity%1 == 0:
                                sum_of_quantity = int(sum_of_quantity)
                            file.write("Produs: " + n_product + "\n")
                            
                            file.write("Lot/bbd: " + batch_string + "\n")
                            file.write("Cantitate: " + quantity_string + "  TOTAL: " + str(sum_of_quantity) + "\n")
                            file.write("Motiv: " + n_reason)
                            file.write("\n\n")
                    except KeyError:
                        print("Eroare - Ignora")
            
            file.close()
            file = open(os.path.join(rootPath_local,"complaints.txt"),"r")
            text = file.readlines()
            text_copy = ""
            for n in text:
                line = n.split()
                new_line = ""
                for m in range(len(line)):
                    if line[len(line)-1] == "//":
                        line[len(line)-1] = ""
                    new_line +=line[m] + " "

                text_copy += "\n" + new_line
            file.close()
            file = open(os.path.join(rootPath_local,"complaints.txt"),"w")
            if quantity_sum%1 == 0:
                quantity_sum = int(quantity_sum)
            file.write(f"""Buna ziua,
            
Au fost constatate urmatoarele neconformitati calitative:
\n""")
            file.write(text_copy+"\n")
            file.write("""\nMultumesc,

\n\n""")
            file.close()
                        
            
            file = open(os.path.join(rootPath_local,"complaints.txt"),"r")
            text = file.read()
            eml = email.message.EmailMessage()
            eml.set_content(str(text))
            eml["Subject"] = f"neconformitate - {ans} - {date} - viciu ascuns"
            eml["To"] = "neconformitati@farmexim.ro"
            eml["Cc"] = "cosmin.olteanu@farmexim.ro;simona.dumitriu@farmexim.ro;nuti.mladin@farmexim.ro"
            file.close()
            file = open(os.path.join(rootPath_local,f"MailReclamatii/{ans}.eml"),"w")
            gen = email.generator.Generator(file)
            gen.flatten(eml)
            file.close()
            for n in dictionary:
                aux_dic = {}
                for m in range(len(dictionary[n])):
                    if m == 0:
                        aux_dic["product"] = dictionary[n][m]
                    if m == 1:
                        aux_dic["batch"] = dictionary[n][m]
                    if m == 2:
                        aux_dic["quantity"] = dictionary[n][m]
                    if m == 3:
                        aux_dic["reason"] = dictionary[n][m]
                    if m == 4:
                        aux_dic["client"] = dictionary[n][m]
                    if m == 5:
                        aux_dic["supplier"] = dictionary[n][m]
                    if m == 6:
                        aux_dic["status"] = dictionary[n][m]
                complaints[n] = aux_dic
                
            generateExcel(complaints,ans,date)
        
print("Fisierele s-au generat cu succes!")



myObj = Main()
myObj.createWindow()


