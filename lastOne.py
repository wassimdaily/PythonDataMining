import re as tool

def extract():
	opFile = open('story.txt', "r").read()
	writeOn = open('out.txt', "w")
	c = tool.compile(r'([^.]*Life[^.]* | [^.]*lesson[^.]*)', flags=tool.I | tool.X)
	result = '\n \n'.join(c.findall(opFile))
	writeOn.write(result)
	print(result)

extract()