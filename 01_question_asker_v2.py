def question_ask(question,answer):
    error = "Please enter a whole number"
    while True:
        try:
            response = int(input(question))
            if response == answer:
                print("Correct")
                return response
            else:
                print("Sorry that is incorrect")
                return response
        except ValueError:
            print(error)










q1 = question_ask("Whats 9 + 10? ", 19)
q2 = question_ask("Whats 3 x 4? ", 12)


