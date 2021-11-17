from logic.service import *
from domain.Vanzare import *


def runAdd(params, lista):
    lista = adaugareVanzare(params[0], params[1], params[2], params[3], params[4], lista)
    return lista


def runDelete(id, lista):
    lista = stergereVanzare(id, lista)
    return lista


def runModificare(params, lista):
    lista = modificareVanzare(params[0], params[1], params[2], params[3], params[4], lista)
    return lista


def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))


def print_usage():
    usage = """
    Adaugare: add [id] [titlu carte] [gen] [pret] [tip reducere client]
    Stergere: delete [id]
    Modificare: update [id] [titlu carte] [gen] [pret] [tip reducere client]
    Afisare: showAll

    Meniu: help
    Iesire: exit
    """
    print(usage)


def runCli(lista):
    print_usage()
    shouldRun = True

    while shouldRun:
        optiuni = input("Dati optiunea cu parametrii separati prin virgula: ")
        optiuni = optiuni.split(";")

        try:
            for optiune in optiuni:
                optiune = optiune.split(",")

                if optiune[0] == "exit":
                    shouldRun = False
                    break
                elif optiune[0] == "help":
                    print_usage()
                elif optiune[0] == "showAll":
                    showAll(lista)

                elif optiune[0] == "add":
                    lista = runAdd(optiune[1:], lista)
                elif optiune[0] == "delete":
                    lista = runDelete(optiune[1], lista)
                elif optiune[0] == "update":
                    lista = runModificare(optiune[1:], lista)

                else:
                    print("Optiunea nu exista!")
        except Exception as error:
            print(f"Eroare: {error}")