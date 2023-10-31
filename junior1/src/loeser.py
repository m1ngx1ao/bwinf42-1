from input_leser import Parameter

def loese(param: Parameter) -> list[list[int]]:
	# initialisiere fuer jede Tuete eine leere Liste von Geschenken
	result = [[] for _ in range(param.tueten_num)]
	tueten_index = 0
	for geschenk_typ_index in range(0, param.geschenk_typ_num):
		# irrelevant, wie viele Geschenke des Geschenktyps verteilt wurden => _
		for _ in range(0, param.geschenk_num_by_typ[geschenk_typ_index]):
			result[tueten_index].append(geschenk_typ_index)
			# Modulo, damit nach der letzten Tuete mit Index 0 angefangen wird
			tueten_index = (tueten_index + 1) % param.tueten_num
	return result
