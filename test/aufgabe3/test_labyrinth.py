from aufgabe3.src.labyrinth import Labyrinth

labyrinth_input = '''13 13
#############
#.....#.....#
#.###.#.###.#
#...#.#...#.#
###.#.###.#.#
#...#.....#.#
#.#########.#
#.....#.....#
#####.#.###.#
#....A#B..#.#
#.#########.#
#...........#
#############

#############
#.......#...#
#...#.#.#...#
#...#.#.....#
#.###.#.#.###
#.....#.#...#
#####.###...#
#.....#.....#
#.#########.#
#...#.......#
#.#.#.#.###.#
#.#...#...#.#
#############'''

labyrinth_mit_pfad_output = '''#############
#.....#.....#
#.###.#.###.#
#...#.#...#.#
###.#.###.#.#
#...#.....#.#
#.#########.#
#.....#.....#
#####.#.###.#
#....!#B..#.#
#.#########.#
#...........#
#############

#############
#.......#...#
#...#.#.#...#
#...#.#.....#
#.###.#.#.###
#.....#.#...#
#####.###...#
#.....#.....#
#.#########.#
#...#>>!....#
#.#.#.#.###.#
#.#...#...#.#
#############'''

def hole_cut():
	return Labyrinth(labyrinth_input)

def test_mauer():
	cut = hole_cut()
	assert cut.ist_mauer((2, 0, 1))
	assert not cut.ist_mauer((2, 1, 1))
	assert not cut.ist_mauer((10, 7, 0))
	assert cut.ist_mauer((10, 8, 0))

def test_a_b():
	cut = hole_cut()
	assert cut.a == (5, 9, 0)
	assert cut.b == (7, 9, 0)

def test_nachbarn():
	cut = hole_cut()
	assert cut.hole_nachbar_mit_kosten(cut.a) == [
		(1, (5, 8, 0)),
		(1, (4, 9, 0)),
		(3, (5, 9, 1)),
	]
	assert cut.hole_nachbar_mit_kosten(cut.b) == [
		(1, (7, 8, 0)),
		(1, (8, 9, 0)),
		(3, (7, 9, 1)),
	]
	assert cut.hole_nachbar_mit_kosten((7, 10, 1)) == [
		(1, (7, 9, 1)),
		(1, (7, 11, 1)),
	]

def test_hole_richtung():
	cut = hole_cut()
	assert cut.hole_richtung((3, 5, 0), (3, 6, 0)) == 'v'
	assert cut.hole_richtung((3, 6, 0), (3, 5, 0)) == '^'
	assert cut.hole_richtung((3, 5, 0), (4, 5, 0)) == '>'
	assert cut.hole_richtung((3, 5, 0), (2, 5, 0)) == '<'
	assert cut.hole_richtung((3, 5, 0), (3, 5, 1)) == '!'
	assert cut.hole_richtung((3, 5, 1), (3, 5, 0)) == '!'

def test_pfad_darstellung():
	cut = hole_cut()
	labyrinth_input_ohne_erste_linie = labyrinth_input[labyrinth_input.index('\n') + 1:]
	erwartet_ohne_pfad = [
		e.split('\n')
		for e in labyrinth_input_ohne_erste_linie.split('\n\n')
	]
	erwartet_mit_pfad = [
		e.split('\n')
		for e in labyrinth_mit_pfad_output.split('\n\n')
	]
	assert cut.zeige_pfad([]) == erwartet_ohne_pfad
	assert cut.zeige_pfad([
		(5, 9, 0),
		(5, 9, 1),
		(6, 9, 1),
		(7, 9, 1),
		(7, 9, 0)
	]) == erwartet_mit_pfad