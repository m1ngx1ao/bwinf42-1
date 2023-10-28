import os
from labyrinth import Labyrinth
from loeser import loese

dateien = os.scandir('aufgabe3/input')
for datei in dateien:
	with open(f'aufgabe3/input/{datei.name}', 'r') as f:
		input_str = f.read()
		f.close()
	laby = Labyrinth(input_str)
	kosten, pfad = loese(laby)
	ebenen_output = laby.zeige_pfad(pfad)
	with open(f'aufgabe3/output/{datei.name}', 'w') as f:
		f.write(f'Dauer des schnellsten Pfades: {kosten}\n\n')
		for von, bis in zip(pfad[:-1], pfad[1:]):
			f.write(f'{von} {laby.hole_richtung(von, bis)} ')
		f.write(f'{pfad[-1]}\n\n')
		for ebene_output in ebenen_output:
			for reihe_output in ebene_output:
				f.write(reihe_output + '\n')
			f.write('\n')
		f.close()
