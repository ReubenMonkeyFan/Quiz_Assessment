
def question_ask(question, answer):
    error = "Please enter a valid answer"
    global score
    while True:
        try:
            response = (input(question))
            if response == answer:
                print("Well Done! That was correct!")
                score += 1
                return response
            elif response != "a" and response != "b" and response != "c":
                print(error)

            else:
                print("Sorry, your answer is incorrect")
                return response
        except ValueError:
            print(error)



# variables


score = 0


# main routine
q1 = question_ask("What is the capital of Belarus?\n a. Minsk \n b. Kyiv \n c. Helsinki \n Answer here: ", "a")
q2 = question_ask("How many total countries are in Europe?\n a. 51 \n b. 47 \n c. 44 \n Answer here: ", "c")
print(score)
