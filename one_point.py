import turtle as Turtle
import math
import time

python3 = True

if python3:
	turtle = Turtle.Pen()
else:
	turtle = Turtle

try:
	Vec2D = Turtle.Vec2D
except AttributeError:
	class Vec2D(tuple):
		def __new__(cls, x, y):
			return tuple.__new__(cls, (x, y))
		def __add__(self, other):
			return Vec2D(self[0]+other[0], self[1]+other[1])
		def __mul__(self, other):
			if isinstance(other, Vec2D):
				return self[0]*other[0]+self[1]*other[1]
			return Vec2D(self[0]*other, self[1]*other)
		def __rmul__(self, other):
			if isinstance(other, int) or isinstance(other, float):
				return Vec2D(self[0]*other, self[1]*other)
		def __sub__(self, other):
			return Vec2D(self[0]-other[0], self[1]-other[1])
		def __neg__(self):
			return Vec2D(-self[0], -self[1])
		def __abs__(self):
			return (self[0]**2 + self[1]**2)**0.5
		def rotate(self, angle):
			perp = Vec2D(-self[1], self[0])
			angle = angle * math.pi / 180.0
			c, s = math.cos(angle), math.sin(angle)
			return Vec2D(self[0]*c+perp[0]*s, self[1]*c+perp[1]*s)
		def __getnewargs__(self):
			return (self[0], self[1])
		def __repr__(self):
			return str(self.__getnewargs__())


turtle.clear()
turtle.speed(0)
#turtle.ht()
#turtle.radians()
#turtle.width(1)
turtle.delay(0)

def grid():
	size = 500
	
	turtle.up()
	turtle.goto(0, 0)
	turtle.down()
	turtle.goto(-size, 0)
	turtle.goto(size, 0)
	turtle.goto(0, 0)
	turtle.goto(0, size)
	turtle.goto(0, -size)
	turtle.goto(0, 0)

def diff(x, y):
	x = x - turtle.xcor()
	y = y - turtle.ycor()
	
	return x, y

def calc_h(x, y=None, degree=True):
	if y is None:
		y = x[1]
		x = x[0]
	x, y = diff(x, y)
	rad = math.atan2(y, x)
	if degree:
		return math.degrees(rad)
	return rad

def point(*a):
	turtle.setheading(calc_h(*a))

def make_vanish(x, y=None):
	size = 500
	
	if y is None:
		y = x[1]
		x = x[0]
	
	turtle.up()
	turtle.goto(-size, y)
	turtle.down()
	turtle.goto(size, y)
	turtle.goto(x, y)
	turtle.dot()
	
	return Vec2D(x, y)

def rect(x, y, w, h):
	turtle.up()
	turtle.goto(x, y)
	turtle.down()
	turtle.setheading(0)
	
	coords = []
	for i in [w,h]*2:
		coords.append(turtle.pos())
		turtle.fd(i)
		turtle.rt(90)
	
	return coords

def replay(l):
	turtle.up()
	turtle.goto(l[0])
	turtle.down()
	
	for x in l:
		turtle.goto(x)

def distance(a, b):
	return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def point1(r, v, d): Percent Distance
	n = []
	for x in r:
		
		turtle.up()
		turtle.goto(x)
		turtle.down()
		
		point(v)
		dist = distance(v, turtle.pos())
		turtle.fd(dist * d / 100)
		
		n.append(turtle.pos())
	
	n.append(n[0])
	
	replay(n)

def point12(r, v, d): # Absolute Distance
	n = []
	
	turtle.up()
	turtle.goto(r[0])
	
	point(v)
	turtle.fd(d)
	
	n.append(turtle.pos())
	n.append(line(r[1], v, y=turtle.pos()[1]))
	n.append(line(r[2], v, x=n[-1][0]))
	n.append(line(r[3], v, x=turtle.pos()[0]))
	n.append(n[0])
	
	replay(n)
	for x in range(4):
		replay([r[x], n[x]])

def line(a, b, x=None, y=None):
	xc = a[0] - b[0]
	yc = a[1] - b[1]
	
	m = yc / xc
	i = a[1] - m * a[0]
	
	if x:
		return (x, (m * x) + i)
	if y:
		return ((y - i) / m, y)

vanish = make_vanish(50, 100)

def go(x, y):
	print('go')
	
	r = rect(x, y, 50, 40)
	point12(r, vanish, 25)
	
	Turtle.update()

def go1(x, y):
	print('go1')
	d = distance((x, y), vanish)
	d = 15 - (d / 50)
	
	r = rect(x, y, 50, 40)
	point1(r, vanish, 30)
	
	Turtle.update()

Turtle.listen()
Turtle.onscreenclick(go, 1, True)
Turtle.onscreenclick(go1, 3, True)
Turtle.listen()
Turtle.update()
Turtle.mainloop()
