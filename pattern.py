#Simple DDA Algorithm 
from graphics import *
import math
 
def main():
    win=GraphWin('Simple_DDA',500,500)
    t=Text(Point(50,50),'Simple_DDA')
    t.draw(win)

    win.setCoords(-500.0, -500.0, 500.0, 500.0)
    # Draw vertical lines
    Line(Point(-500,0), Point(500,0)).draw(win)
    # Draw horizontal lines
    Line(Point(0,-500), Point(0,500)).draw(win)
    def dda():
        # Initialising hex string
        temp = "90C"
        temp  =  temp * 10000
        
        res = "{0:08b}".format(int(temp , 16))

        p1=win.getMouse()
        p1.draw(win)
        p2=win.getMouse()
        p2.draw(win)

        ax=p1.x
        ay=p1.y
        bx=p2.x
        by=p2.y
        print(ax,ay,bx,by)

        dx=bx-ax
        dy=by-ay
        print(dx,dy)

        if abs(dx)>abs(dy):
            len=abs(dx)
        else:
            len=abs(dy)

        xinc = (dx/float(len))
        yinc = (dy/float(len))

        pt=Point(ax,ay)
        pt.setOutline('pink')
        pt.draw(win)
        ax1 = ax
        ay1 = ay

        for i in range(int(len)):
            ax=ax+xinc
            ay=ay+yinc
            ax1=ax+xinc
            ay1=ay+yinc
            print(res[i],temp[i])
            if res[i] == '1':
                pt=Point(int(ax),int(ay))
                pt.setOutline('pink')
                pt.draw(win)
                print(int(ax),int(ay))
            else:
                continue
        dda()
    dda()

    win.getMouse()

main()