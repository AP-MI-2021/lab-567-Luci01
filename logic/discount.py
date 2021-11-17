from domain.Vanzare2 import creeazaVanzare, getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient

def aplicareDiscount(lista):
    '''
    aplica discount pentru reducerile specificate
    :param lista: lista de vanzari
    :return: o noua lista avand vanzarile actualizate
    '''
    listaNoua = []
    for vanzare in lista:
        if getTipReducereClient(vanzare) == "silver":
            vanzareNoua = creeazaVanzare(
                getId(vanzare),
                getTitluCarte(vanzare),
                getGenCarte(vanzare),
                getPret(vanzare) - 5/100 * getPret(vanzare),
                getTipReducereClient(vanzare)
            )
            listaNoua.append(vanzareNoua)
        elif getTipReducereClient(vanzare) == "gold":
            vanzareNoua = creeazaVanzare(
                getId(vanzare),
                getTitluCarte(vanzare),
                getGenCarte(vanzare),
                getPret(vanzare) - 10 / 100 * getPret(vanzare),
                getTipReducereClient(vanzare)
            )
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua