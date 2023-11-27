import random

num_of_friends = int(input("Enter the number of friends joining (including you):\n"))
friends = {}

if num_of_friends < 1:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")
for i in range(num_of_friends):
    friends.update({input(): 0})

bill = int(input("Enter the total bill value:\n"))
for i in friends:
    friends.update({i: round(bill / num_of_friends, 2)})

lucky = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
match lucky:
    case "Yes":
        lucky_person = random.choice(list(friends.keys()))
        for i in friends:
            friends.update({i: round(bill / (num_of_friends - 1), 2)})
        friends.update({lucky_person: 0})
        print(f"{lucky_person} is the lucky one!")
    case _:
        print("No one is going to be lucky")

print(friends)