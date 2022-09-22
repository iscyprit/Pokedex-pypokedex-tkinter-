from turtle import color
import pypokedex
from tkinter import *
from tkinter.ttk import Entry
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

root = Tk()
root.title('Pokedex')

pt = True
x = 0

def Search(event):
    p = pypokedex.get(name=e.get())
    if len(p.types) < 2:
        L2 = Label(root, text=('Type - '+p.types[0]), width=30)
    if len(p.types) == 2:
        L2 = Label(root, text=('Type - '+p.types[0]+ ', '+p.types[1]), width=30)
    L2.grid(row=3, column=0)
    
    #region Base Stats
    s=Label(root,text='HP')
    s.grid(row=4,column=0)
    s=Label(root,text='Atk.')
    s.grid(row=5,column=0)
    s=Label(root,text='Def.')
    s.grid(row=6,column=0)
    s=Label(root,text='Sp.Atk.')
    s.grid(row=7,column=0)
    s=Label(root,text='Sp.Def.')
    s.grid(row=8,column=0)
    s=Label(root,text='Speed')
    s.grid(row=9,column=0)

    pb = ttk.Progressbar(root,orient='horizontal', length=200, maximum=255, value=p.base_stats[0])
    pb.grid(row=4,column=1)
    pb = ttk.Progressbar(root,orient='horizontal', length=200, maximum=255, value=p.base_stats[1])
    pb.grid(row=5,column=1)
    pb = ttk.Progressbar(root,orient='horizontal', length=200, maximum=255, value=p.base_stats[2])
    pb.grid(row=6,column=1)
    pb = ttk.Progressbar(root,orient='horizontal', length=200, maximum=255, value=p.base_stats[3])
    pb.grid(row=7,column=1)
    pb = ttk.Progressbar(root,orient='horizontal', length=200, maximum=255, value=p.base_stats[4])
    pb.grid(row=8,column=1)
    pb = ttk.Progressbar(root,orient='horizontal', length=200, maximum=255, value=p.base_stats[5])
    pb.grid(row=9,column=1)

    t=Label(root, text=p.base_stats[0])
    t.grid(row=4,column=2)
    t=Label(root, text=p.base_stats[1])
    t.grid(row=5,column=2)
    t=Label(root, text=p.base_stats[2])
    t.grid(row=6,column=2)
    t=Label(root, text=p.base_stats[3])
    t.grid(row=7,column=2)
    t=Label(root, text=p.base_stats[4])
    t.grid(row=8,column=2)
    t=Label(root, text=p.base_stats[5])
    t.grid(row=9,column=2)
    #endregion

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
    
root.bind('<Return>',Search)
    
e = Entry(root, width=41)
e.grid(row=0, column=0)

root.mainloop()

