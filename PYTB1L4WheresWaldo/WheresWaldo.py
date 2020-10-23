import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

for x in people:
    print(x)
    if x=="Waldo":
        waldopositie = people.index(x)
        print("Waldo zit op stoel nr: " + str(waldopositie))
        break
    
