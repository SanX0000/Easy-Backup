# importar o tkinker
from tkinter import*

#cores
black = "#f0f3f5" 
white = "#feffff" 
green = "#3fb5a3" 
red = "#fc766d"
letter = "#403d3d" 
blue = "#4a88e8" 

#janela
janela = Tk ()
janela.title ("SpeedTest")
janela.geometry ('350x200')
janela.configure (background=green)
janela.resizable(width=FALSE, height=FALSE)


#divisão da janela
frame_logo = Frame (janela, width=350, height=60, bg=white)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_body = Frame (janela, width=350, height=140, bg=white)
frame_body.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


janela.mainloop ()
