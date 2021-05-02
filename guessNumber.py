import random 

print("Number Guessing Game")
print("Guess a number between 1 and 9")
lowComment = "Your guess was too low : Enter a number higher than "
congrats = "Congratulations !! You Won!!"
i = 0
while i < 5:
    randomNumber = random.randint(1, 30)
    inputedNumber = int(input("Guess a number : "))
    if(inputedNumber == randomNumber):
        print(lowComment ) 
    else :
        print(congrats)
        exit()
