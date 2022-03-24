from dataclasses import dataclass

@dataclass
class Sessel:
    name: str
    farbe: str
    material: str
    preis: float
    sitzhoehe: int = 50

    def __str__(self):
        return f"""
        Hallo, ich bin der Sessel namens {self.name}.
        Ich bin {self.sitzhoehe}cm groß und aus {self.material}.
        Ich bin {self.farbe} und koste €{self.preis}
        Man kann mich werfen :)
        """

    def werfen(self):
        return f"bonk - der Sessel {self.name} hat getroffen."


