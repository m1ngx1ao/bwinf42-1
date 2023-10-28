import os
import PIL.Image
from bild_decoder import decode

dateien = os.scandir('junior2/input')
for datei in dateien:
	name, _ = datei.name.split('.')
	bild = PIL.Image.open(datei.path)
	ergebnis = decode(bild)
	with open(f'junior2/output/{name}.txt', 'w') as f:
		f.write(f'{ergebnis}')
		f.close()