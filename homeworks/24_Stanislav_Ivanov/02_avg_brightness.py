def calculate_area(lst: list[list[int]], row: int, col: int) -> tuple[int, int]:
    if row not in range(len(lst)) or col not in range(len(lst)):
        return 0, 0
    if lst[row][col] == 0:
        return 0, 0

    sum_ = lst[row][col]
    lst[row][col] = 0
    pixels = 1

    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            pixels_to_add, sum_to_add = calculate_area(lst, i, j)
            pixels += pixels_to_add
            sum_ += sum_to_add

    return pixels, sum_


def avg_brightness(given_list: list) -> None:
    lst = given_list.copy()
    for index_row, row in enumerate(lst):
        for index_col, element in enumerate(row):
            if element == 0:
                continue

            pixels, sum_ = calculate_area(lst, index_row, index_col)
            print(f"({index_row}, {index_col}) {(sum_/pixels):.2f}")


if __name__ == "__main__":
    test_list = [
        [170, 0, 0, 255, 221, 0],
        [68, 0, 17, 0, 0, 68],
        [221, 0, 238, 136, 0, 255],
        [0, 0, 85, 0, 136, 238],
        [238, 17, 0, 68, 0, 255],
        [85, 170, 0, 221, 17, 0]
    ]
    avg_brightness(test_list)
