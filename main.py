from logic.service import adaugareVanzare
from Tests.alltests import runAllTests
from UserInterface.UI import runMenu
from UserInterface.cli import runCli

def main():
    runAllTests()
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    lista = adaugareVanzare("3", "Dune", "fictiune", 80, "none", lista)
    lista = adaugareVanzare("4", "Stan si Bran", "comedie", 20, "silver", lista)
    runMenu(lista)

main()