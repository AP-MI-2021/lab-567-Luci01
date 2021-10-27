from domain.Vanzare import Vanzare
from logic.service import Service

def test_service():
    '''

    :return:
    '''
    serv = Service()
    vanzari = serv.get_all()
    assert (len(vanzari) == 0)
    serv.add(10, "Ion", "Drama", 25, "gold")
    vanzari = serv.get_all()
    assert (len(vanzari) == 1)
    try:
        serv.add(10, "Ion", "Drama", 25, "gold")
    except Exception as e:
        assert(str(e) == "Vanzare deja existenta! \n")
    serv.modificare(10, "John", "Comedie", 24.99 , "silver")
    vanzari = serv.get_all()
    assert (vanzari[0].get_titlu_carte() == "John")
    assert (vanzari[0].get_gen_carte() == "Comedie")
    assert (vanzari[0].get_pret() == 24.99)
    assert (vanzari[0].get_tip_reducere() == "silver")
    try:
        serv.modificare(19, "Ion", "Drama", 25, "gold")
    except Exception as e:
        assert (str(e) == "Nu se poate modifica ! \n")
    serv.stergere(10)
    vanzari = serv.get_all()
    assert (len(vanzari) == 0)
    try:
        serv.stergere(11)
    except Exception as e:
        assert (str(e) == "Nu se poate sterge ! \n")

    serv.add(14, "Ioana", "Feminin", 69, "gold")
    serv.add(15, "Ioana", "Neutru" , 70 , "none")
    serv.modificare_gen("Ioana", "Masculin")
    vanzari = serv.get_all()
    assert (vanzari[0].get_gen_carte() == "Masculin")
    assert (vanzari[1].get_gen_carte() == "Masculin")

    try:
        serv.modificare_gen("Ionel", "Neutru")
    except Exception as e:
        assert (str(e) == "Nu se poate modifica ! \n")




