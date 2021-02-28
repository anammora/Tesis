from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import pygame
import os

root=Tk()
root.title('GALERIA')
root.geometry('800x480')
#img = PhotoImage(file='/media/pi/MORAMO/')
#root.tk.call('wm', 'iconphoto', root._w, img)
#root.iconphoto('/media/pi/MORAMO.ico')
imagenes=os.listdir('/media/pi/MORAMO/GALERIA/')
print(imagenes)
for imagen in imagenes:
    imagen=Image.open("IMG/no-sound.png")
    imagen=imagen.resize((700,380))
    imagen= ImageTk.PhotoImage(imagen)
    
    pantalla.insert(END, cancion)
my_img1=ImageTk.PhotoImage(Image.open('/media/pi/MORAMO/GALERIA/img1.jpeg'))
my_img2=ImageTk.PhotoImage(Image.open('/media/pi/MORAMO/GALERIA/img2.jpeg'))
my_img3=ImageTk.PhotoImage(Image.open('/media/pi/MORAMO/GALERIA/img3.jpeg'))
my_img4=ImageTk.PhotoImage(Image.open('/media/pi/MORAMO/GALERIA/img4.jpeg'))
my_img5=ImageTk.PhotoImage(Image.open('/media/pi/MORAMO/GALERIA/img5.jpeg'))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label,B_forward,B_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    B_forward=Button(root,text='>>',command=lambda: forward(image_number+1))
    B_back=Button(root,text='<<',command=lambda:back(image_number-1))

    if image_number==len(image_list):
        B_forward=Button(root,text='>>',state=DISABLE)

    my_label.grid(row=0,column=0,columnspan=3)
    B_back.grid(row=1,column=0)
    B_forward.grid(row=1,column=2)

def back(image_number):
    global my_label,B_forward,B_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    B_forward=Button(root,text='>>',command=lambda: forward(image_number+1))
    B_back=Button(root,text='<<',command=lambda:back(image_number-1))

    if image_number==1:
        B_back=Button(root,text='<<',state=DISABLE)

    my_label.grid(row=0,column=0,columnspan=3)
    B_back.grid(row=1,column=0)
    B_forward.grid(row=1,column=2)

B_back=Button(root,text='<<',command=back)
B_exit=Button(root,text='exit program',command=root.quit)
B_forward=Button(root,text='>>',command=lambda:forward(2))

B_back.grid(row=1,column=0)
B_exit.grid(row=1,column=1)
B_forward.grid(row=1,column=2)

root.mainloop()


