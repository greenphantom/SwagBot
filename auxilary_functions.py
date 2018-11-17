# Module contains helper functions not tied to a specific command
from twilio.rest import Client
import pyttsx3

accountSID = ''
authenticationToken = ''

twilioClient = Client(accountSID, authenticationToken)
twilioNumber = ''
phoneNumber = ''

# engine = pyttsx3.init()


def sendText(message, recipiant=phoneNumber):
    try:
        twilioClient.messages.create(
            body=message,
            from_=twilioNumber,
            to=recipiant)
        bot_print("Message sent successfully!")
    except Exception as e:
        bot_print("Oops, something went wrong...")


def add_method():
    key = prompt_user("Enter the keyword for the command you'd like to change: ")
    if isValid(key):
        cmd = findCommand(key)
        change_method(key)


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


def bot_print(phrase, new_line=False, speak=False):
    if new_line:
        print()
    print("$wagBot: " + phrase)
    # if speak:
    #    # respond(phrase)

#


def process_numerical_error(number, lowerlimit=-1 * float("inf"), upperlimit=float("inf"), range=False, inclusive=True):
    if inclusive:
        if number < lowerlimit or number > upperlimit or (range and number not in range(lowerlimit, upperlimit)):
            bot_print("Sorry, you must pick a valid number.")
            return False
        else:
            return True
    else:
        if number <= lowerlimit or number >= (range and number not in range(lowerlimit, upperlimit)):
            bot_print("Sorry, you must pick a valid number.")
            return False
        else:
            return True


def emphasize(target, string):
    if target == '':
        pass
    print(string.replace(target, target.upper()))


def prompt_user(phrase="", format=True):
    print(phrase)
    temp = input("> ")
    if format:
        temp = temp.lower()
    return temp


# def respond(phrase):
#     engine.say(phrase)
#     engine.runAndWait()
