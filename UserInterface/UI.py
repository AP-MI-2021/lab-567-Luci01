from logic.service import Service

class UI(object):
    '''

    '''

    def __init__(self, service: Service):
        self.service = service

    def print_menu(self):
        '''

        :return:
        '''
        print("Hi :> ")
        print("Ce doresti de la noi?")
        print("Adaugare de vanzare : 1")
        print("Modificare de vanzare : 2")
        print("Stergere de vanzare : 3")
        print("Modificarea genului dupa titlu : 4")
        print("Afisare vanzari : 5")
        print("      Iesire : x")

    def UI_add(self):
        '''

        :return:
        '''
        try:
            id = int(input("Id = "))
        except Exception as e:
            print("Id trb sa fie nr ")
            return
        titlu = input("Titlu = ")
        gen = input("Gen = ")
        try:
            pret = float(input("Pret = "))
        except Exception as e:
            print("Pretul trebuie sa fie numar ")
            return
        reducere = input("Reducere = ")
        if reducere not in ["none", "silver", "gold"]:
            print("Reducere inexistenta! \n")
            return

        try:
            self.service.add(id, titlu, gen, pret, reducere)
        except Exception as e:
            print(str(e))



    def UI_modif(self):
        '''

        :return:
        '''
        try:
            id = int(input("Id = "))
        except Exception as e:
            print("Id trb sa fie nr ")
            return
        titlu = input("Titlu = ")
        gen = input("Gen = ")
        try:
            pret = float(input("Pret = "))
        except Exception as e:
            print("Pretul trebuie sa fie numar ")
            return
        reducere = input("Reducere = ")
        if reducere not in ["none", "silver", "gold"]:
            print("Reducere inexistenta! \n")
            return

        try:
            self.service.modificare(id, titlu, gen, pret, reducere)
        except Exception as e:
            print(str(e))

    def UI_delete(self):
        '''

        :return:
        '''
        try:
            id = int(input("Id = "))
        except Exception as e:
            print("Id trb sa fie nr ")
            return
        try:
            self.service.stergere(id)
        except Exception as e:
            print(str(e))

    def UI_gen_title(self):
        '''

        :return:
        '''

        titlu = input("Titlu = ")
        gen = input("Gen = ")
        try:
            self.service.modificare_gen(titlu, gen)
        except Exception as e:
            print(str(e))

    def UI_print_all(self):
        '''

        :return:
        '''
        vanzari = self.service.get_all()
        if len(vanzari) == 0:
            print ("Nu exista vanzari :( \n")
            return
        for vanzare in vanzari:
            print (vanzare.to_string())



    def rulare_UI(self):
        '''

        :return:
        '''
        self.print_menu()
        while True:
            cmd = input("Introdu comanda dorita pls <3 -> ")
            if cmd == "x":
                print(" Hasta la vista baby !! :^ ")
                return
            if cmd == "1":
                self.UI_add()
            elif cmd == "2":
                self.UI_modif()
            elif cmd == "3":
                self.UI_delete()
            elif cmd == "4":
                self.UI_gen_title()
            elif cmd == "5":
                self.UI_print_all()
            else:
                print("N avem decat 5 comenzi .. ayaye :/ ")
