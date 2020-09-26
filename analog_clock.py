import turtle
import time

win = turtle.Screen()
win.bgcolor("black")
win.setup(height = 600, width = 600)
win.title("Analogue Clock")
win.tracer(0)

# Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

#this function will draw the clock
def draw_clock(hr, mn, sec, pen):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)

    #draw the hour hashes
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw the hands
    # Each tuple in list hands describes the color, the length
    # and the divisor for the angle
    hands = [("orange", 80, 12), ("blue", 110, 60), ("green", 150, 60)]
    time_set = (hr, mn, sec)

    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])

while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    draw_clock(hr, mn, sec, pen)
    win.update()
    time.sleep(1)
    pen.clear()