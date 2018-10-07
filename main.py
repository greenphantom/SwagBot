from textblob import TextBlob
import random
import operator
from command_functions import *
from auxilary_functions import *
import variables

def process_cmd(phrase):
	if phrase in variables.transitive_map:
			temp = variables.command_map.get(variables.transitive_map.get(phrase))
			temp.run()
	else:
		bot_print("ERROR 404: Command not found... returning to main menu...")
		
'''analysis = TextBlob("I really like Python!")'''
variables.init()

active = True
bot_print("Welcome to $wagBot v0.02!\n")
while active:
	bot_print(random.choice(variables.greetings_list) + ", how can I help you today?")
	query = prompt_user("Please enter a phrase: ")
	query = query.lower()
	if query in variables.termination_list:
		bot_print(random.choice(variables.send_offs))
		active = False
	elif query in variables.transitive_map:
		bot_print("Processing command...")
		process_cmd(query)
	else:
		bot_print("I'm confused, let's try again!")
