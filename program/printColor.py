def printHeader(t :str):
    print(f"\033[1;37;44m{t}\033[00m")
def printDir(t :str,d : int = 50):
    print("\033[1;37;45m%-50s\033[00m" % t)
def printSubDir(t :str):
    print(f"\033[35m{t}\033[00m")
def printFile(t :str):
    print(f"\033[32m{t}\033[00m")