from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import pygame


global paused
paused=False
    
def openGaleria():
    global my_label,B_forward,B_back,B_exit,rootV
    rootV=Toplevel()
    rootV.title('GALERIA')
    
    Img=ImgResize(n)
    my_label=Label(rootV,image=Img)
    my_label.grid(row=0,column=0,columnspan=3)
    
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
    
    rootV.mainloop()

    
def ImgResize(image_number):
    #print(image_list)
    my_img1=image_list[image_number]
    ph=Image.open('/media/pi/MORAMO/GALERIA/'+my_img1)
    img=ph.resize((500,350))
    image= ImageTk.PhotoImage(img)
    return image

def forward(image_number):
    global my_label,B_forward,B_back,B_exit,rootV
    
    my_label.grid_forget()
    my_label.image=ImgResize(image_number-1)
    my_img = my_label.image
    my_label=Label(rootV,image=my_img)
    
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
    global my_label,B_forward,B_back,rootV

    my_label.grid_forget()
    my_label.image=ImgResize(image_number-1)
    my_img = my_label.image
    my_label=Label(rootV,image=my_img)
    
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

def play():
    global pantalla
    cancion=pantalla.get(ACTIVE)
    cancion= f'/media/pi/MORAMO/MUSICA/{cancion}.mp3'
    #print (cancion)
    pygame.mixer.music.load(cancion)
    #pygame.mixer.music.load("/media/pi/MORAMO/MUSICA/Camilo-Ropa Cara.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    global pantalla
    pygame.mixer.music.stop()
    pantalla.selection_clear(ACTIVE)

def siguient():
    global indexCancion,proxima,pantalla,canciones
    #proxima=pantalla.curselection()
    #print(type(proxima))
    indexCancion=indexCancion+1
    proxima=(indexCancion,)
    if len(canciones)==(indexCancion):
        indexCancion=0
        proxima=(indexCancion,)
  
    cancion=pantalla.get(proxima)
    cancion=f'/media/pi/MORAMO/MUSICA/{cancion}.mp3'

    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=0)

    pantalla.selection_clear(0,END)

    pantalla.activate(proxima)

    last=None
    pantalla.selection_set(proxima,last)

def anterio():
    global indexCancion,proxima,pantalla,canciones
    
    indexCancion=indexCancion-1
    proxima=(indexCancion,)
    if (indexCancion)==-1:
        #print('hola')
        indexCancion=len(canciones)-1
        proxima=(indexCancion,)
    cancion=pantalla.get(proxima)
    cancion=f'/media/pi/MORAMO/MUSICA/{cancion}.mp3'

    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=0)

    pantalla.selection_clear(0,END)

    pantalla.activate(proxima)

    last=None
    pantalla.selection_set(proxima,last)

def pause(is_paused):
    global paused,pantalla
    is_paused=paused
    
    if paused:
        pygame.mixer.music.unpause()
        paused=False
        
    else:
        pygame.mixer.music.pause()
        paused=True

    
def NoVolum():
    pygame.mixer.music.set_volume(0)
def volum():
    pygame.mixer.music.set_volume(1.0)

def openReproductor():
    global pantalla,indexCancion,proxima,canciones
    root=Toplevel()
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    #root.rowconfigure(2, weight=1)
    root.title('Reproductor de musica')
    root.geometry('600x440')
    pygame.mixer.init()
    indexCancion=0
    proxima=(indexCancion,)
    
    pantalla=Listbox(root,bg='white',fg='black',
    selectbackground='lightblue',selectforeground='black')
    pantalla.grid(row=0,column=0,columnspan=6,sticky=S+N+E+W)
    #pantalla.pack(pady=20)


    #botones=Frame(root)
    #botones.pack()

    imgAnterior=Image.open("IMG/rewind-button.png")
    imgAnterior=imgAnterior.resize((80,80))
    imgAnterior= ImageTk.PhotoImage(imgAnterior)
    anterior=Button(root,image=imgAnterior,text='Anterior',command=anterio)
    anterior.grid(row=2,column=0,sticky=S+E+W)

    imgPlay=Image.open("IMG/play.png")
    imgPlay=imgPlay.resize((80,80))
    imgPlay= ImageTk.PhotoImage(imgPlay)
    reproducir=Button(root,image=imgPlay,text='Reproducir',command=play)
    reproducir.grid(row=2,column=1,sticky=S+E+W)

    imgPausa=Image.open("IMG/pause-button.png")
    imgPausa=imgPausa.resize((80,80))
    imgPausa= ImageTk.PhotoImage(imgPausa)
    pausa=Button(root,image=imgPausa,text='Pausa',command=lambda:pause(paused))
    pausa.grid(row=2,column=2,sticky=S+E+W)

    imgStop=Image.open("IMG/stop-button.png")
    imgStop=imgStop.resize((80,80))
    imgStop= ImageTk.PhotoImage(imgStop)
    detener=Button(root,image=imgStop,text='Detener',command=stop)
    detener.grid(row=2,column=3,sticky=S+E+W)

    imgSiguiente=Image.open("IMG/forward-button.png")
    imgSiguiente=imgSiguiente.resize((80,80))
    imgSiguiente= ImageTk.PhotoImage(imgSiguiente)
    siguiente=Button(root,image=imgSiguiente,text='Siguiente',command=siguient)
    siguiente.grid(row=2,column=4,sticky=S+E+W)

    imgVolume=Image.open("IMG/volume-button.png")
    imgVolume=imgVolume.resize((80,80))
    imgVolume= ImageTk.PhotoImage(imgVolume)
    volume=Button(root,image=imgVolume,text='Volumen',command=volum)
    volume.grid(row=2,column=5,sticky=S+E+W)

    imgMute=Image.open("IMG/no-sound.png")
    imgMute=imgMute.resize((80,80))
    imgMute= ImageTk.PhotoImage(imgMute)
    NoVolume=Button(root,image=imgMute,text='NoVolumen',command=NoVolum)
    NoVolume.grid(row=2,column=6,sticky=S+E+W)

    menubar=Menu(root)
    root.config(menu=menubar)


    canciones=os.listdir('/media/pi/MORAMO/MUSICA/')
    #print(canciones)
    for cancion in canciones:
        #cancion=cancion.replace("/media/pi/MORAMO/MUSICA/","") 
        cancion=cancion.replace(".mp3","")
        pantalla.insert(END, cancion)
        
    root.mainloop()
    


def run():
    global ventana,n,image_list
    #print("nos diga algo")
    
    ventana=Tk()
    ventana.columnconfigure(1, weight=5)
    ventana.columnconfigure(2, weight=5)
    ventana.columnconfigure(3, weight=2)
    ventana.columnconfigure(4, weight=5)
    ventana.columnconfigure(5, weight=2)
    ventana.rowconfigure(0, weight=15)
    ventana.rowconfigure(1, weight=1)
    ventana.rowconfigure(2, weight=20)
    ventana.title("Elige una opcion")
    ventana.geometry("800x480")#Cambiar el nombre de la ventana
    n=0
    image_list=os.listdir('/media/pi/MORAMO/GALERIA/')
    
    
    
    imgF=Image.open("IMG/gallery.png")
    imgF=imgF.resize((100,100))
    imgF= ImageTk.PhotoImage(imgF)
    galeria=Button(ventana,image=imgF,text='Galeria',command=openGaleria)
    galeria.grid(row=2,column=2,sticky=N)

    imgM=Image.open("IMG/music.png")
    imgM=imgM.resize((100,100))
    imgM= ImageTk.PhotoImage(imgM)
    reproductor=Button(ventana,image=imgM,text='Reproductor',command=openReproductor)
    reproductor.grid(row=2,column=4,sticky=N)

        
    imgH=Image.open("IMG/home.png")
    imgH=imgH.resize((50,50))
    imgH= ImageTk.PhotoImage(imgH)
    Home=Button(ventana,image=imgH,text='Home',command=ventana.destroy)
    Home.grid(row=0,column=5,sticky=N+E)

    Musica=Label(ventana,text="MÚSICA",font=("Helvetica", 18,"bold"))
    Musica.grid(row=1,column=4,sticky=S)

    Galeria=Label(ventana,text="GALERIA",font=("Helvetica", 18,"bold"))
    Galeria.grid(row=1,column=2,sticky=S)
    
    ventana.mainloop()


