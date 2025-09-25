vanilla_points=0
chocolate_points=0


answer=input(" are you a), morning person or b a night person")
if answer=="a":
    vanilla_points+=1
elif answer=="b":
    chocolate_points+=1


answer=input(" would you rather a go outside or b stay inside.")
if answer=="a":
    vanilla_points+=1
elif answer=="b":
    chocolate_points+=1


answer=input("are you a an cat person or b a dog person")
if answer=="a":
    vanilla_points+=1
elif answer=="b":
    chocolate_points+=1


answer=input("do you a like hot weather or b like cold weather")
if answer=="a":
    vanilla_points+=1
elif answer=="b":
    chocolate_points+=1



answer=input("do you like a or A sprite or b coke")
if answer=="a":
    vanilla_points+=1
elif answer=="b":
    chocolate_points+=1
print(f"vanilla points = {vanilla_points}")
print(f"chocolate points = {chocolate_points}")
if chocolate_points> vanilla_points:
    print("you are a chocolate person.")
elif vanilla_points> chocolate_points and vanilla_points >=2:
    print("you are a vanilla person")
    





















