from domain.Vanzare2 import toString
from logic.service import adaugareVanzare, stergereVanzare, modificareVanzare
from logic.discount import aplicareDiscount


def printMenu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount")
    print("a. Afisare vanzari")
    print("x. Iesire")


def uiAdaugaVanzare(lista):
    id = input("Specificati id-ul: ")
    titlu_carte = input("Specificati titlul cartii: ")
    gen_carte = input("Specificati genul cartii: ")
    pret = input("Specificati pretul cartii: ")
    tip_reducere_client = input("Specificati tipul de reducere: ")
    return adaugareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista)


def uiStergeVanzare(lista):
    id = input("Specificati id-ul vanzarii de sters: ")
    return stergereVanzare(id, lista)


def uiModificaVanzare(lista):
    id = input("Specificati id-ul vanzarii de modificat: ")
    titlu_carte = input("Specificati un nou titlu cartii: ")
    gen_carte = input("Specificati un nou gen cartii: ")
    pret = float(input("Specificati un nou pret cartii: "))
    tip_reducere_client = input("Specificati un nou tip de reducere: ")
    return modificareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista)


def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))


def uiAplicareDiscount(lista):
    return aplicareDiscount(lista)


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Specificati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaVanzare(lista)
        elif optiune == "2":
            lista = uiStergeVanzare(lista)
        elif optiune == "3":
            lista = uiModificaVanzare(lista)
        elif optiune == "4":
            lista = uiAplicareDiscount(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print ("Optiunea este invalida!")