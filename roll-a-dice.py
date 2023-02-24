import random


answer=input("Do you want to roll a dice or not? (y/n) ")
while answer.lower()=="y":
    num=random.randint(1,6)
    print("[-----]")
    # first row
    if num==5 or num==6 or num==4:
        print("[0   0]")
    elif num==2 or num==3:
        print("[0    ]")
    else:
        print("[     ]")
    #second row
    if num==1 or num==3 or num==5:
        print("[  0  ]")
    elif num==2 or num==4:
        print("[     ]")
    else:
        print("[0   0]")
    #third row
    if num==1:
        print("[     ]")
    elif num==2 or num==3:
        print("[    0]")
    elif num==4 or num==5 or num==6:
        print("[0   0]")
    print("[-----]")
    answer=input("press y to roll again, n to exit: ")
