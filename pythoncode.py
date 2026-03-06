print("Welcome to Mohammed Al Nakeeb's (10701153) number list test!")
while True:
    choice = str(input("Please Select a difficulty: [E]asy , [M]edium, [H]ard.\n:")).lower()
    if choice == "e":
        print("Easy Mode selected!\n")
        questions = 4
        quantity = 3
        minimum = 5
        maximum = 10
        break
    elif choice == "m":
        print("Medium Mode selected!\n")
        questions = 5
        quantity = 4
        minimum = 5
        maximum = 10
        break
    elif choice == "h":
        print("Hard Mode selected!\n")
        questions = 6
        quantity = 5
        minimum = 10
        maximum = 20
        break
    else:
        print("Invalid choice please selected either 'e', 'm', 'h'")

print(f"Your test will have {questions} questions using lists of {quantity} numbers between {minimum} and {maximum}.")
print("The last question is a challenge question and will have twice as many numbers!\n")
input("Press Enter to Begin!")