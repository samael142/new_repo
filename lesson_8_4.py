class Store:

    list_of_stores = []

    def __init__(self, name):
        self.units = 0
        self.list_of_units = []
        self.name = name
        self.list_of_stores.append(self.name)

    @staticmethod
    def info(store):
        return print(f'\nUnits in {store.name}: {store.units}', *store.list_of_store(), sep="\n")

    def add_unit(self, unit):
        try:
            if unit.unit_valid == 1:
                self.units += 1
                self.list_of_units.append(unit)
            else:
                raise WrongUnit
        except WrongUnit as err:
            return print(f"{unit}\n{err}")

    def remove_unit(self, unit):
        self.units -= 1
        self.list_of_units.remove(unit)

    def list_of_store(self):
        return self.list_of_units

    @staticmethod
    def MoveToAnotherStore(unt, frm, to):
        try:
            if unt in frm.list_of_units:
                Store.remove_unit(frm, unt)
                Store.add_unit(to, unt)
            else:
                raise NotInStore
        except NotInStore as err:
            return print(err)

    @staticmethod
    def Get_list_of_stores():
        return Store.list_of_stores


class Periphery:

    typ = None

    def __init__(self, manufacturer, model, mass):
        self.unit = {"type": self.typ, "manufacturer": manufacturer, "model": model, "mass": mass}
        if type(manufacturer) == str and type(model) == str and type(mass) == int:
            self.unit_valid = 1
        else:
            self.unit_valid = 0

    def __str__(self):
        return str(self.unit)


class Printer(Periphery):

    # printer_count = 0
    typ = "printer"


class Copier(Periphery):

    # copier_count = 0
    typ = "copier"


class Mfu(Periphery):

    # mfu_count = 0
    typ = "mfu"


class NotInStore(Exception):
    def __init__(self):
        self.txt = "Unit not in Store!!!"

    def __str__(self):
        return self.txt


class WrongUnit(Exception):
    def __init__(self):
        self.txt = "Wrong unit info!!! --> manufacturer: str, model: str, mass: int"

    def __str__(self):
        return self.txt


printer_1 = Printer("HP", "LaserJet 1000", 5)
mfu_1 = Mfu("Kyocera", "m2040dn", 10)
printer_2 = Printer("HP", "LaserJet 2500", 5)
mfu_2 = Mfu("Kyocera", "m2035dn", 10)
copier_1 = Copier("Xerox", 200, "1500")

store_a = Store("store_a")
store_a.add_unit(printer_1)
store_a.add_unit(mfu_1)
store_a.add_unit(copier_1)
Store.info(store_a)
store_b = Store("store_b")
store_b.add_unit(printer_2)
store_b.add_unit(mfu_2)
Store.info(store_b)

Store.MoveToAnotherStore(printer_1, store_a, store_b)

Store.info(store_a)
Store.info(store_b)

Store.MoveToAnotherStore(printer_1, store_a, store_b)
