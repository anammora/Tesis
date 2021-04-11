from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os


rootV=Tk()
rootV.title('GALERIA')
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
    img=ph.resize((500,350))
    image= ImageTk.PhotoImage(img)
    return image


Img=ImgResize(n)
my_label=Label(image=Img)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label,B_forward,B_back,B_exit
    
    my_label.grid_forget()
    my_label.image=ImgResize(image_number-1)
    my_img = my_label.image
    my_label=Label(image=my_img)
    
    imgSiguiente=Image.open("IMG/forward-button.png")
    imgSiguiente=imgSiguiente.resize((50,50))
    imgSiguiente= ImageTk.PhotoImage(imgSiguiente)
    B_forward.image=imgSiguiente
    imgS=B_forward.image

    B_forward=Button(rootV,text='>>',image=imgS,
                     command=lambda: forward(image_number+1))
    
    imgAnterior=Image.open("IMG/rewind-button.png")
    imgAnterior=imgAnterior.resize((50,50))
    imgAnterior= ImageTk.PhotoImage(imgAnterior)
    B_back.image=imgAnterior
    imgA=B_back.image

    B_back=Button(rootV,text='<<',image=imgA,
                  command=lambda:back(image_number-1))
    
    if image_number==len(image_list):
        B_forward=Button(rootV,image=imgS,text='>>',state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    B_back.grid(row=1,column=0,rowspan=2)
    B_forward.grid(row=1,column=2,rowspan=2)
    

def back(image_number):
    global my_label,B_forward,B_back

    my_label.grid_forget()
    my_label.image=ImgResize(image_number-1)
    my_img = my_label.image
    my_label=Label(image=my_img)
    
    imgSiguiente=Image.open("IMG/forward-button.png")
    imgSiguiente=imgSiguiente.resize((50,50))
    imgSiguiente= ImageTk.PhotoImage(imgSiguiente)
    B_forward.image=imgSiguiente
    imgS=B_forward.image
    
    B_forward=Button(rootV,image=imgS,text='>>',command=lambda: forward(image_number+1))
    
    imgAnterior=Image.open("IMG/rewind-button.png")
    imgAnterior=imgAnterior.resize((50,50))
    imgAnterior= ImageTk.PhotoImage(imgAnterior)
    
    B_back.image=imgAnterior
    imgA=B_back.image
    
    B_back=Button(rootV,image=imgA,text='<<',
                  command=lambda:back(image_number-1))

    if image_number==1:
        B_back=Button(rootV,image=imgA,text='<<',state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    B_back.grid(row=1,column=0,rowspan=2)
    B_forward.grid(row=1,column=2,rowspan=2)
   
imgAnterior=Image.open("IMG/rewind-button.png")
imgAnterior=imgAnterior.resize((50,50))
imgAnterior= ImageTk.PhotoImage(imgAnterior)
B_back=Button(rootV,image=imgAnterior,text='<<',command=back,state=DISABLED)

imgHome=Image.open("IMG/home.png")
imgHome=imgHome.resize((50,50))
imgHome= ImageTk.PhotoImage(imgHome)

B_exit=Button(rootV,image=imgHome,text='exit program',command=rootV.destroy)


imgSiguiente=Image.open("IMG/forward-button.png")
imgSiguiente=imgSiguiente.resize((50,50))
imgSiguiente= ImageTk.PhotoImage(imgSiguiente)
B_forward=Button(rootV,image=imgSiguiente,text='>>',command=lambda:forward(2))

B_back.grid(row=1,column=0,rowspan=2)
B_exit.grid(row=1,column=1,rowspan=2)
B_forward.grid(row=1,column=2,rowspan=2)

def run():
    rootV.mainloop()
    
def destroy():
    rootV.destroy()
    


