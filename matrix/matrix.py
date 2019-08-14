class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = [[int(n) for n in r.split()] for r in matrix_string.split('\n')]
        self.cols = [list(t) for t in zip(*self.rows)]

    def row(self, index):
        return list(self.rows[index - 1])

    def column(self, index):
        return list(self.cols[index - 1])
