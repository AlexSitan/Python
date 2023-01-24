from tkinter import *
import sqlite3


vt = Tk()

vt.title("Prueba  De Interfaz")

vt.geometry("680x1300")
vt.config(bg="darkblue")

title = Label(vt, text = "Registro Saitan")
title.config(font="Helvetica 15", fg ="white", bg = "darkblue")
title.place(x = 150,  y = 50)

gm = Label(vt, text= "Correo Electronico")
gm.config(fg="white", bg="darkblue")
gm.place(x = 40, y=320)

ent = Entry(vt)
ent.place(x = 40, y=370, width=600)

ps = Label(vt, text= "Contraseña")
ps.config(fg="white", bg="darkblue")
ps.place(x = 40,  y=550)

ps2 = Entry(vt)
ps2.config(show="*")
ps2.place(x=40, y=600)

ag = Label(vt, text = "Edad")
ag.config(fg="white", bg="darkblue")
ag.place(x=40, y= 800)

ag2 = Entry(vt)
ag2.place(x=40, y=850, width=100)

def recolector():
	cx = sqlite3.connect("User.db")
	cr =  cx.cursor()
	list = []

	
	gm = ent.get()
	list.append(gm)
	pas = ps2.get()
	list.append(pas)
	ed = ag2.get()
	list.append(ed)
	gml["text"] = gm
	pasw["text"] = pas
	edad["text"] = ed
	list2 = tuple(list)
	
	cr.execute(""" CREATE TABLE REGISTRO(
					ID INTEGER PRIMARY KEY AUTOINCREMENT,
					GMAIL VARCHAR(80) UNIQUE,
					EDAD INTEGER(50),
					PASWORD VARCHAR(90))""")
					
	c = [
		list2
	]
					
	cr.executemany("INSERT INTO REGISTRO VALUES(NULL, ?, ?, ?)", c)
	
	cx.commit()
	cx.close()
	
	
	


snd =  Button(vt, text="Registrar", command=recolector)
snd.config(bg="gray", fg="white")
snd.place(x = 250, y=1000)

gml = Label(vt)
gml.place(x=40, y=1100)

pasw = Label(vt)
pasw.place(x=40, y=1150)

edad = Label(vt)
edad.place(x=40, y=1200)

tp = Label(vt)
tp.place(x = 40, y=1250)






vt.mainloop()

# Author: Alex Sitán
# Tema: Conexion entre "SQLite y Python"
# Contactos: eisnteinsitan@gmail.com
# Programa #No.1