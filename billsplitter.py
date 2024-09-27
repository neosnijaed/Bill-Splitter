# write your code here
import random


def invite_friends():
    friends_count = int(input('Enter the number of friends joining (including you):\n'))
    if friends_count <= 0:
        print('\nNo one is joining for the party')
        return
    print('\nEnter the name of every friend (including you), each on a new line:')
    names = [input() for _ in range(friends_count)]
    split_bill(names)


def split_bill(names: list):
    bill_value = int(input('\nEnter the total bill value:\n'))
    split_value = round(bill_value / len(names), 2)
    names_bill = dict.fromkeys(names, split_value)
    pick_lucky(names_bill, bill_value)


def pick_lucky(names: dict, bill_value: float):
    if input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n') == 'No':
        print('No one is going to be lucky')
        print(names)
    else:
        lucky_one = random.choice(list(names.keys()))
        print(f'{lucky_one} is the lucky one!\n')
        lucky_split_value = round(bill_value / (len(names) - 1), 2)
        for key in names:
            if key == lucky_one:
                names[key] = 0
            else:
                names[key] = lucky_split_value
        print(names)


if __name__ == '__main__':
    invite_friends()
