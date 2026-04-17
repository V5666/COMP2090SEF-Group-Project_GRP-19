from tkinter import*#call library
import tkinter as tk
import tkinter.font as tkFont
from tkinter import scrolledtext
from library import Library
from heap_sort import HeapSorter



library = Library()
win = Tk()
win.title("")

win.geometry("1280x720+250-170")    #set GUI original size
win.minsize(width=400,height=200)   #set GUI Minimun size
win.maxsize(width=1980,height=1080)     #set GUI Maximun size
win.resizable(False,False)  #user can(Ture/1)or can't(False/0)change GUI's size
win.config(bg="skyblue")    #transparency,"alpha"=ture,0.5=50%,eg:win.attributes("-alpha",number)
win.attributes("-alpha",1)  #on top,e.g.:win.attributes("-topmost",True/False")
win.attributes("-topmost",True)


fontStyle = tkFont.Font(family="Lucida Grande", size=25)    #text size

def Result():

    lab_Ses = tk.Label(win,font=fontStyle,text="Heap Sort Result",bg='skyblue')
    lab_Ses.place(anchor=CENTER,x=650,y=80)

    btn_year = tk.Button(win,text="Sort by Year",bg='skyblue',font=fontStyle,command=sort_by_year)
    btn_year.place(anchor=CENTER,x=400,y=150)

    btn_title = tk.Button(win,bg='skyblue',text="Sort by Title",font=fontStyle,command=sort_by_title)
    btn_title.place(anchor=CENTER,x=900,y=150)

    global res_box
    res_box = scrolledtext.ScrolledText(win, wrap=tk.WORD,width=70,height=20,bg='skyblue',font=fontStyle)
    res_box.place(anchor=CENTER,x=620,y=500)
    res_box.config(state='disabled')
    
def sort_by_year():
    sorter = HeapSorter(library.books, key=lambda b: b.year)
    sorted_books = sorter.heap_sort()
    show_result(sorted_books)

def sort_by_title():
    sorter = HeapSorter(library.books, key=lambda b: b.title)
    sorted_books = sorter.heap_sort()
    show_result(sorted_books)

def show_result(book_list):
    res_box.config(state="normal")
    res_box.delete("1.0", tk.END)

    for book in book_list:
        res_box.insert(tk.END, book.get_info() + "\n")

    res_box.config(state="disabled")

Result()
win.mainloop()