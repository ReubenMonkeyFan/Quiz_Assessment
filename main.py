 #functions go here
def yes_no (question):
    valid = False
    while not valid:
        response = input(question).strip().lower()

        if response == "y" or response == "yes":
            response = "yes"
            return response


        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes or no")

def instructions():
    print()
    print("---- How To Play ----")
    print("You will be asked a series of questions about geography")
    print("You will be given 3 possible answers for each question")
    print("You will then enter the answer you think is right by entering either 'a' , 'b' or 'c'")
    print("Try your best to answer every question correctly")
    print()


def question_ask(question, answer):
    error = "Please enter a valid answer"
    global score
    while True:
        try:
            response = (input(question)).lower()
            if response == answer:
                print("Well Done! That was correct! \n Your current score is {}".format(score + 1))
                score += 1
                return response
            elif response != "a" and response != "b" and response != "c":
                print(error)

            else:
                print("Sorry, your answer is incorrect. The correct answer was {} \n Your current score is {} ".format(answer, score))
                return response
        except ValueError:
            print(error)




 # variables

score = 0

 #main routine is here
print(" ---Welcome To The Geography Quiz!--- \n --------- Enjoy your stay ----------")
played_before = yes_no("Have you played before? ")
print()
if played_before == "no":
    instructions()

q1 = question_ask("What is the capital of Belarus?\n a. Minsk \n b. Kyiv \n c. Helsinki \n Answer here: ", "a")
q2 = question_ask("How many total countries are in Europe?\n a. 51 \n b. 47 \n c. 44 \n Answer here: ", "c")
q3 = question_ask("What is the cross on the english flag called?\n a. Saint Georges Cross \n b. Nordic cross  \n c. Maltese Cross \n Answer here: ", "a")
q4 = question_ask("What year did Swaziland change names to Eswatini?\n a. 2010 \n b. 2018\n c. 2017 \n Answer here: ", "b")
q5 = question_ask("What country has 3 capital cities?\n a. Canada \n b. England \n c. South Africa \n Answer here: ", "c")
q6 = question_ask("What year did the Berlin wall fall?\n a. 1988 \n b. 1989\n c. 1990 \n Answer here: ", "b")
q7 = question_ask("What countries capital city is Brussels?\n a. Belgium \n b. Portugal \n c. The Netherlands \n Answer here: ", "a")
q8 = question_ask("To the nearest 10 million, how big is Africa in square kilometers?\n a. 40 million \n b. 30 million\n c. 60 million \n Answer here: ", "b")
q9 = question_ask("When was The Treaty of Waitangi signed?\n a. 1820 \n b. 1830\n c. 1840 \n Answer here: ", "c")
q10 = question_ask("Which one of these countries is double landlocked?\n a. Tajikistan \n b. Pakistan \n c. Uzbekistan \n Answer here: ", "c")

print()
print(" Your total score is {} out of a possible 10 points!".format(score))



