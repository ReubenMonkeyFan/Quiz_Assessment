def question_ask(question,answer):

    response = int(input(question))
    if response == answer:
        print("Correct")
    else:
        print("Sorry that is incorrect")







q1 = question_ask("Whats 10 + 5 ", 15)
q2 = question_ask("Whats 3 x 4 ", 12)


