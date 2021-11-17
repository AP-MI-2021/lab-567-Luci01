def creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client):
    '''
    creeaza o vanzare
    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :return: o lista ce retine o vanzare
    '''
    return [
        id,
        titlu_carte,
        gen_carte,
        pret,
        tip_reducere_client,
    ]

def getId(vanzare2):
    '''
    ia id-ul vanzarii
    :param vanzare: tuple de tipul vanzare
    :return: id-ul vanzarii
    '''
    return vanzare2[0]

def getTitluCarte(vanzare2):
    '''
    ia titlul cartii
    :param vanzare: tuple de tipul vanzare
    :return: titlul cartii
    '''
    return vanzare2[1]

def getGenCarte(vanzare2):
    '''
    ia genul cartii
    :param vanzare: tuple de tipul vanzare
    :return: genul cartii
    '''
    return vanzare2[2]

def getPret(vanzare2):
    '''
    ia pretul cartii
    :param vanzare: tuple de tipul vanzare
    :return: pretul cartii
    '''
    return vanzare2[3]

def getTipReducereClient(vanzare2):
    '''
    ia tipul reducerii clientului
    :param vanzare: tuple de tipul vanzare
    :return: tipul reducerii clientului
    '''
    return vanzare2[4]

def toString(vanzare2):
    return "id: {}, titlu carte: {}, gen carte: {}, pret: {}, tip reducere client: {}".format(
        getId(vanzare2),
        getTitluCarte(vanzare2),
        getGenCarte(vanzare2),
        getPret(vanzare2),
        getTipReducereClient(vanzare2)
    )