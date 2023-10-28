import PIL.Image

def decode(bild: PIL.Image.Image) -> str:
	ergebnis = ''
	p = (0, 0)
	old_p = ()
	while p != old_p:
		char, dx, dy, *_ = bild.getpixel(p)
		ergebnis += chr(char)
		old_p = p
		px, py = p
		p = (px + dx) % bild.width, (py + dy) % bild.height
	return ergebnis