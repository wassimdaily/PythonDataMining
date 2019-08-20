import re

def main(fileName, commandRegex):
	dataSet=[]

	with open('input/storyFile.txt') as storyFile:
		for x, line in enumerate(storyFile):
			if (x < 1300 and re.findall(commandRegex, line)):
				dataSet.append(line)

	with open(fileName, 'w') as wFile:
		wFile.writelines('\n'.join(dataSet))

def extract():
	main('output/mountain.txt', r'\bmountains?\b | \bwaterfall\b')
	main('output/hill.txt',r'\bhill\b')
	main('output/flat.txt',r'\bhi\b')
	main('output/sandy.txt',r'\bbeach\b')

extract()