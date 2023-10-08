import os

listfiles = []
New_files =[]
def monitor_folder(folder_path):
    global listfiles
    while True:
        for filename in os.listdir(folder_path):
            if filename not in listfiles:
                listfiles=os.listdir(folder_path)
                print(f"New file detected: {filename}")
def removeNew_File(a :str):
    global New_files
    New_files.remove(a)
