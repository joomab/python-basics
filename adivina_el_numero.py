import random

def run():
    random_number = random.randint(1,100)

    number = int(input("Elige un número del 1 al 100: "))

    while number != random_number:
        if number < random_number:
            print("Pon un número más grande") 
        else:
            print("Es un número más pequeño")
        
        number = int(input("Elige otro número: "))
    
    print("Ganaste")


if __name__ == "__main__":
    run()