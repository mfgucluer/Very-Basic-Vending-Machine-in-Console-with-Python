print("-----------------------------Welcome to the Vending Machine!-----------------------------")
print("-------------------------------------INFORMATION-------------------------------------")
print("The quantities of the products are written in the parentheses next to the products.\nIf it shows account:none, the machine has not accepted your money. Will refund you.")
print("1-Cake(20): 5TL \n2-Water(20): 1TL \n3-Popcorn(20): 4TL \n4-Coke(20): 3TL \n5-Biscuit(20): 2TL")
caket = 20
watert = 20
popcornt = 20
coket = 20
biscuitt = 20
def cake(para, tane):
    para = para - tane*5
    global request_Money
    global caket
    request_Money = para if para >= 0 and tane<=caket else print("Insufficient balance or product stock")
    if tane <= caket and para>=0:
        caket = caket - tane
    elif caket <= 0 :
        print("Insufficient product stock")
    return para, caket
def water(para, tane):
    para = para - tane*1
    global request_Money
    global watert
    request_Money = para if para >= 0 and tane<=watert else print("Insufficient balance or product stock")
    if tane <= watert and para>=0:
        watert = watert - tane
    elif watert <= 0:
        print("Insufficient product stock")
    return para, watert
def popcorn(para, tane):
    para = para - tane*4
    global request_Money
    global popcornt
    request_Money = para if para >= 0 and tane<=popcornt else print("Insufficient balance or product stock")
    if tane <= popcornt and para>=0:
        popcornt = popcornt - tane
    elif popcornt <= 0:
        print("Insufficient product stock")
    return para, popcornt
def coke(para, tane):
    para = para - tane*3
    global request_Money
    global coket
    request_Money = para if para >= 0 and tane<=coket else print("Insufficient balance or product stock")
    if tane <= coket and para>=0:
        coket = coket - tane
    elif coket <= 0:
        print("Insufficient product stock")
    return para, coket
def biscuit(para, tane):
    para = para - tane*2
    global request_Money
    global biscuitt
    request_Money = para if para >= 0 and tane<=biscuitt else print("Insufficient balance or product stock")
    if tane <= biscuitt and para>=0:
        biscuitt = biscuitt - tane
    elif biscuitt <= 0:
        print("Insufficient product stock")
    return para, biscuitt
choosing = True
while choosing == True:
    request_Money = eval(input("Please enter money:  "))
    choose_Pro = int(input("Please choose product:  "))
    how_many = int(input("How many do you want?:  "))
    if choose_Pro == 1:
        cake(request_Money, how_many)
        print("Account:", request_Money)
        print("1-Cake({0:}): 5TL \n2-Water({1:}): 1TL \n3-Popcorn({2:}): 4TL \n4-Coke({3:}): 3TL \n5-Biscuit({4:}): 2TL".format(caket, watert, popcornt, coket, biscuitt))
    elif choose_Pro == 2:
        water(request_Money, how_many)
        print("Account:", request_Money)
        print("1-Cake({0:}): 5TL \n2-Water({1:}): 1TL \n3-Popcorn({2:}): 4TL \n4-Coke({3:}): 3TL \n5-Biscuit({4:}): 2TL".format(caket, watert, popcornt, coket, biscuitt))
    elif choose_Pro == 3:
        popcorn(request_Money, how_many)
        print("Account:", request_Money)
        print("1-Cake({0:}): 5TL \n2-Water({1:}): 1TL \n3-Popcorn({2:}): 4TL \n4-Coke({3:}): 3TL \n5-Biscuit({4:}): 2TL".format(caket, watert, popcornt, coket, biscuitt))
    elif choose_Pro == 4:
        coke(request_Money, how_many)
        print("Account:", request_Money)
        print("1-Cake({0:}): 5TL \n2-Water({1:}): 1TL \n3-Popcorn({2:}): 4TL \n4-Coke({3:}): 3TL \n5-Biscuit({4:}): 2TL".format(caket, watert, popcornt, coket, biscuitt))
    elif choose_Pro == 5:
        biscuit(request_Money, how_many)
        print("Account:", request_Money)
        print("1-Cake({0:}): 5TL \n2-Water({1:}): 1TL \n3-Popcorn({2:}): 4TL \n4-Coke({3:}): 3TL \n5-Biscuit({4:}): 2TL".format(caket, watert, popcornt, coket, biscuitt))
    else:
        print("Please enter the correct item number!")
    x = input("Do you want to order again? {YES=y---NO=n}")
    if x == "Y" or x=="y":
        print("You can increase the amount of money you want to see in the machine. Enter how much you want to see in the machine and then If you are going to add money to the machine, the number you will enter into the machine should be the sum of the money you will add and your current money.")
        choosing = True
    elif x =="N" or x=="n":
        print("Account: 0 ----- Have a good day -----")
        break

        