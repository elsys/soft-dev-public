def calculate_area(list, row, column):
    if row not in range(len(list)) or column not in range(len(list)):
        return 0, 0
    if list[row][column] == 0:
        return 0, 0

    sum = list[row][column]
    list[row][column] = 0
    pixels = 1

    for i in range(row-1, row+2):
        for j in range(column-1, column+2):
            if (i == row) and (j == column):
                continue
            pixels_to_be_added, sum_to_be_added = calculate_area(list, i, j)
            pixels += pixels_to_be_added
            sum += sum_to_be_added

    return pixels, sum


def avg_brightness(list):
    copy = list
    arr = []
    for row_index, row in enumerate(copy):
        for column_index, element in enumerate(row):
            if element == 0:
                continue

            pixels, sum = calculate_area(copy, row_index, column_index)
            arr.append([ sum/pixels, row_index, column_index])
    
    arr.sort()
    for i in range (0,len(arr)):
        print(f"({arr[i][1]}, {arr[i][2]}) {(arr[i][0]):.2f}")


matrix = [
    [1, 2, 3, 4, 5, 6],
    [0, 0, 0, 0, 0, 0],
    [248, 0, 148, 184, 0, 255],
    [0, 0, 85, 0, 84, 0],
    [238, 0, 0, 0, 0, 255],
    [68, 0, 174, 0, 17, 0]
]
avg_brightness(matrix)