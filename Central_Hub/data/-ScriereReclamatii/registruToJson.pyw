import json
import xlrd, os
from config.definitions import ROOT_DIR, NETWORK_DIR


# def readFromText(file_name):
    # file = open(file_name,"r")
    # text = file.readlines()
    # file.close()
    # return text
    

rootPath = NETWORK_DIR



rootPath_local = ROOT_DIR


    
def writeToJson(text,json_name):
    file = open(json_name,"w")
    json.dump(text,file)
    file.close()
    
def readFromXlsAndToJson(file_path):
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)
    dictionary = {}
    
    for n in range(2100,sheet.nrows):
        list = []
        if sheet.cell_value(n,8) == "$":
            for m in range(2,9):
                x = sheet.cell_value(n,m)
                if m == 4 and float(sheet.cell_value(n,4)) % 1 == 0:
                                    
                    x = int(x)
                    
                list.append(str(x))
                
                
            if sheet.cell_value(n,0) != "":
                dictionary.update({str(int(sheet.cell_value(n,0))):list})
        
    return dictionary
        
    
# def textToJson(text):

    # dictionary = {}
    # for n in range(1,len(text)):
        # text_list = text[n].split()
        # value_list = []
        # value_list.append(text_list[2])
        # value_list.append(text_list[3])
        # value_list.append(text_list[4])
        # value_list.append(text_list[5])
        # value_list.append(text_list[7])
        # for x in range(len(value_list)):
            # value_list[x] = value_list[x].replace("$"," ")
        # dictionary[text_list[0]] = value_list
        
    # return dictionary
    

if __name__ == "__main__":
    # text = readFromText("registru.txt")
    dictionary = readFromXlsAndToJson(os.path.join(rootPath,"Registru reclamatii calitate final.xls"))
    writeToJson(dictionary,os.path.join(rootPath_local,"registru.json"))
    
    