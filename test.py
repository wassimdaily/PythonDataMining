import re


dataSet=[]

with open('story.txt') as storyFile:
	for x in enumerate(storyFile):
		if x[0]< 10:

			print x[0]
