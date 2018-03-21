# This program gets all .txt files from Data folder, removes unnecessary text from the paper,
# and then exports to a csv the relevant information
#
# Author: Rebecca Ansems
import glob, os, re, sys, nltk, string
from string import digits
from nltk.corpus import cmudict 

reload(sys)
sys.setdefaultencoding('utf8#')

phoneme_dict = dict(cmudict.entries())

def syllables_in_word(word):
    if phoneme_dict.has_key(word):   
        return len( [ph for ph in phoneme_dict[word] if ph.strip(string.letters)] )
    else:        
        return 0   

#open all text files in data folder
path = './Data/'
for filename in glob.glob(os.path.join(path, '*.txt')):
	contents = ""
	counter = 0
	#get information from current file
	with open(filename, 'r') as f:
		for line in f.readlines():
			contents += line

		#dictionary to store information about paper
		info = {}

		#INFORMATION CLEANING

		#convert to ascii and remove numbers
		contents = contents.encode('ascii',errors='ignore')
		contents = contents.translate(None, digits)

		#make all lowercase
		contents = contents.lower()

		#remove everything after "references" or "works cited"
		contents = contents.split('references', 1)[0]
		contents = contents.split('works cited', 1)[0]

		#INFORMATION GATHERING

		#see if text is english text
		if 'english' in filename:
			info['IsNativeEnglish'] = True
		else:
			info['IsNativeEnglish'] = False

		#how many words were in text
		info['NumberWords'] = len(contents.split())

		#count number of syllables per word and add to running total to be stores
		numSyl = 0
		for word in contents.split():
			numSyl += syllables_in_word(word)
			info['NumberSyllables'] = numSyl

		print info
