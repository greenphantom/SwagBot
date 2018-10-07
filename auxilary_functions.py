# Module contains helper functions not tied to a specific command
from twilio.rest import Client

accountSID = '' #fill your Twilio SID here
authenticationToken = '' # fill your Twilio AuthToken here

twilioClient = Client(accountSID, authenticationToken)
twilioNumber = '' # fill your Twilio number here
phoneNumber = '' # fill your default number here. Must be verfied by Twilio if using a free account

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

def add_method():
	key = prompt_user("Enter the keyword for the command you'd like to change: ")
	if isValid(key):
		cmd = findCommand(key)
		change_mathod(key)

def findCommand(phrase):
	for cmd in command_list:
		if phrase in cmd:
			return cmd
	return None

def isValid(phrase):
	if phrase in termination_list:
		bot_print("Okay, I'll cancel the request... Returning to the main menu...\n")
		return False
	else:
		return True

def bot_print(phrase):
	print("$wagBot: " + phrase)

def prompt_user(phrase="",format = True):
	print(phrase)
	temp = input("> ")
	if format:
		temp = temp.lower()
	return temp