from Tests.TestService import testAdaugareVanzare, testStergereVanzare, testModificareVanzare, testGetById
from Tests.testdiscount import testAplicareDiscount
from Tests.TestDomain import testVanzare


def runAllTests():
    testVanzare()
    testAdaugareVanzare()
    testStergereVanzare()
    testModificareVanzare()
    testAplicareDiscount()
    testGetById()
