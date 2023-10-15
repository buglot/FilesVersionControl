import os
import threading
import time
import read
listfiles = []
New_files =[]
def monitor_folder(folder_path):
    global listfiles
    global New_files
    listfiles=os.listdir(folder_path)
    while True:
        for filename in os.listdir(folder_path):
            if filename not in listfiles:
                New_files.append(filename)
                listfiles.append(filename)
        time.sleep(10)
def file_match(data:list[str])->dict:
    df = {}  # สร้างพจนานุกรมเปล่าเพื่อเก็บรายการสำหรับแต่ละคีย์
    for x in data:
        key = x.split("_name==")[0]  # ดึงคีย์จากข้อมูล
        if key not in df:
            df[key] = []  # สร้างรายการเปล่าสำหรับคีย์ใหม่ (ถ้ายังไม่มี)
            df[key].append(key)
        df[key].append(x)  # เพิ่มข้อมูลลงในรายการที่เป็นของคีย์นั้น 
    return df
def removeNew_File(a :str):
    global New_files
    New_files.remove(a)
def repoDetect(key:str,folder_path:str):
    for x  in os.listdir(folder_path):
       if x.startswith(key) and x.endswith(".repo"):
           return True
    return False
if __name__ == "__main__":
    print("Sever Manger")
    folder_path = "ftp-data"  # ระบุโฟลเดอร์ที่คุณต้องการตรวจสอบ
    monitor_thread = threading.Thread(target=monitor_folder,args={folder_path})
    monitor_thread.start()
    while 1:
        if New_files != []:
            dr=file_match(New_files)
            for x in dr.keys():
                print(x)
                if repoDetect(x,folder_path):
                    for file in dr[x]:
                        if file != x:
                            os.rename(os.path.join(folder_path,file),os.path.join(folder_path,file+".repo"))
                    continue
                if dr[x]!=[]:
                    data=read.read_files_in_folder(folder_path,dr[x])
                    read.manger_file(data,x,folder_path,dr[x])
                    print("="*95)
            New_files=[]
            listfiles=os.listdir(folder_path)        

    monitor_thread.join()