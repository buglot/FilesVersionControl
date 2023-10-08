from ftplib import FTP
from printColor import *
from dir import * 
import os
import time
ftp = FTP("10.64.59.68")
ftp.login(user="myuser", passwd="mypassword")
printHeader(" Connected Server ")
def printFILEcloud():
    filenames = ftp.nlst()
    for f in filenames:
        if not is_file(ftp,f):
            printSubDir(ftp.nlst(f))
        else:
            printFile(f)
def donwload(files,local =""):
    global ftp
    if local == "":
       
        local= os.path.join("save",files)
    if os.path.exists("save")==False:
            os.mkdir("save")
    with open(local, "wb") as local_file:
        ftp.retrbinary("RETR " + files, local_file.write)
def upload(files):
    global ftp
    remote_file_name = files
    global name
    with open(files, "rb") as local_file:
        ftp.storbinary("STOR " + remote_file_name, local_file)
print()
printDir("\ Could")
printFILEcloud()
name = input("Name : ")
while 1:
    commend = input("promp >> ")
    match(commend.split(" ")[0]):
        case "download":
            if len(commend.split(" "))==2:
                donwload(commend.split(" ")[1])
            else:
                print("Error")
        case "put":
            if os.path.exists("save")==False:
                print("no Folder to save")
            elif os.listdir() is []:
                print("not file put")
            else:
                for x in os.listdir("save"):
                    upload(x+"_"+name+f"{time.time()}")
        case "exit":
            exit()
ftp.quit()


