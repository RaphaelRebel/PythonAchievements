verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2 
km_per_maand = 100
maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand

def main():
    while True:
        km_per_maand = input("Voer een getal in: ")
        try:
            if type(int(km_per_maand)) == int:
                print("Ja, de invoer " + str(km_per_maand) + " is een getal, want ik kan het omzetten naar een float")
                #print("De maandkosten zijn: "+str(maandkosten))
                return maandkosten
                break
            elif type(str(km_per_maand)) == str:
                print("Je moet een getal invullen")
        except ValueError:
            print("Je moet een getal invullen")
        
print(main())
