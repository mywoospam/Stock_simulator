from tkinter import *
import tkinter.messagebox as messagebox
import loginPage
from loginManager import *


def endpage():
    data = { k : inputs[k].get() for k in inputs}
    if availableID != inputs["id"].get():
        messagebox.showwarning("","ID 중복 확인을 해주세요")
        return False
    if "" in data.values():
        tkinter.messagebox.showwarning("","빈 칸을 채워주세요")
        return False

    lm = LoginManager()
    lm.addAccount(data)
    
    window.destroy()
    loginPage.show()

def checkrepeat():
    global availableID
    lm = LoginManager()
    ID = inputs["id"].get()
    print(lm.getIdList())
    if ID in lm.getIdList():
        #사용불가
        messagebox.showwarning("","이미 존재하는 아이디입니다\n다른 아이디를 사용해주세요")
        availableID=''        
    else:
        #사용가능
        messagebox.showinfo("","사용가능한 아이디입니다")
        availableID=ID


def show():
    global window
    window=Tk()
    window.title("Register")
    window.geometry("400x310+100+100")
    frame = LabelFrame(window, text='회원 가입', padx=20)
    frame.pack(padx=10, pady=10)

    global inputs
    global availableID
    inputs = {}
    availableID = ''
    
    inputs["id"] = StringVar()
    inputs["password"] = StringVar()
    inputs["name"] = StringVar()
    inputs["birthday"] = StringVar()
    inputs["number"] = StringVar()

    input_frame = Frame(frame, padx=20, pady=20)
    input_frame.grid(row=0, column=0)

    button_frame = Frame(frame, padx=20, pady=20)
    button_frame.grid(row=1, column=0)

    id_label       = Label(input_frame, text = "아이디   : ")
    password_label = Label(input_frame, text = "비밀번호 : ")
    name_label     = Label(input_frame, text = "  이름   : ")
    birthday_label = Label(input_frame, text = "생년월일 : ")
    number_label   = Label(input_frame, text = "전화번호 : ")

    id_entry       = Entry(input_frame, textvariable = inputs["id"])
    password_entry = Entry(input_frame, textvariable = inputs["password"])
    name_entry     = Entry(input_frame, textvariable = inputs["name"])
    birthday_entry = Entry(input_frame, textvariable = inputs["birthday"])
    number_entry   = Entry(input_frame, textvariable = inputs["number"])

    register_button = Button(button_frame, text="회원가입", command=endpage)
    check_button = Button(input_frame, text="중복확인", command=checkrepeat)

    id_label.grid(row=0, column=0, padx=5, pady=5)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    name_label.grid(row=2, column=0, padx=5, pady=5)
    name_entry.grid(row=2, column=1, padx=5, pady=5)

    birthday_label.grid(row=3, column=0, padx=5, pady=5)
    birthday_entry.grid(row=3, column=1, padx=5, pady=5)

    number_label.grid(row=4, column=0, padx=5, pady=5)
    number_entry.grid(row=4, column=1, padx=5, pady=5)

    check_button.grid(row=0,column=2, padx=5, pady=5)

    register_button.grid(row=2,column=1)

    window.resizable(False, False)


    window.mainloop()


