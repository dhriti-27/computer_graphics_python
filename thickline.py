from graphics import *
import math
def main():
    win = GraphWin("DDA",500,500)

    t=Text(Point(60,60),'simple_dda')
    t.draw(win)
    win.setBackground(color_rgb(23,230,250))
    win.setCoords(-500,500,500,-500)
    Line(Point(-500,0),Point(500,0)).draw(win)
    Line(Point(0,500),Point(0,-500)).draw(win)
    
    
    def dda():
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
        m=dy/dx
        print(m)
        c=ay-m*(ax)
        print(c)
        
        t=10
        
        if abs(dx)>abs(dy):
            len=abs(dx)
        else:
            len=abs(dy)

        xinc = (dx/float(len))
        yinc = (dy/float(len))




        pt=Point(ax,ay)
        pt.setOutline('pink')
        pt.draw(win)
        ax2=ax
        ay2=ay
        ax1=ax
        ay1=ay



        for i in range(int(len)):
            ax2=ax2+xinc
            ay2=ay2+yinc
            pt=Point(int(ax2),int(ay2))
            pt.setOutline('pink')
            pt.draw(win)
            print(int(ax2),int(ay2))
        
        print(ax1,ay1)
        for k in range(int(t)):
             c2 = c + k
             ay1 = ay + k
             ax1 = ax - (k/m)
             for j in range(int(len)):
                ax1=ax1+xinc
                ay1=ay1+yinc
                pt=Point(int(ax1),int(ay1))
                pt.setOutline('pink')
                pt.draw(win)
                print(int(ax1),int(ay1))  
        dda()
    dda()

    win.getMouse()
    
main()
