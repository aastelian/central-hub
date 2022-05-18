
import re, os
from PyPDF2 import PdfFileWriter
from tkinter import messagebox
import subprocess, os, time
from config.definitions import ROOT_DIR



class MainClass(InputClass):


    def generate_client_no_mail_list(self):
        self.client_no_mail_list = []
        for n in self.client_mail_status_dict:
            if self.client_mail_status_dict[n] == "no mail":
                self.client_no_mail_list.append(n)
             
    def generate_page_client_dictionary(self):
        self.pdf_read("instiintari_pdf/0.pdf")
        num_pages = self.input_pdf.getNumPages()
        self.page_client_dict = {}
        for n in range(0,num_pages):
            page = self.input_pdf.getPage(n)
            text = page.extractText()
            
            for i in self.client_no_mail_list:
                if re.search("BORDEROU",text):
                    pass
                elif re.search(r""+i,text):
                    self.page_client_dict[n] = i    #dictionar cu paginile aferente clientilor no_mail
        
        value_list = list(self.page_client_dict.values())
        self.print_list=[]   #lista cu clientii no_mail negasiti si pentru care nu s-au generat paginile
        for i in self.client_no_mail_list:
            if i not in value_list:
                self.print_list.append(i)
               
    def generate_route_list(self):
        self.route_num_list = self.client_route_dict.values()   #lista cu toate rutele
        
        new_route_num_list = []
        for n in self.route_num_list:
            if len(n.split("_")) >= 2:
                try:
                    new_route_num_list.append(int(n.split("_")[1]))
                except:
                    pass
        
        dicti = {}
        for n in new_route_num_list:
            dicti[n] = 1
            
        new_route_num_list = list(dicti.keys())
        new_route_num_list.sort()
        self.route_num_list = new_route_num_list    #lista cu toate rutele (unice)
    def rename(self):
        subprocess.Popen(os.path.join(ROOT_DIR,"rename.bat"),shell=True)
    
    def deleteB(self):
        subprocess.Popen(os.path.join(ROOT_DIR,"del.bat"),shell = True)
    
    def mainClassApp(self):
        
        time.sleep(4)
        self.xls_read(os.path.join(self.root,"raport_vanzari/0.xls"))  #ok
        self.xls_read(os.path.join(self.root,"tabel_no_mail/1.xls"))  #ok
        self.generate_route_list()  #ok
        self.generate_client_no_mail_list() #ok
        self.generate_page_client_dictionary()
        output_pdf = PdfFileWriter()
        self.new_client_route_dict = {}
        for n in self.client_route_dict:    #pentru fiecare client
            try:
                self.new_client_route_dict[n] = int(self.client_route_dict[n].split("_")[1])    #generare dictionar client:ruta(numar)
            except:
                pass
        
        for n in self.route_num_list:   #pentru fiecare (toate) ruta
            clients_dict = {}
            pages = []
            if n%2 == 0:    #pentru fiecare ruta para
                for key,value in self.new_client_route_dict.items():    #pentru fiecare pereche client:ruta para
                    if n == int(value):
                        clients_dict[key] = 1   #generare dictionar cu clientul respectiv
                clients = list(clients_dict.keys()) #generare lista de clienti aferenta rutei n (pare)
                
                
                for m in clients:   #pentru fiecare client din lista <clients>
                    for key,value in self.page_client_dict.items(): #pentru fiecare pereche pagina:client no_mail
                        if m == value:
                            pages.append(key)
                            
                
                    
                for p in pages: #pentru fiecare pagina cu client no_mail
                    page_to_be_written = self.input_pdf.getPage(p)
                    
                    output_pdf.addPage(page_to_be_written)
            
        for n in self.route_num_list:   #pentru fiecare (toate) ruta
            clients_dict = {}
            pages = []
            print(pages)
            if n%2 != 0:    #pentru fiecare ruta imppara
                for key,value in self.new_client_route_dict.items():    #pentru fiecare pereche client:ruta imppara
                    if n == int(value):
                        clients_dict[key] = 1   #generare dictionar cu clientul respectiv
                clients = list(clients_dict.keys()) #generare lista de clienti aferenta rutei n (pare)
                
                
                for m in clients:   #pentru fiecare client din lista <clients>
                    for key,value in self.page_client_dict.items(): #pentru fiecare pereche pagina:client no_mail
                        if m == value:
                            pages.append(key)
                            
                
                    
                for p in pages: #pentru fiecare pagina cu client no_mail
                    page_to_be_written = self.input_pdf.getPage(p)
                    
                    output_pdf.addPage(page_to_be_written)
                    
           
        output_file = open(os.path.join(ROOT_DIR,"OUTPUT.PDF"), "wb")
        output_pdf.write(output_file)
        messagebox.showinfo("Atentie!", f"Acesti clienti nu au fost gasiti. Printeaza-le instiintarile manual:{self.print_list}")
