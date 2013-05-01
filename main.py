import sys
from random import randint
import helper

def hangman():


	# open file with words, get random word, close file
	file = open("Nouns.txt", "rU") # rU removes \n when reading lines
	file_length = helper.file_len("Nouns.txt") # number of lines in document
	word = str(file.readlines()[randint(1, file_length+1)])
	file.close()
	word = word[0: -1] # remove last character, it's something like \r or so
	
	# list of already guessed letters:
	guess_list = []
	
	# set disguised word to all '_' in the beginning
	disguised_word = "_ "*len(word)
	
	# number of lives in hangman game
	lives = 15
	
	# tell the user about the game and hint the length of the word
	print "\nLet's play hangman, simply choose a letter: "
	
	# progress_word
	progress_word = disguised_word
	
	# print word
	print disguised_word
		
	while True:	
		# reset guess
		guess = ""
		
		# to test if the guess is a duplicate
		already = True
		
		while len(guess) < 1 or already:
			# ask for letter input
			print "\nguessed letters so far:", guess_list
			guess = raw_input("Pick a letter (or try to guess the entire word): ")
			if not helper.is_in_word(guess, guess_list):
				already = False
			else:
				print "you already tried that letter:", guess
				# print word
				print disguised_word
						
		guess_list.append(guess)
		guess_list.sort()
		
		if len(guess) == 1:
			if helper.is_in_word(guess, word):
				print "yay,",guess,"is part of my word"
				disguised_word = helper.get_word_template(word, progress_word, guess)
				if disguised_word == word:
					print "yay, you found my word:", word
					break
				print disguised_word
			else:
				print "nay"
				lives -= 1
				if lives <= 0:
					print "I'm sorry, you are dead!"
					print "my word was:", word
					break
				print "remaining lives", lives
				print disguised_word
		
		# check if guessed word is word
		else:
			if helper.is_word(guess, word):
				print "yay, you found my word:",word
				break
			else:
				lives -= 1
				if lives <= 0:
					print "I'm sorry, you are dead!"
					print "my word was:", word
					break
				print "nay"
				print "remaining lives:", lives
				print disguised_word
        		
if __name__ == '__main__':
	hangman()      		
# let's play hangman!

