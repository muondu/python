def converter():
    global what_convert
    what_convert = input("Do you want to convert a) ksh to usd or b) usd to ksh:  ")
converter()

if what_convert == "b":
    usd_cash = int(input("Enter how much dollars you want to convert: "))
    print("The amount you have inputed into kenya shilings = ",usd_cash * 108.59)
elif what_convert == "a":   
    ksd_cash = int(input("Enter how much kenya shillings you want to convert: "))
    print("The amount you have inputed into ud dolars = ",ksd_cash / 108.59)
else:
    print("I did not understand you")
