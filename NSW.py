# Name: Chloe Sheen
# CMSC208 Assignment 5
# Fall 2017

# Example text as a string.
mytext = """NSWs must be classified for phonetic analysis.
This is especially important in the case of numbers,
which differ in their pronunciation depending on their category.
For example, it is necessary to distinguish a year like 1849 from a PIN like 3269.
Phone numbers come in variable forms like 234-6529 or 492-499-1349 or (203)893-5938.
Zip codes can also vary between 29481 or 49381-2395. Below is a PHONE NUMBER
818-279-5902. Below shouldn't be a PHONE NUMBER (818)279-59021.
Below is a ZIP CODE 19010. Below is a YEAR 1996. PASSED ALL TESTS."""

# Strips periods from sentence-final words.
def remove_punctuation(text):
   return [w[:-1] if w[-1] == '.' else w for w in text]

# Returns true iff string c is a single digit
def is_digit(c):
   return c in '0123456789'

# Returns true iff string w consists of all digits.
def is_string_of_digits(w):
   for c in w:
	  if not is_digit(c):
		 return False
   return True

# Returns true iff string w is of the form XXXXX or XXXXX-XXXX where X is a digit.
def is_zip(w):
	if len(w) == 5 or len(w) == 10:
		if len(w) == 10:
			zlist = []
			for i in enumerate(w):
				zlist.append(i)
				zdict = dict(zlist)
			if zdict[5] == '-':
				return True
		return is_string_of_digits(w)
	return False

# Identify phone numbers.
def is_phone(w):
	if len(w) >= 8 and len(w)<13:
		plist = []
		numlist = ['0','1','2','3','4','5','6','7','8','9']
		for i in enumerate(w):
			plist.append(i)
			pdict = dict(plist)

		if pdict[1] in numlist and pdict[3] not in numlist or pdict[0] is '(':
			return True
		return is_string_of_digits(w)
	return False

# Suggested approach to distinguishing years from PINs.
# Returns true iff string word is found in list wordlist within scan_range positions (left or right) of start_pos.
def scan(w, wordlist, word, start_pos, scan_range):
	numlist = ['0','1','2','3','4','5','6','7','8','9']
	if len(w) == 4:
		if is_string_of_digits(w) is True:
			idx = (i for i,w in enumerate(wordlist) if w==word)
			neighbors = []
			for i in idx:
				neighbors.append(wordlist[start_pos-scan_range:start_pos] + wordlist[start_pos+1:start_pos+scan_range])
			for j in range(0,scan_range):
				if neighbors[0][j] == word:
					return True
	return False

# Takes a text t as a list of words with sentence-final punctuation removed and returns that text with markup for the following NSW categories: zip codes, phone numbers, years, and PINs.
def NSW_markup(t):
	markedup = []
	i = 0
	while i < len(t):
		if is_zip(t[i]):
			print '<zip>', t[i], '</zip>'
		elif is_phone(t[i]):
			print '<phone>', t[i], '</phone>'
		elif scan(t[i], t, "PIN", i, 2):
			print '<pin>', t[i], '</pin>'
		elif scan(t[i], t, "PIN", i, 2) is False and is_string_of_digits(t[i]) is True:
			print '<year>', t[i], '</year>'
		else:
			print t[i]
		i+=1
	return markedup

def demo():
   print NSW_markup(remove_punctuation(mytext.split()))

if __name__ == '__main__':
   demo()
