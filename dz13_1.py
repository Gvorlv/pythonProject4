class Personagi:
    def __init__(self, zdorovie, baz_uron):
        self.zdorovie = zdorovie
        self.baz_uron = baz_uron
    def MetodBazUron(self):
        print('базовый урон равен', self.baz_uron)