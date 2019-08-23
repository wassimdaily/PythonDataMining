import re as tool


# file paths
file = 'story.txt'
out = 'out.txt'

writeOn = open(out, "w")
	
def extract():
	dataSet=[]

	with open(file) as opFile:
		for x, line in enumerate(opFile):
			c = tool.compile(r'([^.]*Life[^.]* | [^.]*lesson[^.]*)', flags=tool.I | tool.X)
			result = c.findall(opFile)
			if (x < 1300 and result):
				dataSet.append(line)


extract()