def cp(txt="",a="w",b="bk",inpu=False,flu=False):
	fg={
		"bk": 30, 
		"r" : 91,
		"g" : 92,
		"y" : 93,
		"b" : 94,
		"p" : 95,
		"cy": 96,
		"w" : 97,
		"c" : "0"
	}
	bg={
		"bk": 40,
		"r" : 41,
		"g" : 42,
		"y" : 43,
		"b" : 44,
		"p" : 45,
		"cy": 46,
		"w" : 47,
		"c" : "0"
	}
	if inpu==True:
		return f"\033[1;{fg[a]};{bg[b]}m{txt}\033[0m \033[1;{fg['y']};{bg['bk']}m"
	else: return f"\033[1;{fg[a]};{bg[b]}m{txt}\033[0m"
	if fl==True:
		return"\033[0m"
def main():
	pass
main()
"""
black = bk
red = r
green = g
yellow = y
blue = b
magenta = p
cyan = cy
white = w
reset = c
"""
