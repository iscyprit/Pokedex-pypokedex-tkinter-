from tkinter import *
from PIL import Image,ImageTk
import pypokedex
from urllib.request import urlopen
from io import BytesIO



root = Tk()
root.title("Pokedex")

pt = True
x = 0

def Search(event):
    p = pypokedex.get(name=e.get())
    L1 = Label(root, text=(f'ID - {p.dex}'))
    L1.grid(row=1,column=0)
    if len(p.types) < 2:
        L2 = Label(root, text=('Type - '+p.types[0]))
    if len(p.types) == 2:
        L2 = Label(root, text=('Type - '+p.types[0]+ ', '+p.types[1]))
    L2.grid(row=2,column=0)
    L3 = Label(root, text=('Height - '+str(p.height*10)+'cm'))
    L3.grid(row=3,column=0)
    L4 = Label(root, text=('Weight - '+str(p.weight/10)+'kg'))
    L4.grid(row=4,column=0)

    # read, show, change
    URL = p.sprites[0]['default']
    u = urlopen(URL)
    global raw_data
    raw_data = u.read()
    u.close()

    global x
    global pt
    
    if pt == True:
        x= x+1
        im = Image.open(BytesIO(raw_data)).convert('RGBA')
        photo = ImageTk.PhotoImage(im)
        global label
        label = Label(image=photo)
        label.image = photo
        label.grid()
        e.delete(0, END)
    if x > 0:
        pt = False
    if pt == False:
        img2 = Image.open(BytesIO(raw_data)).convert('RGBA')
        photo1 = ImageTk.PhotoImage(img2)
        label.configure(image=photo1)
        label.image = photo1
        e.delete(0, END)
    
root.bind('<Return>',Search)
    
e = Entry(root, width=41)
e.grid(row=0, column=0)

root.mainloop()
