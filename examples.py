import sys
from openpyxl import Workbook
from rocket import Rocket


def create_rocket_data(rocket: Rocket):
    # opens with 1 default sheet
    wb = Workbook()
    wb.active.title = '{} RocketStats'.format(rocket.name)
    rocket.write_to_sheet(wb.active)

    # Create 3 data sheets
    for i in range(2):
        wb.create_sheet('DataSheet{}'.format(i))

    wb.save('RocketStats.xlsx')
    return


if __name__ == '__main__':
    if sys.argv[1] == 'generate':
        myrocket = Rocket('funky', '1000', '349')
        create_rocket_data(myrocket)
    elif sys.argv[1] == 'derive':
        print('oh hi there')

