from tkinter import *


class Comic:
    def __init__(self, name, stock):
        self._name = name
        self._stock = stock
        comics.append(self)
        comic_names.append(self._name)

def update_label():
    comic_info.set("")
    for i in comics:
        comic_info.set(comic_info.get() + i._name + "   $" + str(i._stock) + "\n")

def add():
    global comic_menu
    Comic(new_comic.get(), new_stock.get())
    update_label()
    comic_menu.grid_forget()
    comic_menu = OptionMenu(root, selected_comic, *comic_names)
    comic_menu.grid(row=1)

comics = []
comic_names = []

Comic("Python Panic", 8)
Comic("Scratch the Cat", 12)
Comic("Tony Tkinter", 3)

root = Tk()
root.title("Comic shit")
root.geometry('600x300')

comic_info = StringVar()

comic_lbl = Label(root, textvariable=comic_info)
comic_lbl.grid(row=0)

selected_comic = StringVar()
selected_comic.set(comic_names[0])
comic_menu = OptionMenu(root, selected_comic, *comic_names)
comic_menu.grid(row=1)

new_comic = StringVar()
new_stock = StringVar()
new_comic.set("Enter Comic name")
new_stock.set("Enter a new stock level")
add_btn = Button(root, text="Add new comic", command=add).grid(row=1, column=2)

comic_entry = Entry(root, textvariable=new_comic).grid(row=2)
stock_entry = Entry(root, textvariable=new_stock).grid(row=2, column=1)

selected_comic_edit = StringVar()
selected_comic_edit.set(comic_names[0])
comic_menu = OptionMenu(root, selected_comic_edit, *comic_names)
comic_menu.grid(row=3)

edit_stock = StringVar()
edit_entry = Entry(root, textvariable=edit_stock).grid(row=3, column=1)
add_btn = Button(root, text="Edit comic stock level", command=update_label).grid(row=1, column=1)

update_label()

root.mainloop()
