def schreibe(datei_name: str, tueten: list[list[int]]):
	with open(f'junior1/output/{datei_name}', 'w') as f:
		for tuete in tueten:
			f.write(','.join([str(t) for t in tuete]) + '\n')
		f.close()
