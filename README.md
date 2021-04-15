# Win_Console_API
Windows Console API

## C Code : winAPI.c
### Usage
* #include "winAPI.c"

## Python (C Module) Code : pywinAPI.c
### Build
* python setup.py build
### Install
* python setup.py install
### Usage
* from winAPI iport *

## Function List
### gotoxy(x, y)
* 콘솔창 커서 좌표 이동 함수
### wrIsX()
* 콘솔창 커서 X축(가로) 좌표 리턴 함수
### wrIsY()
* 콘솔창 커서 Y축(세로) 좌표 리턴 함수
### changeTxtColor(color)
* 콘솔창 글자 색 변경 함수
### hideConsoleCursor(hide_flag)
* 콘솔창 커서 깜박임 제거 함수
* 1 -> hide
* 0 -> show
