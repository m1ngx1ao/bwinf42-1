tueten_num = 11
geschenk_type_num = 5
geschenk_num_by_type = [2, 11, 6, 2, 1]

tueten_inhalt = [[] for _ in range(11)]

######################
tueten_index = 0
geschenk_num_index = 0
while geschenk_num_index < len(geschenk_num_by_type):
	geschenk_num_value = geschenk_num_by_type[geschenk_num_index]
	while geschenk_num_value > 0:
		tueten_inhalt[tueten_index].append(geschenk_num_index)
		geschenk_num_value -= 1
		if tueten_index < tueten_num - 1:
			tueten_index += 1
		else:
			tueten_index = 0
	geschenk_num_index += 1




#################

print(tueten_inhalt)