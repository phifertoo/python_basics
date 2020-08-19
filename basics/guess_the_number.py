import random
print('What is your name?')
name = input()
secretNumber = random.randint(1,20)
print(name + ', I am thinking of a number between 1 and 20')

for guessTaken in range (1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job ' + name + '! You guessed my number')
else:
    print('No more guess. I was thinking of ' + secretNumber)