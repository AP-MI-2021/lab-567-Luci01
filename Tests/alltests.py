from Tests.TestService import testAdaugareVanzare, testStergereVanzare, testModificareVanzare, testGetById
from Tests.testcerinta import testAplicareDiscount, testModificareaGenuluiPentruTitlu, testListaGenuri, \
    testPretMinimPentruFiecareGen, testOrdonareCrescatorDupaPret, testListaTitluriPentruFiecareGen, \
    testAfisareNumarTitluriDistincte
from Tests.TestDomain import testVanzare
from Tests.testUndoRedo import testUndoRedo


def runAllTests():
    testVanzare()
    testAdaugareVanzare()
    testStergereVanzare()
    testModificareVanzare()
    testAplicareDiscount()
    testGetById()
    testModificareaGenuluiPentruTitlu()
    testListaGenuri()
    testPretMinimPentruFiecareGen()
    testOrdonareCrescatorDupaPret()
    testListaTitluriPentruFiecareGen()
    testAfisareNumarTitluriDistincte()
    testUndoRedo()