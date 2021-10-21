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
    print("ADD RULES HERE")

 #main routine is here

played_before = yes_no("Have you played before? ")

if played_before == "no":
    instructions()

print("Program Continues")


