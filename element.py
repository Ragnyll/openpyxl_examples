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
        # calculating things are hard
        # call some subroutine to make it a little easier
        a_multiplier = multiply_avocados(2)
        return self.atomic_weight * a_multiplier

    def write_to_sheet(self, sheet):
        sheet.title = '{} Rocket Stats'.format(self.name)
        cell_range = sheet['A1': 'A3']
        cell_range[0][0].value = self.name
        cell_range[1][0].value = self.atomic_weight
        cell_range[2][0].value = self.periodic_number

        return
