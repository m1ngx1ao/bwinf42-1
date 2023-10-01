import os
from labyrinth import Labyrinth

dateien = os.scandir('aufgabe3/input')
for datei in dateien:
	with open(f'aufgabe3/input/{datei.name}', 'r') as f:
		input_str = f.read()
		f.close()
	l = Labyrinth(input_str)
	ebenen_output = l.zeige_pfad([])
	with open(f'aufgabe3/output/{datei.name}', 'w') as f:
		for ebene_output in ebenen_output:
			for reihe_output in ebene_output:
				f.write(reihe_output + '\n')
			f.write('\n')
		f.close()