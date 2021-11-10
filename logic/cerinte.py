from domain.Vanzare import creeazaVanzare, getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient


def aplicareDiscount(lista):

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

def modificareaGenuluiPentruTitlu(titlu, gen, lista):

    listaNoua = []
    for vanzare in lista:
        if getTitluCarte(vanzare) == titlu:
            vanzareNoua = creeazaVanzare(
                getId(vanzare),
                getTitluCarte(vanzare),
                gen,
                getPret(vanzare),
                getTipReducereClient(vanzare)
            )
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua

def listaGenuri(lista):

    listaNoua = []
    for vanzare in lista:
        gen = getGenCarte(vanzare)
        if gen not in listaNoua:
            listaNoua.append(gen)
    return listaNoua

def pretMinimPentruFiecareGen(lista):

    listaNoua = listaGenuri(lista)
    listaPreturi = []
    for i in listaNoua:
        minim = None
        for vanzare in lista:
            gen = getGenCarte(vanzare)
            pret = getPret(vanzare)
            if gen == i:
                if minim == None:
                    minim = pret
                elif pret < minim:
                    minim = pret
        listaPreturi.append(minim)
    return listaPreturi

def ordonareCrescatorDupaPret(lista):

    return sorted(lista, key=getPret)

def listaTitluriPentruFiecareGen(gen, lista):

    listaTitluri = []
    for vanzare in lista:
        if getGenCarte(vanzare) == gen:
            if getTitluCarte(vanzare) not in listaTitluri:
                listaTitluri.append(getTitluCarte(vanzare))
    return listaTitluri


def afisareNumarTitluriDistincte(lista):

    listaGen = listaGenuri(lista)
    listaNumarTitluri = []
    for i in listaGen:
        listaNumarTitluri.append(len(listaTitluriPentruFiecareGen(i, lista)))
    return listaNumarTitluri

def Undo(lista, undolist, redolist):
    if len(undolist) > 0:
        redolist.append(lista)
        lista = undolist.pop()
    else:
        return None
    return lista

def Redo(lista, undolist, redolist):
    if len(redolist) > 0:
        undolist.append(lista)
        lista = redolist.pop()
    return lista
