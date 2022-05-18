import subprocess
import time, os
from config.definitions import ROOT_DIR



rootPath = ROOT_DIR


subprocess.Popen(os.path.join(rootPath,"registruToJson.pyw"), shell = True)
time.sleep(2)
subprocess.Popen(os.path.join(rootPath,"jsonToComplaint_aastelian.pyw"), shell = True)