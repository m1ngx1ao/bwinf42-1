import PIL.Image

def decode(bild: PIL.Image.Image) -> str:
	ergebnis = ''
	p = (0, 0)
	alt_p = None
	while p != alt_p:
		# vierter Wert ist manchmal gesetzt (alpha-Kanal), aber hier irrelevant
		iso_code, dx, dy, *_ = bild.getpixel(p)
		# chr gibt character auch für nicht-ASCII Codes
		ergebnis += chr(iso_code)
		alt_p = px, py = p
		# Modulo damit nach Grenze rechts / unten es wieder links / oben im Bild weitergeht
		p = (px + dx) % bild.width, (py + dy) % bild.height
	return ergebnis
