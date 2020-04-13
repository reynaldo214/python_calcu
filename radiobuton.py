from tkinter import *

raiz=Tk()
raiz.iconbitmap("imagenes/icono.ico")
raiz.title("cabron")
varOption=IntVar()
def imprimir():
    if varOption.get()==1:
        milabel.config(text="elegiste masculino")
    else:
        milabel.config(text="elegiste femenino")
Label(raiz, text="GENERO").pack()
Radiobutton(raiz,text="Masculino", value=1, variable=varOption, command=imprimir).pack()
Radiobutton(raiz,text="Femenino", value=2, variable=varOption, command=imprimir).pack()
milabel=Label()
milabel.pack()
#----------------segunda parte-------------
miframe=Frame(raiz)
miframe.config(width=500)
miframe.pack()


foto=PhotoImage(file="icocno.png")
Label(miframe, image=foto).pack()
milabel3=Label(miframe)
milabel3.pack()
def impresion():
    milabel3.config(text="")
milabel2=Label(miframe)
milabel2.pack()
milabel2.config(text="PRUEBA")
Checkbutton(miframe, text="prueba1", command=impresion()).pack()
Checkbutton(miframe, text="prueba2", command=impresion()).pack()




raiz.mainloop()