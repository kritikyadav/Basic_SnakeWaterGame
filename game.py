'''Snake Water Game'''
import random
win=0
lose=0
same=0
i=1
print("There are 10 Rounds in this game\nAfter 10 rounds this game will automatically terminate")
while(i<=10):
    l=["Snake","Water","Gun"]
    a=random.choice(l)
    n=int(input('''
Enter 1 for Snake
Enter 2 for Water
Enter 3 for Gun
'''))
    if n==1:
        if a=="Snake":
            print("Snake   VS   Snake")
            print(".....same_pinch......")
            same = same+1
        elif a=="Water":
            print("Water   VS    Snake")
            print(".......You Win.......")
            win = win+1
        elif a=="Gun":
            print("Gun    VS     Snake")
            print("......You Lose......")
            lose = lose+1
    elif n==2:
        if a=="Snake":
            print("Snake   VS   Water")
            print("......You Lose......")
            lose = lose+1
        elif a=="Water":
            print("Water   VS    Water")
            print(".....same_pinch......")
            same = same+1
        elif a=="Gun":
            print("Gun    VS     Water")
            print(".......You Win.......")
            win = win+1
    elif n==3:
        if a=="Snake":
            print("Snake   VS   Gun")
            print(".......You Win.......")
            win = win+1
        elif a=="Water":
            print("Water   VS    Gun")
            print("......You Lose......")
            lose = lose+1
        elif a=="Gun":
            print("Gun    VS     Gun")
            print("......same_pinch......")
            same = same+1
    else:
        print("Invalid input. Try again")
        continue
    print("Wins= ", win)
    print("Lose= ", lose)
    print("Same= ", same)
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    i+=1
