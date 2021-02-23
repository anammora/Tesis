from tkinter import *
from tkinter import filedialog
import pygame

root=Tk()
root.title('Reproductor de musica')
root.geometry('500x300')
pygame.mixer.init()

def anadir():
    canciones=filedialog.askopenfilenames(initialdir='/',title='Elige cancion',
                                          filetypes=(('mp3','*.mp3'),('all files','*.*')))

    for cancion in canciones:
        cancion=cancion.replace("/media/pi/MORAMO/MUSICA/","") 
        cancion=cancion.replace(".mp3","")

        pantalla.insert(END, cancion)
      
def play():
    cancion=pantalla.get(ACTIVE)
    cancion= f'{cancion}.mp3'

    pygame.mixer.music.load("/home/pi/MORAMO/MUSICA/Camilo-Ropa Cara.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    pantalla.seleccion_clear(ACTIVE)

def siguiente():
    proxima=pantalla.curselection()
    proxima=proxima[0]+1
    cancion=pantalla.get(proxima)
    cancion=f'{cancion}.mp3'

    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=0)

    pantalla.selection_clear(0,END)

    pantalla.activate(proxima)

    last=None
    pantalla.seleccion_set(proxima,last)

def anterior():
    proxima=pantalla.curselection()
    proxima=proxima[0]-1
    cancion=pantalla.get(proxima)
    cancion=f'{cancion}.mp3'

    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=0)

    pantalla.selection_clear(0,END)

    pantalla.activate(proxima)

    last=None
    pantalla.seleccion_set(proxima,last)

global paused
paused=False

def pause(is_paused):
    global paused
    paused=is_paused
    
    if paused:
        pygame.mixer.music.unpause()
        pause=False
    else:
        pygame.mixer.music.pause()
        pause=True

def borrar1():
    pantalla.delete(ANCHOR)
    pygame.mixer.music.stop()

def borrar_todas():
    pantalla.delete(0,END)
    pygame.mixer.music.stop()

pantalla=Listbox(root,bg='lightblue',fg='blue',width=60,
selectbackground='white',selectforeground='black')    
pantalla.pack(pady=20)

botones=Frame(root)
botones.pack()

anterior=Button(botones,text='Anterior',command=anterior)
anterior.grid(row=0,column=0)

reproducir=Button(botones,text='Reproducir',command=play)
reproducir.grid(row=0,column=1)

pausa=Button(botones,text='Pausa',command=lambda:pause(paused))
pausa.grid(row=0,column=2)

detener=Button(botones,text='Detener',command=stop)
detener.grid(row=0,column=3)

siguiente=Button(botones,text='Siguiente',command=siguiente)
siguiente.grid(row=0,column=4)

menubar=Menu(root)
root.config(menu=menubar)

anadir_cancion=Menu(menubar)
menubar.add_cascade(label="Anadir cancion",menu=anadir_cancion)
anadir_cancion.add_command(label="Anadir una o mas canciones",command=anadir)

remover=Menu(menubar)
menubar.add_cascade(label="Borrar Canciones",menu=remover)
remover.add_command(label="Borrar una cacnion de la pantall",command=borrar1)
remover.add_command(label="Borrar todas las Canciones",command=borrar_todas)
    
root.mainloop()



