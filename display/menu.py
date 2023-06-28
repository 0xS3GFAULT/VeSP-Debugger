from colors.colors import *
from engine.engine import *
import os

def display_main_menu():
	if(os.name == "posix"):
		os.system("clear")
	elif(os.name == "nt"):
		os.system("cls")
	print(vesp.colors.YELLOW+"""
\t   _____ _____  ____   __      __   _____ _____         __   ___  
\t  / ____|  __ \\|  _ \\  \\ \\    / /  / ____|  __ \\       /_ | |__ \\ 
\t | |  __| |  | | |_) |  \\ \\  / /__| (___ | |__) | __   _| |    ) |
\t | | |_ | |  | |  _ <    \\ \\/ / _ \\\\___ \\|  ___/  \\ \\ / / |   / / 
\t | |__| | |__| | |_) |    \\  /  __/____) | |       \\ V /| |_ / /_ 
\t  \\_____|_____/|____/      \\/ \\___|_____/|_|        \\_/ |_(_)____|    

                                                       Written by R.Hoarau\n"""+vesp.colors.RESET)