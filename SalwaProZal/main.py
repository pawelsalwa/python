# -*- coding: utf-8 -*-
"""
Python- program zaliczeniowy - gra z komputerem z uzyciem
	   biblioteki Tkinter

@author: salwus
"""

from GameState import *
from Tkinter import *
from time import sleep
import pickle

master = Tk()

gs = GameState()

msg = ""
def checkForEnd():
	"""sprawdz, czy gra zostala zakonczona oraz wypisz kto zwyciezyl"""
	global gs, msg
	if(gs.php<=0 or gs.pm <=0):
		msg = "!!!!computer WON!!!!\n" +msg
		l1.config(text = msg )
		
		sleep(3)
		master.destroy()
		
	if(gs.chp<=0 or gs.cm <=0):
		msg = "!!!!you WON!!!!\n" +msg
		l1.config(text = msg )

		sleep(3)
		master.destroy()

#========================================================================================
def enemyTurn():
	"""tura przeciwnika z roznym prawdopodobienstwem zagran"""
	global gs
	from random import randint
	x = randint(0,30)
	
	if(gs.cm < 2): #jezeli ma 1 many
		defend()
	elif(gs.chp < x): #jezeli computer ma malo hp
		defend()
	else: #jezeli gracz ma malo hp lub komputer wystarczajaco duzo
		attack()
	checkForEnd()
	#def gainVP():
	#	global msg
	#	gs.cvp += 1
	#	gs.cm -= 3
def defend():
	"""akcja komputera odpowiadajaca zagraniu defensywnemu"""
	global msg	
	gs.chp += 2
	gs.cm += 2
	msg = "computer healed himself\n" +msg
	l1.config(text = msg )
def attack():
	"""akcja komputera odpowiadajaca zagraniu ofensywnemu"""
	global msg
	gs.php -= 4
	gs.cm -= 1
	msg = "computer dealt 4 dmg to you\n" +msg
	l1.config(text = msg )
#========================================================================================
def updatel2():
	"""zaaktualizuj panel l2 wyswietlajacy info o stanie gry"""
	global l2
	l2.config(text = "your hp ="+str(gs.php)+"| enemy hp = "+str(gs.chp)+"\nyour mana = "+str(gs.pm)+" | enemy mana = "+str(gs.cm))
#========================================================================================
def fb1():
	"""akcja ofensywna po wcisnieciu buttona b1"""
	global l1,l2,msg,gs
	
	gs.chp -= 4
	gs.pm -= 1
	
	updatel2()
	msg = "you dealed 4 dmg to your opponent\n"+msg
	l1.config(text = msg )
	checkForEnd()
	enemyTurn()
#========================================================================================			
def fb2():
	"""akcja defensywna po wcisnieciu buttona b2"""
	global l1,l2,msg,gs
	
	gs.php += 2
	gs.pm += 2
	
	updatel2()
	msg = "you gained 2 health\n"  +msg
	l1.config(text = msg )
	checkForEnd()
	enemyTurn()
#========================================================================================	
def save():
	"""zapisz gre przez serializacje obiektu GameState do pliku"""
	global gs, msg
	f = open("save.dat", "w")
	pickle.dump(gs, f)
	f.close()
	updatel2()
	msg = "game saved\n" +msg
	l1.config(text = msg )
#========================================================================================
def load():
	"""wczytaj gre przez deserializacje obiektu GameState z pliku"""
	global gs, msg
	f = open("save.dat", "r")
	gs = pickle.load(f)
	f.close()
	updatel2()
	msg = "game loaded\n" +msg
	l1.config(text = msg )
#========================================================================================	
#tworze buttony
b1 = Button(master, text="deal 4 dmg, costs 1 mana", command=fb1)
b2 = Button(master, text="gain 2 health, and 2 mana", command=fb2)
b3 = Button(master, text="save game", command=save)
b4 = Button(master, text="load saved game", command=load)
#tworze labele
l1 = Label(master, text = "Here're each player last moves...")
l2 = Label(master, text = "your hp ="+str(gs.php)+"| enemy hp = "+str(gs.chp)+"\nyour mana = "+str(gs.pm)+" | enemy mana = "+str(gs.cm))	  
#umieszczam komponenty w oknie
b1.grid(row = 0, column =1, sticky = N)
b2.grid(row = 1, column =1, sticky = N)
b3.grid(row = 0, column =3, sticky = N)
b4.grid(row = 1, column =3, sticky = N)
l1.grid(row = 3, column =1, rowspan = 2, columnspan = 1)
l2.grid(row = 0, column =2, rowspan = 2, columnspan = 1)

#b1.pack()
#b2.pack()
#petla glowna okna
mainloop()


