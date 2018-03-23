# -*- coding: utf-8 -*-

# This program gets all .txt files from Data folder, removes unnecessary text from the paper,
# and then exports to a csv the relevant information
#
# Author: Rebecca Ansems

import glob, os, re, sys, nltk, string, csv
from string import digits
from nltk.corpus import cmudict

phoneme_dict = dict(cmudict.entries())

#NLTK get syllables in word
def syllables_in_word(word):
	if phoneme_dict.has_key(word):   
		return len( [ph for ph in phoneme_dict[word] if ph.strip(string.letters)] )
	else:        
		return 0   

allData = []
path = './bada'

print 'START CLEANING'

#get total number of files
number_files = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
cleaned_data = 1

#open all text files in data folder
for filename in glob.glob(os.path.join(path, '*.txt')):
	contents = ""
	#get information from current file
	with open(filename, 'r') as f:
		for line in f.readlines():
			contents += line

		#dictionary to store information about paper
		info = {}

		#do not include if text is too short (less than 200 characters)
		if len(contents) > 199:

			####INFORMATION GATHERING

			#see if text is english text
			if 'english' in filename:
				info['IsNativeEnglish'] = 1
			else:
				info['IsNativeEnglish'] = 0

			#how many characters were in text
			num_characters = len(contents)
			info['NumberCharacters'] = num_characters

			#how many words were in text
			number_words = len(contents.split())
			info['NumberWords'] = number_words

			#base number of sentences on the number of periods in text
			numPeriods = contents.count('.')
			info['NumberSentences'] = numPeriods

			#count number of syllables per word and add to running total to be stores
			numSyl = 0
			for word in contents.split():
				numSyl += syllables_in_word(word)
				info['NumberSyllables'] = numSyl

			#calculate some averages
			asw = float(numSyl)/float(number_words)
			info['ASW'] = asw
			asl = float(number_words)/float(numPeriods)
			info['ASL'] = asl

			#calculate reading scores
			info['FRES'] = 206.835 - (1.015 * asl) - (84.6 * asw)
			info['FKGL'] = (0.39 * asl) + (11.8 * asw) - 15.59

			#add current information to dictionary of all data and print current 
			print str(cleaned_data) + '/' + str(number_files)+" ",
			cleaned_data += 1
			allData.append(info)


print '\n\nSTART EXPORT'

#save all data to csv
export_counter = 0
with open('Data.csv', 'wb') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['IsNativeEnglish','NumberCharacters','NumberWords','NumberSentences',
		'NumberSyllables','ASW','ASL','FRES','FKGL'])
	for dic in allData:
			writer.writerow([dic['IsNativeEnglish'],dic['NumberCharacters'],dic['NumberWords'],
				dic['NumberSentences'],dic['NumberSyllables'],dic['ASW'],dic['ASL'],dic['FRES'],dic['FKGL']])
			print str(export_counter+1) + '/' + str(len(allData))+" ",
			export_counter += 1