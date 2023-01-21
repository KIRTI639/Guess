import random         #Used to get random number
import math            #Used to import module 'math'
import sys              #Used for exiting program
import os               #Used for Clear Screen, to find path of the file
import Guess        #Used to import module 'Guess'

#Screen for selecting any option
def screen():
    print("\n\t1: Play Guessing")
    print("\t2: Highest Score")
    print("\t3: Current Score")
    #print("\t4: Difficulty Level")
    print("\t5: Need Help...?")
    print("\t6: About Game")
    print("\t7: Exit")
    choice=int(input("\n\tEnter Choice : "))
    return choice

def level():
    print("\n\t'Difficulty Level' function is currently not available in this version. We will upgrade this soon.")
    print("\t\tStay Safe! Stay Home!")
    input()
    
def helpme():
    print("\n\t==> FAQs :\n")
    print("\t1 : How to play this game ?")
    print("\t2 : How can I increase my score ?")
    print("\t3 : What about Difficulty Level ?")
    print("\t4 : Ask a question")
    print("\t5 : Go Back")
    ch = int(input("\n\tPlease select any option : "))
    return ch

def about():
    help(Guess)
    input()

def faq1():
    print("\n--> FAQs / How to Play the Guessing Game ?")
    print("\n\tFirst of all, computer will get a random number between (lower bound & upper bound)")
    print("\t using random module and stored in a variable.")
    print("\tThen a player will guess the number in a range of lower and upper bound.")
    print("\tIf player guesses the correct number, player will win the game, the game will be ended ")
    print("\tand final score will be stored in a .txt file")
    print("\tOtherwise, player lose the game and current score will store in .txt file.")
    input()

def faq2():
    print("\n--> FAQs / How can I increase my score ?")
    print("\n\tIf you are absolute beginner, you should play in 'Easy' mode. So that you can perform")
    print("\tyour best.")
    print("\tGradually, you can switch to 'Medium' level and then 'Hard' level.")
    input()

def faq3():
    print("\n--> FAQs / What about Difficulty Level ?")
    print("\n\tThese are the different different modes in which player can choose the level of game.")
    print("\tThere are three type of levels such as - 'Easy', 'Medium' and 'Hard'.")
    print("\tWe recommend you to play in 'Easy' mode. Therefore you can make good score.")
    input()

def ask_ques():
    if os.path.exists('Data.txt'):
        name = input("\n\tPlease Enter Username : ")
        message = input("\tEnter your queries : ")
        f = open('Data.txt','a')
        string = name+','+message
        f.write(string)
        f.write("\n")
        f.close()
        print("\n\tThanks for connecting us. We are happy to connect with you!")
        input()
    else:
        name = input("\n\tPlease Enter Username : ")
        message = input("\tEnter your queries : ")
        f = open('Data.txt','w')
        string = name+','+message
        f.write(string)
        f.write("\n")
        f.close()
        print("\n\tThanks for connecting us. We are happy to connect with you!")
        input()
        
#Get the hight score from the file
def high():
    if os.path.exists('High.txt'):
        size=os.path.getsize('High.txt')
        if size==0:
            return 0
        else:
            f=open('High.txt')
            h=f.read()
            h=int(h)
            return h
    else:
        f=open("High.txt","w")
        return 0

#Get the current score from the file
def current():
    f=open('Current.txt')
    c=f.readline()
    print('\tLast Score is :',c)
    input()

def diff_level():
    print("\n\t1: Easy")
    print("\t2: Medium")
    print("\t3: Hard")
    diff = int(input("\tPlease select any one : "))
    if diff>=1 and diff<=3:
        return diff
    else:
        print("\tPlease enter 1, 2, or 3")
        input()
        diff_level()

def play():
    diff = diff_level()
    if diff==1:
        lower = 1
        upper = 10
        multi = 60
    elif diff==2:
        lower = 1
        upper = 100
        multi = 45
    elif diff==3:
        lower = 1
        upper = 400
        multi = 30
    x = random.randint(lower, upper)
    chances = round(math.log(upper - lower + 1, 2))
    print("\n\tYou've only ",chances," chances to guess the number!\n")
    count = 0
    # Guesses depends upon range
    while count < round(math.log(upper - lower + 1, 2)):
        count += 1
        score=1000 - (count-1)*multi
        print("\tGuess a number between {} and {} :- ".format(lower,upper),end='')
        guess = int(input("\t"))
        if x == guess:
            if count==1:
                print("\n\tCongratulations you did it in {}st try.".format(count))
                print("\tYour Score is :",score)
            elif count == 2:
                print("\n\tCongratulations you did it in {}nd try.".format(count))
                print("\tYour Score is :",score)
            elif count == 3:
                print("\n\tCongratulations you did it in {}rd try.".format(count))
                print("\tYour Score is :",score)
            else:
                print("\n\tCongratulations you did it in {}th try.".format(count))
                print("\tYour Score is :",score)
            L=[]
            h=high()
            if score < h:
                L.append(h)
                L.append(score)
                m=max(L)
                f1 = open('Current.txt','w')
                f2 = open('High.txt','w')
                s=str(score)
                #h=str(h)
                f1.write(s)
                f1.close()
                f2.write(str(m))
                f2.close()
            else:
                f1 = open('Current.txt','w')
                f2 = open('High.txt','w')
                s=str(score)
                f2.write(s)
                f2.close()
                f1.write(s)
                f1.close()    
            break
        elif x > guess:
            print("\tYou guessed too small!")
            chances-=1
            print("\tRemaining Chances :",chances)
        elif x < guess:
            print("\tYou Guessed too high!")
            chances-=1
            print("\tRemaining Chances :",chances)
        if count >= round(math.log(upper - lower + 1, 2)):
            print("\n\tThe number is %d" % x)
            print("\tBetter Luck Next time!")
            f1 = open('Current.txt','w')
            f1.write('0')
            f1.close()
    input()
    
#Main Body :- Program starts from here....
def main():
    while True:
        os.system("cls")       #It clears the screen.
        m = screen()
        if m==1:
            play()
        elif m==2:
            h=high()
            print("\tHigh Score is :",h)
            input()
        elif m==3:
            current()
        elif m==4:
            level()
        elif m==5:
            while True:
                os.system("cls")
                ans = helpme()
                if ans==1:
                    faq1()
                    #input()
                elif ans==2:
                    faq2()
                elif ans==3:
                    faq3()
                elif ans == 4:
                    ask_ques()
                elif ans==5:
                    main()
                else:
                    print('\tInvalid Choice...! Please Enter Valid Choice.')
                    input()
        elif m==6:
            about()
        elif m==7:
            sys.exit()
        else:
            print('\tInvalid Choice...! Please Enter Valid Choice.')
            input()

main()
 
