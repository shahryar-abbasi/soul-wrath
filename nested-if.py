name = input("Enter your name: ")
passport = input("Do you have a valid passport? (Y/N): ").upper()
visa = input("Do you have a valid visa? (Y/N): ").upper()
ticket = input("Do you have a flight ticket? (Y/N): ").upper()

if passport == "Y":
    if visa == "Y":
        if ticket == "Y":
            print(f"{name}, you're ready to travel!")
        else:
            print(f"{name}, you need to book a flight ticket.")
    else:
        print(f"{name}, you need a valid visa.")
else:
    print(f"{name}, you must have a valid passport.")
