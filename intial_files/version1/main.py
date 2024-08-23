import random
import art
from game_data import data


def pick_people(num):
    """
    Here you can random pick people from the list data.
    :param num: List[dict]
    :return: List[dict]
    """
    people_list = random.choices(data, k=num)
    return people_list


def comp(person1, person2, choice_l):
    """
    Here when you choose one person which you think that will have higher count
    , it will compare your choice with the rest one. If your choice is right,
    it returns True, else, it returns False.
    :param person1: dictionary
    :param person2: dict
    :param choice_l: str
    :return: bool
    """
    if choice_l == 'A':
        if person1['follower_count'] > person2['follower_count']:
            return True
        else:
            return False
    elif choice_l == 'B':
        if person1['follower_count'] < person2['follower_count']:
            return True
        else:
            return False


def info(people1, people2):
    """
    Here we organize information of people1 and people2 and print them out
    :type people1: dictionary
    :type people2: dict
    :return: none
    """
    print(f"Compare A: {people1['name']}, a {people1['description']}, from {people1['country']}.")
    print(art.vs)
    print(f"Against B: {people2['name']}, a {people2['description']}, from {people2['country']}.")


score = 0
choice = ''
res = True
while res:
    print(art.logo)
    # Once you are right, it will print your new score.
    if score > 0:
        print(f"You're right! Current score: {score}.")
    # Here use the function pick_people to random pick 2 people, it is a list
    # The result will be assigned to a variable people
    # The first one is 'A', The second one is 'B'.
    people = pick_people(2)
    A = people[0]
    B = people[1]
    info(A, B)
    choice = input("Who has more followers? Type 'A' or 'B': ")
    # The comparison result will be assigned to variable res.
    res = comp(A, B, choice)
    # if res is True, score will be increased by 1
    # if not True, your final score will be print out and game over!
    if res:
        score += 1
        print('\n' * 20)
    else:
        print('\n' * 20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}. Game Over!")
        print('\n' * 5)
        break