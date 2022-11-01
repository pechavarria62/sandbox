
import os

# files path.
FOLDER_PATH = r"d:"

def listDir(dir):
    filesNames = os.listdir(dir)
    for filesName in filesNames:
        print('File Name ' + filesName)


if __name__ == '__main__':
    listDir(FOLDER_PATH)
