import random



print("wytypuj wynik:")
typ = int(input())
liczba = random.randint(1, 9)





while liczba != typ:
    print("wylosowana liczba:", liczba)
    print("niestety nie tym razem")
    print("wytypuj wynik:")
    typ = int(input())
    liczba = random.randint(1, 9)

else:
    print("wylosowana liczba:", liczba)
    print("gratulacje wygrałes koniec programu")

