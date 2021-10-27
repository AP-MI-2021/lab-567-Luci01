from Tests.TestDomain import test_domain
from Tests.TestService import test_service
from logic.service import Service
from UserInterface.UI import UI

def teste():
    test_domain()
    test_service()



def main():
    teste()
    service = Service()
    ui = UI(service)
    ui.rulare_UI()


main()