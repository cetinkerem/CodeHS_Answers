speed(0)

def write_text(text, size):
    __turtle.write(text, align="center", font=("Arial", size, "normal"))

def draw_point(x, y):
    setposition(x, y)
    pendown()
    begin_fill()
    circle(2)
    end_fill()
    
def draw_height(x, y):
    setposition(x, 0)
    color("red")
    left(90)
    pos = 0
    while pos < y:
        forward(5)
        penup()
        if pos < y:
            forward(5)
            pendown()
        pos=pos+10
    penup()

def set_up_axes():
    setposition(-200,0)
    color("blue")
    setposition(200,0)
    penup()
    setposition(-175, -15)
    write_text("(200,0)", 10)
    setposition(175,-15)
    write_text("(-200,0)", 10)
    setposition(0,200)
    pendown()
    setposition(0,-200)
    penup()
    setposition(25, 185)
    write_text("(0,200)", 10)
    setposition(25,-185)
    write_text("(0,-200)", 10)
    setposition(0,0)
    color("black")
    pendown()
    pensize(3)

def set_up_base():
    draw_point(-100, 0)
    draw_point(100, 0)
    penup()
    setposition(0,-15)
    write_text("base", 10)
    setposition(0, -30)
    write_text(200, 10)
    setposition(100, 0)
    pendown()

def label_height(x, y):
    if x > 0:
        setposition(x-20,y/2)
        write_text("height", 10)
        setposition(x-20, y/2-15)
        write_text(y, 10)
    else:
        setposition(x+20,y/2)
        write_text("height", 10)
        setposition(x+20, y/2-15)
        write_text(y, 10)
    color("black")

# -------------------------------------------
# Fill in this function to print the area of the triangle to the screen
# Hint: You'll need to use variables and the write_text function!
def calculate_area(y):
    setposition(0, -80)
    write_text("Area (in sq. pixels):" + str((200 * y)/2), 20)
    setposition(0, -110)


# -------------------------------------------

set_up_axes()
set_up_base()
x_coordinate = int(input("What is the x-value of the final point: "))
y_coordinate = int(input("What is the y-value of the final point: "))
draw_point(x_coordinate, y_coordinate)
draw_point(-100, 0)
draw_height(x_coordinate, y_coordinate)
label_height(x_coordinate, y_coordinate)
calculate_area(y_coordinate)
setposition(0, -200)
