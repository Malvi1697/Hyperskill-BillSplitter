import random
random.seed(20)

prompt = int(input("Enter the number of friends joining (including you):\n"))
print("")

friend_list = {}
total = 0

if prompt > 0:
    print("Enter the name of every friend (including you), each on a new line: ")
    for i in range(prompt):
        friend_name = input()
        friend_list[friend_name] = 0
    print("")
    total_bill = int(input("Enter total bill value:\n"))
    total = round(int(total_bill) / prompt, 2)
    for i in friend_list:
        friend_list[i] = total
    print("")
    prompt = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    if prompt == "Yes":
        friend_list_list = list(friend_list)
        random_person = random.choice(friend_list_list)
        total_lucky = round(total_bill / (len(friend_list_list) - 1), 2)
        for i in friend_list:
            friend_list[i] = total_lucky
        friend_list[random_person] = 0
        print("")
        print(random_person + " is the lucky one!")
        print("")
        print(friend_list)
    else:
        print("")
        print("No one is going to be lucky")
        print("")
        print(friend_list)
else:
    print("No one is joining for the party")
