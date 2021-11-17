from domain.Vanzare2 import creeazaVanzare, getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient


def testVanzare():
    vanzare = creeazaVanzare("10", "Stan si Bran", "comedie", 20, "gold")
    assert getId(vanzare) == "10"
    assert getTitluCarte(vanzare) == "Stan si Bran"
    assert getGenCarte(vanzare) == "comedie"
    assert getPret(vanzare) == 20
    assert getTipReducereClient(vanzare) == "gold"