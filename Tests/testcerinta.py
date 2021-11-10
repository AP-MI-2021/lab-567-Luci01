from domain.Vanzare import getPret, getTitluCarte, getGenCarte, getId
from logic.service import getById, adaugareVanzare
from logic.cerinte import aplicareDiscount, modificareaGenuluiPentruTitlu, listaGenuri, pretMinimPentruFiecareGen, \
    ordonareCrescatorDupaPret, listaTitluriPentruFiecareGen, afisareNumarTitluriDistincte


def testAplicareDiscount():
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 20, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 60, "silver", lista)
    lista = adaugareVanzare("3", "Dune", "fictiune", 80, "none", lista)

    lista = aplicareDiscount(lista)

    assert getPret(getById("1", lista)) == 18
    assert getPret(getById("2", lista)) == 57
    assert getPret(getById("3", lista)) == 80

def testModificareaGenuluiPentruTitlu():
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    lista = adaugareVanzare("3", "Dune", "fictiune", 80, "none", lista)
    lista = adaugareVanzare("4", "Stan si Bran", "comedie", 20, "silver", lista)

    lista = modificareaGenuluiPentruTitlu("Stan si Bran", "povesti", lista)

    assert getGenCarte(getById("1", lista)) == "drama"
    assert getGenCarte(getById("3", lista)) == "fictiune"
    assert getGenCarte(getById("4", lista)) == "povesti"

def testListaGenuri():
    lista = []
    listaGen = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    lista = adaugareVanzare("3", "Dune", "fictiune", 80, "none", lista)
    lista = adaugareVanzare("4", "Stan si Bran", "comedie", 20, "silver", lista)

    listaGen = listaGenuri(lista)

    assert len(listaGen) == 3
    assert listaGen[0] == "drama"
    assert listaGen[1] == "fictiune"
    assert listaGen[2] == "comedie"

def testPretMinimPentruFiecareGen():
    lista = []
    listaPreturi = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    lista = adaugareVanzare("3", "Dune", "fictiune", 80, "none", lista)
    lista = adaugareVanzare("4", "Stan si Bran", "comedie", 20, "silver", lista)
    lista = adaugareVanzare("5", "O scrisoare pierduta", "comedie", 45, "none", lista)

    listaPreturi = pretMinimPentruFiecareGen(lista)

    assert listaPreturi[0] == 30
    assert listaPreturi[1] == 50
    assert listaPreturi[2] == 20

def testOrdonareCrescatorDupaPret():
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    lista = adaugareVanzare("3", "Dune", "fictiune", 80, "none", lista)
    lista = adaugareVanzare("4", "Stan si Bran", "comedie", 20, "silver", lista)
    lista = adaugareVanzare("5", "O scrisoare pierduta", "comedie", 45, "none", lista)

    rezultat = ordonareCrescatorDupaPret(lista)

    assert getId(rezultat[0]) == "4"
    assert getId(rezultat[1]) == "1"
    assert getId(rezultat[2]) == "5"
    assert getId(rezultat[3]) == "2"
    assert getId(rezultat[4]) == "3"

def testListaTitluriPentruFiecareGen():
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    lista = adaugareVanzare("3", "Dune", "fictiune", 80, "none", lista)
    lista = adaugareVanzare("4", "Stan si Bran", "comedie", 20, "silver", lista)
    lista = adaugareVanzare("5", "O scrisoare pierduta", "comedie", 45, "none", lista)


    listaTitluriFictiune = listaTitluriPentruFiecareGen("fictiune", lista)

    assert len(listaTitluriFictiune) == 2
    assert listaTitluriFictiune[0] == "Razboiul Stelelor"
    assert listaTitluriFictiune[1] == "Dune"

    listaTitluriPovesti = listaTitluriPentruFiecareGen("comedie", lista)

    assert len(listaTitluriPovesti) == 2
    assert listaTitluriPovesti[0] == "Stan si Bran"
    assert listaTitluriPovesti[1] == "O scrisoare pierduta"

def testAfisareNumarTitluriDistincte():
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    lista = adaugareVanzare("3", "Dune", "fictiune", 80, "none", lista)
    lista = adaugareVanzare("4", "Stan si Bran", "comedie", 20, "silver", lista)
    lista = adaugareVanzare("5", "O scrisoare pierduta", "comedie", 45, "none", lista)

    rezultat = afisareNumarTitluriDistincte(lista)

    assert rezultat[0] == 1
    assert rezultat[1] == 2
    assert rezultat[2] == 2