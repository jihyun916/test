import turtle

t = turtle.Turtle()
t.shape('turtle')
#t.hideturtle()

t.speed(5)

''' 바다 '''
t.penup()
t.goto(800, -300)
t.pendown()
t.color('#002E5E')
t.begin_fill()
t.goto(800, -700)
t.goto(800, -150)
t.goto(-800, -150)
t.goto(-800, -700)
t.end_fill()

t.penup()
t.goto(-800, -300)
t.pendown()
t.color('#001948')
t.begin_fill()
t.goto(800, -700)
t.goto(800, -150)
t.goto(-800, -150)
t.goto(-800, -700)
t.end_fill()


# t.penup()
# t.goto(-800, -150)
# t.pendown()
# t.color('#00153B')
# t.begin_fill()
# t.goto(800, -700)
# t.goto(800, -100)
# t.goto(-800, -100)
# t.goto(-800, -100)
# t.end_fill()



''' 하늘 '''
t.penup()
t.goto(-800, -100)
t.pendown()
t.color('black')
t.begin_fill()
t.goto(800, -100)
t.goto(800, 700)
t.goto(-800, 700)
t.goto(-800, -100)
t.end_fill()

''' 구름 '''
t.penup()
t.goto(500, 300)
t.pendown()
t.color('#474747', 'gray')
t.left(180)
t.begin_fill()
t.circle(300, 180, 20)
t.end_fill()

t.penup()
t.goto(410, 50)
t.pendown()
t.color('#474747', 'gray')
t.left(180)
t.begin_fill()
t.circle(450, 180, 20)
t.end_fill()


''' 별 '''

''' 달 '''


input()