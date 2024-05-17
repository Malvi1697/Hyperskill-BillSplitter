import random

def get_number_of_friends():
    return int(input("Enter the number of friends joining (including you):\n"))

def get_friend_names(count):
    if count > 0:
        print("Enter the name of every friend (including you), each on a new line: ")
        return {input(): 0 for _ in range(count)}
    else:
        print("No one is joining for the party")
        return {}

def get_total_bill():
    return float(input("Enter total bill value:\n"))

def calculate_split(bill, number_of_friends, friends):
    split_amount = round(bill / number_of_friends, 2)
    for name in friends:
        friends[name] = split_amount
    return friends

def choose_lucky_friend(friends):
    if input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower() == 'yes':
        lucky_friend = random.choice(list(friends))
        if len(friends) > 1:
            bill_without_lucky = round(sum(friends.values()) / (len(friends) - 1), 2)
            for friend in friends:
                friends[friend] = bill_without_lucky
        friends[lucky_friend] = 0
        print(f"{lucky_friend} is the lucky one!")
    else:
        print("No one is going to be lucky")

def display_payments(friends):
    for name, amount in friends.items():
        print(f"{name} will pay {amount}")

def main():
    random.seed(20)
    number_of_friends = get_number_of_friends()
    if number_of_friends > 0:
        friends = get_friend_names(number_of_friends)
        total_bill = get_total_bill()
        friends = calculate_split(total_bill, number_of_friends, friends)
        choose_lucky_friend(friends)
        display_payments(friends)

if __name__ == "__main__":
    main()