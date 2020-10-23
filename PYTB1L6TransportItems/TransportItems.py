import time, os
def main():
    
    factory = ["car"]
    distribution = []
    shop = []

    os.system('cls')

    print("Factory[car]")
    print("distribution[]")
    print("shop[]")

    if len(factory) > 0:
        factory.clear()
        time.sleep(1)
        distribution.append("car")
        print("Factory[]")
        print("distribution[car]")
        print("shop[]")
    os.system('cls')
    if len(distribution) > 0:
        factory.clear()
        time.sleep(1)
        shop.append("car")
        print("Factory[]")
        print("distribution[]")
        print("shop[car]")
    os.system('cls')
main()
retry = input("Wil jij dit progamma opnieuw proberen? Y/N: ").upper()
while True:
    if retry == "y".upper() or retry == "n".upper():
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
    




