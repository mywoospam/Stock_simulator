from tkinter import *

from bankManager import *
import chartPage

def endpage():
    window.destroy()
    chartPage.show(user_info)

def show(_user_info):
    global user_info
    user_info = _user_info

    bm = BankManager(user_info)
    my_stock = bm.getStock()

    global window
    window = Tk() 
    window.geometry("350x240") 
        
    mylabel = Label(window, text ='투자내역',pady=5)  
    mylabel.pack() 
     
    myscroll = Scrollbar(window) 
    myscroll.pack(side = RIGHT, fill = Y) 
     
    mylist = Listbox(window, yscrollcommand = myscroll.set )  
    for i in my_stock:
        mylist.insert(END,"{}  {} ".format(i,my_stock[i])) 
    mylist.pack(side = TOP, fill = BOTH,padx=10,pady=5 )    
     
    myscroll.config(command = mylist.yview) 


    btn = Button(window)
    btn.config(width=5, height=1)
    btn.config(text='닫기',command = endpage)
    btn.pack()

    window.resizable(False,False)
    window.mainloop() 
