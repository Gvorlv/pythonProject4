from dz13_1 import*
class Mag(Personagi):
   def __init__(self, nik, rassa, pol, cvet_volos, tip_vnesh, zdorovie, baz_uron):
       self.nik = nik
       self.rassa = rassa
       self.pol = pol
       self.cvet_volos = cvet_volos
       self.tip_vnesh = tip_vnesh
       super().__init__(zdorovie, baz_uron)

   @classmethod
   def udar_mech(cls):
       super().MetodBazUron()
       return 'удар мечом - наносит 2 урона'

   @classmethod
   def udar_shit(cls):
       super().MetodBazUron()
       return 'удар щитом – наносит 1 урон'
   @classmethod
   def iscel(cls):
       return 'исцеление - восстанавливает 5 здоровья'
   def info(self):
       return f'ник: {self.nik} расса: {self.rassa} пол: {self.pol} цвет волос: {self.cvet_volos} тип внешности: {self.tip_vnesh} '



class Voin(Personagi):
    def __init__(self, nik, rassa, pol, cvet_volos, tip_vnesh, zdorovie, baz_uron):
        self.nik = nik
        self.rassa = rassa
        self.pol = pol
        self.cvet_volos = cvet_volos
        self.tip_vnesh = tip_vnesh
        super().__init__(zdorovie, baz_uron)


    @classmethod
    def zamoroz(cls):
        super().MetodBazUron()
        return 'заморозка – наносит 1 урона'

    @classmethod
    def og_shar(cls):
        super().MetodBazUron()
        return 'огненный шар - наносит 5 урона и произносится 5 секунд'

    @classmethod
    def iscel(cls):
        return 'исцеление - восстанавливает 5 здоровья'

    def info(self):
        return f'ник: {self.nik} |расса: {self.rassa} |пол: {self.pol} |цвет волос: {self.cvet_volos} |тип внешности: {self.tip_vnesh} '

tip_pers = 0
while tip_pers != 'Маг' and tip_pers != 'Воин':
    tip_pers=input('выберете тип персонажа Маг или Воин ', )

nik=input('введите ник ', )
rassa=input('введите рассу ', )
pol=input('введите пол ', )
cvet_volos=input('введите цвет волос ', )
tip_vnesh=input('введите тип внешности ', )
zdorovie=input('введите здоровье ', )
baz_uron=input('введите базовый урон ', )

if tip_pers=='Маг':
    personaj=Mag(nik, rassa, pol, cvet_volos, tip_vnesh, zdorovie, baz_uron)
    print(personaj.info())

elif tip_pers=='Воин':
    personaj=Voin(nik, rassa, pol, cvet_volos, tip_vnesh)
    print(personaj.info())

