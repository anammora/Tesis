from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root=Tk()
root.title('GALERIA')
#root.geometry('800x480')

n=0
image_list=os.listdir('/media/pi/MORAMO/GALERIA/')

#my_img1=image_list[n]
#im = Image.open('/media/pi/MORAMO/GALERIA/'+my_img1)
#ph = ImageTk.PhotoImage(im)

def ImgResize(image_number):
    #print(image_list)
    my_img1=image_list[image_number]
    ph=Image.open('/media/pi/MORAMO/GALERIA/'+my_img1)
    img=ph.resize((500,380))
    image= ImageTk.PhotoImage(img)
    return image

Img=ImgResize(n)
my_label=Label(image=Img)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label,B_forward,B_back,B_exit
    
    my_label.grid_forget()
    print(image_number)
    Img=ImgResize(image_number-1)
    my_label=Label(image=Img)
    B_forward=Button(root,text='>>',command=lambda: forward(image_number+1))
    B_back=Button(root,text='<<',command=lambda:back(image_number-1))
    
    if image_number==len(image_list):
        B_forward=Button(root,text='>>',state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    B_back.grid(row=1,column=0)
    B_exit.grid(row=1,column=1)
    B_forward.grid(row=1,column=2)

def back(image_number):
    global my_label,B_forward,B_back

    my_label.grid_forget()
    Img=ImgResize(image_number-1)
    my_label=Label(image=Img)
    B_forward=Button(root,text='>>',command=lambda: forward(image_number+1))
    B_back=Button(root,text='<<',command=lambda:back(image_number-1))

    if image_number==1:
        B_back=Button(root,text='<<',state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    B_back.grid(row=1,column=0)
    B_forward.grid(row=1,column=2)
    

B_back=Button(root,text='<<',command=back)
B_exit=Button(root,text='exit program',command=root.destroy)
B_forward=Button(root,text='>>',command=lambda:forward(2))

B_back.grid(row=1,column=0)
B_exit.grid(row=1,column=1)
B_forward.grid(row=1,column=2)

root.mainloop()


