from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import pygame
import os


root=Tk()
root.title('Reproductor de musica')
root.geometry('800x480')
pygame.mixer.init()
indexCancion=0
proxima=(indexCancion,)

      
def play():
    cancion=pantalla.get(ACTIVE)
    cancion= f'/media/pi/MORAMO/MUSICA/{cancion}.mp3'
    #print (cancion)
    pygame.mixer.music.load(cancion)
    #pygame.mixer.music.load("/media/pi/MORAMO/MUSICA/Camilo-Ropa Cara.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    pantalla.selection_clear(ACTIVE)

def siguiente():
    global indexCancion,proxima
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

def anterior():
    global indexCancion,proxima
    
    indexCancion=indexCancion-1
    proxima=(indexCancion,)
    if (indexCancion)==-1:
        print('hola')
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
    
global paused
paused=False

def pause(is_paused):
    global paused
    is_paused=paused
    
    if paused:
        pygame.mixer.music.unpause()
        paused=False
        
    else:
        pygame.mixer.music.pause()
        paused=True

    
def NoVolume():
    pygame.mixer.music.set_volume(0)
def volume():
    pygame.mixer.music.set_volume(1.0)    
    
    

pantalla=Listbox(root,bg='white',fg='black', height=15,width=80,
selectbackground='white',selectforeground='black')    
pantalla.pack(pady=20)

botones=Frame(root)
botones.pack()

imgAnterior=Image.open("IMG/rewind-button.png")
imgAnterior=imgAnterior.resize((90,90))
imgAnterior= ImageTk.PhotoImage(imgAnterior)
anterior=Button(botones,height=80,width=80,image=imgAnterior,text='Anterior',command=anterior)
anterior.grid(row=0,column=0)

imgPlay=Image.open("IMG/play.png")
imgPlay=imgPlay.resize((80,80))
imgPlay= ImageTk.PhotoImage(imgPlay)
reproducir=Button(botones,height=80,width=80,image=imgPlay,text='Reproducir',command=play)
reproducir.grid(row=0,column=1)

imgPausa=Image.open("IMG/pause-button.png")
imgPausa=imgPausa.resize((80,80))
imgPausa= ImageTk.PhotoImage(imgPausa)
pausa=Button(botones,height=80,width=80,image=imgPausa,text='Pausa',command=lambda:pause(paused))
pausa.grid(row=0,column=2)

detener=Button(botones,text='Detener',command=stop)
detener.grid(row=0,column=3)

imgSiguiente=Image.open("IMG/forward-button.png")
imgSiguiente=imgSiguiente.resize((80,80))
imgSiguiente= ImageTk.PhotoImage(imgSiguiente)
siguiente=Button(botones,height=80,width=80,image=imgSiguiente,text='Siguiente',command=siguiente)
siguiente.grid(row=0,column=4)

imgVolume=Image.open("IMG/volume-button.png")
imgVolume=imgVolume.resize((80,80))
imgVolume= ImageTk.PhotoImage(imgVolume)
volume=Button(botones,height=80,width=80,image=imgVolume,text='Volumen',command=volume)
volume.grid(row=0,column=5)

imgMute=Image.open("IMG/no-sound.png")
imgMute=imgMute.resize((80,80))
imgMute= ImageTk.PhotoImage(imgMute)
NoVolume=Button(botones,height=80,width=80,image=imgMute,text='NoVolumen',command=NoVolume)
NoVolume.grid(row=0,column=6)

menubar=Menu(root)
root.config(menu=menubar)


canciones=os.listdir('/media/pi/MORAMO/MUSICA/')
print(canciones)
for cancion in canciones:
    #cancion=cancion.replace("/media/pi/MORAMO/MUSICA/","") 
    cancion=cancion.replace(".mp3","")
    pantalla.insert(END, cancion)
def run():
    root.mainloop()



