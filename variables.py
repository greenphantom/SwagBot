# Defines the global maps to refrence accross all scripts
import xml.etree.ElementTree as ET
from command_functions import *
import functions
import inspect

def init():
	global command_map
	global function_map
	global alias_map
	global transitive_map
	global termination_list
	global greetings_list
	global send_offs

	command_map = {}
	function_map = {}
	alias_map = {}
	transitive_map = {}
	termination_list = []
	greetings_list = []
	send_offs = []

	termination_list = fill_termination_list()
	command_map = fill_commands()
	map_functions()
	greetings_list = fill_greetings()
	send_offs = fill_send_offs()

def map_functions():
	operations = inspect.getmembers(functions, inspect.isfunction)
	for tup in operations:
		if tup[0] in command_map:
			# bot_print("Added: " + tup[0])
			cmd = command_map.get(tup[0]).addOperation(tup[1])

def fill_commands():
	tree = ET.parse('XML/commands.xml')
	aliases = []
	root = tree.getroot()

	for command in root:
		for element in command:
			if element.tag == "keyword":
				keyword = element.text
				transitive_map.update({keyword:keyword})
			elif element.tag == "desc":
				desc = element.text
			elif element.tag == "others":
				cmd = Command(keyword,desc)
				command_map.update({keyword:cmd})
				for alias in element:
					aliases.append(alias.text)
					transitive_map.update({alias.text:keyword})
				alias_map.update({keyword:aliases})
	return command_map

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