# Module 7
#   Programming Assignment 10
#     Prob-5.py

# Ilya Panasevich

from graphics import *

def main():
    win = GraphWin("Event Loop", 500, 500)
    p1 = win.getMouse()
    circ = Circle(p1, 20)
    circ.draw(win)
    count = 1
    endFlag = False
    
    input()

main()    