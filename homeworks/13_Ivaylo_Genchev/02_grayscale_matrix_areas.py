from random import randint  # generate random values in a matrix
from dataclasses import dataclass  # cell class

"""
Задача 1:
Графично изображение е представено с матрица от m реда и n колони. Клетките на
матрицата, във всяка от които е записана целочислена стойност от 0 до 255, съответстват на пикселите
в графичното изображение (формат grayscale).
Всяка клетка в матрицата има до 8 съседа — до 4 по диагонал, до два, разположени хоризонтално,
и до два – вертикално.
Област в изображението е непрекъсната последователност от съседни клетки с ненулеви стойности.
Черните елементи, представени със стойност 0, се считат за контури на областите. Така, една област се
определя от граница от нулеви елементи и границите на матрицата.
Дефинирайте функция, `avg_brightness` която получава като аргумент матрица от посочения вид и
извежда на стандартния изход средната яркост на всяка от областите, сортирани в низходящ
ред според яркостта. Средна яркост на дадената област се изчислява като средно-аритметично на
стойностите на всички клетки (пиксели), образуващи областта. За всяка област изведете координатите
на една произволна клетка от нея и средната яркост на областта.
"""


@dataclass
class Cell:
    row: int
    column: int
    value: int
    is_accessed: bool = False  # prevent getting the same area twice

    def __int__(self):
        return self.value


class Matrix:
    def __init__(self, rows: int, columns: int, contour_chance: int):
        """Generate a random grayscale matrix rowsXcolumns where figurations have a contour_chance to appear over any brightness."""
        if rows < 1:
            raise ValueError(
                f"Invalid value {rows}. 'rows' has to be a positive integer."
            )

        if columns < 1:
            raise ValueError(
                f"Invalid value {columns}. 'columns' has to be a positive integer."
            )

        if contour_chance < 1 or contour_chance > 100:
            raise ValueError(
                f"Invalid value {contour_chance}. 'contour_chance' has to be a positive integer."
            )

        self.grayscale_matrix: list[list[Cell]] = [
            [
                Cell(row=m, column=n, value=0)
                if randint(1, 100) < contour_chance
                else Cell(row=m, column=n, value=randint(0, 255))
                for n in range(0, columns)
            ]
            for m in range(0, rows)
        ]
        self.rows = rows
        self.columns = columns

    def surrounding_cells(self, cell: Cell) -> list[Cell]:
        """Get a list of cells surrounding a cell."""
        surrounding: list[Cell] = []

        if cell.row != 0:  # upper
            surrounding.append(self.grayscale_matrix[cell.row - 1][cell.column])
            if cell.column != 0:  # upper left
                surrounding.append(self.grayscale_matrix[cell.row - 1][cell.column - 1])
            if cell.column < self.columns - 1:  # upper right
                surrounding.append(self.grayscale_matrix[cell.row - 1][cell.column + 1])

        if cell.row < self.rows - 1:  # bottom
            surrounding.append(self.grayscale_matrix[cell.row + 1][cell.column])
            if cell.column != 0:  # bottom left
                surrounding.append(self.grayscale_matrix[cell.row + 1][cell.column - 1])
            if cell.column < self.columns - 1:  # bottom right
                surrounding.append(self.grayscale_matrix[cell.row + 1][cell.column + 1])

        if cell.column != 0:  # left
            surrounding.append(self.grayscale_matrix[cell.row][cell.column - 1])

        if cell.column < self.columns - 1:  # right
            surrounding.append(self.grayscale_matrix[cell.row][cell.column + 1])

        return surrounding

    def get_area(self, cell: Cell, area: list[Cell], total_brightness: int = 0) -> int:
        """
        Get a list of all cells surrounded by contours (cells with no brightness).
        List is written in 'area'.
        Function returns total brightness of all cells in the area.
        """

        if cell.is_accessed == False and cell.value != 0:
            # append cell if it hasn't been accessed (avoid repeats) and isn't a contour
            area.append(cell)
            cell.is_accessed = True
            total_brightness += cell.value

            for surrounding in self.surrounding_cells(cell):
                total_brightness = self.get_area(surrounding, area, total_brightness)

        return total_brightness

    def avg_brightness(self):
        """Calculate average brightness of all areas."""

        areas: list[tuple[tuple[Cell], int]] = []

        for row in self.grayscale_matrix:
            for cell in row:
                if cell.is_accessed == False and cell.value != 0:  # redundant
                    area: list[Cell] = []
                    total_brightness: int = self.get_area(cell, area)

                    # append area tuple and avrg brightness
                    areas.append((tuple(area), total_brightness / len(area)))

        # sort new list based on average brightness in descending order
        areas.sort(reverse=True, key=lambda x: x[1])

        # print info
        for area_info in areas:
            print("-----------------------------------------------------------")
            print(f"Cells in area: {len(area_info[0])}")
            random_cell: Cell = area_info[0][randint(0, len(area_info[0]) - 1)]
            print(
                f"Random cell ({random_cell.value}): ({random_cell.row},{random_cell.column})"
            )
            print(f"Average brightness: {round(area_info[1], 2)}")

    def __str__(self) -> str:
        matrix_str: str = ""
        most_number_digits: int = 3

        for row in self.grayscale_matrix:
            for cell in row:

                matrix_str += f" {cell.value}{(most_number_digits - len(str(cell.value)) + 1) * ' '}"
            matrix_str += "\n\n\n"

        return matrix_str


if __name__ == "__main__":
    matrix: Matrix = Matrix(rows=8, columns=8, contour_chance=70)
    print(matrix)
    matrix.avg_brightness()
