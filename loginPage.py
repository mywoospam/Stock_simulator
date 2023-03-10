from tkinter import *
import tkinter.messagebox as messagebox
import chartPage
import registerPage
from loginManager import *



def showChartpage():
    lm = LoginManager()
    ID = id_input.get()
    password = password_input.get()
    if ID not in lm.getIdList():
        messagebox.showwarning("","존재하지 않는 아이디입니다")
        return False
    if not lm.check(ID, password):
        messagebox.showwarning("","비밀번호가 일치하지 않습니다")
        return False
        
    window.destroy()
    chartPage.show(lm.getLoginInfo(ID))

def showRegisterpage():
    window.destroy()
    registerPage.show()
    


def show():
    global window
    window=Tk()

    global id_input, password_input
    id_input = StringVar()
    password_input = StringVar()
    
    window.title("Login")
    window.geometry("350x250+100+100")
    frame = LabelFrame(window, text='주식 가상 거래', padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    input_frame = Frame(frame, padx=20, pady=20)
    button_frame = Frame(frame, padx=20, pady=20)
    input_frame.grid(row=0, column=0)
    button_frame.grid(row=1, column=0)

    id_label       = Label(input_frame, text = "아이디   : ")
    password_label = Label(input_frame, text = "비밀번호 : ")
    id_entry       = Entry(input_frame, textvariable = id_input)
    password_entry = Entry(input_frame, textvariable = password_input)

    register_button = Button(button_frame, text="회원가입", command=showRegisterpage)
    login_button = Button(button_frame, text="로그인", command=showChartpage)

    id_label.grid(row=0, column=0, padx=10, pady=10)
    password_label.grid(row=1, column=0, padx=10, pady=10)
    id_entry.grid(row=0, column=1, padx=10, pady=10)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    login_button.grid(row=2,column=0, sticky="e", padx=10)
    register_button.grid(row=2,column=1, sticky="w")

    window.resizable(False, False)
    window.mainloop()


