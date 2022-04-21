from classes.subject import Subject

def test_subject():
    s = Subject(name="Leben")

    assert s.name == "Leben"