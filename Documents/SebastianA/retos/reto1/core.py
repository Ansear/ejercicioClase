import json 
import os

    
def savefile(name,data):
    if(checkfile(name) == False):
        with open('data/'+name,'w') as f:
            json.dump(data,f,indent=4)
            f.close()
    else:
        with open('data/'+name,'r+') as f:
            file = json.load(f)
            file["data"].append(data)
            f.seek(0)
            json.dump(file,f,indent=4)
            f.close()
def loadInfo(name):
    if(checkfile(name) == True):
        with open('data/'+name,'r') as f:
            return json.load(f)

def checkfile(name):
    try:
        with open('data/'+name,'r') as f:
            return True
    except FileNotFoundError:
        return False