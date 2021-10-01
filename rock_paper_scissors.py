import random

def main():
    user = input("Choose 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "It's a tie"
    if win(user, computer):
        return "You Won"
    return "You Lose"
def win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
print(main())

