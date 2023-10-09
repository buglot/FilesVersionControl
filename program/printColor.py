def printHeader(t :str,end :str = "\n"):
    print(f"\033[1;37;44m{t}\033[00m",end=end)
def printDir(t :str,d : int = 50):
    print("\033[1;37;45m%s\033[00m" % t)
def printSubDir(t :str,end :str = "\n"):
    print(f"\033[35m{t}\033[00m",end=end)
def printFile(t :str):
    print(f"\033[32m{t}\033[00m")