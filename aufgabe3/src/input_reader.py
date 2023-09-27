blub = 'Hallo Dugg'
a = blub.split(' ')
for b in blub:
	print(b)

input_str = '''13 13
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
input_str = '''#############
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
#############'''

wall_matrix = [
	[s == '#' for s in input_str_line]
	for input_str_line in input_str.split('\n')
]

pass
####

# duggi class labyrinth
class Labyrinth:
	def __init__(self):
		#input_str
		labyrinth = list[bool]
		#for index in line:
		#	if index == '':
		#		first_floor = False
		#	if index == '#':
		#		labyrinth[lines[line[False]]]
		#	else:
		#		labyrinth[lines[line[True]]]
#
		pass
	def is_wall(self, c: tuple[int, int, int]) -> bool:
		return False
	def get_a(self) -> tuple[int, int, int]:
		return (0, 0, 0)
	def get_b(self):
		pass
	def get_nachbar_mit_kosten(self, c: tuple[int, int, int]) \
			-> list[tuple[int, tuple[int, int, int]]]:
		return [(3, (4, 5, 1)), (1, (4, 4, 0))]

l = Labyrinth()
assert l.is_wall(2, 0, 1)
assert not l.is_wall(2, 1, 1)
assert not l.is_wall(10, 7, 0)
assert l.is_wall(10, 8, 0)
#assert l.get_a() == (6, 9, 0)
#assert l.get_b() == (8, 9, 0)