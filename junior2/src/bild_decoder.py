import PIL.Image

def decode(bild: PIL.Image.Image) -> str:
	loesungssatz = ''
	p = (0, 0)
	old_p = ()
	while p != old_p:
		#j'ai un point p - je dois regarder ce qu'il y a dedans
		char, px, py, *_ = bild.getpixel(p)
		#trouve la lettre
		loesungssatz += chr(char)
		#va au prochain
		old_px, old_py = p
		p = (old_px + px) % bild.width, (old_py + py) % bild.height
		old_p = (old_px, old_py)
	return loesungssatz



def __hole_naechste_infos(x: int, y: int) -> tuple[str, tuple[int, int]]:
	return ('s', (x, y))