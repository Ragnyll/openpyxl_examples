import consts

def multiply_avocados(multiplier):
    return multiplier * consts.AVOCADOS_NUMBER

class Element:
    def __init__(self, name, weight, periodic_number):
        self.name = name
        self.atomic_weight = weight
        self.periodic_number = periodic_number
        return

    def calculate_gforce_weight(self):
        """calculating things are hard

        call some subroutine to make it a little easier
        """
        a_multiplier = multiply_avocados(2)
        return self.atomic_weight * a_multiplier

    def bond(self, other):
        """Tries to bond this element with other
        """
        if self.name == other.name:
            print('The bond occured')
        else:
            raise BondException('element cant bond')

        return

    def write_to_sheet(self, sheet):
        sheet.title = '{} Element Stats'.format(self.name)
        cell_range = sheet['A1': 'A3']
        cell_range[0][0].value = self.name
        cell_range[1][0].value = self.atomic_weight
        cell_range[2][0].value = self.periodic_number

        return


class BondException(Exception):
    """A failure occured when trying to bond 2 elements"""
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return 'The elements could not bond for some reason'
