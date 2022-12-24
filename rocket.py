import consts

def multiply_gravity(multiplier):
    return

class Rocket:
    def __init__(self, name, weight, fuel_in_litres):
        self.name = name
        self.weight = weight
        self.fuel_in_litres = fuel_in_litres
        return

    def calculate_gforce_weight(self):
        # calculating lift is hard
        # call some subroutine to make it a little easier
        g_multiplier = multiply_gravity(2)
        return self.weight * g_multiplier

    def write_to_sheet(self, sheet):
        sheet.title = '{} Rocket Stats'.format(self.name)
        cell_range = sheet['A1': 'A3']
        cell_range[0][0].value = self.name
        cell_range[1][0].value = self.weight
        cell_range[2][0].value = self.fuel_in_litres

        return
