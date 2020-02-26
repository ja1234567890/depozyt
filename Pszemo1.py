
def start():
    print("wybierz opcję:")
    print("1: oblicz deltę")
    print("2: lista w odwrotnej kolejności:")
    print("3: pogoda - Lodz")
    print("0 - zakończ")


start()
x = int(input())
print("wybieram {}".format(x))


if x not in [1,2,3]:
    print("wybierz liczbe z zakresu od 1 do 3")
else:
    print("ok, to robimy {}".format(x))

while x != 0:




    if x  == 1 :
        print("wpisz a:")
        a = int(input())
        print("wpisz b:")
        b = int(input())
        print("wpisz c:")
        c = int(input())
        delta = b ** 2 - 4 * a * c
        print("delta dla a={}, b={}, c={} jest równa: {}".format(a, b, c, delta))




    if x == 2 :
        print("Wpisz liste rzeczy do zrobienia downie:")
        print("1:")
        a = input()
        print("2:")
        b = input()
        print("3:")
        c = input()
        print(c, b, a)

    if x  == 3 :
        import requests
        screen = requests.get("http://wttr.in/lodz")
        print("start")
        print(dir(screen))
        print(screen.text)
        print(screen.headers)

    start()
    x = int(input())
    print("wybieram {}".format(x))
    if x not in [1,2,3]:
        print("wybierz liczbe z zakresu od 1 do 3")
    else:
        print("ok, to robimy {}".format(x))

try:
    x=1
    x=2
    x=3
except Exception as w:
    print("wybierz liczbe z zakresu od 1 do 3")
    print(w)


