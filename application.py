from classes.sessel import Sessel

sessel_1 = Sessel(name="Frank",
                  farbe="orange",
                  material="Kuntstoff",
                  preis=20.00,
                  sitzhoehe=200
                  )
sessel_2  = Sessel(name="kurzer Frank",
                  farbe="orange",
                  material="Kuntstoff",
                  preis=20.00,

                  )
sessel_3 = Sessel(name="Karl",
                  farbe="grau",
                  material="Holz",
                 sitzhoehe=15,
                  preis=49.9
                  )

print(sessel_1)
print(sessel_2)
print(sessel_3)
print(sessel_3.werfen())

