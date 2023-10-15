def printHeader(t :str,end :str = "\n"):
    print(f"\033[1;37;44m{t}\033[00m",end=end)
def printHeaderFile(t :str,end :str = "\n"):
    print(f"\033[1;37;42m{t}\033[00m",end=end)
def printDiff(t :str,d : int = 50):
    print("\033[0;32;41m%s\033[00m" % t)
def printHeaderFile2(t :str,end :str = "\n"):
    print(f"\033[1;30;43m{t}\033[00m",end=end)
