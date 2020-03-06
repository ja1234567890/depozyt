

import random



for i in range(3):
    print("próba:", i+1, "z 3")
    print("wytypuj wynik:")
    typ = input()
    liczba = random.randint(1, 9)
    print("wylosowana liczba:", liczba)

    if typ != liczba:
        print("niestety nie tym razem")



    else:
        print("wylosowana liczba:", liczba)
        print("gratulacje wygrałes koniec programu")
        break
