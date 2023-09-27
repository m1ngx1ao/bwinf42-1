class Labyrinth():
	def __init__(self, datei_name: str):
		with open(f'aufgabe3/input/{datei_name}', 'r') as f:
			input_str = f.read()
			f.close()
		input_str_wo_size = input_str[input_str.index('\n') + 1:]
		is_wall = []
		for z, input_str_floor in enumerate(input_str_wo_size.split('\n\n')):
			is_wall_floor = []
			for y, input_str_line in enumerate(input_str_floor.split('\n')):
				is_wall_line = []
				for x, input_str_digit in enumerate(input_str_line):
					is_wall_line.append(input_str_digit == '#')
					if input_str_digit == 'A':
						self.a = (x, y, z)
					if input_str_digit == 'B':
						self.b = (x, y, z)
				is_wall_floor.append(is_wall_line)
			is_wall.append(is_wall_floor)
		self.__is_wall = is_wall
		assert self.a is not None
	def is_wall(self, c: tuple[int, int, int]) -> bool:
		x, y, z = c
		return self.__is_wall[z][y][x]
	def get_nachbar_mit_kosten(self, c: tuple[int, int, int]) \
			-> list[tuple[int, tuple[int, int, int]]]:
		return [(3, (4, 5, 1)), (1, (4, 4, 0))]

l = Labyrinth('zauberschule0.txt')
assert l.is_wall((2, 0, 1))
assert not l.is_wall((2, 1, 1))
assert not l.is_wall((10, 7, 0))
assert l.is_wall((10, 8, 0))
assert l.a == (5, 9, 0)
assert l.b == (7, 9, 0)