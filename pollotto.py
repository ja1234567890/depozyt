def start():
    print("wybierz grę:")
    print("1. duży lotek")
    print("2. graj na własnych zasadach")
    print("0 - zakończ program")


start()
x = int(input())
print("wybieram: {}".format(x))

import random

if x == 0:
    print("The end")

if x == 1:

    print("wpisz 6 liczb z zakresu 1 - 49")
    lista = []

    i = 1
    while i < 7:
        typ = int(input("Podaj {} liczbę z 6 wybranych liczb: ".format(i)))
        if typ < 1 or typ > 49:
            print("WPISZ LCZBĘ Z PRZEDZIALU OD 1 DO 49")
        if typ > 0 and typ < 50 and lista.count(typ) == 0:
            lista.append(typ)
            i = i + 1
        else:
            print("Ta liczba została już wytypowana. Podaj inną.")

    lista = set(lista)
    print("wybrane przez Ciebie liczby to:", lista)

    liczby = set()
    i = 0
    while i < 6:
        liczba = random.randint(1, 49)
        if liczba not in liczby:
            liczby.add(liczba)
            i = i + 1


    print("wylosowane liczby to:", liczby)

    trafione = set(liczby & lista)

    if trafione != set():
        print("\nIlość trafień: %s" % len(trafione))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

if x == 2:
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    minliczba = int(input("Podaj minimalną losowaną liczbę: "))
    maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))


    if maksliczba < minliczba:
        print("Popraw maksymalną losowaną liczbę")

    if ileliczb >= (maksliczba - minliczba):
        print("Ilość typowanych liczb musi być mniejsza niż ilość liczb losowanych")
        

    else:
        print("Wytypuj %s liczb z przedziału %s do %s: " % (ileliczb, minliczba, maksliczba))


        liczby = []
        i = 0
        while i < ileliczb:
            typ = int(input("Podaj {} liczbę z {} wybranych liczb: ".format(i+1, ileliczb)))
            if typ < minliczba or typ > maksliczba:
                print("WPISZ LCZBĘ Z PRZEDZIALU OD {} DO {}".format(minliczba, maksliczba))
            if typ > (minliczba - 1) and typ < (maksliczba + 1) and liczby.count(typ) == 0:
                liczby.append(typ)
                i = i + 1
            else:
                print("Ta liczba została już wytypowana. Wybierz inna")

        liczby = set(liczby)
        print("Wybrane przez Ciebie liczby to:", liczby)

        wylosowane = set()
        i = 0
        while i < ileliczb:
            los = random.randint(minliczba, maksliczba)
            if los not in wylosowane:
                wylosowane.add(los)
                i = i + 1

        print("wylosowane liczby to: {}".format(wylosowane))

        trafy = set(wylosowane & liczby)

        if trafy != set():
            print("\nIlość trafień: %s" %len(trafy))
            print("Trafione liczby: ", trafy)
        else:
            print("Brak trafień. Spróbuj jeszcze raz")