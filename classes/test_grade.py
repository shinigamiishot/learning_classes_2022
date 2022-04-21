from classes.grade import Grade
from classes.subject  import Subject


def test_grade():
    s : Subject("Leben")
    g : Grade(value=4, subject=s)

    assert g.value == 4
    assert s.value == s