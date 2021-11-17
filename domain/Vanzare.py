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
    return {'id': id, 'titlu_carte': titlu_carte, 'gen_carte': gen_carte, 'pret': pret, 'tip_reducere_client': tip_reducere_client}

def getId(vanzare):
    '''
    ia id-ul vanzarii
    :param vanzare: tuple de tipul vanzare
    :return: id-ul vanzarii
    '''
    return vanzare['id']

def getTitluCarte(vanzare):
    '''
    ia titlul cartii
    :param vanzare: tuple de tipul vanzare
    :return: titlul cartii
    '''
    return vanzare['titlu_carte']

def getGenCarte(vanzare):
    '''
    ia genul cartii
    :param vanzare: tuple de tipul vanzare
    :return: genul cartii
    '''
    return vanzare['gen_carte']

def getPret(vanzare):
    '''
    ia pretul cartii
    :param vanzare: tuple de tipul vanzare
    :return: pretul cartii
    '''
    return vanzare['pret']

def getTipReducereClient(vanzare):
    '''
    ia tipul reducerii clientului
    :param vanzare: tuple de tipul vanzare
    :return: tipul reducerii clientului
    '''
    return vanzare['tip_reducere_client']

def toString(vanzare):
    return "id: {}, titlu carte: {}, gen carte: {}, pret: {}, tip reducere client: {}".format(
        getId(vanzare),
        getTitluCarte(vanzare),
        getGenCarte(vanzare),
        getPret(vanzare),
        getTipReducereClient(vanzare)
    )