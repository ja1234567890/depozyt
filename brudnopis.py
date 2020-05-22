import requests
import requests.exceptions
from bs4 import BeautifulSoup

def pobierz_dane():
    waluty_xml = requests.get('http://www.nbp.pl/kursy/xml/LastA.xml')
    waluty_xml.encoding = 'ISO-8859-2'
    waluty_soup = BeautifulSoup(waluty_xml.text, 'html.parser')
    data = waluty_soup.data_publikacji.string
    waluty = {'data': data}

    for pozycja in waluty_soup.find_all('pozycja'):
        kod = pozycja.kod_waluty.string
        nazwa = pozycja.nazwa_waluty.string
        przelicznik = int(pozycja.przelicznik.string)
        kurs = float(pozycja.kurs_sredni.string.replace(',', '.'))
        waluty[kod] = {'nazwa': nazwa, 'przelicznik': przelicznik, 'kurs': kurs}

    return waluty

def dwa():

    waluty_xml = requests.get('http://www.nbp.pl/kursy/xml/LastA.xml')
    waluty_xml.encoding = 'ISO-8859-2'
    waluty_soup = BeautifulSoup(waluty_xml.text, 'html.parser')
    data = waluty_soup.data_publikacji.string
    waluty = {'data': data}
    print("doprzeliczenia:", doprzeliczenia, "poprzeliczeniu:", poprzeliczeniu, "kwota:", kwota)






def waluta1 (doprzeliczenia):
    waluty_xml = requests.get('http://www.nbp.pl/kursy/xml/LastA.xml')
    waluty_xml.encoding = 'ISO-8859-2'
    waluty_soup = BeautifulSoup(waluty_xml.text, 'html.parser')
    data = waluty_soup.data_publikacji.string
    waluty = {'data': data}
    for pozycja in waluty_soup.find_all('pozycja'):
        if pozycja.kod_waluty.string == doprzeliczenia:
            kod1 = pozycja.kod_waluty.string
            nazwa1 = pozycja.nazwa_waluty.string
            przelicznik1 = int(pozycja.przelicznik.string)
            kurs1 = float(pozycja.kurs_sredni.string.replace(',', '.'))
            waluty[kod1] = {'nazwa': nazwa1, 'przelicznik': przelicznik1, 'kurs': kurs1}  # ?????
            wynik1 = przelicznik1 * kwota * kurs1
            print("wynik1:", wynik1, "przelicznik1:",przelicznik1, "kurs1:", kurs1)
            return (wynik1)

def waluta2 (poprzeliczeniu):
    waluty_xml = requests.get('http://www.nbp.pl/kursy/xml/LastA.xml')
    waluty_xml.encoding = 'ISO-8859-2'
    waluty_soup = BeautifulSoup(waluty_xml.text, 'html.parser')
    data = waluty_soup.data_publikacji.string
    waluty = {'data': data}
    for pozycja in waluty_soup.find_all("pozycja"):
        if pozycja.kod_waluty.string == poprzeliczeniu:
            kod2 = pozycja.kod_waluty.string
            nazwa2 = pozycja.nazwa_waluty.string
            przelicznik2 = int(pozycja.przelicznik.string)
            kurs2 = float(pozycja.kurs_sredni.string.replace(',', '.'))
            waluty[kod2] = {'nazwa': nazwa2, 'przelicznik': przelicznik2, 'kurs': kurs2}  # ?????
            wynik2 = przelicznik2 * kwota * kurs2
            print("wynik2:", wynik2, "przelicznik2:", przelicznik2, "kurs2:", kurs2)
            return(wynik2)






pobierz_dane()

print("wpisz symbol waluty, którą chcesz przeliczyć [złoty - PLN, Dolar Amerykański - USD itd.]")
doprzeliczenia = input().upper()
print("Wybrałeś {}".format(doprzeliczenia))


print("wpisz symbol waluty, na ktorą mam przeliczyć")
poprzeliczeniu = input().upper()
print("Wybrałeś {}".format(poprzeliczeniu))


print("wpisz kwotę jaką chcesz przeliczyć")
kwota = int(input())
print("Przeliczam {} {} na {}".format(kwota, doprzeliczenia, poprzeliczeniu))

dwa()
print(doprzeliczenia)

waluta1(doprzeliczenia)
waluta2(poprzeliczeniu)



wynik = wynik1/wynik2
print("Po przeliczeniu {} {} na {} otrzymujemy wynik: {} {} to {} {}".format(kwota, doprzeliczenia, poprzeliczeniu, kwota, doprzeliczenia, wynik, poprzeliczeniu))