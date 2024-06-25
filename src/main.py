from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.draw(150, 50, 200, 100)

    c1.draw_move(c2)

    win.wait_for_close()

main()