class Card:
	"""
	"""
	valid_suit = ['heart', 'diamond', 'club', 'spade']
	valid_values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
	valid_color = ['red', 'black']
	suit_graphic = {'heart': '\u2665', 'diamond': '\u2666', 'club': '\u2663', 'spade': '\u2660'}

	def __init__(self, suit, value, color = None):
		"""
		TODO: add color!
		"""
		if suit not in self.valid_suit:
			# TODO: raise an exception
			print(f'Card suit {suit} is not valid')
		else:
			self.suit = suit
		if value not in self.valid_values:
			# TODO: raise an exception
			print(f'Card value {value} is not valid')
		else:
			self.value = value
		self.card_length = 14
		self.card_height = 8
		self.color = None

	def __repr__(self):
		"""
		"""
		side_bars = '||'
		top_bars = '='
		vert_line = f'\t.:{top_bars * (self.card_length - 4)}:.\n'
		empty_line = f"\t{side_bars}{' ' * (self.card_length - len(side_bars) * 2)}{side_bars}\n"

		num = f' {str(self.value)}'
		symbol = f'{self.suit_graphic[self.suit]} '
		first_line = f"\t{side_bars}{num}{' ' * (self.card_length - len(side_bars) * 2 - len(num) - len(symbol))}{symbol}{side_bars}\n"

		output = vert_line
		output += first_line
		for i in range(0, self.card_height - 1):
			output += empty_line
		output += vert_line

		return output
