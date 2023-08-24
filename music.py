from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os
root = Tk()
root.title('Music player')
root.geometry("920x350")
root.resizable(False,False)
root.configure(bg="#0f1a2b")
mixer.init()
paused=False
current_song=""
songs=[]
directory=''

def Add_Music():
    global current_song,directory
    directory = filedialog.askdirectory()
    for song in os.listdir(directory):
        name,ext=os.path.splitext(song)
        if ext =='.mp3':
            songs.append(song)
    
    for song in songs:
        Playlist.insert("end",song)
    Playlist.selection_set(0)
    current_song=songs[Playlist.curselection()[0]]


def Play_Music():
    global paused,current_song,directory
    if not paused:
        mixer.music.load(os.path.join(directory,current_song))
        mixer.music.play()
        print(current_song[0:-4])
        music.config(text=current_song[0:-4])

    else :
        mixer.music.unpause()
        paused=False
        
def pause_music():
    global paused
    mixer.music.pause()
    paused=True
def next_song():
    global paused,current_song,directory
    try:
        Playlist.selection_clear(0,END)
        Playlist.selection_set(songs.index(current_song)+1)
        current_song=songs[Playlist.curselection()[0]]
        Play_Music()
    except:
        pass
def pre_song():
    global paused,current_song,directory
    try:
        Playlist.selection_clear(0,END)
        Playlist.selection_set(songs.index(current_song)-1)
        current_song=songs[Playlist.curselection()[0]]
        Play_Music()
    except:
        pass
    

Icon_Image = PhotoImage(file="img\\logo.png")
root.iconphoto(False,PhotoImage(file="img\\logo.png"))

Top_Image =PhotoImage(file="img\\top.png")
Label(root,image=Top_Image,bg="#0f1a2b").pack()


logo_Image = PhotoImage(file="img\\logo.png")
Label(root, image=logo_Image, bg="#0f1a2b").place(x=67,y=107)


Button_Play = PhotoImage(file="img\\play.png")
Button(root, image=Button_Play, bg="#0f1a2b", bd=0, command=Play_Music).place(x=500, y=260)

Button_Pause = PhotoImage(file="img\\pause.png")
Button(root, image=Button_Pause, bg="#0f1a2b", bd=0, command=pause_music).place(x=580, y=260)

Button_Next = PhotoImage(file="img\\next.png")
Button(root, image=Button_Next, bg="#0f1a2b", bd=0, command=next_song).place(x=660, y=260)

Button_Pre = PhotoImage(file="img\\pre.png")
Button(root, image=Button_Pre, bg="#0f1a2b", bd=0, command=pre_song).place(x=420, y=260)

music=Label(root,text="",font=("Arial Rounded MT",12,'bold'),fg="white",bg="#0f1a2b")
music.place(x=155,y=320,anchor="center")
Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=325,y=20, width=570, height=200)
add_img=PhotoImage(file="img\\add.png")
Button(root, image=add_img,bg="#0f1a2b", bd=0,command=Add_Music).place(x=800, y=260)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=900, font=("Times new roman", 10), bg="#333333", fg="grey",selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
