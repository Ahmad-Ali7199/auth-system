import time
from auto_password import *
from recovery import *
real_password = "Riphah"
a = 4
while True:
    i = 0
    while a > 0:
        print(a, "Chance only for attempt password ")
        user_password = input("Enter your password : ")
        if real_password == user_password:
            print("Your password is correct ")
            auto_generator()
            break
        else:
            print("your password is incorrect ")
            a -= 1
    print("Forget password")
    print("1.Yes")
    print("2.No")
    forget_password = input("Choose option from the given list :")
    if forget_password == "1" or forget_password == "Yes" or forget_password == "yes":
        recovery_mode()
    elif forget_password == "2" or forget_password == "No" or forget_password == "no":
        while i == 0:
            print("Again enter password")
            print("1.Yes")
            print("2.No")
            again_enter_password = input("Choose option from the given list :")
            if again_enter_password == "1" or again_enter_password == "Yes" or again_enter_password == "yes":
                print("You enter again password after wait of 10 seconds")
                time.sleep(10)
                a = 4
                i += 1
            elif again_enter_password == "2" or again_enter_password == "No" or again_enter_password == "no":
                exit()
            else:
                print("Invalid input")
    else:
        print("Invalid input")
