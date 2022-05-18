import xlrd
from PyPDF2 import PdfFileReader
import os
from config.definitions import ROOT_DIR

class InputClass():
    def __init__(self):
        self.root = ROOT_DIR
    
    def xls_read(self,filename):
        input_xls = xlrd.open_workbook(filename)
        input_sheet = input_xls.sheet_by_index(0)
        
        
        
        if filename == os.path.join(self.root,"raport_vanzari/0.xls"):
            i = 4
            self.client_route_dict = {}
            try:
                while input_sheet.cell_value(i,0) != "":
                    i += 1
            except IndexError:
                pass
            last_row_index = i-1
            
            for i in range(5,last_row_index+1):
                self.client_route_dict[str(input_sheet.cell_value(i,1))] = str(input_sheet.cell_value(i,20))
                   
        elif filename == os.path.join(self.root,"tabel_no_mail/1.xls"):
            self.client_mail_status_dict = {}
            i = 1
            try:
                while input_sheet.cell_value(i,0) != "":
                    i += 1
            except IndexError:
                pass
            last_row_index = i-1
            
            for i in range(1,last_row_index+1):
                self.client_mail_status_dict[str(input_sheet.cell_value(i,1))] = str(input_sheet.cell_value(i,7))
    
            
                
    def pdf_read(self, filename):
        self.input_pdf = PdfFileReader(os.path.join(self.root,filename))
        
  