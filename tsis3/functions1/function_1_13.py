import random
def is_number_correct(number):
    counter=1
    rand=random.randint(1,20)
    while True:
        if number==rand:
            print("Good job,"," ",name,"! ","You guessed my number in"," ",counter," guesses!",sep="")
            break
        elif number<rand:
            print("Your guess is too low.")
            print("Take a guess")
            number=int(input())
            counter+=1
        elif number>rand:
            print("Your guess is too high.")
            print("Take a guess")
            number=int(input())
            counter+=1
print("Hello! What is your name?")
name=input()
print("Well", name, "I am thinking of a number between 1 and 20.", sep=", ")
print("Take a guess.")
number=int(input())
is_number_correct(number)