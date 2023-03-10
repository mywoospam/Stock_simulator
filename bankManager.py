from loginManager import LoginInfo
import pickle as pk
from datetime import datetime


class BankManager:
    def __init__(self, loginInfo):
        self.__file_name = loginInfo.ID + ".bin"
        file_name = self.__file_name
        try:
            #파일 읽어오기
            with open(file_name,"rb") as f:
                self.__bank = pk.load(f)
        except FileNotFoundError:
            #파일 없을 시엔 빈 Bank 생성
            self.__bank = Bank()

        #불러온 내용 다시 저장해놓기
        with open(file_name,"wb") as f:
            pk.dump(self.__bank,f)

    def getMoney(self):
        return self.__bank.getMoney()
    def getStock(self): 
        return self.__bank.getStock()
    def getTrade(self):
        return self.__bank.getTrade()

    def buyStock(self, name, price, amount):
        file_name = self.__file_name
        if self.__bank.buyStock(name, price, amount):
            #구매 성공시 파일에 저장
            with open(file_name,"wb") as f:
                pk.dump(self.__bank,f)
            return True
        else: return False

    def sellStock(self, name, price, amount):
        file_name = self.__file_name
        if self.__bank.sellStock(name, price, amount):
            #구매 성공시 파일에 저장
            with open(file_name,"wb") as f:
                pk.dump(self.__bank,f)
            return True
        else: return False




class Bank:
    def __init__(self, money = 1000000, stock = {}, trade={}):
        self.__money = money
        self.__stock = stock #보유 주식
        self.__trade = trade #거래 내역
    def getMoney(self):
        return self.__money
    def getStock(self): 
        return self.__stock
    def getTrade(self):
        return self.__trade
    
    def buyStock(self, name, price, amount):  #성공시 true 반환
        if self.__money>=price*amount:
            if name in self.__stock: self.__stock[name] += amount
            else:                    self.__stock[name] = amount
            #trade_info dict의 내용구성 수정 필요
            trade_info = {"일시":datetime.now(), "가격":price, "수량":amount, "매매":"매수"}
            if name in self.__trade: self.__trade[name].append(trade_info)
            else:                    self.__trade[name] = [trade_info]
            self.__money -= price*amount
            return True
        else: return False
    def sellStock(self, name, price, amount):  #성공시 true 반환
        if name not in self.__stock:
            return False
        if self.__stock[name] >= amount:
            self.__stock[name] -= amount
            if self.__stock[name] == 0:
                #주식 수량이 0이면 stock dict에서 항목 삭제
                del self.__stock[name]
            #trade_info dict의 내용구성 수정 필요
            trade_info = {"일시":datetime.now(), "가격":price, "수량":amount, "매매":"매도"}
            if name in self.__trade: self.__trade[name].append(trade_info)
            else:                    self.__trade[name] = [trade_info]
            self.__money += amount * price
        else: return False
