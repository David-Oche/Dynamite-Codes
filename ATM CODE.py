#To write a code used in an ATM machine
name = input("Enter your username: \n")
qualifiedUsers = ["David","Jesse","Deki","Kelechi","Chisom","Ifeanyi","Ibekam","fortune"]
usersPassword = ["1111","2222","3333","4444","5555","6666","7777","8888"]
if(name in qualifiedUsers):
    userId = qualifiedUsers.index(name)
    password = input("Enter your password\n")
    if(password == usersPassword[userId]):
        print("Welcome %s" % name)
        print("")
        from datetime import date
        today = date.today()
        print("Today's Date is:", today)
        import time
        clock = time.strftime("%I:%M:%S")
        print("And The Time is:", clock)
        print("")
        print("1.   How much would you like to withdraw?")
        print("2.   How much would you like to deposit?")
        print("3.   Complaints")
        print("")
        user =int(input("Enter an option:"))
        if(user==1):
            input("How much would you like to withdraw?")
            print("Take your cash")
        elif(user==2):
            previousBalance=500
            deposit=int(input("How much would you like to deposit?\n"))
            currentBalance= previousBalance + deposit
            print(" Your Current Balance is:",currentBalance )
        elif(user==3):
            input("What issue would you like to report: ")
            print("Thank you for contacting us")
        else:
            print("Enter a correct option")
            print("")
    else:
        print("invalid password")
else:
    print("Sorry you are not a registerd user, sign up and try again.")

