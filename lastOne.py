import re as tool

# file paths
file = 'story.txt'
out = 'out.txt'

opFile = open(file, "r").read()
writeOn = open(out, "w")
	
def extract():
	c = tool.compile(r'([^.]*Life[^.]* | [^.]*lesson[^.]*)', flags=tool.I | tool.X)
	result = '\n \n'.join(c.findall(opFile))
	writeOn.write(result)
	print(result)

extract()