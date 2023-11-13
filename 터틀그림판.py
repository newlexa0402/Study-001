from control import *
import turtle as t

t.shape('turtle')

# 키와 함수 연결
t.onkeypress(go_right, 'Right')  # 오른쪽 화살표 키와 오른쪽 이동 함수 연결
t.onkeypress(go_up, 'Up')         # 위쪽 화살표 키와 위쪽 이동 함수 연결
t.onkeypress(go_left, 'Left')     # 왼쪽 화살표 키와 왼쪽 이동 함수 연결
t.onkeypress(go_down, 'Down')     # 아래쪽 화살표 키와 아래쪽 이동 함수 연결
t.onkeypress(pen_updown, 'Return') # Enter 키와 펜 올리고 내리는 함수 연결
t.onkeypress(change_color, 'c')    # 'c' 키와 색상 변경 함수 연결
t.onkeypress(clear, 'Escape')      # ESC 키와 화면 지우는 함수 연결

t.listen()    # 키 입력 감지 시작
t.mainloop()  # 창 열려있게 유지