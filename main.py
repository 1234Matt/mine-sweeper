import pyglet


# window = pyglet.window.Window()
#
# pyglet.app.run()


class PlayingField:
    LEVEL_VALUE_ERROR = "Level can be 1, 2 or 3 only."

    def __init__(self, level):
        self._level = level
        self._size = self.__get_size_from_level(level)
        self._count_of_mines = self.__get_number_of_mines_from_level(level)
        self._grid = [[self._size], [self._size]]

        self.__generate_playing_field(self._count_of_mines, self._size, self._grid)

    def __get_size_from_level(self, level):
        if level == 1:
            return 8
        if level == 2:
            return 16
        if level == 3:
            return 24

        raise ValueError(self.LEVEL_VALUE_ERROR)

    def __get_number_of_mines_from_level(self, level):
        if level == 1:
            return 10
        if level == 2:
            return 40
        if level == 3:
            return 99

        raise ValueError(self.LEVEL_VALUE_ERROR)

    def __generate_playing_field(self, count_of_mines, size, grid):
        self.__generate_empty_cells(grid)
        self.__generate_mines(grid)

    def __generate_empty_cells(self, grid):
        for row in grid:
            for cells in row:
                cell = range(cells)
                print(cell)

        # V DVOU DIMENZIONALNICH LISTECH MAME JENOM CISLA [[24],[24]] NECHCEME JE ROVNOU UDELAT [[12345...24],[12345...24]] PAK PRES NE PUJDE ITEROVAT SNADNO

        # PREDCHOZI KOD CO TU ZBYL PO POSLEDNE
        # for row in grid.items():
        #     for cell in row.items():
        #         grid[row][cell] = "test"
        # print(grid[5][5])

    def __generate_mines(self, grid):
        pass


class Cell(PlayingField):
    pass


class Mine(Cell):
    pass


class Empty(Cell):
    pass


playing_field = PlayingField(3)
