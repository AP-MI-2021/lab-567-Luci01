from domain.Vanzare2 import getId, creeazaVanzare


def adaugareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista):
    '''
    adauga o vanzare intr-o lista
    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :param lista: lista de vanzari
    :return: o lista continand atat elementele vechi, cat si vanzarea nou adaugata
    '''
    vanzare = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
    return lista + [vanzare]

def stergereVanzare(id, lista):
    '''
    sterge o vanzare dintr-o lista
    :param id: id-ul vanzarii care trebuie sterse
    :param lista: lista de vanzari
    :return: lista continuand vechile elemente mai putin vanzarea care a fost stearsa
    '''
    return [vanzare for vanzare in lista if getId(vanzare) != id]

def modificareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista):
    '''
    modifica vanzarea cu id-ul dat dintr-o lista
    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :param lista: o lista de vanzari
    :return: lista modificata
    '''
    listaNoua = []
    for vanzare in lista:
        if getId(vanzare) == id:
            vanzareNoua = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua

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