from domain.Vanzare2 import getPret, getTitluCarte, getGenCarte
from logic.service import getById, adaugareVanzare
from logic.discount import aplicareDiscount


def testAplicareDiscount():
    lista = []
    lista = adaugareVanzare("1", "Stan si Bran", "comedie", 20, "silver", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 40, "gold", lista)
    lista = adaugareVanzare("3", "Castig la lotto", "povesti", 50, "none", lista)

    lista = aplicareDiscount(lista)

    assert getPret(getById("1", lista)) == 19
    assert getPret(getById("2", lista)) == 36
    assert getPret(getById("3", lista)) == 50