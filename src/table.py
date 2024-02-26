from prettytable import from_csv
from prettytable.colortable import ColorTable, Theme


class Table:
    def __init__(self):
        self.table = None

    def display(self):
        print(self.table)

    @staticmethod
    def from_csv(filename):
        t = Table()
        with open(filename, "r") as csvfile:
            pt = from_csv(csvfile)
        color_table = ColorTable(
            theme=Theme(
                default_color="37",
                vertical_color="33;41",
                horizontal_color="33;41",
                junction_color="33;41",
            )
        )
        color_table.field_names = pt.field_names
        color_table.add_rows(pt._rows)
        del pt
        color_table.align = "l"
        t.table = color_table
        return t