from ftplib import FTP
from printColor import *
from dir import * 
import threading
import os
import time
loop = True
ftp = FTP(input("IP FTP: "))
if d:=input("Port (n is skip):")=="n":
    pass
else:
    ftp.port = d
ftp.login(user="myuser", passwd="mypassword")
printHeader(" Connected Server ")
def upload(files,x,name):
        global ftp
        named_tuple = time.localtime() 
        time_string = time.strftime("%H-%M-%S", named_tuple)
        
        remote_file_name = x+"_name=="+name+time_string
        with open(files, "rb") as local_file:
            ftp.storbinary("STOR " + remote_file_name, local_file)
def printFILEcloud():
    filenames = ftp.nlst()
    for f in filenames:
        if not is_file(ftp,f):                
            printSubDir(ftp.nlst(f))
        else:
            printFile(f)
def donwload(files,local =""):
    global ftp
    global loop
    loop = False
    if local == "":
        local= os.path.join("save",files)
    if os.path.exists("save")==False:
        os.mkdir("save")
    with open(local, "wb") as local_file:
        ftp.retrbinary("RETR " + files, local_file.write)
        local_file.close()
    times = os.path.getatime(local)
    with open(os.path.join(".p",files),"w") as f:
        f.write(str(times))
        f.close()
    loop =True
def dectecing():
    global loop
    while 1:
        if os.path.exists("save")==False:
            os.mkdir("save")
        elif os.listdir() is []:
            pass
        else:
            if loop:
                for x in os.listdir("save"):
                    if os.path.exists(os.path.join(".p",x))==True:
                        if history(x)< os.path.getmtime(os.path.join("save",x)):
                            upload(os.path.join("save",x),x,name)
                            with open(os.path.join(".p",x),"w") as f:
                                f.write(str(os.path.getmtime(os.path.join("save",x))))
                                f.close()
                    else:
                        with open(os.path.join(".p",x),"w") as f:
                            f.write(str(os.path.getmtime(os.path.join("save",x))))
                            f.close()
                        upload(os.path.join("save",x),x,name)
def history(files):
    timee = 0
    histo=os.path.join(".p",files)
    with open(histo) as f:
        timee =f.readline()
    
    return float(timee)
if __name__ == "__main__":
    if os.path.exists(".p")==False:
        os.makedirs(".p")
    print()
    printDir("\ Could")
    printFILEcloud()
    name = input("Name : ")
    monitor_thread = threading.Thread(target=dectecing)
    monitor_thread.start()
    while 1:
        commend = input("promp >> ")
        match(commend.split(" ")[0]):
            case "download":
                if len(commend.split(" "))==2:
                    donwload(commend.split(" ")[1])
                elif len(commend.split(" "))==3:
                    donwload(commend.split(" ")[1],commend.split(" ")[2])
                else:
                    print("Error")
            case "exit":
                exit()
    monitor_thread.join()
    ftp.quit()