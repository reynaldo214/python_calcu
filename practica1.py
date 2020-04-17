from tkinter import *
from decimal import *
raiz=Tk()
raiz.iconbitmap("imagenes/icono.ico")
raiz.title("calculadora")

miframe=Frame(raiz)
miframe.pack()
#----variables de la segunda prueba
con=0
con1=0
con2=0
captador=0
captador1=0
total=0
total1=1
total2=1
contadorsigno=0
signoanterior=""

#-----------funcion de teclado--------------
def dgitar(num):
    global con
    global captador
    global signoanterior
    global contadorsigno
    if type(num)==int:
        if con == 0:
            numerodepantalla.set(num)
            captador=Decimal(num)
            con=1
        else:
            captador=Decimal(numerodepantalla.get()+str(num))
            numerodepantalla.set(str(captador))
            print(captador)

    elif num == '.':
        print("es punto")
    else:
        if contadorsigno==0:
            signoanterior=num
            numerodepantalla.set(str(captador))
            con = 0
            tipo_operacion(num)
            print(signoanterior)
            contadorsigno=contadorsigno+1
        elif signoanterior==num:
            numerodepantalla.set(str(captador))
            con = 0
            tipo_operacion(num)
            print(signoanterior)
        else:
            tipo_operacion(signoanterior)
            con=0
            print(signoanterior)
            signoanterior=num

    #global separador
    #if type(num) is int:
     #   print(numerodepantalla.get())
      #  if numerodepantalla.get() == '0':
       #     print("es cero")
        #    numerodepantalla.set("")
        #else:
         #   if separador == 1:
          #      print("se separo cadena")
           #     numerodepantalla.set("")
        #numerodepantalla.set(numerodepantalla.get() + str(num))
    #else:
     #   if not '.' in numerodepantalla.get() and numerodepantalla.get() != 0:
      #      numerodepantalla.set(numerodepantalla.get() + num)

#-------- ver tipo de operacion
def tipo_operacion(num):
    global total
    global captador
    global con1
    global con2
    global total1
    global total2
    if num =="+":
        print("estas entrando a al suma con el captador en" + str(captador))
        captador1=captador
        total=total+captador1
        numerodepantalla.set(str(total))
        captador=0
        con1=1
        con2=1
        total2=2
    elif num == "-":
        print("estas entrando a al resta con un total de " + str(captador))
        captador1 = captador
        if con1==0:
            total=captador1-total
            con1=1
            con2=1
        else:
            total = total-captador1

        print(total)
        numerodepantalla.set(str(total))
        captador=0
        con1=1
        con2=1
        total2=2
    elif num== "*":
        print("estas entrando a la multiplicacion con el cpatador en" + str(captador))
        captador1 = captador
        if con2==0:
            total=captador1*total1
            con2=1
        else:
            total = total * captador1
        numerodepantalla.set(str(total))
        captador = 0
        con1=1
        con2=1
        total2=2
    else:
        print("estas entrando a la dicision con el cpatador en" + str(captador))
        captador1 = captador
        if total2==1:
            print("estas en el si del if")
            total=Decimal(captador1/total2)
            total2=2
        else:
            total = total / captador1
            print("estas eb el no del if")
        print(total)
        numerodepantalla.set(str(total))
        captador = 0
        con1=1
        con2 = 1
        total2=2
#-----------codigo de pantalla--------------
numerodepantalla=StringVar()
numerodepantalla.set(0)
pantalla=Entry(miframe,textvariable=numerodepantalla)
pantalla.grid(row=1, column=1,columnspan=4,padx=10,pady=10)
pantalla.config(bg="black",fg="green",justify="right",font="Impact",width=40)

#---------------codigo de la fila uno-----------------
boton7=Button(miframe, text="7", width=10,command=lambda:dgitar(7))
boton7.grid(row=2,column=1)
boton8=Button(miframe, text="8", width=10,command=lambda:dgitar(8))
boton8.grid(row=2,column=2)
boton9=Button(miframe, text="9", width=10,command=lambda:dgitar(9))
boton9.grid(row=2,column=3)
botondiv=Button(miframe, text="/", width=10,command=lambda:dgitar("/"))
botondiv.grid(row=2,column=4)

#---------------codigo de la fila dos-----------------
boton4=Button(miframe, text="4", width=10,command=lambda:dgitar(4))
boton4.grid(row=3,column=1)
boton5=Button(miframe, text="5", width=10,command=lambda:dgitar(5))
boton5.grid(row=3,column=2)
boton6=Button(miframe, text="6", width=10,command=lambda:dgitar(6))
boton6.grid(row=3,column=3)
botonmult=Button(miframe, text="x", width=10,command=lambda:dgitar("*"))
botonmult.grid(row=3,column=4)

#---------------codigo de la fila tres-----------------
boton1=Button(miframe, text="1", width=10,command=lambda:dgitar(1))
boton1.grid(row=4,column=1)
boton2=Button(miframe, text="2", width=10,command=lambda:dgitar(2))
boton2.grid(row=4,column=2)
boton3=Button(miframe, text="3", width=10,command=lambda:dgitar(3))
boton3.grid(row=4,column=3)
botonres=Button(miframe, text="-", width=10,command=lambda:dgitar("-"))
botonres.grid(row=4,column=4)

#---------------codigo de la fila tres-----------------
boton0=Button(miframe, text="0", width=10,command=lambda:dgitar(0))
boton0.grid(row=5,column=1)
botonpunto=Button(miframe, text=".", width=10,command=lambda:dgitar("."))
botonpunto.grid(row=5,column=2)
botonigual=Button(miframe, text="=", width=10,command=lambda:dgitar("="))
botonigual.grid(row=5,column=3)
botonsuma=Button(miframe, text="+", width=10,command=lambda:dgitar("+"))
botonsuma.grid(row=5,column=4)

raiz.mainloop()