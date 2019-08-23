import re as tool

def extract():
	with open('../story.txt') as opFile:
		for x in enumerate(opFile):
			if x[0]< 5:
				writeOn = open('out.txt', "w")
				c = tool.compile(r'([^.]*Life[^.]* | [^.]*lesson[^.]*)', flags=tool.I | tool.X)
				result = '\n'.join(c.findall(x[1]))
				writeOn.write(result)
				print(result)

extract()