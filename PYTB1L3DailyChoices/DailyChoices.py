# Introductie
print("Hallo! Ik ben Raphael en vandaag ga jij een dag in mijn leven mee maken.")
# Hier begint de eerste vraag
print("Je word wakker door je eigen wekker")
print("A: Je blijft slapen")
print("B: Je staat op")

keuze1 = input("Kies A of B: ").upper()

if keuze1 == "A":
        print("Je besluit te blijven slapen, maar later ga je toch maar naar school om nog de laatste uren te halen.")
elif keuze1 == "B":
        print("Je besluit op te staan en naar school te reizen.")
else:
        print("Type alsjeblieft alleen A of B in")
        
# Hier begint de tweede vraag

print("Maar voordat je naar school gaat moet je nog wel besluiten of je wat wilt eten.")
print("A: Je eet ontbijt")
print("B: Je gaat zo snel mogelijk naar school")

keuze2 = input("Kies A of B: ").upper()

if keuze2 == "A":
        print("Je besluit te ontbijten, je zal nu meer focused zijn voor de rest van de dag.")
elif keuze2 == "B":
        print("Je besluit zo snel mogelijk naar school te gaan. Je hebt niet gegeten maar je bent wel optijd")
else:
        print("Type alsjeblieft alleen A of B in")

# Hier begint de derde vraag

print("In de pauze kan je kiezen of je snel langs de Burger King wilt gaan, of dat je op school blijft.")
print("A: Je gaat langs de Burger King")
print("B: Je blijft op school")

keuze3 = input("Kies A of B: ").upper()

if keuze3 == "A":
        print("Je besluit naar de Burger King te gaan, Dit zaL je meer geld kosten dan nodig is.")
elif keuze3 == "B":
        print("Je besluit op school te blijven, dit zorgt ervoor dat je meer tijd heb om je klaar te maken.")
else:
        print("Type alsjeblieft alleen A of B in")

# Vierde vraag

print("Eenmaal thuis moet je besluiten of je gaat sporten")
print("A: Je gaat sporten")
print("B: Je blijft thuis")

keuze4 = input("Kies A of B: ").upper()

if keuze4 == "A":
        print("Je besluit te gaan sporten, hierdoor kan je weer zelfverzekerd de dag eindigen.")
elif keuze4 == "B":
        print("Je besluit thuis te blijven, hierdoor heb je meer tijd voor jezelf.")
else:
        print("Type alsjeblieft alleen A of B in")

print("Aan het einde van de dag moet je besluiten of je vroeg naar bed wilt gaan of met je vrienden wilt blijven gamen")
print("A: Je gaat optijd naar bed")
print("B: Je gaat gamen met de rest van je vrienden")

keuze5 = input("Kies A of B: ").upper()

if keuze5 == "A":
        print("Je besluit optijd naar bed te gaan, nu zal je zeker optijd opstaan morgen.")
elif keuze5 == "B":
        print("Je besluit te gaan gamen, misschien word je morgen niet optijd wakker maar je hebt wel herinneringen gemaakt met je vrienden.")
else:
        print("Type alsjeblieft alleen A of B in")
