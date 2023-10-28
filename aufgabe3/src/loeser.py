import heapq
from labyrinth import Labyrinth

def loese(laby: Labyrinth) -> tuple[int, list[tuple[int, int, int]]]:
	gesehen: set[tuple[int, int, int]] = set()
	geplant: list[tuple[int, tuple[int, int, int], list[tuple[int, int, int]]]] \
		= [(0, laby.a, [laby.a])]
	while geplant:
		kosten, c, pfad = heapq.heappop(geplant)
		if c == laby.b:
			return (kosten, pfad)
		if not c in gesehen:	
			gesehen.add(c)
			for naechste_kosten, naechstes_c in laby.hole_nachbar_mit_kosten(c):
				heapq.heappush(geplant,
				   (naechste_kosten + kosten, naechstes_c, pfad + [naechstes_c])
				)
	assert False