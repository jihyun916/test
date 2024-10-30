import turtle

turtle.screensize(300, 300)

t = turtle.Turtle()
t.shape('circle')

t.speed(10)

# 배경
t.penup()
t.goto(500, 500)
t.pendown()
t.color('#100030')
t.begin_fill()
t.goto(500, -500)
t.goto(-500, -500)
t.goto(-500, 500)
t.goto(500, 500)
t.end_fill()


# 바다
t.penup()
t.goto(2000, -2250)
t.pendown()
t.color('#11006c')
t.begin_fill()
t.left(90)
t.circle(2050, 180, 20)
t.end_fill()

# 언덕
t.penup()
t.right(90)
t.goto(450, -180)
t.pendown()
t.color('black')
t.begin_fill()
t.circle(1000, 180, 20)
t.end_fill()

# 집
t.penup()
t.right(90)
t.goto(430, -250)
t.pendown()
t.color('white', '#0A0A0A')
t.begin_fill()
t.goto(430, -20)
t.goto(230, -20)
t.goto(230, -250)
t.goto(430, -250)
t.end_fill()

t.penup()
t.goto(420, -80)
t.right(90)
t.pendown()
t.begin_fill()
t.color('white', '#0D0D0D')
t.goto(150, -80)
t.goto(225, -30)
t.goto(230, -5)
t.goto(420, -5)
t.end_fill()

# 창문
t.penup()
t.goto(304, -135)
t.dot(65, 'white')

t.penup()
t.goto(304, -135)
t.dot(61, '#F8F2B9')

t.penup()
t.goto(270, -134)
t.pendown()
t.begin_fill()
t.color('#0D0D0D')
t.goto(270, -136)
t.goto(340, -136)
t.goto(340, -134)
t.goto(270, -134)
t.end_fill()

t.penup()
t.goto(303, -100)
t.pendown()
t.begin_fill()
t.color('#0D0D0D')
t.goto(303, -167)
t.goto(305, -167)
t.goto(305, -100)
t.goto(303, -100)
t.end_fill()

# 배
t.penup()
t.goto(-118, -190)
t.pendown()
t.color('white')
t.begin_fill()
t.goto(-31, -190)
t.goto(-50, -218)
t.goto(-96, -218)
t.goto(-118, -190)
t.end_fill()

t.penup()
t.goto(-80, -190)
t.pendown()
t.begin_fill()
t.goto(-80, -135)
t.goto(-78, -135)
t.goto(-62, -149)
t.goto(-78, -157)
t.goto(-78, -190)
t.end_fill()

# 달
t.penup()
t.goto(320, 330)
t.pendown()
t.dot(100, 'white')

t.penup()
t.goto(345, 345)
t.pendown()
t.dot(85, '#100030')

# 별
t.shapesize(0.1)

x = [-304.0, -331.0, -262.0, -221.0, -156.0, -98.0, -71.0, -65.0, 107.0, 26.0, 253.0, 359.0, 
     198.0, 93.0, 334.0, 105.0, -101.0, -330.0, -325.0, 119.0, -184.0, -16.0, -220.0]
y = [297.0, 228.0, 192.0, 267.0, 237.0, 213.0, 165.0, 340.0, 327.0, 272.0, 155.0, 200.0,
     238.0, 161.0, 26.0, -5.0, 43.0, 110.0, -83.0, -172.0, -18.0, -69.0, 368.0]

for i in range(len(x)):
    t.penup()
    t.goto(x[i], y[i])
    t.stamp()
    t.pendown()

input()