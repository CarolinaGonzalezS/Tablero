from tkinter import *

root = Tk()
root.title('Tabllero Ajedrez')

canvas=Canvas(width=550, height=550, bg='red')
canvas.pack(expand=YES, fill=BOTH)
#PRIMERA FILA
canvas.create_line(0, 25, 400, 25, width=50, fill='white')
canvas.create_line(50, 25, 100, 25, width=50, fill='black')
canvas.create_line(150, 25, 200, 25, width=50, fill='black')
canvas.create_line(250, 25, 300, 25, width=50, fill='black')
canvas.create_line(350, 25, 400, 25, width=50, fill='black')
#SEGUNDA FILA
canvas.create_line(0, 75, 400, 75, width=50, fill='black')
canvas.create_line(50, 75, 100, 75, width=50, fill='white')
canvas.create_line(150, 75, 200, 75, width=50, fill='white')
canvas.create_line(250, 75, 300, 75, width=50, fill='white')
canvas.create_line(350, 75, 400, 75, width=50, fill='white')
#TERCEERA FILA
canvas.create_line(0, 125, 400, 125, width=50, fill='white')
canvas.create_line(50, 125, 100, 125, width=50, fill='black')
canvas.create_line(150, 125, 200, 125, width=50, fill='black')
canvas.create_line(250, 125, 300, 125, width=50, fill='black')
canvas.create_line(350, 125, 400, 125, width=50, fill='black')
#CUARTA FILA
canvas.create_line(0, 175, 400, 175, width=50, fill='black')
canvas.create_line(50, 175, 100, 175, width=50, fill='white')
canvas.create_line(150, 175, 200, 175, width=50, fill='white')
canvas.create_line(250, 175, 300, 175, width=50, fill='white')
canvas.create_line(350, 175, 400, 175, width=50, fill='white')
#QUINTA FILA
canvas.create_line(0, 225, 400, 225, width=50, fill='white')
canvas.create_line(50, 225, 100, 225, width=50, fill='black')
canvas.create_line(150, 225, 200, 225, width=50, fill='black')
canvas.create_line(250, 225, 300, 225, width=50, fill='black')
canvas.create_line(350, 225, 400, 225, width=50, fill='black')
#SEXTA FILA
canvas.create_line(0, 275, 400, 275, width=50, fill='black')
canvas.create_line(50, 275, 100, 275, width=50, fill='white')
canvas.create_line(150, 275, 200, 275, width=50, fill='white')
canvas.create_line(250, 275, 300, 275, width=50, fill='white')
canvas.create_line(350, 275, 400, 275, width=50, fill='white')
#SEPTIMA FILA
canvas.create_line(0, 325, 400, 325, width=50, fill='white')
canvas.create_line(50, 325, 100, 325, width=50, fill='black')
canvas.create_line(150, 325, 200, 325, width=50, fill='black')
canvas.create_line(250, 325, 300, 325, width=50, fill='black')
canvas.create_line(350, 325, 400, 325, width=50, fill='black')
#OCTAVA FILA
canvas.create_line(0, 375, 400, 375, width=50, fill='black')
canvas.create_line(50, 375, 100, 375, width=50, fill='white')
canvas.create_line(150, 375, 200, 375, width=50, fill='white')
canvas.create_line(250, 375, 300, 375, width=50, fill='white')
canvas.create_line(350, 375, 400, 375, width=50, fill='white')

