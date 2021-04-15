import os
from winAPI import *

if __name__ == '__main__':
    changeTxtColor(4)
    hideConsoleCursor(1)
    print("Hello")
    gotoxy(1, 1)
    changeTxtColor(5)
    print("Hello")
    gotoxy(2, 6)
    changeTxtColor(6)
    print("Hello")
    gotoxy(3, 8)
    changeTxtColor(7)
    os.system("pause")
