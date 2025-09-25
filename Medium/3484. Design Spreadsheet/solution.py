class Spreadsheet:

    matrix = {}

    def __init__(self, rows: int):
        self.matrix = {}

    def setCell(self, cell: str, value: int) -> None:
        self.matrix[cell] = value

    def resetCell(self, cell: str) -> None:
        self.matrix[cell] = 0

    def valueCell(self, cell):
        if cell[0].isdigit():
            return int(cell)
        else:
            return self.matrix.get(cell, 0)

    def getValue(self, formula: str) -> int:
        first, second = formula[1:].split('+')
        return self.valueCell(first) + self.valueCell(second)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
