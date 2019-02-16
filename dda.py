from graphics import *
import time
def day2():
	win = GraphWin("DDA LINE DRAWING",800,800)
	t1 = Text(Point(200,50), "DDA LINE DRAWING ALGORITHM")
	t1.draw(win)
	t1.setOutline("Orange")
	pt1=win.getMouse()
	pt2=win.getMouse()
	x1=pt1.x
	y1=pt1.y
	x2=pt2.x
	y2=pt2.y
	dx=x2-x1
	dy=y2-y1
	#m=dy/dx
	#print(m)
	if abs(dx)>abs(dy): 
		s=abs(dx)
	else:
		s=abs(dy)
			
	xinc=dx/s
	yinc=dy/s
	pt=Point(x1,y1)
	pt.draw(win)

	for y in range(int(s)):
				x1=x1+xinc
				y1=y1+yinc
				p1=Point(int(x1+0.5),int(y1+0.5))
				p1.setFill('blue')
				p1.draw(win)
				time.sleep(0.05)

	win.getMouse()
day2()
