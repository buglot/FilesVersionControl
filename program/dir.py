

def is_file(ftp,filename):
    try:
        
        return ftp.size(filename) is not None
    except:
        return None