#importing libraries
from pytube import YouTube
from pytube.cli import on_progress
from customtkinter import *

#set the color theme
set_appearance_mode("System")
set_default_color_theme("blue")

# set the window
root = CTk()
root.title("Youtube Audio Downloader")
root.geometry("400x400")
root.iconbitmap("./assets/icone_ytb.ico")

#label
label = CTkLabel(root, text = "Entrez l'url de votre vidéo :", width = 250)
label.place(relx = 0.5, rely = 0.32, anchor = CENTER)

label2 = CTkLabel(root, text = "Entrez le chemin d'accès :", width = 250)
label2.place(relx = 0.5, rely = 0.48, anchor = CENTER)

# input field
input = CTkEntry(master = root, width = 250, border_width = 0)
input.place(relx = 0.5, rely = 0.4, anchor = CENTER)

input2 = CTkEntry(master = root, width = 250, border_width = 0)
input2.place(relx = 0.5, rely = 0.56, anchor = CENTER)

#on complete function
def on_complete(stream, file_path) :
    print("Done !")


#function that download the video
def telecharger() :
    url = str(input.get())
    path = str(input2.get())
    if path == None :
        path = './videos'
    youtube = YouTube(url, on_complete_callback = on_complete)
    video = youtube.streams.get_highest_resolution()
    video.download(path)

# button
btn = CTkButton(master = root, text = "Valider", command = telecharger, width = 250)
btn.place(relx = 0.5, rely = 0.66, anchor = CENTER)

#run the window
root.mainloop()
