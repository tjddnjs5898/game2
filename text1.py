#방향키 좌우로 움직여 빨간 공 피하기게임 (공에 닿으면 게임종료)
import turtle
import random

win = turtle.Screen()
win.title("간단 공 피하기")
win.setup(400, 400)
win.bgcolor("lightblue")

player = turtle.Turtle()
player.shape("turtle")
player.penup()
player.goto(0, -150)

enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(random.randint(-180, 180), 150)

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

def game_loop():
    enemy.sety(enemy.ycor() - 20)
    if enemy.ycor() < -200:
        enemy.goto(random.randint(-180, 180), 150)
    if player.distance(enemy) < 20:
        player.hideturtle()
        enemy.hideturtle()
        win.bgcolor("black")
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.color("white")
        pen.write("게임 종료!", align="center", font=("Arial", 24, "bold"))
        return
    win.ontimer(game_loop, 200)

game_loop()
win.mainloop()
