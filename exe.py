# control_functions.py

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

# 메인 함수
def main():
    t.shape('turtle')  # 터틀 모양 설정

    # 키와 함수 연결
    t.onkeypress(go_right, 'Right')  # 오른쪽 화살표 키와 오른쪽 이동 함수 연결
    t.onkeypress(go_up, 'Up')         # 위쪽 화살표 키와 위쪽 이동 함수 연결
    t.onkeypress(go_left, 'Left')     # 왼쪽 화살표 키와 왼쪽 이동 함수 연결
    t.onkeypress(go_down, 'Down')     # 아래쪽 화살표 키와 아래쪽 이동 함수 연결
    t.onkeypress(pen_updown, 'Return') # Enter 키와 펜 올리고 내리는 함수 연결
    t.onkeypress(change_color, 'c')    # 'c' 키와 색상 변경 함수 연결
    t.onkeypress(clear, 'Escape')      # ESC 키와 화면 지우는 함수 연결

    t.listen()       # 키 이벤트 감지 시작
    t.mainloop()     # 터틀 그래픽 이벤트 루프 시작

# 프로그램 실행 시 main 함수 호출
if __name__ == "__main__":
    main()
