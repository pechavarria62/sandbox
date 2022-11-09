
import os
# Program prints out the files and folders names you have in path.

# imput_path = input("Enter path please: ")
# FOLDER_PATH =  r"imput_path"
FOLDER_PATH = r"/Volumes/personal/repos/sandbox"  # files path.

def listDir(dir):
    filesNames = os.listdir(dir)
    for filesName in filesNames:
        print('File Name ' + filesName)


if __name__ == '__main__':
    listDir(FOLDER_PATH)
#-------------------------------------------------------
# Example Output:
# File Name hello.py    
# File Name texts_files 
# File Name ._.vscode    
# File Name if.py       
# File Name ForLoops.py  
# File Name try.py       
# File Name fors_ifs.py 
# File Name functions.py 
# File Name programs.py  
# File Name hard-drive-read.py

