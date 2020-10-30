import time, os
def main():
    
    factory = ["fiets"]
    distribution = []
    shop = []


    print("Factory: " + str(factory))
    print("Distrubution: " + str(distribution))
    print("Shop: " + str(shop))
    print("==============")
    
    if len(factory) > 0:
        
        x = factory.pop(0)
        time.sleep(1)
        distribution.append(x)
        print("Factory: " + str(factory))
        print("Distrubution: " + str(distribution))
        print("Shop: " + str(shop))
        print("==============")
    
    
    if len(distribution) > 0:
        x = distribution.pop(0)
        time.sleep(1)
        shop.append(x)
        print("Factory: " + str(factory))
        print("Distrubution: " + str(distribution))
        print("Shop: " + str(shop))
        print("==============")

    os.system('clear')
    
main()

retry = input("Wil jij dit progamma opnieuw proberen? Y/N: ").upper()
while True:
    if retry == "Y" or retry == "N":
        if retry == "Y":
            main()
            retry = input("Wil jij dit progamma opnieuw proberen? Y/N: ").upper()
        else :
            os.system('cls')
            print("Dankjewel")
            break
    else:
        print("Type Y/N in")
        retry = input("Wil jij dit progamma opnieuw proberen? Y/N: ").upper()
    




