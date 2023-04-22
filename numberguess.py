import random
diff=input("Enter the diffculty of the game\n easy\n middle\n hard\n")
ran_val_easy=random.randint(1,100)
ran_val_middle= random.randint(1,1000)
ran_val_hard= random.randint(1,10000)
count=6
def easy():
    print("you have 1 to 100 number")
    for i in range (count):
            print("you have only ",count-i,"chance to guess the number")
            guess=int(input("Guess number: \n"))
            if ran_val_easy == guess :
                print("you guess it")
                break
            elif ran_val_easy > guess:
                print("Too small!")
            elif ran_val_easy < guess:
                print("Too high!")
    print("game over!!")
    print("The number is " , ran_val_easy)
def middle():
    print("you have 1 to 1000 number")
    for i in range (count):
        print("you have only ",count-i,"chance to guess the number")
        guess=int(input("Guess number: \n"))
        if ran_val_middle == guess :
            print("you guess it")
            print("game over!!")
            print("The number is " , ran_val_middle)
            break
        elif ran_val_middle > guess:
            print("Too small!")
        elif ran_val_middle < guess:
            print("Too high!")
    print("game over!!")
    print("The number is " , ran_val_middle)        
def hard():
    count=9
    print("you have 1 to 10000 number")
    for i in range (count):
        print("you have only ",count-i,"chance to guess the number")
        guess=int(input("Guess number: \n"))
        if ran_val_hard == guess :
            print("you guess it")
            print("game over!!")
            print("The number is " , ran_val_hard)
            break
        elif ran_val_hard > guess:
            print("Too small!")
        elif ran_val_hard < guess:
            print("Too high!")
    print("game over!!")
    print("The number is " , ran_val_hard)

# level
if(diff == 'easy'):
    easy()

elif(diff == 'middle'):
    middle()
elif(diff == 'hard'):
    hard()