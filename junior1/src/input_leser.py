class Parameter:
	def __init__(self, datei_name: str):
		with open(f'junior1/input/{datei_name}', 'r') as f:
			linien = [int(l.strip()) for l in f.readlines()]
			f.close()
		self.tueten_num = linien[0]
		self.geschenk_type_num = linien[1]
		self.geschenk_num_by_type = linien[2:]