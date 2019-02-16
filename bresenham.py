from graphics import *
import time
def day1():
	win = GraphWin("MyWindow",800,800)
	
	pt1=win.getMouse()
	pt2=win.getMouse()
	x1=pt1.x
	y1=pt1.y
	x2=pt2.x
	y2=pt2.y
	m=((y2-y1)/(x2-x1))
	print(m)
	dx=abs(x2-x1)
	dy=abs(y2-y1)
	p=(2*dy)-dx
	pt1=Point(x1,y1)
	pt1.draw(win)
	
	while(x1<=x2):
		x1=x1+1
		if(p<0):
			p=p+(2*dy)
		else:
			y1=y1+1
			p=p+(2*dy)-(2*dx)
		pt=Point(x1,y1)
		pt.draw(win)
		time.sleep(0.05)
	win.getMouse()
day1()
