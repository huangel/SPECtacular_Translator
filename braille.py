##############################
# Translates English text to #
# braille					 #
##############################

ascii_string = 'abcdefghijklmnopqrstuvwxyz '
braille_string = '⠈⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽ '
transtab = str.maketrans(ascii_string, braille_string)

def translate_eng_to_brailles(text):
	"""
	input: a string of sentence 
	output: a string of brailles pattern 
	"""
	ascii_string = 'abcdefghijklmnopqrstuvwxyz '
	braille_string = '⠈⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽ '
	transtab = str.maketrans(ascii_string, braille_string)
	return text.lower().translate(transtab)

if __name__ == '__main__':
	text = 'hello My name is Angel'
	print(translate_eng_to_brailles(text))






