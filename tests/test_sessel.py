from classes.sessel import Sessel

def test_sessel():
    s1 = Sessel(name="Karl",
                  farbe="grau",
                  material="Holz",
                 sitzhoehe=15,
                  preis=49.9)

    assert s1.name == "Karl"
    assert s1.farbe == "grau"
    assert s1.material ==  "Holz"
    assert s1.preis == 49.9
    assert s1.sitzhoehe == 15
    assert s1.werfen() == "bonk - der Sessel Karl hat getroffen."