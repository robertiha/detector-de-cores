import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

root = Tk()
root.title('Detector de cores')
root.geometry('800x470+100+100')
root.configure(bg='#E3E1D9')
root.resizable(False, False)

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetypes=[('PNG file', '*.png'), ('JPG file', '*.jpg'), ('ALL Files', '*.*')])

    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=295, height=280)
    lbl.image=img

def findcolor():
    color_thief = ColorThief(filename)
    palette = color_thief.get_palette(color_count=11)

    rgb1 = palette[0]
    rgb2 = palette[1]
    rgb3 = palette[2]
    rgb4 = palette[3]
    rgb5 = palette[4]
    rgb6 = palette[5]
    rgb7 = palette[6]
    rgb8 = palette[7]
    rgb9 = palette[8]
    rgb10 = palette[9]


    cor1  = f'#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}'
    cor2  = f'#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}'
    cor3  = f'#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}'
    cor4  = f'#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}'
    cor5  = f'#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}'
    cor6  = f'#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}'
    cor7  = f'#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}'
    cor8  = f'#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}'
    cor9  = f'#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}'
    cor10 = f'#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}'

    """
    - rgb[0], rgb[1], rgb[2] representam oas valores de RGB -> vermelho, verde e azul
    - :02x significa:
        - x --> converte um número inteiro em hexadecimal
        - 02 -> garante que o número terá pelo menos dois dígitos, 
                preenchendo com zero à esquerda, se necessário
    """

    cores.itemconfig(id1, fill=cor1)
    cores.itemconfig(id2, fill=cor2)
    cores.itemconfig(id3, fill=cor3)
    cores.itemconfig(id4, fill=cor4)
    cores.itemconfig(id5, fill=cor5)
    cores2.itemconfig(id6, fill=cor6)
    cores2.itemconfig(id7, fill=cor7)
    cores2.itemconfig(id8, fill=cor8)
    cores2.itemconfig(id9, fill=cor9)
    cores2.itemconfig(id10, fill=cor10)

    hex1.config(text=cor1)
    hex2.config(text=cor2)
    hex3.config(text=cor3)
    hex4.config(text=cor4)
    hex5.config(text=cor5)
    hex6.config(text=cor6)
    hex7.config(text=cor7)
    hex8.config(text=cor8)
    hex9.config(text=cor9)
    hex10.config(text=cor10)


# icon
icone_img = PhotoImage(file='icons8-rgb-70.png')
root.iconphoto(False, icone_img)

Label(root,width=120, height=10,bg='#C7C8CC').pack()

# frame
frame = Frame(root, width=700, height=370, bg='#F2EFE5')
frame.place(x=50, y=50)

logo = PhotoImage(file='icons8-rgb-70.png') #size 100x100px
Label(frame, image=logo, bg='#F2EFE5').place(x=15, y=16)

Label(frame, text='Detector de cor', font='arial 25 bold', bg='#F2EFE5').place(x=90, y=30) #ver depois

#cor1
cores = Canvas(frame, bg='#fff', width=150, height=260, bd = 0)
cores.place(x=15, y=93)

id1 = cores.create_rectangle((10,10,50,50),fill = "#b8255f")
id2 = cores.create_rectangle((10,60,50,100),fill = "#B1F0F7")
id3 = cores.create_rectangle((10,110,50,150),fill = "#81BFDA")
id4 = cores.create_rectangle((10,160,50,200),fill = "#F5F0CD")
id5 = cores.create_rectangle((10,210,50,250),fill = "#FADA7A")


hex1 = Label(cores, text = '#b8255f', fg='#000', font = 'arial 12 bold', bg = 'white')
hex1.place(x=55, y=20)
hex2 = Label(cores, text = '#B1F0F7', fg='#000', font = 'arial 12 bold', bg = 'white')
hex2.place(x=55, y=70)
hex3 = Label(cores, text = '#81BFDA', fg='#000', font = 'arial 12 bold', bg = 'white')
hex3.place(x=55, y=120)
hex4 = Label(cores, text = '#F5F0CD', fg='#000', font = 'arial 12 bold', bg = 'white')
hex4.place(x=55, y=170)
hex5 = Label(cores, text = '#FADA7A', fg='#000', font = 'arial 12 bold', bg = 'white')
hex5.place(x=55, y=220)

# Segunda coluna de cores
cores2 = Canvas(frame, bg='#fff', width=150, height=260, bd=0)
cores2.place(x=193, y=93)  # Movemos para a direita (de 20 para 110)

id6 = cores2.create_rectangle((10, 10, 50, 50), fill="#FBF5E5")
id7 = cores2.create_rectangle((10, 60, 50, 100), fill="#C890A7")
id8 = cores2.create_rectangle((10, 110, 50, 150), fill="#A35C7A")
id9 = cores2.create_rectangle((10, 160, 50, 200), fill="#F5F0CD")
id10 = cores2.create_rectangle((10, 210, 50, 250), fill="#212121")

hex6 = Label(cores2, text="#FBF5E5", fg="#000", font="arial 12 bold", bg="white")
hex6.place(x=55, y=20)  # Movemos para direita e alinhamos à esquerda
hex7 = Label(cores2, text="#C890A7", fg="#000", font="arial 12 bold", bg="white")
hex7.place(x=55, y=70)
hex8 = Label(cores2, text="#A35C7A", fg="#000", font="arial 12 bold", bg="white")
hex8.place(x=55, y=120)
hex9 = Label(cores2, text="#F5F0CD", fg="#000", font="arial 12 bold", bg="white")
hex9.place(x=55, y=170)
hex10 = Label(cores2, text="#212121", fg="#000", font="arial 12 bold", bg="white")
hex10.place(x=55, y=220)


# select image
select_image = Frame(frame, width=313, height=337, bg = '#d6dee5')
select_image.place(x=370, y=16)

f = Frame(select_image, bd = 3, bg = 'black', width= 295, height= 280, relief= GROOVE)
f.place(x=10, y=10)

lbl = Label(f, bg= 'black')
lbl.place(x=0, y=0)

Button(select_image, text='Select Image', width=12, height=1, font = 'arial 14 bold', command=showimage).place(x=10, y=295)
Button(select_image, text='Find Colors', width=10, height=1, font='arial 14 bold', command=findcolor).place(x=175, y=295)


root.mainloop()