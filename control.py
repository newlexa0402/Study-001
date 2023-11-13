# control.py

import turtle as t  # turtle 모듈을 t로 가져온다
import random       # random 모듈을 가져온다

# 오른쪽으로 이동하는 함수
def go_right():
    t.setheading(0)   # 터틀의 방향을 오른쪽(0도)으로 설정
    t.forward(10)     # 10 픽셀만큼 이동

# 위쪽으로 이동하는 함수
def go_up():
    t.setheading(90)  # 터틀의 방향을 위쪽(90도)으로 설정
    t.forward(10)     # 10 픽셀만큼 이동

# 왼쪽으로 이동하는 함수
def go_left():
    t.setheading(180)  # 터틀의 방향을 왼쪽(180도)으로 설정
    t.forward(10)      # 10 픽셀만큼 이동

# 아래쪽으로 이동하는 함수
def go_down():
    t.setheading(270)  # 터틀의 방향을 아래쪽(270도)으로 설정
    t.forward(10)      # 10 픽셀만큼 이동

# 펜을 올리거나 내리는 함수
def pen_updown():
    if t.isdown():    # 펜이 내려져 있으면
        t.penup()      # 펜을 올린다
    else:
        t.pendown()    # 펜을 내린다

# 터틀의 색상을 랜덤으로 변경하는 함수
def change_color():
    colors = ['red', 'green', 'blue', 'orange', 'black']  # 색상 리스트
    choice = random.choice(colors)                       # 랜덤으로 색상 선택
    t.color(choice)                                      # 터틀의 색상을 변경

# 화면을 지우고 검은 펜으로 설정하는 함수
def clear():
    t.clear()           # 화면을 지운다
    t.color('black')    # 펜의 색상을 검은색으로 설정
