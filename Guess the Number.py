import  random
number=random.randint(1,10)
guess = -1

print('Guess The Number!')
while guess != number :
    guess=int(input('Input Number: '))
    if guess == number :
        print('Correct, You Got it !')
    elif guess < number :
        print('Number more than',guess)
    elif guess > number :
        print('Number less than',guess)