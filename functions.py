# Module contains all the functions that are tied to commands
# Functions are linked via name (i.e. functions should be named the same as the primary keyword of the command)
# As of now, all functions must take in variables.command_map,variables.termination_list,and variables.alias_map

import datetime
import time
import xml.etree.ElementTree as ET

from auxilary_functions import *
import variables

'''accountSID = '' #fill your Twilio SID here
authenticationToken = '' # fill your Twilio AuthToken here

twilioClient = Client(accountSID, authenticationToken)
twilioNumber = '' # fill your Twilio number here
phoneNumber = '' # fill your default number here. Must be verfied by Twilio if using a free account'''

def add():
	bot_print("Sure, thing...")
	cmd_name = prompt_user("What the name of the new command?: ")
	alias = prompt_user("Enter available aliases to edit (put space between phrases): ").split()
	desc = prompt_user("Enter a description for you new command: ")
	tree = ET.parse('XML/commands.xml')
	root = tree.getroot()
	commands = ET.SubElement(root,'temp')
	new_command = ET.SubElement(commands,"command")
	new_command_key = ET.SubElement(new_command,"keyword")
	new_command_key.text = cmd_name
	new_command_other = ET.SubElement(new_command,"others")
	if len(aliases) > 0:
		for alias in aliases:
			child = ET.SubElement(new_command_other,"alias")
			child.text = alias
	new_command_desc = ET.SubElement(new_command,"desc")
	new_command_desc.text = desc
	tree.write('XML/commands.xml')
	variables.command_map.update({cmd_name:Command(cmd_name, desc)})
	variables.alias_map.update({cmd_name:aliases})


def reminder():
	bot_print("Cool, what's the reminder you would like to set?")
	reminder = prompt_user('Enter a reminder: ');
	if reminder in variables.termination_list:
		bot_print("Okay, I'll cancel the request... Returning to the main menu...\n")
		return
	bot_print("Got it. What time do you want to be reminded?")
	time = prompt_user('Enter a time: ');
	if time in variables.termination_list:
		bot_print("Okay, I'll cancel the request... Returning to the main menu...\n")
		return
	bot_print("Okay, what day do you want to be reminded?")
	day = prompt_user('Enter a day: ')
	if day in variables.termination_list:
		bot_print("Okay, I'll cancel the request... Returning to the main menu...\n")
		return
	day = int(day)
	date = datetime.date(datetime.date.today().year, datetime.date.today().month, day)
	bot_print("REMINDER: " + reminder)

def text():
	bot_print("Cool, what message would you like to send?")
	message = prompt_user('Enter a message: ')
	if message in variables.termination_list:
		bot_print("Okay, I'll cancel the request... Returning to the main menu...\n")
	else:
		''' Add this feature if I buy a Twilio account. Won't work otherwise :/
		bot_print("What number would you like to send your message to? (Press enter for default)")
		number = input('> ')
		if number == "":
			number = phoneNumber
		sendText(message,number)'''
		sendText(message)

def list():
	bot_print("Okay, here are all my current commands...");
	for cmd in variables.command_map.values():
			bot_print("="*50)
			print(cmd)
			print("Aliases include: ", variables.alias_map.get(cmd.primary_keyword),"\n")