from ftplib import FTP
from printColor import *
from dir import * 

ftp = FTP("192.168.1.33")
ftp.login(user="myuser", passwd="mypassword")
printHeader(" Connected Server ")

filenames = ftp.nlst()
print()
printDir("\ Could")
for f in filenames:
    if not is_file(ftp,f):
        printSubDir(ftp.nlst(f))
    else:
        printFile(f)

ftp.quit()


