from domain.Vanzare import Vanzare

def test_domain():
    vanzare = Vanzare(98 , "Ciuleandra" , "Horror" , 9.99 , "none" )
    assert (vanzare.get_ID() == 98 )
    assert (vanzare.get_titlu_carte() == "Ciuleandra" )
    assert (vanzare.get_gen_carte() == "Horror")
    assert (abs(vanzare.get_pret() - 9.99) < 0.00001 )
    assert (vanzare.get_tip_reducere() == "none")
    vanzare.set_gen_carte("Drama")
    assert (vanzare.get_gen_carte() == "Drama" )
    assert (vanzare.to_string() == "98 Ciuleandra Drama 9.99 none")
