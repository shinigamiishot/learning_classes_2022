from dataclasses import dataclass, field

@dataclass
class Gegenstand:
    name: str
    aggregatzustand: str
    legal: bool
    artikel: str

    def __str__(self):
        ist_legal = "legal"
        if not self.legal:
            ist_legal = "illegal"
        return f"""{self.artikel} {self.name} ist {self.aggregatzustand} ,jedoch {ist_legal}"""



g1 = Gegenstand(name="Messer", aggregatzustand="fest", legal= False, artikel="Das")



