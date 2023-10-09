import os

def read_files_in_folder(folder_path):
    # สร้างพจนานุกรมเพื่อเก็บเนื้อหาของแต่ละไฟล์
    file_contents = {}

    # ใช้ os.listdir() เพื่อรับรายชื่อไฟล์ในโฟลเดอร์
    file_names = os.listdir(folder_path)

    # อ่านและเก็บเนื้อหาของไฟล์ในพจนานุกรม
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):  # ตรวจสอบว่าเป็นไฟล์
            with open(file_path, 'r') as file:
                file_content = file.read()
                file_contents[file_name] = file_content.split('\n')

    # ส่งคืนพจนานุกรมที่เก็บเนื้อหาของไฟล์
    return file_contents

def get_lines_from_files(file_contents,i:int,*arg):
    lines_list = []

    # วนลูปผ่านพจนานุกรมและดึงข้อมูลแต่ละบรรทัดเข้าสู่รายการ
    for x in arg:
        try:
            lines_list.append(file_contents[x][i])
        except:
            lines_list.append("")

    return lines_list

# เรียกใช้งานฟังก์ชันและระบุโฟลเดอร์ที่คุณต้องการตรวจจับและอ่านไฟล์
folder_path = 'C:\\Krittin\\Web\\Project\\File'  # เปลี่ยนเป็นเส้นทางของโฟลเดอร์ที่คุณต้องการตรวจจับและอ่านไฟล์
result = read_files_in_folder(folder_path)

# ดึงข้อมูลแต่ละบรรทัดจากพจนานุกรมและแปลงเป็นรายการ (list)
lines_list = get_lines_from_files(result,2,"a.txt","e.txt","c.txt")

# แสดงรายการของข้อมูลแต่ละบรรทัด
for line in lines_list:
    print(line)



def compare_lines_with_main(data:dict,main :str,file: str)-> list:
    compare = []
    now = 0
    line_main = len(data[main])
    line_filecompare = len(data[file])
    if line_main >line_filecompare :
        try:
            for x in range(line_main):
                if data[main][x] != data[file][x] :
                    compare.append(x)
                now = x
        except:
            for x in range(now,line_main):
                compare.append(x)
    else:
        try:
            for x in range(line_filecompare):
                if data[main][x] != data[file][x] :
                    compare.append(x)
                now = x
        except:
            for x in range(now,line_filecompare):
                compare.append(x)
    return compare
def find_common_pairs(*arg):
    if not arg:
        return []  # ไม่มีรายการที่จะเปรียบเทียบ

    common_pairs = []  # รายการที่จะเก็บคู่ที่มีสมาชิกเหมือนกัน

    # วนลูปผ่านคู่ของรายการและหาคู่ที่มีสมาชิกเหมือนกัน
    for i in range(len(arg)):
        for j in range(i + 1, len(arg)):
            pair = (arg[i], arg[j])  # สร้างคู่รายการ
            common_elements = [x for x in pair[0] if x in pair[1]]  # หาสมาชิกที่เหมือนกัน
            if common_elements:
                common_pairs.append(pair)

    return common_pairs
def compare_files(data :dict,main : str,*files) -> bool :
    line=[]
    for x in files:
        line.append(compare_lines_with_main(x))
    c= find_common_pairs(line)
    if c !=[]:
        return False,[]

    return True,line

def manger_file(data :dict,main : str,*files):
    if len(files)>1:
        if compare_files(data,main,files):
            
