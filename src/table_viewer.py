class TableViewer:
    def to_table(self, data):
        return tabulate(data, headers='keys', tablefmt='pipe')