class Scoop:
    def __init__(self, flavour: str):
        self.flavour = flavour


def create_scoops() -> list:
    scoops = [Scoop(x) for x in ['vanilla', 'chocolate', 'permsimmon']]
    return scoops


scoops = create_scoops()
for s in scoops:
    print(s.flavour)
