import random
import turtle
import time
delay = 0.15
##This is a simple project of Recep Topaktas.
 
gameWindow = turtle.Screen()
gameWindow.title('SNAKE GAME')
gameWindow.bgcolor('lightgreen')
gameWindow.setup(width=600, height=600)
gameWindow.tracer(0)
 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(0, 100)
head.direction = "stop"
 
yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("yellow")
yemek.penup()
yemek.shapesize(0.80, 0.80)
yemek.goto(0, 0)
 
queues = []
puan = 0
 
info_game = turtle.Turtle()
info_game.speed(0)
info_game.shape("square")
info_game.color("white")
info_game.penup()
info_game.hideturtle()
info_game.goto(0, 260)
info_game.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
 
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
 
 
 
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"
 
gameWindow.listen()
gameWindow.onkey(go_up, "Up")
gameWindow.onkey(go_down, "Down")
gameWindow.onkey(go_right, "Right")
gameWindow.onkey(go_left, "Left")
 
while True:
    gameWindow.update()
 
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
 
        for kuyruk in queues:
            kuyruk.goto(1000, 1000)
        queues = []
 
        puan = 0
        delay = 0.1
 
        info_game.clear()
        info_game.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
 
    if head.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)
 
        new_queue = turtle.Turtle()
        new_queue.speed(0)
        new_queue.shape("square")
        new_queue.color("white")
        new_queue.penup()
        queues.append(new_queue)
 
        delay -= 0.001
 
        puan = puan + 25
        info_game.clear()
        info_game.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
 
    for index in range(len(queues) - 1, 0, -1):
        x = queues[index - 1].xcor()
        y = queues[index - 1].ycor()
        queues[index].goto(x, y)
 
    if len(queues) > 0:
        x = head.xcor()
        y = head.ycor()
        queues[0].goto(x, y)
 
    move()
 
    for segment in queues:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in queues:
                segment.goto(1000, 1000)
            queues = []
            puan = 0
            info_game.clear()
            info_game.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.16
 
    time.sleep(delay)
    ##  I wish you good games.