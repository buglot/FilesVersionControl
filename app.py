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
        df[key].append(x)  # เพิ่มข้อมูลลงในรายการที่เป็นของคีย์นั้น 
    df[key].append(key)  
    return df
def removeNew_File(a :str):
    global New_files
    New_files.remove(a)
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
                if dr[x]!=[]:
                    data=read.read_files_in_folder(folder_path,dr[x])
                    read.manger_file(data,x,folder_path,dr[x])
            New_files=[]
            listfiles=os.listdir(folder_path)        

    monitor_thread.join()