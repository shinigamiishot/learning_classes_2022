from classes.gegenstand import Gegenstand

def test_gegenstand():
    g1 = Gegenstand(name="Messer", aggregatzustand="fest", legal= False, artikel="Das")

    assert g1.name == "Messer"
    assert g1.aggregatzustand == "fest"
    assert g1.legal == False
    assert g1.artikel == "Das"


    assert str(g1) == "Das Messer ist fest ,jedoch illegal"



