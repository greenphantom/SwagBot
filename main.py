from textblob import TextBlob
import xml.etree.ElementTree as ET
import random
from command_functions import *

def fill_commands():
	command_list = []
	tree = ET.parse('XML/commands.xml')
	aliases = []
	root = tree.getroot()

	for command in root:
		for element in command:
			if element.tag == "keyword":
				keyword = element.text
			elif element.tag == "desc":
				desc = element.text
			elif element.tag == "others":
				for alias in element:
					aliases.append(alias.text)
		command_list.append(Command(keyword,desc,aliases))
		aliases = []
	return command_list

def fill_greetings():
	greetings_list = []
	tree = ET.parse('XML/greetings.xml')
	root = tree.getroot()

	for greeting in root:
		greetings_list.append(greeting.text)
	return greetings_list

def fill_termination_list():
	termination_list = []
	tree = ET.parse('XML/termination_keys.xml')
	root = tree.getroot()

	for key in root:
		termination_list.append(key.text)
	return termination_list

def fill_send_offs():
	send_offs = []
	tree = ET.parse('XML/send_offs.xml')
	root = tree.getroot()

	for key in root:
		send_offs.append(key.text)
	return send_offs

def process_cmd(phrase):
	for cmd in command_list:
		if phrase in cmd:
			command = cmd.primary_keyword
			temp = cmd
			break

	if "text" == command:
		text(termination_list)


	elif "reminder" == command:
		reminder(termination_list)


	elif "commands" == command:
		temp.addOperation(list)
		temp.run(command_list)


	elif "add" == command:
		add()


	else:
		bot_print("ERROR 404: Command not found... returning to main menu...")
		
'''analysis = TextBlob("I really like Python!")'''
termination_list = fill_termination_list()
command_list = fill_commands()
greetings_list = fill_greetings()
send_offs = fill_send_offs()


active = True
bot_print("Welcome to $wagBot v0.01!\n")
while active:
	bot_print(random.choice(greetings_list) + ", how can I help you today?")
	query = prompt_user("Please enter a phrase: ")
	if query in termination_list:
		bot_print(random.choice(send_offs))
		active = False
	elif query in command_list:
		bot_print("Processing command...")
		process_cmd(query)
	else:
		bot_print("I'm confused, let's try again!")
