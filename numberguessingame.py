import random

print("welcome to the guess the number game")
while True:
    secretnumber = random.randint(1,30)
    attempts = 0
    print("\nI've picked a number between 1 and 30. Try to guess it!")
    while True:
        userinput = int(input("enter your number"))
        attempts+=1
        if userinput<secretnumber:
            print("too low.....")
        elif userinput>secretnumber:
            print("too high.....")
        else:
            print(f"yah!..you have guessed the number {secretnumber} in {attempts} attempts")
            break
    
    play_again = input("Do you want to play again? (yes/no): ").upper()
    if play_again != "YES":
        print("Thank you for playing! Goodbye.")
        break