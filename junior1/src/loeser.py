from input_leser import Parameter

def loese(param: Parameter) -> list[list[int]]:
	result = [[] for _ in range(param.tueten_num)]
	tueten_index = 0
	for geschenk_typ_index in range(0, param.geschenk_typ_num):
		for _ in range(0, param.geschenk_num_by_typ[geschenk_typ_index]):
			result[tueten_index].append(geschenk_typ_index)
			tueten_index = (tueten_index + 1) % param.tueten_num
	return result
