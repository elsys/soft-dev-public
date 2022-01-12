from copy import deepcopy
from random import randint

def check_sides(matrix, x, y, shape_coords_list = None):
	matrix_cpy = matrix
	if shape_coords_list is None:
		shape_coords_list = []
	shape_coords_list.append((x, y))
	matrix_cpy[x][y] = 0
	if x - 1 >= 0 and matrix_cpy[x - 1][y] != 0:
		check_sides(matrix_cpy, x - 1, y, shape_coords_list)

	if y - 1 >= 0 and matrix_cpy[x][y - 1] != 0:
		check_sides(matrix_cpy, x, y - 1, shape_coords_list)

	if y + 1 < len(matrix[0]) and matrix_cpy[x][y + 1] != 0:
		check_sides(matrix_cpy, x, y + 1, shape_coords_list)

	if x + 1 < len(matrix) and matrix_cpy[x + 1][y] != 0:
		check_sides(matrix_cpy, x + 1, y, shape_coords_list)

	if x - 1 >= 0  and y - 1 >= 0 and matrix_cpy[x - 1][y - 1] != 0:
		check_sides(matrix_cpy, x - 1, y - 1, shape_coords_list)

	if x - 1 >= 0  and y + 1 < len(matrix[0]) and matrix_cpy[x - 1][y + 1] != 0:
		check_sides(matrix_cpy, x - 1, y + 1, shape_coords_list)

	if x + 1 < len(matrix) and y - 1 >= 0 and  matrix_cpy[x + 1][y - 1] != 0:
		check_sides(matrix_cpy, x + 1, y - 1, shape_coords_list)
		
	if x + 1 < len(matrix) and y + 1 < len(matrix[0]) and matrix_cpy[x + 1][y + 1] != 0:
		check_sides(matrix_cpy, x + 1, y + 1, shape_coords_list)

	return shape_coords_list

def brigthness(list, matrix):
	sum = 0
	for i in list:
		x = i[0]
		y = i[1]
		sum += matrix[x][y]
	return (sum / len(list))

def avg_brigthness(matrix):
	copy_of_img = deepcopy(matrix)
	list = []
	for i in range(len(copy_of_img)):
		for j in range(len(copy_of_img[i])):
			if len(list) > 1:
				for k in range(len(list)):
					if (i, j) not in list[k] and copy_of_img[i][j] != 0:
						list.append(check_sides(copy_of_img, i, j))
			else:
				if copy_of_img[i][j] != 0:
					list.append(check_sides(copy_of_img, i, j))

	brigthness_list = []
	sum = 0
	for i in range(len(list)):
		brigthness_list.append(brigthness(list[i], matrix))
	brigthness_list.sort(reverse = True)
	print(brigthness_list)
	
	for i in list:
		print(brigthness(i, matrix), i[randint(0, len(i) - 1)])