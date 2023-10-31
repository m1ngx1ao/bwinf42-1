import heapq
from labyrinth import Labyrinth, punkt_typ

def __konstruire_pfad(letzter_punkt: punkt_typ,
		vorgaenger_fuer_punkt: dict[punkt_typ, punkt_typ | None]) -> list[punkt_typ]:
	ergebnis = []
	p = letzter_punkt
	while p:
		ergebnis.append(p)
		p = vorgaenger_fuer_punkt[p]
	# Punkte des Pfades sind von hinten nach vorne -> Umkehrung notwendig
	ergebnis.reverse()
	return ergebnis

def loese(laby: Labyrinth) -> tuple[int, list[punkt_typ]]:
	gesehen_mit_vorgaenger: dict[punkt_typ, punkt_typ | None] = {}
	# Start mit Punkt A - hat keinen Vorgaenger
	geplant: list[tuple[int, punkt_typ, punkt_typ | None]] \
		= [(0, laby.a, None)]
	while geplant:
		# O(log n) - Liste geplant bleibt nach pop wie Heap strukturiert
		kosten, c, vorgaenger = heapq.heappop(geplant)
		if not c in gesehen_mit_vorgaenger:	
			gesehen_mit_vorgaenger[c] = vorgaenger
			if c == laby.b:
				# Abbruchkriterium der Schleife - Ziel gefunden
				# einmalig O(n)
				return (kosten, __konstruire_pfad(laby.b, gesehen_mit_vorgaenger))
			for naechste_kosten, naechstes_c in laby.hole_nachbar_mit_kosten(c):
				# O(log n) - Liste geplant bleibt nach push wie Heap strukturiert
				heapq.heappush(geplant,
				   (naechste_kosten + kosten, naechstes_c, c)
				)
	# Kein Weg von A nach B -> Aufgabe unloesbar
	assert False