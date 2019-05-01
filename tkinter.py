#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameLabel = Label(self,text="Congratulation! You found the treasure.Leave your name below and I'll give you money!")
		self.nameLabel.pack()
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.amountLabel = Label(self,text='How much do you want:')
		self.amountLabel.pack()
		self.amountInput = Entry(self)
		self.amountInput.pack()
		self.alertButton = Button(self,text='Confirm',command=self.lol)
		self.alertButton.pack()

	def lol(self):
		name = self.nameInput.get()
		messagebox.showinfo('Message','%s, you foolish! Stop dreaming and work harder!!!' % name)

app = Application()
app.master.title('RMB giveaway')
app.mainloop()