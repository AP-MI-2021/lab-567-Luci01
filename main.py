from logic.service import adaugareVanzare
from Tests.runalltests import runAllTests
from UserInterface.UI import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugareVanzare("1", "Stan si Bran", "comedie", 20, "gold", lista)
    lista = adaugareVanzare("3", "Castig la lotto", "povesti", 50, "none", lista)
    runMenu(lista)

main()