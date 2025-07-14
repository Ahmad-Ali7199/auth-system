def recovery_mode():
    real_password = "Riphah"
    print("Recovery mode")
    print("1.Recover your password")
    print("2.No")
    mode = input("Choose from given options : ")
    if mode == "1":
        while True:
            print("Recover your password from : ")
            print("1.Backup Security Question")
            print("2.Backup Pin")
            print("3.Exit")
            recover_password = input("Choose option from the given list : ")
            if recover_password == "1":
                print("Only one chance to attempt security question otherwise your program is automatically off")
                print("What is your favourite subject ?")
                security_q = input("Answer of the given question : ")
                if (security_q == "Programming fundamentals" or security_q == "programming fundamentals"
                        or security_q == "pf" or security_q == "PF"):

                    print("Your answer is correct")
                    print("Successfully you recovered your password")
                    print("Your password is '", real_password, "'")
                    a = 4
                    break
                else:
                    print("Your password is incorrect ")
                    exit()
            elif recover_password == "2":
                print("Only one chance to attempt backup pin otherwise your program is automatically off")
                backup_pin = input("Enter your backup pin : ")
                if backup_pin == "12345":
                    print("Your pin is correct")
                    print("Successfully you recovered your password")
                    print("Your password is '", real_password, "'")
                    a = 4
                    break
                else:
                    print("Your pin is incorrect")
                    exit()
            elif recover_password == "3":
                exit()
            else:
                print("Invalid input")
    elif mode == "2":
        print("Exit from recovery mode")
    else:
        print("Invalid input")
