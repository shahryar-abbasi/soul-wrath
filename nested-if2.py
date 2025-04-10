score =int(input("enter your score"))
coins =int(input("enter your coins "))
time =float(input("enter your time"))
if score >= 100:
    if coins >=50:
        if time <=5:
            print("congrats level cleared $$")
        else:
            print("time exceeded")
    else:
        print("less coins $$")
else:
    print("low score")