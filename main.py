import re as tool

# file paths
story = 'storyFile.txt'
input = 'input.txt'
output = 'output.txt'

storyFile = open(story, "r").read(5)


def findData():
	writeOn = open(output, "w")
	with open(input) as fp:
		line = fp.readline()
		while line:
			line = fp.readline()
			targetMatch = "[^.]* "+line+" [^.]*\."
			searcher = tool.findall(targetMatch, storyFile)
			writeOn.write(str(searcher))
			print(searcher)
	writeOn.close()
	fp.close()

findData()