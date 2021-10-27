from domain.Vanzare import Vanzare

class Service(object):

    def __init__(self):
        '''
        Metoda care initializeaza lista de elemente vanzari
        '''

        self.vanzari = []

    def size(self):
        '''

        :return:
        '''
        return len(self.vanzari)

    def add(self, ID, titlu, gen, pret, tip):
        '''

        :return:
        '''
        vanzaree = Vanzare(ID, titlu, gen, pret, tip)
        for vanzare in self.vanzari:
            if vanzare.get_ID() == ID:
                raise Exception("Vanzare deja existenta! \n")
        self.vanzari.append(vanzaree)

    def modificare(self, ID, titlu_nou, gen_nou, pret_nou, tip_nou):
        '''

        :return:
        '''
        for vanzare in self.vanzari:
            if vanzare.get_ID() == ID:
                vanzare.set_titlu_carte(titlu_nou)
                vanzare.set_gen_carte(gen_nou)
                vanzare.set_pret(pret_nou)
                vanzare.set_tip_reducere(tip_nou)
                return
        raise Exception("Nu se poate modifica ! \n")


    def stergere(self, id):
        '''

        :return:
        '''
        for vanzare in self.vanzari:
            if vanzare.get_ID() == id:
                self.vanzari.remove(vanzare)
                return
        raise Exception("Nu se poate sterge ! \n")

    def get_all(self):
        '''

        :return:
        '''
        return self.vanzari

    def modificare_gen(self, titlu, gen):
        '''

        :param titlu:
        :param gen:
        :return:
        '''
        ok = 0
        for vanzare in self.vanzari:
            if vanzare.get_titlu_carte() == titlu:
                vanzare.set_gen_carte(gen)
                ok = 1
        if ok == 0:
            raise Exception("Nu se poate modifica ! \n")
