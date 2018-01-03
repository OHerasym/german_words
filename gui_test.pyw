import easygui
import io
import random
import time
import ctypes

MessageBox = ctypes.windll.user32.MessageBoxW

words = [word.split(',') for word in io.open('words.txt', mode='r', encoding='utf-8')]

def set_answers(list_answers):
	return random.shuffle(list_answers)

def get_random():
	return random.randrange(len(words))

def check_word(word, answer):
	field_names = ['Enter word:']
	field_value = easygui.multenterbox(word, '123', field_names)
	check_work = ' ' + field_value[0]

	if check_work in answer:
		pass
	else:
		MessageBox(None, 'Correct is: ' + answer, 'Wrong!', 0)
		check_word(word, answer)


for i in range(len(words)):
	random_1, random_2, random_3 = get_random(), get_random(), get_random()
	random_4, random_5, random_6 = get_random(), get_random(), get_random()

	answers = [words[random_1][1], words[random_2][1], words[random_3][1]]
	answers_2 = [words[random_4][0], words[random_5][0], words[random_6][0]]
	set_answers(answers)
	set_answers(answers_2)

	answer = easygui.buttonbox(words[random_1][0], 'German', answers)
	None if answer is words[random_1][1] else MessageBox(None, 'Wrong!', 'Wrong!', 0)

	answer_2 = easygui.buttonbox(words[random_4][1], 'Ukr', answers_2)
	None if answer_2 is words[random_4][0] else MessageBox(None, 'Wrong!', 'Wrong!', 0)

	check_word(words[random_1][0], words[random_1][1])

	time.sleep(300)