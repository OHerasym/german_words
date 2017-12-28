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
	answers = [words[random_1][1], words[random_2][1], words[random_3][1]]
	set_answers(answers)
	answer = easygui.buttonbox(words[random_1][0], 'German', answers)


	if answer is words[random_1][1]:
		print('OK!')
	else:
		print('Wrong!')
	
	field_names = ['Enter word:']
	field_value = easygui.multenterbox(words[random_1][0], '123', field_names)
	# print(field_value)
	# print(field_value[0])
	# print(words[random_1][1])

	check_work = ' ' + field_value[0]
	# print(check_work)

	if check_work in words[random_1][1]:
		print('OK OK!')
	else:
		print('Wrong Wrong!')
		print('Correct answer: ', words[random_1][1])

	time.sleep(400)