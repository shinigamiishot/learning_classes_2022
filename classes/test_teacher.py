from classes.teacher import Teacher
from classes.student import Student
from classes.subject import Subject

def test_teacher():
    t = Teacher(firstname="Rainer",
                lastname="Amler",
                identification_number=1234
                )
    assert len(t.students) == 0
    assert len(t.subjects) == 0