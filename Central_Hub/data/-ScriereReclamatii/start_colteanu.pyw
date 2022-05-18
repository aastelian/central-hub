import subprocess
import time, os

file = open("root_path.txt","r")
rootPath_copy = file.readline()

rootPath = rootPath_copy.replace("\n","")
file.close()

subprocess.Popen(os.path.join(rootPath,"-ScriereReclamatii/registruToJson.pyw"), shell = True)
time.sleep(2)
subprocess.Popen(os.path.join(rootPath,"-ScriereReclamatii/jsonToComplaint_colteanu.pyw"), shell = True)