from logic.service import adaugaVanzareUndoRedo
from logic.cerinte import Undo, Redo


def testUndoRedo():
    lista = []
    undo = []
    redo = []


    lista = adaugaVanzareUndoRedo("1", "Enigma Otiliei", "drama", 30, "gold", lista, undo, redo)
    lista = adaugaVanzareUndoRedo("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista, undo, redo)
    lista = adaugaVanzareUndoRedo("3", "Dune", "fictiune", 80, "none", lista, undo, redo)

    assert lista ==[{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'}, {'id': '2', 'titlu_carte': 'Razboiul Stelelor', 'gen_carte': 'fictiune', 'pret': 50.00, 'tip_reducere_client': 'silver'}, {'id': '3', 'titlu_carte': 'Dune', 'gen_carte': 'fictiune', 'pret': 80.00, 'tip_reducere_client': 'none'}]

    lista = Undo(lista, undo, redo)

    assert lista ==[{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'}, {'id': '2', 'titlu_carte': 'Razboiul Stelelor', 'gen_carte': 'fictiune', 'pret': 50.00, 'tip_reducere_client': 'silver'}]

    lista = Undo(lista, undo, redo)

    assert lista ==[{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'}]

    lista = Undo(lista, undo, redo)

    assert lista == []

    lista = Undo(lista, undo, redo)

    assert lista is None


    undo = []
    redo = []
    lista = []

    lista = adaugaVanzareUndoRedo("1", "Enigma Otiliei", "drama", 30, "gold", lista, undo, redo)
    lista = adaugaVanzareUndoRedo("2", "Razboiul Stelelor", "fictiune", 50, "silver", lista, undo, redo)
    lista = adaugaVanzareUndoRedo("3", "Dune", "fictiune", 80, "none", lista, undo, redo)
    lista= Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'}, {'id': '2', 'titlu_carte': 'Razboiul Stelelor', 'gen_carte': 'fictiune', 'pret': 50.00, 'tip_reducere_client': 'silver'}, {'id': '3', 'titlu_carte': 'Dune', 'gen_carte': 'fictiune', 'pret': 80.00, 'tip_reducere_client': 'none'}]

    lista = Undo(lista, undo, redo)
    lista = Undo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'}]

    lista= Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'}, {'id': '2', 'titlu_carte': 'Razboiul Stelelor', 'gen_carte': 'fictiune', 'pret': 50.00, 'tip_reducere_client': 'silver'}]

    lista = Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'}, {'id': '2', 'titlu_carte': 'Razboiul Stelelor', 'gen_carte': 'fictiune', 'pret': 50.00, 'tip_reducere_client': 'silver'}, {'id': '3', 'titlu_carte': 'Dune', 'gen_carte': 'fictiune', 'pret': 80.00, 'tip_reducere_client': 'none'}]

    lista = Undo(lista, undo, redo)
    lista = Undo(lista, undo, redo)
    lista = adaugaVanzareUndoRedo("4", "Stan si Bran", "comedie", 20.00, "none", lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'},
                   {'id': '4', 'titlu_carte': 'Stan si Bran', 'gen_carte': 'comedie', 'pret': 20.00, 'tip_reducere_client': 'none'}]
    lista = Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'},
                   {'id': '4', 'titlu_carte': 'Stan si Bran', 'gen_carte': 'comedie', 'pret': 20.00, 'tip_reducere_client': 'none'}]
    lista = Undo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'}]

    lista = Undo(lista, undo, redo)

    assert lista == []

    lista = Redo(lista, undo, redo)
    lista = Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'},
                     {'id': '4', 'titlu_carte': 'Stan si Bran', 'gen_carte': 'comedie', 'pret': 20.00,'tip_reducere_client': 'none'}]

    lista = Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Enigma Otiliei', 'gen_carte': 'drama', 'pret': 30.00, 'tip_reducere_client': 'gold'},
                     {'id': '4', 'titlu_carte': 'Stan si Bran', 'gen_carte': 'comedie', 'pret': 20.00,'tip_reducere_client': 'none'}]