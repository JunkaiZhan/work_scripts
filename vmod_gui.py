#!/usr/local/bin/python3

import re, sys, time, math
import vmod

from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.font as tkFont

class Application:

	def __init__(self):
		window = Tk()
		window.title("IP RTL Generator")

		window.geometry("400x160+500+300")
		window.minsize(200, 100)
		window.maxsize(420, 200)

		bgColor="#272822"
		fgColor="#fdfcf2"

		head_font = tkFont.Font(family='Arial', size=16, weight=tkFont.BOLD)
		body_font = tkFont.Font(family='Arial', size=14, weight=tkFont.NORMAL)
		
		frame1 = Frame(window)
		frame1.pack()

		self.bsLength = StringVar()

		label_bs = Label(frame1, text=">>>> Barral Shifter Design", font=head_font)
		label_ar_bs = Label(frame1, text="Size of Shifter: ", font=body_font)
		entry = Entry(frame1, textvariable=self.bsLength, font=body_font)
		label_unit = Label(frame1, text="bits", font=body_font)
		btget = Button(frame1, text="Generate", font=body_font, command=self.processBS)

		label_bs.grid(row=0, column=0, columnspan=4, sticky=W)
		label_ar_bs.grid(row=1, column=0, sticky=W)
		entry.grid(row=1, column=1, sticky=W)
		label_unit.grid(row=1, column=2, sticky=W)
		btget.grid(row=1, column=3, sticky=W)

		frame2 = Frame(window)
		frame2.pack()

		self.srcsAdderBit = StringVar()

		label_sa = Label(frame2, text=">>>> Square Root Carry Select Adder Design", font=head_font)
		label_ar_sa = Label(frame2, text="Size of Adder: ", font=body_font)
		entry_sa = Entry(frame2, textvariable=self.srcsAdderBit, font=body_font)
		label_unit_sa = Label(frame2, text="bits", font=body_font)
		btget_sa = Button(frame2, text="Generate", font=body_font, command=self.processSRCSAdder)

		label_sa.grid(row=0, column=0, columnspan=4, sticky=W)
		label_ar_sa.grid(row=1, column=0, sticky=W)
		entry_sa.grid(row=1, column=1, sticky=W)
		label_unit_sa.grid(row=1, column=2, sticky=W)
		btget_sa.grid(row=1, column=3, sticky=W)

		frame3 = Frame(window)
		frame3.pack()

		self.proAdderBit = StringVar()

		label_pa = Label(frame3, text=">>>> Progressive Carry Adder Design", font=head_font)
		label_ar_pa = Label(frame3, text="Size of Adder: ", font=body_font)
		entry_pa = Entry(frame3, textvariable=self.proAdderBit, font=body_font)
		label_unit_pa = Label(frame3, text="bits", font=body_font)
		btget_pa = Button(frame3, text="Generate", font=body_font, command=self.processProAdder)

		label_pa.grid(row=0, column=0, columnspan=4, sticky=W)
		label_ar_pa.grid(row=1, column=0, sticky=W)
		entry_pa.grid(row=1, column=1, sticky=W)
		label_unit_pa.grid(row=1, column=2, sticky=W)
		btget_pa.grid(row=1, column=3, sticky=W)
		
		window.mainloop()


	def processBS(self):
		vmod.barralShifter(int(self.bsLength.get()))
		tkinter.messagebox.showinfo(">> Congraduration <<", "Generate Barral Shifter RTL Successfully!")

	def processSRCSAdder(self):
		vmod.srcsAdder(int(self.srcsAdderBit.get()))
		tkinter.messagebox.showinfo(">> Congraduration <<", "Generate Square Root Carry Select Adder RTL Successfully!")

	def processProAdder(self):
		vmod.proCarryAdder(int(self.srcsAdderBit.get()))
		tkinter.messagebox.showinfo(">> Congraduration <<", "Generate rogressive Carry Adder RTL Successfully!")


Application()	