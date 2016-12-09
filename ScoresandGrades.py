def enterScore():
    response = input("Please enter a score")
    return response

def evalutateScore(value):

    if int(value) in range(59,70):
        print "Score: " + str(value) + "; Your grade is D"
    elif int(value) in range(69, 80):
        print "Score: " + str(value) + "; Your grade is C"
    elif int(value) in range(79, 90):
        print "Score: " + str(value) + "; Your grade is B"
    elif int(value) in range(89, 101):
        print "Score: " + str(value) + "; Your grade is A"
    elif in(value) in range(0, 59):
        print "Please enter number above 59"


    print "Scores and Grades"
    for vaue in scores:
        evalutateScore(value)
