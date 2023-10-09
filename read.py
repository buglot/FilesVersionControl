import os

def read_files_in_folder(folder_path):
    file_contents = {}
    file_names = os.listdir(folder_path)
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):  # ตรวจสอบว่าเป็นไฟล์
            with open(file_path, 'r') as file:
                file_content = file.read()
                file_contents[file_name] = file_content.split('\n')
    return file_contents

def get_lines_from_files(file_contents,i:int,*arg):
    lines_list = []

    for x in arg:
        try:
            lines_list.append(file_contents[x][i])
        except:
            lines_list.append("")

    return lines_list

def compare_lines_with_main(data:dict,main :str,file: str)-> list:
    compare = []
    line_main = len(data[main])
    line_filecompare = len(data[file])
    if line_main >line_filecompare :
        try:
            for x in range(line_main):
                if data[main][x] != data[file][x] :
                    compare.append(x)

        except:
            for xx in range(x,line_main):
                compare.append(xx)
    else:
        try:
            for x in range(line_filecompare):
                if data[main][x] != data[file][x] :
                    compare.append(x)
        except:
            for xx in range(x,line_filecompare):
                compare.append(xx)
    return compare
def find_common_pairs(arg : list):
    if not arg:
        return [] 

    common_pairs = []

    for i in range(len(arg)):
        for j in range(i + 1, len(arg)):
            pair = (arg[i], arg[j])  
            common_elements = [x for x in pair[0] if x in pair[1]]  
            if common_elements:
                common_pairs.append(pair)

    return common_pairs
def compare_files(data :dict,main : str,files : list) -> bool :
    line=[]
    for x in files:
        line.append(compare_lines_with_main(data,main,x))
    c= find_common_pairs(line)
    if c !=[]:
        return False,[]

    return True,line

def manger_file(data :dict[str,list],main : str,path:str,*files):
    if len(files)>1:
        dos =compare_files(data,main,files)
        if dos[0]:
            maindata = data[main]
            mainlen=len(maindata)
            for ii,x in enumerate(dos[1]):
                for j in x:
                    if mainlen<(maxload:=max(x)):
                        for xd in range(mainlen-1,maxload):
                            data[main].append("")
                        maindata=data[main]
                        mainlen = len(maindata)
                        
                    try:
                        maindata.insert(j,data[files[ii]][j])
                    except:
                        maindata.insert(j,data[main][j])
                    maindata.pop(j+1)
            with open(os.path.join(path,main),"w") as f:
                for x in range(df:=len(maindata)):
                    f.writelines(maindata[x])
                    if x != df-1:
                        f.writelines("\n")
                f.close()
           
    else:
        os.remove(os.path.join(path,main))
        os.rename(os.path.join(path,files[0]),os.path.join(path,main))

if __name__=="__main__":
    data=read_files_in_folder("ftp-data")
    manger_file(data,"a.txt","ftp-data","b.txt","c.txt")
                        
            
