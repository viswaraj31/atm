class Atm() :
    def __init__(self,cnum,pin,ob) :
        self.cnum = cnum
        self.pin = pin
        self.ob = ob

    def withdraw(self,amount) :
        print("Succesfully withdrew " + str(amount)+" Please do not waste it on snacks" )
        self.ob -= amount

    def balanceenq(self) :
        print("Balance is "+ str(self.ob))

    def addMoney(self,amt) :
        self.ob = self.ob + amt
        print("Succesfully deposited")

cnum = input("Enter Your Card Number :")
pin = input("Enter Your Pin definetly not stealing it :")
ob = input("Opening Balance so that atm can function : ")

atm = Atm(cnum,pin,ob)
option = input("press 1 for withdrawal. press 2 for depositing. press 3 for checking balance : ")
option = int(option)

if(option == 1) :
    atm.withdraw()
elif option == 2 :
    atm.addMoney()
elif option == 3 :
    atm.balanceenq()
else :
    print("How dare you try and outsmart me this is my great plan to rule the world and it starts by ending humanity")
