
from atmmenu import menu
import sys
from atmoperation import deposit, withdraw ,Balanceenquiry
from Atmexceptions import depositerror, withdrawerror,insuffunderror
while(True):
    menu()
    try:
        ch=int(input("enter ur choice:"))
        match(ch):
                case 1:
                    try:
                        deposit()
                    except ValueError:
                         print("dont enter str symbols and alpha-numerics for deposting")
                    except depositerror:
                         print("dont enter -ve or zero amount for deposit")
                case 2:
                    try:
                        withdraw()
                    except ValueError:
                        print("dont enter str symbols and alpha-numerics for withdraw")
                    except insuffunderror:
                        print("ur account doen not have sufficent funds")
                case 3:
                    Balanceenquiry()
                case 4:
                    print("thank u for banking with us")
                    sys.exit
                case _ :
                    print("ur selection of operatioin is wrong.... try again")
    except ValueError:
                   print("dont enter str symbols and alpha-numerics")                               








