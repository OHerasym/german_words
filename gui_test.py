import sys
import easygui
import codecs
import io
import random
import time

words = [word.split(',') for word in io.open('words.txt', mode='r', encoding='utf-8')]

def set_answers(list_answers):
	return random.shuffle(list_answers)

for i in range(len(words)):
	random_1 = random.randrange(len(words))
	random_2 = random.randrange(len(words))
	random_3 = random.randrange(len(words))

	random_4 = random.randrange(len(words))
	random_5 = random.randrange(len(words))
	random_6 = random.randrange(len(words))

	answers = [words[random_1][1], words[random_2][1], words[random_3][1]]
	answers_2 = [words[random_4][0], words[random_5][0], words[random_6][0]]
	set_answers(answers)
	set_answers(answers_2)

	answer = easygui.buttonbox(words[random_1][0], 'German', answers)
	print('OK!') if answer is words[random_1][1] else print('Wrong!')

	answer_2 = easygui.buttonbox(words[random_4][1], 'Ukr', answers_2)
	print('OK2!') if answer_2 is words[random_4][0] else print('Wrong2!')
	
	field_names = ['Enter word:']
	field_value = easygui.multenterbox(words[random_1][0], '123', field_names)

	check_work = ' ' + field_value[0]

	if check_work in words[random_1][1]:
		print('OK OK!')
	else:
		print('Wrong Wrong!\nCorrect answer: ', words[random_1][1])

	time.sleep(300)