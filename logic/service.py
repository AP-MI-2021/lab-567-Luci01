from domain.Vanzare import getId, creeazaVanzare

def getById(id, lista):
    '''
    gaseste o vanzare cu id-ul dat in lista
    :param id: string
    :param lista: lista de vanzari
    :return: vanzarea cu id-ul dat din lista sau None, daca aceasta nu exista
    '''
    for vanzare in lista:
        if getId(vanzare) == id:
            return vanzare
    return None


def adaugareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista):

    if getById(id, lista) is not None:
        raise ValueError("Id-ul deja exista! ")
    vanzare = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
    return lista + [vanzare]
def adaugaVanzareUndoRedo(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista, undoList, redoList):

    if getById(id, lista) is not None:
        raise ValueError("Id-ul deja exista! ")
    vanzare = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
    undoList.append(lista)
    redoList.clear()
    return lista + [vanzare]

def stergereVanzare(id, lista):

    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul specificat!")
    return [vanzare for vanzare in lista if getId(vanzare) != id]

def modificareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista):

    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul specificat!")
    listaNoua = []
    for vanzare in lista:
        if getId(vanzare) == id:
            vanzareNoua = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua