punkt_typ = tuple[int, int, int]

class Labyrinth:
	def __init__(self, input_str: str):
		input_str_ohne_groesse = input_str[input_str.index('\n') + 1:]
		ist_mauer : list[list[list[bool]]] = []
		for z, input_str_ebene in enumerate(input_str_ohne_groesse.split('\n\n')):
			ist_mauer_ebene = []
			for y, input_str_reihe in enumerate(input_str_ebene.split('\n')):
				ist_mauer_reihe = []
				for x, input_str_char in enumerate(input_str_reihe):
					ist_mauer_reihe.append(input_str_char == '#')
					if input_str_char == 'A':
						self.a = (x, y, z)
					if input_str_char == 'B':
						self.b = (x, y, z)
				ist_mauer_ebene.append(ist_mauer_reihe)
			ist_mauer.append(ist_mauer_ebene)
		self.__ist_mauer = ist_mauer
		assert self.a is not None
	def ist_mauer(self, c: punkt_typ) -> bool:
		x, y, z = c
		return self.__ist_mauer[z][y][x]
	def hole_nachbar_mit_kosten(self, c: punkt_typ) \
			-> list[tuple[int, punkt_typ]]:
		x, y, z = c
		kandidaten = [
			(1, (x, y - 1, z)),
			(1, (x - 1, y, z)),
			(1, (x, y + 1, z)),
			(1, (x + 1, y, z)),
			(3, (x, y, 1 - z))
		]
		# k sind die Kosten, c der Kandidat 
		# - ist c eine Mauer? dann aussortieren
		return [(k, c) for k, c in kandidaten if not self.ist_mauer(c)]
	def hole_richtung(self, von: punkt_typ, bis: punkt_typ) -> str:
		vx, vy, vz = von
		bx, by, bz = bis
		# irrelevant, in welche Richtung die Etage gewechselt wurde
		# -> nur der Betrag relevant
		bewegung = (bx - vx, by - vy, abs(bz - vz))
		match bewegung:
			case -1, 0, 0:
				return '<'
			case 1, 0, 0:
				return '>'
			case 0, -1, 0:
				return '^'
			case 0, 1, 0:
				return 'v'
			case 0, 0, 1:
				return '!'
		# Anfrage einer Bewegung nicht zum Nachbarn -> Fehler
		assert False
	def zeige_pfad(self, pfad: list[punkt_typ]) -> list[list[str]]:
		darstellung = [
			[
				['#' if b else '.' for b in mauer_reihe]
				for mauer_reihe in mauer_ebene
			]
			for mauer_ebene in self.__ist_mauer
		]
		ax, ay, az = self.a
		darstellung[az][ay][ax] = 'A'
		bx, by, bz = self.b
		darstellung[bz][by][bx] = 'B'
		for stelle in range(0, len(pfad) - 1):
			x, y, z = pfad[stelle]
			darstellung[z][y][x] = self.hole_richtung(pfad[stelle], pfad[stelle + 1])
		return [
			[''.join(mauer_reihe) for mauer_reihe in mauer_ebene]
			for mauer_ebene in darstellung
		]