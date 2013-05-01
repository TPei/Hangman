# hangman helper functions

# check if guessed letter is in word (word can be a word, list ...)
def is_in_word(guess, word):
	#print guess
	#print word
	for letter in word:
		if letter == guess:
			return True
			
	return False

# check if guessed word is word
def is_word(guess, word):
    if guess == word:
        return True
    else:
        return False

# get length of file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
        
dict = {}
def get_word_template(word, progress_word, guess):
	# split word by guess
	split_word = word.split(guess)
	
	# list the postions at which the guessed letter was found
	letter_list = [-1]
	
	# find split elements from word split by guess
	for sub in split_word:
		# save positions of found letters
		letter_list.append(letter_list[-1]+len(sub)+1)
		
	# remove first element (we only needed it for calculations)
	letter_list.pop(0)
	# remove last element, because it's the end of the word
	letter_list.pop()
	
	# add letters to dictionary with position as key
	for i in letter_list:
		dict[str(i)] = guess
		
	new_word = ""
	
	# go through dictionary and add either '_' or the dictionary entry to new_word
	for i in range(0, len(word)):
		# if we know a letter at that position of the word
		if str(i) in dict:
			new_word += str( dict[str(i)] )
		else:
			new_word += "_ "
		
	#print new_word	
	#print dict	
	#print letter_list
	return new_word
		
	
def bla():
# check if letter is in word
	if helper.is_in_word(guess, word):
		print "yay"
		letter_list = [0]
		#for i in letter_list:
		split_word = word.split(guess);
		for sub in split_word:
			letter_list.append(letter_list[-1]+ len(sub))
			
		"""				
		# split word so that we can replace the letters by '_' and gradually go back
		split_word = word.split(guess);
		# count all substrings between found letters and replace by '_'
		for sub in split_word:
			# save positions of found letters
			letter_list = [0]
			for i in letter_list:
				letter_list.append(1) #letter_list[-1]+ len(sub))
			if sub != split_word[-1]:
				disguised_word += str(" _"*len(sub)) + str(guess)
			else:
				disguised_word += str("_ "*len(sub))
		print disguised_word"""
		print letter_list