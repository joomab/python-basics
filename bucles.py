""" contador = 0
print("2 elevado a "+ str(contador) + " es igual a: "+ str(2**contador)) """

def run():
    LIMIT = 10

    counter = 0
    pot_2 = 2**counter
    while pot_2 < LIMIT:
        print("2 elevado a "+ str(counter) + " es igual a: "+ str(pot_2))
        counter = counter + 1
        pot_2 = 2**counter
        

if __name__ == "__main__":
    run()