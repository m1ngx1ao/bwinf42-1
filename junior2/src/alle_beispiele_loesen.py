import os
import PIL.Image
from bild_decoder import decode

for datei in os.scandir('junior2/input'):
	name, _ = datei.name.split('.')
	loesungswort = decode(PIL.Image.open(datei.path))
	with open(f'junior2/output/{name}.txt', 'w', encoding='utf-8') as f:
		f.write(loesungswort)
		f.close()