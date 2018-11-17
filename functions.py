# Module contains all the functions that are tied to commands
# Functions are linked via name (i.e. functions should be named the same as the primary keyword of the command)
# As of now, all functions must take in variables.command_map,variables.termination_list,and variables.alias_map

import datetime
import time
import random
import xml.etree.ElementTree as ET

from auxilary_functions import *
from external_scripts import *
# import external_scripts.string as str
# import external_scripts.web as web
import variables

google_client_ID = ''
client_secret = ''

'''accountSID = '' #fill your Twilio SID here
authenticationToken = '' # fill your Twilio AuthToken here

twilioClient = Client(accountSID, authenticationToken)
twilioNumber = '' # fill your Twilio number here
phoneNumber = '' # fill your default number here. Must be verfied by Twilio if using a free account'''


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


def text(*args):
    message = ''
    for i in range(len(args)):
        message += args[i] + " "
    if message == '':
        bot_print("Cool, what message would you like to send?")
        message = prompt_user('Enter a message: ', False)
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


def clear(size='45'):
    size = int(size)
    print('\n' * size)


def list(phrase=''):
    bot_print("Okay, here are all my current commands involving the phrase: " + phrase) if phrase != '' else bot_print("Okay, here are all my current commands...")
    for cmd in variables.command_map.values():
        if cmd == phrase or phrase in cmd.command_desc or phrase == '':
            bot_print("=" * 50)
            emphasize(phrase, str(cmd))
            print("Aliases include: ", variables.alias_map.get(cmd.primary_keyword), "\n")


def rm_substring(str='', substring=''):
    if str == '':
        bot_print("Sweet, what string would you like to remove from?")
        str = prompt_user("Please enter your string: ")
    if substring == '':
        bot_print("Got it. Now, what substring would you like to remove from it?")
        substring = prompt_user("Please enter the substring: ", False)
    result = string.remove_substring(str, substring)
    bot_print("Done! The result is: " + result)


def search(q=''):
    bot_print("Awesome! What would you like to search for?")
    if (q == ''):
        q = prompt_user('Please enter your search phrase: ', False)
    web.search_Google(q)  # web is the module in package where this is located
    bot_print("Great! I've opened the search result in a new tab for you.\n")


def quicksort(n='0'):
    bot_print("Great, this is a quicksort demo.")
    n = int(n)
    process_numerical_error(n, lowerlimit=0, inclusive=False)
    while n <= 0:
        n = int(prompt_user('Please choose a the length of the list for the demo: '))
        process_numerical_error(n, lowerlimit=0, inclusive=False)
    demo = random.sample(range(n), n)
    bot_print("This is the list before: " + str(demo))
    sort.quickSort(demo, 0, n - 1)  # sort is the module in package where this is located
    bot_print("Your sorted list is: " + str(demo), True)


def sum(num1='0', num2='0'):
    bot_print("Starting add routine...")
    if num1 == '':
        num1 = int(prompt_user("Please enter num 1: "))
    if num2 == '':
        num2 = int(prompt_user("Please enter num 2: "))
    num1 = int(num1)
    num2 = int(num2)
    bot_print(str(num1) + ' + ' + str(num2) + ' = ' + str(add.add(num1, num2)))
