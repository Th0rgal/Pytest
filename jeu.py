from random import randint

target = randint (0, 10)
tries = 10
print("Attention tu n'auras que " + str(tries) + " essais")


for i in range (1, tries+1):
    user_input = int(input("rentre un nombre:"))

    remaining_trials =  str(tries-i)

    if user_input == target:
        print("super tu as trouvé!!! <3")
        break
    elif user_input < target:
        print("c'est trop petit, il te reste " + remaining_trials + " essais")
    else:
        print("c'est trop grand, il te reste " + remaining_trials + " essais")

else:
    print("Tu n'as pas trouvé en 10 essais, tu mérites la mort")
