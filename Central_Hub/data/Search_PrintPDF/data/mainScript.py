from PyPDF2 import PdfFileReader, PdfFileWriter
import re
from tkinter import messagebox
import os

class MainClass():

        
    def print_func(self,client_to_be_printed):
        
        output_pdf = PdfFileWriter()
        pages_to_be_printed = [k for k, v in self.page_dict.items() if v == client_to_be_printed]
        
        for i in pages_to_be_printed:
        
            page_to_be_printed = self.input_pdf.getPage(int(i))
            output_pdf.addPage(page_to_be_printed)
            
        if os.path.exists("../output") == False:
            os.makedirs("../output")
        output_file = open("../output/"+client_to_be_printed+".pdf","wb")
        output_pdf.write(output_file)
        self.defaultValue.set("Alege clientul dorit")
        messagebox.showinfo("Succes!", "Fisierul a fost generat")
        
    def search_func(self,clients):
        self.input_pdf = PdfFileReader("C:/Rapoarte/0.pdf")
        searched_text = clients
        
        num_pages = self.input_pdf.getNumPages()
        self.client_dict = {}
        self.page_dict = {}
        
        for i in range(0,num_pages):
            page_obj = self.input_pdf.getPage(i)
            text = page_obj.extractText()
            
            
            if re.search(searched_text,text):
                
                client_start_index = int(text.index(searched_text))
                try:
                    client_stop_index = int(text.index("INSTIINTARE"))
                except:
                    pass
                client = text[client_start_index:client_stop_index]
                self.client_dict[client] = i
                self.page_dict[i] = client
        self.client_list = []
        self.client_list = list(self.client_dict.keys())
        
                
        if self.client_list == []:
            return 0
            
        else:
            return 1
      