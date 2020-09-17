from random import randint
#Vraag om username
username = input("Username:")

print("Username: %s" %username)

#Shuffle stats
randint(10,100)
randomNumber1 = randint(10,100)
randomNumber2 = randint(10,100)
randomNumber3 = randint(10,100)

print("Jumpforce: %d / 100" %randomNumber1)
print("Speed: %d / 100" %randomNumber2)
print("Strength: %d / 100" %randomNumber3)

print("Special Power:")
print("1. Teleportation")
print("2. Super strenth")
print("3. Time travel")
print("4. Telekinises")
print("5. Invulnerability")

SP = input("Choose 1, 2, 3, 4 or 5: ")
if SP == "1":
    print("Teleportation")

elif SP == "2":
    print("Super strength")

elif SP == "3":
    print("Time travel")

elif SP == "4":
    print("Telekinises")

elif SP == "5":
    print("Invulnerability")

else:
    print("Wrong input, try again.")



     
