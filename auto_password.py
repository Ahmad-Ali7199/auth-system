def auto_generator():
    print("Welcome to the auto-generated password maker")
    name = input("What is your name : ")
    while True:
        print("Which password you required :")
        print("1.Numbers")
        print("2.Alphabets")
        print("3.Alphanumeric")
        print("4.Exit")
        choose_option = input("Choose from given options : ")
        if (choose_option == "Numbers" or choose_option == "numbers" or
                choose_option == "NUMBERS" or choose_option == "1"):

            import random
            print("You can only receive a auto-generated password of up to 30 numbers ")
            print("Otherwise you face an error and you won't be able to get the password")
            password_length = int(input("How lengthy password you require : "))
            number = "012345678910111213141516171819"
            auto_password = number
            try:
                password = "".join(random.sample(auto_password, password_length))
                print("'", name, "' You choose the '", password_length, "' character password and your password is : '",
                      password, "'")
            except Exception as e:
                print("Error:", e)

        elif (choose_option == "Alphabets" or choose_option == "alphabets" or
              choose_option == "ALPHABETS" or choose_option == "2"):

            import random
            print("You can only receive a auto-generated password of up to 52 characters ")
            print("Otherwise you face an error and you won't be able to get the password")
            password_length = int(input("How lengthy password you require : "))
            alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alpha_l = "abcdefghijklmnopqrstuvwxyz"
            auto_password = alpha_l + alpha_u
            try:
                password = "".join(random.sample(auto_password, password_length))
                print("'", name, "' You choose the '", password_length, "' character password and your password is : '",
                      password, "'")
            except Exception as e:
                print("Error:", e)
        elif (choose_option == "Alphanumeric" or choose_option == "alphanumeric" or
              choose_option == "ALPHANUMERIC" or choose_option == "3"):

            import random
            print("You can only receive a auto-generated password of up to 67 alpha-numeric characters ")
            print("Otherwise you face an error and you won't be able to get the password")
            password_length = int(input("How lengthy password you require : "))
            alpha_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alpha_l = "abcdefghijklmnopqrstuvwxyz"
            number = "1234567890"
            symbols = "@$#*_"
            auto_password = alpha_l + alpha_u + number + symbols
            try:
                password = "".join(random.sample(auto_password, password_length))
                print("'", name, "' You choose the '", password_length, "' character password and your password is : '",
                      password, "'")
            except Exception as e:
                print("Error:", e)
        elif choose_option == "4" or choose_option == "Exit":
            print("Exit from the program")
            print("1.Yes")
            print("2.No")
            say = input("You really want to exit this program : ")
            if say == "1" or say == "Yes" or say == "yes":
                exit()

        else:
            print("Invalid input")
