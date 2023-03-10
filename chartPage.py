from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mplfinance.original_flavor import candlestick2_ohlc
from pykrx import stock
import pandas as pd
from loginManager import *
import myPage
import loginPage

def mypage():
    window.destroy()
    myPage.show(user_info)
    
def mytradepage():
    print("거래내역")
    
def myinvestmentpage():
    print("투자내역")

def searchstock():
    print("검색")

def buystock():
    print("매수")

def sellstock():
    print("매도")

def show(_user_info):
    global user_info
    user_info = _user_info
    
    global window
    inputs ={}
    window = Tk()
    window.title("주식 가상 거래")
    window.geometry("365x250")
    frame = LabelFrame(window)
    frame.pack(padx=0, pady=10)
    
    inputs["stock"] = StringVar()
    inputs["presentprice"] = StringVar()
    inputs["presentpercent"] = StringVar()
    inputs["mypossess"] = StringVar()
    inputs["dealstock"] = StringVar()
    
    input_frame = LabelFrame(frame, text="종목 검색",padx=5, pady=5)
    input_frame.grid(row=1, column=0)
    
    button_frame = Frame(frame, padx=5, pady=5)
    button_frame.grid(row=0, column=0)
    
    stock_label = Label(input_frame, text='종목 : ')
    stock_entry = Entry(input_frame, textvariable = inputs["stock"])
    presentprice_label = Label(input_frame, text='현재가 : ')
    presentprice_entry = Entry(input_frame, textvariable = inputs["presentprice"])
    presentpercent_label = Label(input_frame, text='추이 : ')
    presentpercent_entry = Entry(input_frame, textvariable = inputs["presentpercent"])
    mypossess_label = Label(input_frame, text='보유수량 : ')
    mypossess_entry = Entry(input_frame, textvariable = inputs["mypossess"])
    dealstock_label = Label(input_frame, text='거래 : ')
    dealstock_entry = Entry(input_frame, textvariable = inputs["dealstock"])
    
    
    mypage_button = Button(button_frame, text="내 정보", command=mypage)
    mytrade_button = Button(button_frame, text="거래내역", command=mytradepage)
    myinvestment_button  = Button(button_frame, text="투자내역", command=myinvestmentpage)
    buystock_button  = Button(input_frame, text="매수", command=buystock)
    sellstock_button  = Button(input_frame, text="매도", command=sellstock)
    search_button  = Button(input_frame, text="검색", command=searchstock)
   
    stock_label.grid(row=0,column=0, padx=5, pady=5)
    stock_entry.grid(row=0,column=1, padx=5, pady=5)
    presentprice_label.grid(row=1,column=0, padx=5, pady=5)
    presentprice_entry.grid(row=1,column=1, padx=5, pady=5)
    presentpercent_label.grid(row=2,column=0, padx=5, pady=5)
    presentpercent_entry.grid(row=2,column=1, padx=5, pady=5)
    mypossess_label.grid(row=3,column=0, padx=5, pady=5)
    mypossess_entry.grid(row=3,column=1, padx=5, pady=5)
    dealstock_label.grid(row=4,column=0, padx=5, pady=5)
    dealstock_entry.grid(row=4,column=1, padx=5, pady=5)
    
    mypage_button.grid(row=0, column=0,padx=5)
    mytrade_button.grid(row=0, column=1,padx=5)
    myinvestment_button.grid(row=0, column=2,padx=5)
    search_button.grid(row=0, column=2,padx=5)
    buystock_button.grid(row=4, column=2,padx=5)
    sellstock_button.grid(row=4, column=3,padx=5)
    
    window.resizable(False, False)
    
    window.mainloop()
