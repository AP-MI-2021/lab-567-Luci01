from logic.service import adaugaVanzareUndoRedo
from logic.cerinte import Undo, Redo


def testUndoRedo():
    lista = []
    undo = []
    redo = []


    lista = adaugaVanzareUndoRedo("1", "Harry Potter", "fantastic", 100, "none", lista, undo, redo)
    lista = adaugaVanzareUndoRedo("2", "Invitatie la vals", "dragoste", 45, "silver", lista, undo, redo)
    lista = adaugaVanzareUndoRedo("3", "Ion", "fantastic", 34, "gold", lista, undo, redo)

    assert lista ==[{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'}, {'id': '2', 'titlu_carte': 'Invitatie la vals', 'gen_carte': 'dragoste', 'pret': 45.00, 'tip_reducere_client': 'silver'}, {'id': '3', 'titlu_carte': 'Ion', 'gen_carte': 'fantastic', 'pret': 34.00, 'tip_reducere_client': 'gold'}]

    lista = Undo(lista, undo, redo)

    assert lista ==[{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'}, {'id': '2', 'titlu_carte': 'Invitatie la vals', 'gen_carte': 'dragoste', 'pret': 45.00, 'tip_reducere_client': 'silver'}]

    lista = Undo(lista, undo, redo)

    assert lista ==[{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'}]

    lista = Undo(lista, undo, redo)

    assert lista == []

    lista = Undo(lista, undo, redo)

    assert lista is None


    undo = []
    redo = []
    lista = []


    lista = adaugaVanzareUndoRedo("1", "Harry Potter", "fantastic", 100, "none", lista, undo, redo)
    lista = adaugaVanzareUndoRedo("2", "Invitatie la vals", "dragoste", 45, "silver", lista, undo, redo)
    lista = adaugaVanzareUndoRedo("3", "Ion", "fantastic", 34, "gold", lista, undo, redo)
    lista= Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'}, {'id': '2', 'titlu_carte': 'Invitatie la vals', 'gen_carte': 'dragoste', 'pret': 45.00, 'tip_reducere_client': 'silver'}, {'id': '3', 'titlu_carte': 'Ion', 'gen_carte': 'fantastic', 'pret': 34.00, 'tip_reducere_client': 'gold'}]

    lista = Undo(lista, undo, redo)
    lista = Undo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'}]

    lista= Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'}, {'id': '2', 'titlu_carte': 'Invitatie la vals', 'gen_carte': 'dragoste', 'pret': 45.00, 'tip_reducere_client': 'silver'}]

    lista = Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'}, {'id': '2', 'titlu_carte': 'Invitatie la vals', 'gen_carte': 'dragoste', 'pret': 45.00, 'tip_reducere_client': 'silver'}, {'id': '3', 'titlu_carte': 'Ion', 'gen_carte': 'fantastic', 'pret': 34.00, 'tip_reducere_client': 'gold'}]

    lista = Undo(lista, undo, redo)
    lista = Undo(lista, undo, redo)
    lista = adaugaVanzareUndoRedo("4", "Scufita Rosie", "povesti", 100.00, "none", lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'},
                   {'id': '4', 'titlu_carte': 'Scufita Rosie', 'gen_carte': 'povesti', 'pret': 100.00, 'tip_reducere_client': 'none'}]
    lista = Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'},
                   {'id': '4', 'titlu_carte': 'Scufita Rosie', 'gen_carte': 'povesti', 'pret': 100.00, 'tip_reducere_client': 'none'}]
    lista = Undo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'}]

    lista = Undo(lista, undo, redo)

    assert lista == []

    lista = Redo(lista, undo, redo)
    lista = Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'},
                   {'id': '4', 'titlu_carte': 'Scufita Rosie', 'gen_carte': 'povesti', 'pret': 100.00, 'tip_reducere_client': 'none'}]

    lista = Redo(lista, undo, redo)

    assert lista == [{'id': '1', 'titlu_carte': 'Harry Potter', 'gen_carte': 'fantastic', 'pret': 100.00, 'tip_reducere_client': 'none'},
                   {'id': '4', 'titlu_carte': 'Scufita Rosie', 'gen_carte': 'povesti', 'pret': 100.00, 'tip_reducere_client': 'none'}]