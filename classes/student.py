from dataclasses import dataclass, field

from classes.person import Person

@dataclass
class Student(Person):
    grades: list[str] = field(default_factory=list)
