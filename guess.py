import random
random_no = random.randint(1, 10)
guess = 0
while guess != random_no:
    guess = int(input("Guess a Number(from 1 to 10): "))
    if guess < random_no:
        print("Be Bold Increase Your Guess")
    elif guess > random_no:
        print("Don't Be Too Bold Decrease Your Guess")
print("JackPot computer too generated {}".format(guess))

