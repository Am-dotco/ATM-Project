#ATMOperations.py<--Module Name
from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00 # Here bal is Called Global Variable
def deposit():
    damt=float(input("Enter your deposit amount: "))# Possibility of raising ValueError
    if damt<=0:
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUR Account xxxxxxx123 Credited with INR:{}".format(damt))
        print("\tNow UR Account Balance after Deposit:{} ".format(bal))

def withdraw():
    global bal
    wamt = float(input("Enter your withdraw amount: "))  # Possibility of raising ValueError
    if wamt <= 0:
        raise WithDrawError
    elif (wamt+500)>bal:
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("\tUR Account xxxxxxx123 Debited with INR:{}".format(wamt))
        print("\tNow UR Account Balance after Withdraw:{} ".format(bal))

def balenq():
    print("\tUR Account Balance:{} ".format(bal))
