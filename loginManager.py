import pickle as pk

class LoginManager:
    def __init__(self):
        try:
            #파일 읽어오기
            with open("account.bin","rb") as f:
                self.__data = pk.load(f)
        except FileNotFoundError:
            #파일 없을 시엔 빈 list 생성
            self.__data = []

        #불러온 내용 다시 저장해놓기
        with open("account.bin","wb") as f:
            pk.dump(self.__data,f)

    def getIdList(self):
        lst = []
        for account in self.__data:
            lst.append(account.ID[:])
        return lst

    def check(self, ID, password):
        for account in self.__data:
            if account.ID == ID:
                print(account.ID, account.name, account.birthday, account.number)
                return (account.password == password)
        return False

    def getLoginInfo(self, ID):
        for account in self.__data:
            if account.ID == ID:
                return account

    def addAccount(self, ID, password, name, birthday, number):
        li = LoginInfo(ID, password, name, birthday, number)
        self.__data.append(li)
        with open("account.bin","wb") as f:
            pk.dump(self.__data,f)

    def addAccount(self, inputs):
        li = LoginInfo(inputs["id"], inputs["password"], inputs["name"], inputs["birthday"], inputs["number"])
        self.__data.append(li)
        with open("account.bin","wb") as f:
            pk.dump(self.__data,f)



class LoginInfo:
    def __init__(self,ID,password, name, birthday, number):
        self.ID=ID
        self.password=password
        self.name=name
        self.birthday=birthday
        self.number=number
        
    '''
    def getID(self):
        return self.__ID
    def getPassword(self):
        return self.__Password
    def setPassword(self,Password):
        self.__Password=Password
    '''        
