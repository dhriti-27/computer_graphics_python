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
        print(dx,dy)
        
        k=(math.log10(max(dx,dy)))/math.log10(2)
        k=math.ceil(k)
        temp=pow(2,k)
        len=temp
        print(k)
         

        xinc=dx/temp
        yinc=dy/temp



        xinc=(dx/float(len))
        yinc=(dy/float(len))

        pt=Point(ax,ay)
        pt.setOutline('pink')
        pt.draw(win)

        for i in range(int(len)):
            ax=ax+xinc
            ay=ay+yinc
            pt=Point(int(ax),int(ay))
            pt.setOutline('pink')
            pt.draw(win)
            print(int(ax),int(ay))
            
        dda()
    dda()

    win.getMouse()
    
main()
