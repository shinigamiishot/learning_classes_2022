from classes.student import Student

def test_student():
    s = Student(firstname="Rainer",
                lastname="Amler",
                identification_number=1234)

    assert len(s.grades) == 0