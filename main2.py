import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os
import pyperclip

root = Tk()
root.title('Detector de cores')
root.geometry('800x470+100+100')
root.configure(bg='#E3E1D9')
root.resizable(False, False)

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetypes=[('PNG file', '*.png'), ('JPG file', '*.jpg'), ('ALL Files', '*.*')])

    img = Image.open(filename)

    #tamanho do label
    label_width = 295
    label_height = 280

    # Calcula dimensões mantendo a proporção
    img_width, img_height = img.size
    ratio = min(label_width / img_width, label_height / img_height)
    new_width = int(img_width * ratio)
    new_height = int(img_height * ratio)


    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img

    # Centraliza a imagem no Label
    lbl.place(relx=0.5, rely=0.5, anchor="center")

# laço for para criar retângulos e rótulos em branco
def create_empty_rectangles(canvas, num_colors=5):
    rectangles = []
    hex_labels = []

    for i in range(num_colors):
        y_position = 10 + i * 50
        # retângulo em branco
        rect_id = canvas.create_rectangle((10, y_position, 50, y_position + 40), fill="white")
        rectangles.append(rect_id)
        
        # rótulo sem texto
        hex_label = Label(canvas, text="", fg='#000', font='arial 12 bold', bg='white')
        hex_label.place(x=55, y=y_position + 5)
        hex_labels.append(hex_label)
    
    return rectangles, hex_labels

# Função para copiar os códigos hexadecimais
def copy_hex_codes():
    hex_codes = []
    for label in hex_labels1 + hex_labels2:
        hex_codes.append(label.cget("text"))  # Pega o texto de cada rótulo
    hex_text = "\n".join(hex_codes)  # Junta os códigos em uma única string
    pyperclip.copy(hex_text)  # Copia para a área de transferência

# icon
icone_img = PhotoImage(file='icons8-rgb-70.png')
root.iconphoto(False, icone_img)

Label(root,width=120, height=10,bg='#C7C8CC').pack()

# frame
frame = Frame(root, width=700, height=370, bg='#F2EFE5')
frame.place(x=50, y=50)

logo = PhotoImage(file='icons8-rgb-70.png') #size 100x100px
Label(frame, image=logo, bg='#F2EFE5').place(x=15, y=16)
Label(frame, text='Detector de cores', font='arial 20 bold', bg='#F2EFE5').place(x=95, y=35)

#cor1
cores = Canvas(frame, bg='#fff', width=150, height=260, bd = 0)
cores.place(x=15, y=93)

#cores 2
cores2 = Canvas(frame, bg='#fff', width=150, height=260, bd=0)
cores2.place(x=193, y=93)

# Função para detectar e exibir as cores
def findcolor():
    color_thief = ColorThief(filename)
    palette = color_thief.get_palette(color_count=11)

    # Converte as cores para hexadecimal
    colors = [f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}' for rgb in palette[:10]]

    # Preenche os retângulos e rótulos com as cores detectadas
    for i, color in enumerate(colors[:5]):  # Primeira coluna (5 cores)
        cores.itemconfig(box_color1[i], fill=color)
        hex_labels1[i].config(text=color)
    
    for i, color in enumerate(colors[5:10]):  # Segunda coluna (5 cores)
        cores2.itemconfig(box_color2[i], fill=color)
        hex_labels2[i].config(text=color)

box_color1, hex_labels1 = create_empty_rectangles(cores)
box_color2, hex_labels2 = create_empty_rectangles(cores2)


# select image
select_image = Frame(frame, width=313, height=337, bg = '#d6dee5')
select_image.place(x=370, y=16)

f = Frame(select_image, bd = 3, bg = '#B4B4B8', width= 295, height= 280, relief= GROOVE)
f.place(x=10, y=10)

lbl = Label(f, bg= '#B4B4B8')
lbl.place(x=0, y=0)

# botoes
Button(select_image, text='Select Image', width=10, height=1, font = 'arial 14 bold', command=showimage).place(x=10, y=295)
Button(select_image, text='Find 🔎', width=6, height=1, font='arial 14 bold', command=findcolor).place(x=145, y=295)
Button(select_image, text='Copy', width=5, height=1, font='arial 14 bold', command=copy_hex_codes).place(x=233, y=295)

root.mainloop()