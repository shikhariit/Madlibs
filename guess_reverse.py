import random
low = 1
high = 10
feedback = ''
while feedback != 'c':
    guess = random.randint(low, high)
    feedback = input("Is {} is too high(h) or too low(l) or correct(c): ".format(guess))
    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
print("I guessed it right")
