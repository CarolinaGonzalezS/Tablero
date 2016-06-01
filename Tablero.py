from tkinter import *

root = Tk()
root.title('Tabllero Ajedrez')

canvas=Canvas(width=550, height=550, bg='red')
canvas.pack(expand=YES, fill=BOTH)
#PRIMERA FILA
canvas.create_line(0, 25, 550, 25, width=50, fill='black')
canvas.create_line(50, 25, 100, 25, width=50, fill='white')
canvas.create_line(150, 25, 200, 25, width=50, fill='white')
canvas.create_line(250, 25, 300, 25, width=50, fill='white')
canvas.create_line(350, 25, 400, 25, width=50, fill='white')
canvas.create_line(450, 25, 500, 25, width=50, fill='white')
#SEGUNDA FILA
canvas.create_line(0, 75, 550, 75, width=50, fill='white')
canvas.create_line(50, 75, 100, 75, width=50, fill='black')
canvas.create_line(150, 75, 200, 75, width=50, fill='black')
canvas.create_line(250, 75, 300, 75, width=50, fill='black')
canvas.create_line(350, 75, 400, 75, width=50, fill='black')
canvas.create_line(450, 75, 500, 75, width=50, fill='black')
