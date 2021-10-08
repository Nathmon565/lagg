osImported = False
msvcrtImported = False
try:
	import os
	osImported = True
except ImportError:
	print("ERROR: Can't import os!")
try:
	import msvcrt
	msvcrtImported = True
except ImportError:
	print("ERROR: Can't import msvcrt!")
import time
import random

allCaps = False
allLower = False
prntDelayModifier = 1.00

def prnt(stringToPrint, newLine = True, delayModifier = 1.00):
	'''Prints lines with delays for each character to imitate typing speed'''
	#Adjust the speed
	delayModifier *= prntDelayModifier
	if(allCaps):
		stringToPrint = str(stringToPrint).upper()
	elif(allLower):
		stringToPrint = str(stringToPrint).lower()
	else:
		stringToPrint = str(stringToPrint)
	time.sleep(0.3 * delayModifier) #line wait
	for char in stringToPrint:
		print(char, end = "", flush = True)
		time.sleep(0.03 * delayModifier) #character wait
		#Special character exceptions
		if(char == "." or char == ":" or char == ";" or char == "|" or char =="<" or char == ">"):
			time.sleep(0.2 * delayModifier)
		elif(char == "," or char == "/" or char == "\\" or char == "(" or char == ")" or char == "{" or char == "}" or char == "[" or char == "]" or char == "-" or char == "+"):
			time.sleep(0.1 * delayModifier)
		elif(char == "!" or char == "="):
			time.sleep(0.25 * delayModifier)
		elif(char == "?"):
			time.sleep(0.3 * delayModifier)
	if(newLine == True):
		print("")

def prntInput(stringToPrompt, speedModifier = 1) -> str:
	'''Asks for input using prnt("stringToPrompt", False) returning input()'''
	prnt(stringToPrompt, False, speedModifier)
	return input()

def inputHidden(prompt) -> str:
	'''Same as input(), but it replaces all input with asterisks.\nReturns what was typed'''
	if(not msvcrtImported):
		print("ERROR: msvcrt not imported!")
		return
	
	print(prompt, end = "")
	string = ""
	charCount = 0 #keep track of how many chars we can backspace
	while 1:
		c = msvcrt.getch()
		if c == b'\n' or c == b'\r': #enter or misc char
			print()
			return string
		if c == b'\x03': #ctrl + c
			raise KeyboardInterrupt
		if c == b'\b': #backspace
			if(charCount > 0):
				charCount -= 1
				print("\b \b", end = "")
				string = string[:-1]
		else: #anything else
			charCount += 1
			print("*", end = "")
			string += str(c)[2:-1]
	print("\r\n")

def wait():
	'''Wait until the user presses any key'''
	while 1:
		c = msvcrt.getch()
		if(c == b'\x03'):
			raise KeyboardInterrupt
		else:
			break

def limitedChoice(choices, instant=False) -> int:
	'''Takes user input within the int limit of choices 1-choices inclusive. Returns int'''
	while(True):
		userInput = input("\n")
		try:
			userInput = int(userInput)
			if(userInput <= choices and userInput > 0):
				return userInput
			else:
				if(instant):
					print("Number out of range.")
				else:
					prnt("Number out of range.")
		except ValueError:
			if(instant):
				print("Enter a valid number.")
			else:
				prnt("Enter a valid number.")

def chooseMenu(optionToChoose: list, instant = False) -> int:
	'''Offers multiple choices and takes integer input. Will ask again if NaN or out of range.\n
	optionToChoose = ["Option 1", "Option 2"...]
	instant determines whether to use function print() or prnt()'''
	numberOfChoices = len(optionToChoose)-1
	count = 1
	optionToChoose.insert(0,"null")
	if(instant):
		print("")
	else:
		prnt("")
	while(numberOfChoices >= 0):
		numberOfChoices -= 1
		if(instant):
			print(str(count) + ") " + str(optionToChoose[count]))
		else:
			prnt(str(count) + ") " + str(optionToChoose[count]))
		count += 1
	
	return limitedChoice(len(optionToChoose))

def clear():
	'''Clears the terminal'''
	try:
		_ = os.system('cls')
	except:
		print("error: Functions.clear() only works on Windows systems")

def setDefaultSettings():
	'''Set the print settings to default'''
	global allCaps 
	allCaps = False
	global allLower
	allLower = False
	global prntDelayModifier
	prntDelayModifier = 1.00

def setCustomSettings(caps : bool, lower : bool, delay : int):
	'''Set the print settings to custom settings'''
	global allCaps 
	allCaps = caps
	global allLower
	allLower = lower
	global prntDelayModifier
	prntDelayModifier = delay

def coinFlip() -> bool:
	'''Returns true or false'''
	return random.randint(0, 1) == 0