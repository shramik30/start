#atmoperations.py
from Atmexceptions import depositerror,withdrawerror,insuffunderror 
bal=500
def deposit():
    damt=float(input("enter dposit amnt:"))
    if (damt<0):
        raise depositerror
    else:
        global bal
        bal=bal+damt
def withdraw(): 
    global bal
    wamt=float(input("enter withdraw amnt:"))
    if (wamt<0):
        raise withdrawerror
    elif (wamt+500>bal):
        raise insuffunderror
    else:
        bal=bal-wamt
def Balanceenquiry():
    print("ur account balance={}".format(bal))