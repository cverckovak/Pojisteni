from novy_uzivatel import Pojistenec
from databaze import Databaze

databaze = Databaze()

pokracovat = True
while pokracovat:

    print("___________________________\nEvidence pojištěných\n___________________________\n")
    akce = input("Vyber si akci:\n 1 - Pridat nového pojšteného\n 2 - Vypsat vsechny pojištěné\n 3 - Vyhledat pojištěného\n 4 - Konec\n")
    try:
        akce = int(akce)
    except:
        print("Neplatná volba")


    if akce == 1:
        print("Zvolili jste variantu 1 - Přidat nového pojištěného")
        jmeno = input("Zadejte jméno pojištěnce: ")
        prijmeni = input("Zadejte příjmení pojištěnce: ")
        vek = input("Zadejte věk pojištěnce: ")
        cislo = input("Zadejte telefoní číslo pojištěnce: ")

        databaze.pridej_pojistence(jmeno, prijmeni, vek, cislo)

    elif akce == 2:
        print("Zvolili jste variantu 2 - Vypsat vsechny pojištené")
        pojistenci = databaze.vrat_pojistence
        for index in databaze.vrat_pojistence():
            print(index.jmeno, index.prijmeni, index.vek, index.cislo)


    elif akce == 3:
        print("Zvolili jste variantu 3 - 3. Vyhledat pojištěného")
        hledany_jmeno = input("Zadej jméno: ")
        hledany_prijmeni = input("Zadej příjmení: ")
        for index in databaze.vrat_pojistence():
            if index.jmeno == hledany_jmeno and index.prijmeni == hledany_prijmeni:
                print(index)


    elif akce == 4:
        print("Ukončili jste program")


    nezadano = True
    while nezadano:
        odpoved = input("Přejete si pokračovat? Ano/Ne: \n")
        if (odpoved == "Ano" or odpoved == "ano"):
            nezadano = False
        elif (odpoved == "Ne" or odpoved == "ne"):
            nezadano = False
            pokracovat = False
        else:
            pass