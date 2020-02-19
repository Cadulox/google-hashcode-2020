def open_file(path):
	with open(f'./input/{path}.in', 'r') as file:
		content = []
		for item in file:
			content.append(item)
		return content


def get_max_slices(list_value):
	aux = ''
	for n in list_value:
		if n == ' ':
			break
		aux += n
	target = int(aux)
	return target


def get_slices(list_slices):
	slices = []
	temp1 = list_slices.split('\n')
	temp2 = temp1[0].split(' ')
	for number in temp2:
		slices.append(int(number))
	return slices


def solve_problem(total_slices, nums_slices):
	best_solution = []
	score = j = 0
	i = len(nums_slices) - 1
	test1 = test2 = True
	while (i >= 0) and test1:
		temp_best_solution = []
		j = i
		add = 0
		while (j >= 0) and test2:
			temp = nums_slices[j]
			if (add + temp) < total_slices:
				add += temp
				temp_best_solution.append(j)
			elif (add + temp) == total_slices:
				add += temp
				temp_best_solution.append(j)
				test1 = False
				test2 = False
			j -= 1
		if score < add:
			score = add
			best_solution = temp_best_solution
		if len(best_solution) == len(nums_slices):
			test1 = False
		i -= 1
	return sorted(best_solution)


def save_file(list_output, path):
	op = str(len(list_output)) + '\n'
	for item in list_output:
		op += str(item) + ' '
	with open(f'./output/{path}.out', 'w') as fileOutput:
		fileOutput.write(op)


fileNames = ("a_example", "b_small", "c_medium", "d_quite_big", "e_also_big")
for name in fileNames:
	result = open_file(name)
	max_slices = get_max_slices(result[0])
	number_slices = get_slices(result[1])
	output = solve_problem(max_slices, number_slices)
	save_file(output, name)
