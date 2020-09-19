
import tkinter as tk
h = 700
w = 700

root = tk.Tk()

canvas = tk.Canvas(root, height = h, width = w)
canvas.pack()

frame = tk.Frame(root, bg='purple')
frame.place(relwidth=1, relheight=1)

entry = tk.Entry(frame, bg='yellow')
entry.pack(side='left')

            

button = tk.Button(frame, text ='text button', bg= 'purple', fg='purple')
button.pack()

root.mainloop()
