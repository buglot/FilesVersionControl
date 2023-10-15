import os
import printColor
def read_files_in_folder(folder_path,file_names:list):
    file_contents = {}
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
    printColor.printHeader("|%5s|%-40s"%("lines"," main : "+main),"")
    printColor.printHeaderFile("|%5s|%-40s|"%("lines"," "+file))
    if line_main >line_filecompare :
        try:
            for x in range(line_main):
                if data[main][x] != data[file][x]:
                    compare.append(x)
                    printColor.printDiff("|%5d| %-39s|%5d| %-39s|"%(x+1,data[main][x],x+1,data[file][x]))

        except:
            for xx in range(x,line_main):
                compare.append(xx)
                printColor.printDiff("|%5d| %-39s|%5d| %-39s|"%(xx+1,data[main][xx],xx+1,"<--no line"))
    else:
        try:
            for x in range(line_filecompare):
                if data[main][x] != data[file][x] :
                    compare.append(x)
                    printColor.printDiff("|%5d| %-39s|%5d| %-39s|"%(x+1,data[main][x],x+1,data[file][x]))
        except:
            for xx in range(x,line_filecompare):
                compare.append(xx)
                printColor.printDiff("|%5d| %-39s|%5d| %-39s|"%(xx+1,"<--no line",xx+1,data[file][xx]))
    return compare
def find_common_pairs(arg : list,files:list,data:dict):
    if not arg:
        return [] 

    common_pairs = []
    dect = 0
    print("find pair line")
    for i in range(len(arg)):
        for j in range(i + 1, len(arg)):
            pair = (arg[i], arg[j])
            head=0  
            common_elements = []
            for x in pair[0]:
                if x in pair[1]:
                    dect=1
                    if head ==0:
                        head=1
                        printColor.printHeaderFile("|%5s|%-40s"%("lines"," "+files[i]),"")
                        printColor.printHeaderFile2("|%5s|%-40s|"%("lines"," "+files[j]))
                    printColor.printDiff("|%5d| %-39s|%5d| %-39s|"%(x+1,data[files[i]][x],x+1,data[files[j]][x]))
                    common_elements.append(x) 
            if common_elements:
                common_pairs.append(pair)
    if dect==0:
        print("### not find ###")
    return common_pairs
def compare_files(data :dict,main : str,files : list) -> bool :
    line=[]
    for x in files:
        line.append(compare_lines_with_main(data,main,x))
    c= find_common_pairs(line,files,data)
    print("="*75)
    if c !=[]:
        return False,[]

    return True,line

def manger_file(data :dict[str,list],main : str,path:str,files:list):
    if len(files)>1:
        dos =compare_files(data,main,files)
        if dos[0]:
            maindata = data[main]
            mainlen=len(maindata)
            for ii,x in enumerate(dos[1]):
                if x!=[]:
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
            filies_Seve(os.path.join(path,main),maindata)
            for d in files:
                os.remove(os.path.join(path,d))   
        else:
            for d in files:
                os.rename(os.path.join(path,d),os.path.join(path,d+".repo"))   
    else:
        os.remove(os.path.join(path,main))
        os.rename(os.path.join(path,files[0]),os.path.join(path,main))
def filies_Seve(path:str,data:list,sep:str="\n"):
    with open(os.path.join(path),"w") as f:
        for x in range(df:=len(data)):
            f.write(data[x])
            if x != df-1:
                f.write(sep)
        f.close()

                        
            
