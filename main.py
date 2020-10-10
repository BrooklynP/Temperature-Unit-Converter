from tkinter import *

root = Tk()
root.config(bg = '#000')
c = StringVar()
f = StringVar()

def ctof():
    cel1 = int(cel_entry.get())
    far1 = (cel1*1.8)+32
    f.set(far1)

def ftoc():
    far2 = int(far_entry.get())
    cel2 = (far2 - 32)/1.8
    c.set(cel2)    

lbl_Celsius = Label(root, text='Celsius' ,fg = '#ffbf00')
lbl_Far = Label(root, text='Farh....')
lbl_Kev = Label(root, text = 'Kelvin')
cel_entry = Entry(root, textvariable = c)
far_entry = Entry(root, textvariable = f)
kev_entry = Entry(root)
btn_Convert = Button(root, text='Convert', bg='#ffaa00', command = convert)

lbl_Celsius.grid(row=0)
lbl_Far.grid(row=1)
lbl_Kev.grid(row = 2)
cel_entry.grid(row = 0, column = 1)
far_entry.grid(row = 1, column = 1)
kev_entry.grid(row = 2, column = 1)
btn_Convert.grid(row = 3, columnspan = 2)