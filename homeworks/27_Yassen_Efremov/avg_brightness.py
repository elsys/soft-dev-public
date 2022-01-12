# =============================================================================================== #
# Classes, Functions, Global variables #


def avg_recursive(matrix, cell_row, cell_col, avg_region_brightness):
	avg_region_brightness.append(matrix[cell_row][cell_col])		# add the brightness of the current cell
	matrix[cell_row][cell_col] = 0	# Mark the cell as visited
	# Start calling the function recursively on all the neighboor cells
	for i in range(-1, 2):
		for j in range(-1, 2):
			# Check if the next indexes are out of range
			if (0 <= cell_row + i < len(matrix)) and (0 <= cell_col + j < len(matrix[0])):
				# Check if the next cell has brightness 0 or is the current cell
				if (matrix[cell_row + i][cell_col + j] != 0) and ([i, j] != [0, 0]):
					avg_recursive(matrix, cell_row + i, cell_col + j, avg_region_brightness)		


def avg_brightness(matrix):
	matrix_copy = [list(matrix_inner) for matrix_inner in matrix]		# copy so that we don't modify the passed list
	avg_brightnesses = []

	# Look for cells with brightness above 0 and start recursively going through them
	for i in range(0, len(matrix_copy)):
		for j in range(0, len(matrix_copy[0])):
			if matrix_copy[i][j] > 0:
				avg_region_brightness = []
				avg_recursive(matrix_copy, i, j, avg_region_brightness)
				avg_brightnesses.append(avg_region_brightness)

	avg_brightnesses.sort(key = lambda row: sum(row) / len(row), reverse=True)
	for row in avg_brightnesses:
		print(sum(row) / len(row))


# =============================================================================================== #


def main():

	# Example
	matrix = (
		(170,   0,   0, 255, 221,   0),
		( 68,   0,  17,   0,   0,  68),
		(221,   0, 238, 136,   0, 255),
		(  0,   0,  85,   0, 136, 238),
		(238,  17,   0,  68,   0, 255),
		( 85, 170,   0, 221,  17,   0)
	)

	avg_brightness(matrix)


# =============================================================================================== #


if __name__ == "__main__":
	main()
