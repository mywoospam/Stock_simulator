from tkinter import *
import tkinter.messagebox as messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mplfinance.original_flavor import candlestick2_ohlc
from pykrx import stock
import pandas as pd

from bs4 import BeautifulSoup
import requests, lxml
from urllib import parse

from loginManager import *
from bankManager import *
import whichStock

import myPage
import loginPage
import investmentPage



def mypage():
    window.destroy()
    myPage.show(user_info)
    
def mytradepage():
    window.destroy()
    whichStock.show(user_info)
    
def myinvestmentpage():
    window.destroy()
    investmentPage.show(user_info)

def searchstock():
    target = inputs["stock"].get()
    target = parse.quote(target, encoding='euc-kr')

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = 'https://finance.naver.com/search/searchList.naver?query=' + target
    r = requests.get(url, headers = headers).text
    bs = BeautifulSoup(r, 'lxml')

    try:
        s_list = bs.find_all('tr')[1]
    except IndexError as e:
        messagebox.showwarning("검색 실패","해당되는 주식을 찾을 수 없습니다.")
        inputs["presentprice"].set("-")
        inputs["presentpercent"].set("-")
        inputs["mypossess"].set("-")
        return
        
    s_list = s_list.find_all('td')
    stock_name = s_list[0].text.strip()
    stock_price = s_list[1].text # 거래가격
    stock_percent = s_list[3].text

    global cur_stock
    cur_stock = stock_name
    inputs["stock"].set(stock_name)
    inputs["presentprice"].set(stock_price)
    inputs["presentpercent"].set(stock_percent)

    bm = BankManager(user_info)
    my_stock = bm.getStock()
    if stock_name in my_stock:
        inputs["mypossess"].set(my_stock[stock_name])
    else:
        inputs["mypossess"].set(0)
    
def buystock():
    if cur_stock != inputs["stock"].get():
        messagebox.showwarning("매수 실패","주식 검색을 먼저 해주세요.")
        return
    
    stock_amount = inputs["dealstock"].get()
    if not stock_amount.isnumeric():
        messagebox.showwarning("매수 실패","올바르지 않은 수 입니다.")
        return
    
    stock_name = cur_stock
    stock_price = int(inputs["presentprice"].get().replace(",",""))
    stock_amount = int(stock_amount)
    
    bm = BankManager(user_info)
    try_result = bm.buyStock(stock_name, stock_price, stock_amount)
    if try_result==False:
        messagebox.showwarning("매수 실패","매수에 실패하였습니다")
        return
    my_stock = bm.getStock()
    if stock_name in my_stock:
        inputs["mypossess"].set(my_stock[stock_name])
    else:
        inputs["mypossess"].set(0)

def sellstock():
    if cur_stock != inputs["stock"].get():
        messagebox.showwarning("매도 실패","주식 검색을 먼저 해주세요.")
        return
    
    stock_amount = inputs["dealstock"].get()
    if not stock_amount.isnumeric():
        messagebox.showwarning("매도 실패","올바르지 않은 수 입니다.")
        return
    
    stock_name = cur_stock
    stock_price = int(inputs["presentprice"].get().replace(",",""))
    stock_amount = int(stock_amount)
    
    bm = BankManager(user_info)
    try_result = bm.sellStock(stock_name, stock_price, stock_amount)
    if try_result==False:
        messagebox.showwarning("매도 실패","매도에 실패하였습니다")
        return
    my_stock = bm.getStock()
    if stock_name in my_stock:
        inputs["mypossess"].set(my_stock[stock_name])
    else:
        inputs["mypossess"].set(0)
    

def show(_user_info):
    global user_info
    user_info = _user_info
    
    global window
    window = Tk()
    window.title("주식 가상 거래")
    window.geometry("365x250")
    frame = LabelFrame(window)
    frame.pack(padx=0, pady=10)

    global  inputs
    inputs ={}
    inputs["stock"] = StringVar()
    inputs["presentprice"] = StringVar()
    inputs["presentpercent"] = StringVar()
    inputs["mypossess"] = StringVar()
    inputs["dealstock"] = StringVar()

    global cur_stock #검색된 주식의 이름을 저장
    cur_stock = "임시 문자열"
    
    input_frame = LabelFrame(frame, text="종목 검색",padx=5, pady=5)
    input_frame.grid(row=1, column=0)
    
    button_frame = Frame(frame, padx=5, pady=5)
    button_frame.grid(row=0, column=0)
    
    stock_label = Label(input_frame, text='종목 : ')
    stock_entry = Entry(input_frame, textvariable = inputs["stock"])
    presentprice_label = Label(input_frame, text='현재가 : ')
    presentprice_entry = Entry(input_frame, textvariable = inputs["presentprice"], state= "disabled")
    presentpercent_label = Label(input_frame, text='전날대비 : ')
    presentpercent_entry = Entry(input_frame, textvariable = inputs["presentpercent"], state= "disabled")
    mypossess_label = Label(input_frame, text='보유수량 : ')
    mypossess_entry = Entry(input_frame, textvariable = inputs["mypossess"], state= "disabled")
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
