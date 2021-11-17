from domain.Vanzare import creeazaVanzare, getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient


def testVanzare():
    vanzare = creeazaVanzare("1", "Enigma Otiliei", "drama", 30, "gold")
    assert getId(vanzare) == "1"
    assert getTitluCarte(vanzare) == "Enigma Otiliei"
    assert getGenCarte(vanzare) == "drama"
    assert getPret(vanzare) == 30
    assert getTipReducereClient(vanzare) == "gold"