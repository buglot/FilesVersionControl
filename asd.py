import os

with open(os.path.join("ftp-data","a.txt"),"r") as f:
    d=f.readlines()
    f.close()

print(d,sep="\n")

with open(os.path.join("ftp-data","a.txt"),"w") as f:
    f.write("peter")
    f.close()