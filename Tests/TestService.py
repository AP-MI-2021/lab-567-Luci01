from domain.Vanzare2 import getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient
from logic.service import adaugareVanzare, getById, stergereVanzare, modificareVanzare


def testAdaugareVanzare():
    lista = []
    lista = adaugareVanzare("1", "Stan si Bran", "comedie", 20, "gold", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getTitluCarte(getById("1", lista)) == "Stan si Bran"
    assert getGenCarte(getById("1", lista)) == "comedie"
    assert getPret(getById("1", lista)) == 20
    assert getTipReducereClient(getById("1", lista)) == "gold"

def testStergereVanzare():
    lista = []
    lista = adaugareVanzare("1", "Stan si Bran", "comedie", 20, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 30, "silver", lista)

    lista = stergereVanzare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

def testModificareVanzare():
    lista = []
    lista = adaugareVanzare("1", "Stan si Bran", "fantastic", 20, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 30, "silver", lista)

    lista = modificareVanzare("1", "Moara cu Noroc", "realist", 15, "none", lista)

    vanzareModificata = getById("1", lista)
    assert getId(vanzareModificata) == "1"
    assert getTitluCarte(vanzareModificata) == "Moara cu Noroc"
    assert getGenCarte(vanzareModificata) == "realist"
    assert getPret(vanzareModificata) == 15
    assert getTipReducereClient(vanzareModificata) == "none"

    vanzareNemodificata = getById("2", lista)
    assert getId(vanzareNemodificata) == "2"
    assert getTitluCarte(vanzareNemodificata) == "Razboiul Stelelor"
    assert getGenCarte(vanzareNemodificata) == "fictiune"
    assert getPret(vanzareNemodificata) == 30
    assert getTipReducereClient(vanzareNemodificata) == "silver"

def testGetById():
    lista = []
    lista = adaugareVanzare("1", "Stan si Bran", "comedie", 20, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 30, "silver", lista)
    assert getById("1", lista) == lista[0]
    assert getById("2", lista) == lista[1]
    assert getById("3", lista) is None



