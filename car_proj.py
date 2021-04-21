#jangeonhee car proj
import turtle 
import math as m

t_world=turtle.Turtle()
t1=turtle.Turtle()
t_world.speed(0)
t1.speed(0)
t_world.hideturtle()
t1.hideturtle()

screen_length=500
screen_height=600
car_base_length = 80
car_base_height = 25

Initial_dest = 0
Final_dest = 0
car_base_length = 80
car_base_height = 25
car_base_a1 = 0
car_base_b1 = 0
car_base_c1 = 0
car_base_d1 = 0
car_roof_right1 = 0
car_roof_left1 = 0
car_base_a2 = 0
car_base_b2 = 0
car_base_c2 = 0
car_base_d2 = 0
car_roof_right2 = 0
car_roof_left2 = 0




def world():
	global Initial_dest, Final_dest
	#horizon
	t_world.color("skyblue")
	t_world.fillcolor("skyblue")
	t_world.up()
	t_world.goto(-(screen_length/2),(screen_height/3))
	t_world.begin_fill()
	t_world.down()
	t_world.setheading(0)
	t_world.forward(screen_length)
	t_world.left(90)
	t_world.forward(screen_height/3)
	t_world.left(90)
	t_world.forward(screen_length)
	t_world.left(90)
	t_world.forward(screen_height/3)
	t_world.end_fill()
	
	#landscape
	t_world.up()
	t_world.goto(-(screen_length/2),(screen_height/3))
	t_world.down()
	t_world.color("lightgreen")
	t_world.begin_fill()
	t_world.setheading(0)
	t_world.forward(screen_length)
	t_world.right(90)
	t_world.goto(screen_length,-(screen_height/2))
	t_world.goto(-(screen_length/2), -(screen_height/2))
	t_world.goto(-(screen_length/2), (screen_height/3))
	t_world.end_fill()	
	
	#road
	t_world.up()
	t_world.goto((screen_length/8), (screen_height/3))#road corner_a
	t_world.down()
	t_world.fillcolor("gray")
	t_world.begin_fill()
	t_world.goto((screen_length/4), (screen_height/3))#road corner_b
	t_world.goto(-(screen_length/5), -(screen_height/2))#road corner_c
	t_world.goto(-(screen_length*4), -(screen_height))#road corner_d goes past max canvas 
	
	#cars invisible path
	t_world.end_fill()
	t_world.color("gray")
	t_world.up()
	t_world.goto(((screen_length/4)+(screen_length/8))/2, (screen_height/3))
	Initial_dest = t_world.pos()
	t_world.down()
	t_world.goto((-(screen_length/5)-(screen_length*4)/2), -screen_height)
	Final_dest = t_world.pos()
	
def car(color, scale_x, scale_y, speed, init_path, final_path):
	global car_base_a1, car_base_b1, car_base_c1, car_base_d1, car_roof_right1, car_roof_left1
	t1.up()
	#scaling car pos
	t1.goto(init_path)
	t1.setheading(t1.towards(final_path))
	t1.forward(speed)
	t1.setheading(0)
	t1.down()
	t1.fillcolor(color)
	t1.begin_fill()
	t1.forward(car_base_length*scale_x/2)
	car_base_a1 = t1.pos()
	t1.circle(car_base_height*scale_x/2,180)
	car_base_b1 = t1.pos()
	t1.right(90)
	t1.circle(car_base_height*scale_x/2,90)
	car_roof_right1 = t1.pos()
	t1.forward(car_base_length*scale_x-car_base_height*scale_x)
	car_roof_left1 = t1.pos()
	t1.circle(car_base_height*scale_x/2,90)
	car_base_c1 = t1.pos()
	t1.setheading(180)
	t1.circle(car_base_height*scale_x/2,180)	
	car_base_d1 = t1.pos()
	t1.end_fill()
	Tires(car_base_d1, car_base_a1, scale_x, scale_y)
	car_window(color, scale_x, scale_y, speed, init_path, final_path)
	side_panel(color, scale_x, scale_y, speed, init_path, final_path)
	car_mirror(color, scale_x)
	car_light(scale_x, scale_y, speed, init_path, final_path)
	car_plate(scale_x, scale_y, speed, init_path, final_path)


def car_window(color, scale_x, scale_y, speed, init_path, final_path):
	t1.up()
	t1.goto(init_path)
	t1.setheading(t1.towards(final_path))
	t1.forward(speed)
	t1.down()
	t1.setheading(90)
	t1.up()
	t1.forward(car_base_height*scale_y)
	t1.down()
	t1.color("skyblue")
	t1.begin_fill()
	t1.right(90)
	t1.forward(car_base_length*scale_x/2*0.7)
	t1.left(90)
	t1.forward(car_base_height*scale_y*0.4)
	t1.left(90)
	t1.forward(car_base_length*scale_x*0.7)
	t1.left(90)
	t1.forward(car_base_height*scale_y*0.4)
	t1.left(90)
	t1.forward(car_base_length*scale_x/2*0.7)
	t1.end_fill()
	#side window
	t1.up()
	t1.goto(car_roof_right2)
	t1.down()
	t1.color("dark"+color)
	t1.width(0.8*scale_x)
	t1.fillcolor("skyblue")
	t1.begin_fill()
	t1.goto(car_roof_right1)
	t1.circle(-car_base_height*scale_x/2,90)
	t1.goto(car_base_b2)
	t1.circle(-car_base_height*scale_x/2,-90)
	t1.end_fill()
	t1.width(1)

	
	
def side_panel(color, scale_x, scale_y, speed, init_path, final_path):
	t1.up()
	t1.goto(car_roof_left1)
	t1.down()
	t1.color("dark"+color)
	t1.width(0.8*scale_x)
	t1.goto(car_roof_left2)
	t1.width(1)
	t1.up()
	t1.goto(car_base_a1)
	t1.color("black")
	t1.fillcolor(color)
	t1.begin_fill()
	t1.setheading(0)
	t1.down()
	t1.circle(car_base_height*scale_x/2,180)
	t1.goto(car_base_b2)
	t1.circle(car_base_height*scale_x/2,-180)
	t1.color(color)
	t1.goto(car_base_a1)
	t1.end_fill()
	
def car_light(scale_x, scale_y, speed, init_path, final_path):
	t1.up()
	t1.goto(init_path)
	t1.setheading(t1.towards(final_path))
	t1.forward(speed)
	t1.goto(car_base_a1)
	t1.setheading(90)
	t1.forward(car_base_height*scale_y*0.5)
	t1.down()
	t1.color("yellow")
	t1.begin_fill()
	t1.circle(4*scale_x)
	t1.end_fill()
	#light 2
	t1.up()
	t1.goto(init_path)
	t1.setheading(t1.towards(final_path))
	t1.forward(speed)
	t1.goto(car_base_d1)
	t1.setheading(90)
	t1.forward(car_base_height*scale_y*0.5)
	t1.down()
	t1.color("yellow")
	t1.begin_fill()
	t1.circle(-4*scale_x)
	t1.end_fill()

def car_mirror(color, scale_x):
	t1.up()
	t1.goto(car_base_b1)
	t1.down()
	t1.color("dark"+ color)
	t1.fillcolor()
	t1.begin_fill()
	t1.setheading(-80)
	t1.circle(4*scale_x)
	t1.end_fill()
	t1.up()
	t1.goto(car_base_c1)
	t1.down()
	t1.color("dark"+ color)
	t1.fillcolor()
	t1.begin_fill()
	t1.setheading(80)
	t1.circle(4*scale_x)
	t1.end_fill()
	
def car_plate(scale_x, scale_y, speed, init_path, final_path):
	t1.up()
	t1.goto(init_path)
	t1.setheading(t1.towards(final_path))
	t1.forward(speed)
	t1.down()
	t1.setheading(90)
	t1.up()
	t1.forward(car_base_height/3*scale_y)
	t1.down()
	t1.color("white")
	t1.begin_fill()
	t1.right(90)
	t1.forward(car_base_length*scale_x/2*0.4)
	t1.left(90)
	t1.forward(car_base_height*scale_y*0.3)
	t1.left(90)
	t1.forward(car_base_length*scale_x*0.4)
	t1.left(90)
	t1.forward(car_base_height*scale_y*0.3)
	t1.left(90)
	t1.forward(car_base_length*scale_x/2*0.4)
	t1.end_fill()
	t1.left(90)
	t1.forward(car_base_height*scale_y*0.3)
	
def car_side(color, scale_x, scale_y, speed, init_path, final_path):
	global car_base_a2, car_base_b2, car_base_c2, car_base_d2, car_roof_right2, car_roof_left2
	t1.up()
	#scaling car pos
	t1.goto(init_path)
	t1.setheading(t1.towards(final_path))
	t1.forward(speed)
	#car's body
	t1.setheading(0)
	t1.down()
	#t1.color("darkblue")
	t1.color(color)
	#t1.fillcolor(color)
	t1.begin_fill()
	t1.forward(car_base_length*scale_x/2)
	car_base_a2 = t1.pos()
	t1.circle(car_base_height*scale_x/2,180)
	car_base_b2 = t1.pos()
	t1.right(90)
	t1.circle(car_base_height*scale_x/2,90)
	car_roof_right2 = t1.pos()
	t1.forward(car_base_length*scale_x-car_base_height*scale_x)
	car_roof_left2 = t1.pos()
	t1.circle(car_base_height*scale_x/2,90)
	car_base_c2 = t1.pos()
	t1.setheading(180)
	t1.circle(car_base_height*scale_x/2,180)	
	car_base_d2 = t1.pos()
	t1.forward(car_base_length*scale_x/2)
	car_base_mid = t1.pos()
	t1.end_fill()
	Tires(car_base_d2, car_base_a2, scale_x, scale_y)

def Tires(car_base_d, car_base_a, scale_x, scale_y):
	#car's tires1
	t1.color("black")
	t1.begin_fill()
	t1.up()
	t1.goto(car_base_d[0], car_base_d[1])
	t1.down()
	t1.right(90)
	t1.forward(15*scale_y)
	t1.left(90)
	t1.forward(12*scale_x)
	t1.left(90)
	t1.forward(15*scale_y)
	t1.left(90)
	t1.forward(12*scale_x)
	#car's tires2
	t1.up()
	t1.goto(car_base_a[0], car_base_a[1])
	t1.down()
	t1.right(-90)
	t1.forward(15*scale_y)
	t1.right(90)
	t1.forward(12*scale_x)
	t1.right(90)
	t1.forward(15*scale_y)
	t1.right(90)
	t1.forward(12*scale_x)
	t1.end_fill()

	
def moving_car(color):
	car_base_a1 = 0
	car_base_b1 = 0
	car_base_c1 = 0
	car_base_d1 = 0
	car_roof_right1 = 0
	car_roof_left1 = 0

	car_base_a2 = 0
	car_base_b2 = 0
	car_base_c2 = 0
	car_base_d2 = 0
	car_roof_right2 = 0
	car_roof_left2 = 0
	y=0
	
	for x1 in range (8):
		if(x1>5):
			y+=1
		y+=0.5
		#waaa!! inspired by the last calculus class xD
		car_side(color,y,y,(x1*m.e**(x1/2))+x1*50,Initial_dest,Final_dest)
		car(color,y,y,(x1*m.e**(x1/2))+x1*60,Initial_dest,Final_dest)
		t1.clear()	

world()
moving_car("red")
moving_car("blue")
moving_car("pink")
moving_car("green")
