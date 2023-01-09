#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 18:10:23 2023

@author: pooja
"""

from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = 'blue')

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

def asciiconverter():
    input_word=enter_word.get()
    for letter in input_word:
        label["text"] += str(ord(letter)) + " "
        
ascii = int (ord(letter))
encrypted = ascii -1

label12["text"] += str(chr(encrypted))

btn=Button(root,text="Display Ascii code and encrypted value:",command=asciiconverter, bg='gold', fg = 'black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label = Label(root, text = "Name in Ascii : ", bg="light yellow", fg="black")
label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()