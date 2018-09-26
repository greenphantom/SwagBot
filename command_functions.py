# Command function module
import xml.etree.ElementTree as ET
from twilio.rest import Client
import datetime
import time

accountSID = '' #fill your Twilio SID here
authenticationToken = '' # fill your Twilio AuthToken here

twilioClient = Client(accountSID, authenticationToken)
twilioNumber = '' # fill your Twilio number here
phoneNumber = '' # fill your default number here. Must be verfied by Twilio if using a free account

class Command:
	def __init__(self,primary_call,desc = "",alias=None,func = None):
		self.primary_keyword = primary_call
		if alias == None:
			self.keywords = []
		else:
			self.keywords = alias
		self.command_desc = desc
		self.operation = func

	def __contains__(self,keyword):
		if keyword.lower() in self.keywords or keyword.lower() == self.primary_keyword:
			return True
		else:
			return False

	def __eq__(self,cmd):
		if cmd in self.keywords or cmd == self.primary_keyword:
			return True
		else:
			return False

	def __str__(self):
		statment =  "\nPrimary keyword : "+self.primary_keyword
		statment += "\nAlias Commands : "
		for alias in self.keywords:
			statment += alias + " | "
		statment += "\nDescription : "+self.command_desc+"\n"
		return statment

	def addOperation(self,func):
		self.operation = func

	def run(self,*args):
		if self.operation != None:
			self.operation(*args)
		else:
			raise ValueError('ERROR 501: No operation defined for this function!')

def bot_print(phrase):
	print("$wagBot: " + phrase)

def prompt_user(phrase="",format = True):
	print(phrase)
	temp = input("> ")
	if format:
		temp = temp.lower()
	return temp


def add_command(cmd_name,aliases,desc):
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

def reminder(termination_list):
	bot_print("Cool, what's the reminder you would like to set?")
	reminder = prompt_user('Enter a reminder: ');
	if reminder in termination_list:
		bot_print("Okay, I'll cancel the request... Returning to the main menu...\n")
		return
	bot_print("Got it. What time do you want to be reminded?")
	time = prompt_user('Enter a time: ');
	if time in termination_list:
		bot_print("Okay, I'll cancel the request... Returning to the main menu...\n")
		return
	bot_print("Okay, what day do you want to be reminded?")
	day = prompt_user('Enter a day: ')
	if day in termination_list:
		bot_print("Okay, I'll cancel the request... Returning to the main menu...\n")
		return
	day = int(day)
	date = datetime.date(datetime.date.today().year, datetime.date.today().month, day)
	bot_print("REMINDER: " + reminder)

def text(termination_list):
	bot_print("Cool, what message would you like to send?")
	message = prompt_user('Enter a message: ')
	if message in termination_list:
		bot_print("Okay, I'll cancel the request... Returning to the main menu...\n")
	else:
		''' Add this feature if I buy a Twilio account. Won't work otherwise :/
		bot_print("What number would you like to send your message to? (Press enter for default)")
		number = input('> ')
		if number == "":
			number = phoneNumber
		sendText(message,number)'''
		sendText(message)

def sendText(message,recipiant=phoneNumber):
	try:
		twilioClient.messages.create(
				body = message,
				from_ = twilioNumber,
				to = recipiant)
		bot_print("Message sent successfully!")
	except Exception as e:
		bot_print("Oops, something went wrong...")
	finally:
		bot_print("Returning to main menu...\n")

def add():
	bot_print("Sure, thing...")
	cmd_name = prompt_user("What the name of the new command?: ")
	alias = prompt_user("Enter available aliases to edit (put space between phrases): ").split()
	desc = prompt_user("Enter a description for you new command: ")
	add_command(cmd_name,alias,desc)

def list(command_list):
	print('in list')
	bot_print("Okay, here are all my current commands...");
	for cmd in command_list:
			bot_print("="*50)
			print(cmd)