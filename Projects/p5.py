import random

print("     ________________________________     ")
print("     |                              |     ")
print("     |                              |     ")
print("     |       Penalty Shootout       |     ")
print("     |                              |     ")
print("_____|______________________________|_____")
print("")
print("")

score = 0

for i in range(0,5):
        options=["TL","BL","M","TR","BR"]
        computerOption = random.choice(options)

        userOption = input("where do you want to shoot? TL,TR,M,BL,BR") 

        if computerOption == userOption: 
            print("blocked")
        else:
            print("GOAL!!")
score += 1
print("your score:" + str (score))


