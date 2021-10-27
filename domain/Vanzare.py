class Vanzare(object):
    ID = 0
    titlu_carte = ""
    gen_carte = ""
    pret = 0
    tip_reducere = ""

    def __init__(self, id , titlu , gen , pret , tip ):
        self.ID = id
        self.titlu_carte = titlu
        self.gen_carte = gen
        self.pret = pret
        self.tip_reducere = tip

    def get_ID(self):
        return self.ID

    def get_titlu_carte(self):
        return self.titlu_carte

    def get_gen_carte(self):
        return self.gen_carte

    def get_pret(self):
        return self.pret

    def get_tip_reducere(self):
        return self.tip_reducere

    def set_titlu_carte(self, titlu):
        self.titlu_carte = titlu

    def set_gen_carte(self, gen):
        self.gen_carte = gen

    def set_pret(self, pret):
        self.pret = pret

    def set_tip_reducere(self, tip):
        self.tip_reducere = tip

    def to_string(self):
        return str(self.ID) +  " "  + self.titlu_carte + " " + self.gen_carte + " " + str(self.pret) + " " + self.tip_reducere


