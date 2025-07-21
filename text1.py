#방햘키 자우로 움직여 빨간 공 피하기 게임.
#점수 표시 추가
#게임 속도 점점 빨라짐 추가
#게임 재시작(스페이스바) 추가

import turtle
import random

# 화면 설정
win = turtle.Screen()
win.title("공 피하기 게임")
win.setup(400, 400)
win.bgcolor("lightblue")

# 플레이어 설정
player = turtle.Turtle()
player.shape("turtle")
player.penup()
player.goto(0, -150)

# 적 설정
enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(random.randint(-180, 180), 150)

# 점수 표시
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 160)
pen.write(f"점수: {score}", align="center", font=("Arial", 16, "bold"))

# 이동 함수
def move_left():
    x = player.xcor() - 20
    if x < -180: x = -180
    player.setx(x)

def move_right():
    x = player.xcor() + 20
    if x > 180: x = 180
    player.setx(x)

win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")

# 게임 루프
speed = 200
def game_loop():
    global score, speed
    enemy.sety(enemy.ycor() - 20)

    if enemy.ycor() < -200:
        enemy.goto(random.randint(-180, 180), 150)
        score += 1
        pen.clear()
        pen.write(f"점수: {score}", align="center", font=("Arial", 16, "bold"))
        if speed > 50 and score % 5 == 0:
            speed -= 10  # 속도 증가

    if player.distance(enemy) < 20:
        game_over()
        return

    win.ontimer(game_loop, speed)

# 게임 종료
def game_over():
    player.hideturtle()
    enemy.hideturtle()
    pen.goto(0, 0)
    pen.write("게임 종료\n스페이스바로 재시작", align="center", font=("Arial", 16, "bold"))
    win.onkey(restart_game, "space")

# 재시작
def restart_game():
    global score, speed
    player.goto(0, -150)
    player.showturtle()
    enemy.goto(random.randint(-180, 180), 150)
    enemy.showturtle()
    score = 0
    speed = 200
    pen.clear()
    pen.goto(0, 160)
    pen.write(f"점수: {score}", align="center", font=("Arial", 16, "bold"))
    game_loop()

# 시작
game_loop()
win.mainloop()

