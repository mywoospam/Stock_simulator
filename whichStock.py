from tkinter import *
from loginManager import *
from bankManager import *
import chartPage
import tradePage2

def endpage():
    stockname = stockname_input.get()
    window.destroy()
    tradePage2.show(user_info, stockname)

def show(_user_info):
    global user_info
    user_info = _user_info

    global window
    window = Tk()
    
    global stockname_input
    stockname_input = StringVar()

    
    
    window.title("whichStock")
    window.geometry("370x95")
    frame = LabelFrame(window, text='거래 내역 종목 검색',padx=5, pady=5)
    frame.pack(padx=10, pady=10)

    input_frame = Frame(frame, padx=5, pady=5)
    input_frame.grid(row=0, column=0)


    stockname_label = Label(input_frame, text = "거래내역 볼 종목 : ")
    stockname_entry = Entry(input_frame, textvariable = stockname_input)

    endpage_button = Button(input_frame, text="검색", command = endpage)

    stockname_label.grid(row=0, column=0, padx=5, pady=5)
    stockname_entry.grid(row=0, column=1, padx=5, pady=5)

    endpage_button.grid(row=0, column=3,padx=5)


    window.resizable(False, False)
    window.mainloop()
