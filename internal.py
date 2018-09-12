from tkinter import *
from tkinter import messagebox


class Comic:
    def __init__(self, name, stock):
        self._name = name
        self._stock = stock
        self._sold = 0
        comics.append(self)
        comic_names.append(self._name)


        #function for restocking 
    def _restock_final(self, stock):
        #error checking that stock isn't > 20
        if self._stock + stock > 20:
            error = "max_stock"
            notify_func(error)

        #error checking that input is not 0 or a negative
        elif stock <= 0:
            error = "neg_input"
            notify_func(error)

        else:
            #changes being made
            self._stock += stock
            #updating lists
            update_stock()
            error = "restock_succeed"
            notify_func(error)


    def _sell_final(self, sell):
        #error checking that it will not put stock into negatives
        if self._stock - sell < 0:
            error = "zero_stock"
            notify_func(error)

        #error checking, input isn't negative or 0
        elif sell <= 0:
            error = "neg_input"
            notify_func(error)

        else:
            #changes being made
            self._stock -= sell
            self._sold += sell
            #updating the stock and sold lists
            update_stock()
            sold_stock()
            #message saying successful sale
            error = "sold_succeed"
            notify_func(error) 


def update_stock():
    stock_info.set("")
    #loops list for current stock
    for i in comics:
        stock_info.set(stock_info.get() + i._name + "   :" + str(i._stock) + "\n")

# this function is used to add new comics to the stock list
def add():
    #confirming users decsicion
    if messagebox.askyesno("Warning!", "Are you sure you wish to add {}?".format(add_comic.get())):
        #checking if the comic is already in the list
        if add_comic.get() in comic_names:
            error = "item_exists"
            notify_func(error)

        #checking the input is not  empty
        elif len(add_comic.get()) == 0 or add_comic.get() == " ":
            error = "empty_add"
            notify_func(error) 
            
        else:
            #will have 0 stock to start off with
            Comic(add_comic.get(), 0)
            #updates everything
            update_stock()
            update_optionmenu()
            sold_stock()
            #message to confirm its been added
            error = "item_added"
            notify_func(error)

def sell():
    #error checking
    try:
        #confirming users decsicion
        if messagebox.askyesno("Warning!", "Are you sure you wish to sell {} copies of {}?".format(sell_comic.get(), selling_comic.get())):
            for i in comics:
                if i._name == selling_comic.get():
                    #running function in the class
                    i._sell_final(sell_comic.get())
    #message if not an int
    except:
        error = "not_int"
        notify_func(error)


#function for deleting comics
def delete():
        if messagebox.askyesno("Warning!", "Are you sure you wish to delete {}?".format(delete_comic.get())):
            for i in comics:
                #finds comic and deletes it.
                if i._name == delete_comic.get():
                    comics.remove(i)
                    comic_names.remove(i._name)
                    #update all of the lists once its gone 
                    update_stock()
                    sold_stock()
                    update_optionmenu()
                    error = "del_succeed"
                    notify_func(error)

def sold_stock():
    sold_info.set("")
    #loops through the list for sold stock
    for i in comics:
        sold_info.set(sold_info.get() + i._name + "   :" + str(i._sold) + "\n")



#function for restocking 
def restock():
    #error checking
    try:
        #confirming they want to do it
        if messagebox.askyesno("Warning!", "Are you sure you wish to restock {} with {} comics?".format(selected_comic.get(), restock_comic.get())):
            for i in comics:
                if i._name == selected_comic.get():
                    #running the function in the class
                    i._restock_final(restock_comic.get())
    #invalid message
    except:
        error = "not_int"
        notify_func(error)        

def update_optionmenu():
    #globalised
    global comic_menu
    global selling_menu
    global delete_menu

    comic_menu.children["menu"].delete(0, "end")
    selling_menu.children["menu"].delete(0, "end")
    delete_menu.children["menu"].delete(0, "end")

    #go through the list
    for c in comics:
        comic_menu.children["menu"].add_command(label=c._name, command=lambda comic=c._name: selected_comic.set(comic))
        selling_menu.children["menu"].add_command(label=c._name, command=lambda comic=c._name: selling_comic.set(comic))
        delete_menu.children["menu"].add_command(label=c._name, command=lambda comic=c._name: delete_comic.set(comic))

    #reset the displayed one in case the first one is deleted
    selected_comic.set(comic_names[0])
    selling_comic.set(comic_names[0])
    delete_comic.set(comic_names[0])

#function for all of the errors
def notify_func(error):
    #message if function puts stock less than 0
    if error == "zero_stock":
        messagebox.showinfo("Warning!", "There isn't enough stock to sell")
    #message if stock is larger than 20
    elif error == "max_stock":
        messagebox.showinfo("Warning!", "There is a max of 20 stock")
    #message is successfully sold successfully
    elif error == "sold_succeed":
        messagebox.showinfo("Success!", "Items sold successfully ")
    #message if item already exists
    elif error == "item_exists":
        messagebox.showinfo("Warning!", "Items already exists")
    #message if  its empty
    elif error == "empty_add":
        messagebox.showinfo("Warning!", "Comic must have a title")
    #message if item added successfully
    elif error == "item_added":
        messagebox.showinfo("Success!", "Items added successfully ")    
    #message if input isn't an int
    elif error == "not_int":
        messagebox.showinfo("Warning!", "You must input an int")
    #message if input is negative
    elif error == "neg_input":
        messagebox.showinfo("Warning", "Input can not be zero or a negative")
    #message when comic is deleted successfully
    elif error == "del_succeed":
        messagebox.showinfo("Success!", "Items deleted successfully")
 

comics = []
comic_names = []

# comics that are pre existing 
Comic("Python Panic", 8)
Comic("Scratch the Cat", 12)
Comic("Tony Tkinter", 3)

#basic set up for the window
root = Tk()
root.title("Crazy Comics")
root.geometry("1000x800")

#title for crazy comics
title = Label(root, text="Crazy Comics", width=10)
title.grid(columnspan=3 , column=1)

#printing stock
stock_title = Label(root, text="Stock", width=10)
stock_title.grid(columnspan=2, column=1, row=2)

#label showing the stock
stock_info = StringVar()
stock_lbl = Label(root, textvariable=stock_info, justify="left")
stock_lbl.grid(columnspan=2, column=1, row=3)

#adding comics label 
add_title = Label(root, text="Add", width=20)
add_title.grid(column=0, row=7)

#input box
add_comic = StringVar()
add_comic.set("Enter comic name")
add_input = Entry(root, textvariable=add_comic, width=20)
add_input.grid(column=1, row=7)

#button for adding comic
add_btn = Button(root, text="Add new comic", command=add, width=20)
add_btn.grid(column=3, row=7)


#restocking comics label
restock_title = Label(root, text="Restock", width=20)
restock_title.grid(column=0, row=11)

#restocking comics drop down
selected_comic = StringVar()
selected_comic.set(comic_names[0])
comic_menu = OptionMenu(root, selected_comic, *comic_names)
comic_menu.config(width=20)
comic_menu.grid(column=1, row=11)

#restocking input
restock_comic = IntVar()
restock_comic.set("Enter number of comics to add")
restock_input = Entry(root, textvariable=restock_comic, width=20)
restock_input.grid(column=2, row=11)

#button for restocking comics
restock_btn = Button(root, text="Restock comic", command=restock, width=20)
restock_btn.grid(column=3, row=11)

#selling comics label
selling_title = Label(root, text="Sell", width=20)
selling_title.grid(column=0, row=9)

#selling dropdown
selling_comic = StringVar()
selling_comic.set(comic_names[0])
selling_menu = OptionMenu(root, selling_comic, *comic_names)
selling_menu.config(width=20)
selling_menu.grid(column=1, row=9)

#input for selling comics
sell_comic = IntVar()
sell_comic.set("Enter number of comics to sell")
sell_input = Entry(root, textvariable=sell_comic, width=20)
sell_input.grid(column=2, row=9)

#button for selling comics
sell_btn = Button(root, text="Sell comic", command=sell, width=20)
sell_btn.grid(column=3, row=9)


#deleting comics label
delete_title = Label(root, text="Delete", width=20)
delete_title.grid(column=0, row=13)

#selling dropdown
delete_comic = StringVar()
delete_comic.set(comic_names[0])
delete_menu = OptionMenu(root, delete_comic, *comic_names)
delete_menu.config(width=20)
delete_menu.grid(column=1, row=13)

#button for deleting comics
delete_btn = Button(root, text="Delete comic", command=delete, width=20)
delete_btn.grid(column=3, row=13)

#printing sold comics
sold_title = Label(root, text="Sold Today", width=10)
sold_title.grid(columnspan=2, column=2, row=2)

#label showing sold comis today
sold_info = StringVar()
sold_lbl = Label(root, textvariable=sold_info, justify="left")
sold_lbl.grid(columnspan=2, column=2, row=3)



update_stock()
sold_stock()
root.mainloop()
