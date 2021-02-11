#colour mixer

from tkinter import *
colours = ['#FF0000','#FFa700','#FFFF00','#00FF00','#00a7FF','#0000FF','#FF00a7']

window = Tk()
window.config(bg='black')
window.geometry(f'{49*len(colours)+5}x185')

c1 = IntVar(window,0)
c2 = IntVar(window,1)

canvas = Canvas(window,width=49*len(colours)-9,height=80,bg='black')
canvas.place(x=5,y=97)

def mix(c1,c2):
  cols = [hex((int(c1[i:i+2],16)+int(c2[i:i+2],16)+1)//2)[2:] for i in range(1,6,2)]
  for i in range(3):
    if len(cols[i]) == 1:
      cols[i] = '0'+cols[i]
  return '#'+''.join(cols)

def update():
  canvas.configure(bg=mix(colours[c1.get()],colours[c2.get()]))

for i in range(len(colours)):
  Radiobutton(window,fg=colours[i],bg=colours[i],variable=c1,value=i,borderwidth=10,command=update).place(y=5,x=i*49+5)
  Radiobutton(window,fg=colours[i],bg=colours[i],variable=c2,value=i,borderwidth=10,command=update).place(y=51,x=i*49+5)

update()
window.mainloop()
