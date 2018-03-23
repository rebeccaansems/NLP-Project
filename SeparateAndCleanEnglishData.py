import re, glob

#used for file naming purposes
counter = 0;

for filename in glob.glob('test.txt'):
	contents = ""
	print 'start'
	#get information from current file
	with open(filename, 'r') as f:
		for line in f.readlines():
			print '*',
			contents += line

	#split on letter.letter
	splitLines = contents.splitlines()
	for para in splitLines:
		if len(para) > 199:
			newFileName = './Data/english ('+str(counter)+').txt'
			
			#save to new file
			text_file = open(newFileName, "w")
			text_file.write(para)
			text_file.close()

			print str(counter) + '/' + len(splitLines)+" ",

			counter += 1


