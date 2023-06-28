from colors.colors import *
from display.menu import *
from engine.engine import *
import sys

"""commandes
help							: affiche toutes les commandes disponibles
		<commande> 				: affiche l'aide d'une commande
see/s	
		code/c <debut-fin>  	 : voir le code décodé avec les adresses à côté
		registers/reg/r 		 : voir l'ensemble des registres
		memory/mem/m <debut-fin> : voir l'ensemble de la mémoire 
		breakpoints/break/b 	 : voir les breakpoints placés dans le debugger

breapoint/break/b                
		adresse 	: placer un breakpoint à une certaine adresse
		instruction : placer un breakpoint à toutes les instructions déterminées

del/d <adresse>					 : supprime un breakpoint placé à une certaine adresse

run/r  							 : lancer le programme depuis le premier breakpoint 

starti  					     : placer un breakpoint au tout début et lancer le programme 

continue/c 						 : continue le programme depuis le dernier breakpoint

next/n 							 : exécute l'instruction suivante

"""

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