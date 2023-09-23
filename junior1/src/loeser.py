from input_leser import Parameter

def loese(param: Parameter) -> list[list[int]]:
    tueten_inhalt = [[] for _ in range(param.tueten_num)]
    tueten_index = 0
    geschenk_num_index = 0
    while geschenk_num_index < len(param.geschenk_num_by_type):
        geschenk_num_value = param.geschenk_num_by_type[geschenk_num_index]
        while geschenk_num_value > 0:
            tueten_inhalt[tueten_index].append(geschenk_num_index)
            geschenk_num_value -= 1
            if tueten_index < param.tueten_num - 1:
                tueten_index += 1
            else:
                tueten_index = 0
        geschenk_num_index += 1
    return tueten_inhalt