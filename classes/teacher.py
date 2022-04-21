from dataclasses import dataclass

from classes.subject import Subject
from classes.person import Person

@dataclass
class Teacher(Person):
    students: list[Student] = field(default_factory=list)
    subject: list[Subject] = field(default_factory=list)