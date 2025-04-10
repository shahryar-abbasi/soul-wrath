print("welcome to the simulation game$$")

choice = int(input("""select action you want to perform
                    1-study
                    2-rest
                    3-workout                     
        """))

match choice:
    case 3:
        print("you want to work out...")
        workoutchoice = int(input("""you want to workout at home or in gym
                            1-home
                            2-gym
        """))
        if(workoutchoice == 1):
            print("you select to workout at home \ncrush it")
        elif(workoutchoice == 2):
            print("you select to workout at gym \n go for  it")
        else:("invalid choice....")
    case default:
        print("try again...")

print("task completed successfully....")