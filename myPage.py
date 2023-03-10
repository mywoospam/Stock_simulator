from tkinter import *
from loginManager import *
from bankManager import *
import loginPage
import chartPage

def endpage():
    window.destroy()
    chartPage.show(user_info)

def show(_user_info):
    global user_info
    user_info = _user_info

    bm = BankManager(user_info)
    
    global window
    inputs={}
    window = Tk()
    window.title("my page")
    window.geometry('275x240')
    frame = LabelFrame(window, text='내 정보', padx=5)
    frame.pack(padx=0, pady=10)

    inputs["id"] = StringVar()
    inputs["name"] = StringVar()
    inputs["birthday"] = StringVar()
    inputs["num"] = StringVar()
    inputs["money"] = StringVar()

    inputs["id"].set(user_info.ID)
    inputs["name"].set(user_info.name)
    inputs["birthday"].set(user_info.birthday)
    inputs["num"].set(user_info.number)
    inputs["money"].set(bm.getMoney())
    
    input_frame = Frame(frame, padx=5, pady=5)
    input_frame.grid(row=0, column=0)
    button_frame = Frame(frame, padx=5, pady=5)
    button_frame.grid(row=1, column=0)
    
    myid_label       = Label(input_frame, text='ID : ')
    myid_entry       = Label(input_frame, textvariable = inputs["id"])
    myname_label     = Label(input_frame, text='이름 : ')
    myname_entry     = Entry(input_frame, textvariable = inputs["name"])
    mybirthday_label = Label(input_frame, text='생년월일 : ')
    mybirthday_entry = Entry(input_frame, textvariable = inputs["birthday"])
    mynum_label      = Label(input_frame, text='전화번호 : ')
    mynum_entry      = Entry(input_frame, textvariable = inputs["num"])
    mymoney_label    = Label(input_frame, text='보유원화 : ')
    mymoney_entry    = Entry(input_frame, textvariable = inputs["money"])
    
    endpage_button = Button(button_frame, text="닫기", command=endpage)
   
    myid_label.grid(row=0,column=0, padx=5, pady=5)
    myid_entry.grid(row=0,column=1, padx=5, pady=5)
    myname_label.grid(row=1,column=0, padx=5, pady=5)
    myname_entry.grid(row=1,column=1, padx=5, pady=5)
    mybirthday_label.grid(row=2,column=0, padx=5, pady=5)
    mybirthday_entry.grid(row=2,column=1, padx=5, pady=5)
    mynum_label.grid(row=3,column=0, padx=5, pady=5)
    mynum_entry.grid(row=3,column=1, padx=5, pady=5)
    mymoney_label.grid(row=4,column=0, padx=5, pady=5)
    mymoney_entry.grid(row=4,column=1, padx=5, pady=5)
    
    endpage_button.grid(row=0, column=0,padx=5)
   
    

    window.resizable(False, False)
    window.mainloop()

