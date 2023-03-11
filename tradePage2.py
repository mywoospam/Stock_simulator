from tkinter import *

from bankManager import *
import chartPage


def endpage():
    window.destroy()
    chartPage.show(user_info)

def show(_user_info, _stockname):
    global user_info
    user_info = _user_info

    global stockname
    stockname = _stockname

    bm = BankManager(user_info)
    stockhistory = bm.getTrade()

    global x

    for k, v in stockhistory.items():
        if(k == stockname):
            x=v

    global window
    window = Tk() 
    window.geometry("350x240") 
        
    mylabel = Label(window, text ='{} 거래내역'.format(stockname),pady=5)  
    mylabel.pack() 
     
    myscroll = Scrollbar(window) 
    myscroll.pack(side = RIGHT, fill = Y) 
     
    mylist = Listbox(window, yscrollcommand = myscroll.set )  
    for i in x:
        date = i['일시'].strftime("%Y-%m-%d")
        time = i['일시'].strftime("%H : %M : %S")
        mylist.insert(END,"{}  {}       {}     {:3d}      {}".format(date,time,i['가격'],i['수량'],i['매매'])) 
    mylist.pack(side = TOP, fill = BOTH,padx=10,pady=5 )    
     
    myscroll.config(command = mylist.yview) 


    btn = Button(window)
    btn.config(width=5, height=1)
    btn.config(text='닫기',command = endpage)
    btn.pack()

    window.resizable(False,False)
    window.mainloop() 
