from domain.Vanzare import getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient
from logic.service import adaugareVanzare, getById, stergereVanzare, modificareVanzare


def testAdaugareVanzare():
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getTitluCarte(getById("1", lista)) == "Enigma Otiliei"
    assert getGenCarte(getById("1", lista)) == "drama"
    assert getPret(getById("1", lista)) == 30
    assert getTipReducereClient(getById("1", lista)) == "gold"

def testStergereVanzare():
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    lista = stergereVanzare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    try:
        lista = stergereVanzare("3", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False

def testModificareVanzare():
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "fantastic", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)

    lista = modificareVanzare("1", "Dune", "fictiune", 80, "none", lista)

    vanzareModificata = getById("1", lista)
    assert getId(vanzareModificata) == "1"
    assert getTitluCarte(vanzareModificata) == "Dune"
    assert getGenCarte(vanzareModificata) == "fictiune"
    assert getPret(vanzareModificata) == 80
    assert getTipReducereClient(vanzareModificata) == "none"

    vanzareNemodificata = getById("2", lista)
    assert getId(vanzareNemodificata) == "2"
    assert getTitluCarte(vanzareNemodificata) == "Razboiul Stelelor"
    assert getGenCarte(vanzareNemodificata) == "fictiune"
    assert getPret(vanzareNemodificata) == 50
    assert getTipReducereClient(vanzareNemodificata) == "silver"

    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)

    try:
        lista = modificareVanzare("3", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    except ValueError:
        vanzareNemodificata = getById("1", lista)
        assert getId(vanzareNemodificata) == "1"
        assert getTitluCarte(vanzareNemodificata) == "Enigma Otiliei"
        assert getGenCarte(vanzareNemodificata) == "drama"
        assert getPret(vanzareNemodificata) == 30
        assert getTipReducereClient(vanzareNemodificata) == "gold"
    except Exception:
        assert False

def testGetById():
    lista = []
    lista = adaugareVanzare("1", "Enigma Otiliei", "drama", 30, "gold", lista)
    lista = adaugareVanzare("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista)
    assert getById("1", lista) == lista[0]
    assert getById("2", lista) == lista[1]
    assert getById("3", lista) is None


