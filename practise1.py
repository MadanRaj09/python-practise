print("exam results")
marks = 140
if marks > 100:
    print("INVALID MARKS,marks cannot exceed 100")

elif marks >= 75 and marks <= 84:
    print("First class,good!!", marks)

elif marks >= 60 and marks <= 74:
    print("second class,keep it up!!",marks)

elif marks > 35 and marks < 60:
        print("third class,try harder!!", marks)

elif marks >= 85 and marks < 100:
    print("distinction,the leader!!",marks)

elif marks == 100:
    print("distinction,the Master!!",marks)

elif marks == 35:
    print("you have just passed")
    print("third class,try harder!!", marks)
else:
    print("you have failed",marks)
    print("better luck next time")

