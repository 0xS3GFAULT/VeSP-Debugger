from colors.colors import *
from display.menu import *
from engine.engine import *
import sys

if __name__=="__main__":
	display_main_menu()
	while True:
		try:
			command = input("\t>>> ").lower().strip().split(" ")
			command = [x.strip() for x in command]
			command = [x for x in command if x!='']
			if(len(command) == 0):
				continue
			elif(command[0] not in COMMANDS):
				print(vesp.colors.RED+"\tCommand not found. Type 'help' for help."+vesp.colors.RESET)
			else:
				COMMANDS[command[0]](command)
		except KeyboardInterrupt:
			print()
			quit()