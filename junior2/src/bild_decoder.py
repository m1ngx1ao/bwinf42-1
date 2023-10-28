import PIL.Image

def decode(bild: PIL.Image.Image) -> str:
	ergebnis = ''
	p = (0, 0)
	alt_p = None
	while p != alt_p:
		iso_code, dx, dy, *_ = bild.getpixel(p)
		ergebnis += chr(iso_code)
		alt_p = px, py = p
		p = (px + dx) % bild.width, (py + dy) % bild.height
	return ergebnis
