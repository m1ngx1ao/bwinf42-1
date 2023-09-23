# fuer input-datei-namen
# lese datei
# speichere parameter in objekt

class Parameter:
	def __init__(self, datei_namen: str):
	#alle_zahlen = open('input.wundertuete0.txt' ,'r')
		with open(f'junior1/input/{datei_namen}', 'r') as f:
			linien = [int(l.strip()) for l in f.readlines()]
			f.close()
		self.tueten_num = linien[0]
		self.geschenk_type_num = linien[1]
		self.geschenk_num_by_type = linien[2:]

#class Tisch:
#    def __init__(self, laenge: int):
#        self.laenge = laenge
#    def wer_bist_du(self):
#        return f'Ich bin {self.laenge} lang.'
#
#t = Tisch(4.5)
#print(t.wer_bist_du())
#print(t.laenge)

#tueten_num = 11
#geschenk_type_num = 5
#geschenk_num_by_type = [2, 11, 6, 2, 1]
