#ATMProjDemo.py	<---Main Program
from ATMExcept import DepositError, WithDrawError, InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDON'T DEPOSIT ZERO OR -VE AMOUNT-TRY AGAIN")
                except ValueError:
                    print("\tDON'T DEPOSIT ALNUMS,STRS AND SYMBOLS-TRY AGAIN")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDON'T WITHDRAW ZERO OR -VE AMOUNT-TRY AGAIN")
                except InSuffFundError:
                    print("\tUR ACCOUNT DOES NOT HAVE FUNDS--TRY AGAIN")
                except ValueError:
                    print("\tDON'T WITHDRAW ALNUMS,STRS AND SYMBOLS-TRY AGAIN")
            case 3:
                balenq()
            case 4:
                print("THX FOR USING THIS PROJECT")
                break  # OR exit()
            case _:
                print("\tUR Selection of Choice is Wrong -Try Again")
    except ValueError:
        print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR CHOICE-TRY AGAIN")