import sys
import os
from colors.colors import *

def clear():
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")

def color(l):
	if(len(l) == 1):
		print(vesp.colors.RED+"\tColor command needs arguments. Type 'help color' for help."+vesp.colors.RESET)
		return
	if(l[1] == "yes" or l[1] == 'y'):
		vesp.color = True
		vesp.colors.BLACK = "\u001b[30m"
		vesp.colors.RED = "\u001b[31m"
		vesp.colors.GREEN = "\u001b[32m"
		vesp.colors.YELLOW = "\u001b[33m"
		vesp.colors.BLUE = "\u001b[34m"
		vesp.colors.MAGENTA = "\u001b[35m"
		vesp.colors.CYAN = "\u001b[36m"
		vesp.colors.WHITE = "\u001b[37m"
		vesp.colors.RESET = "\u001b[0m"
	elif(l[1] == "no" or l[1] == 'n'):
		vesp.color = False
		vesp.colors.BLACK = "\u001b[0m"
		vesp.colors.RED = "\u001b[0m"
		vesp.colors.GREEN = "\u001b[0m"
		vesp.colors.YELLOW = "\u001b[0m"
		vesp.colors.BLUE = "\u001b[0m"
		vesp.colors.MAGENTA = "\u001b[0m"
		vesp.colors.CYAN = "\u001b[0m"
		vesp.colors.WHITE = "\u001b[0m"
		vesp.colors.RESET = "\u001b[0m"
	else:
		print(vesp.colors.RED+"\tInvalid color command. Type 'help color' for help."+vesp.colors.RESET)

def help_command(command):
	help_command_dict = {"clear": lambda :print(vesp.colors.YELLOW+"\tclear : clears screen (works for NT and POSIX operating system only)"+vesp.colors.RESET),
	"see": lambda :print(vesp.colors.YELLOW+"\tsee / s : dumps memory, code, register and see breakpoints\n\n\t          Dump code : \n\t                     see code / c <min_address>-<max_address>\n\t                     Example : see code 4-a "+vesp.colors.RESET+"# see code from the address 0004 to 000a.\n\t                               "+vesp.colors.YELLOW+"s c all "+vesp.colors.RESET+"# see all the code"+vesp.colors.YELLOW+"\n\n\t          See Breakpoints : \n\t                           see breakpoint / break / b\n\n\t          See Registers : \n\t                         see registers / reg / r\n\n\t          Dump memory : \n\t                         see memory / mem / m <min_address>-<max_address>\n\t                         Example : see memory 34-fa "+vesp.colors.RESET+"# dump memory from the address 0034 to 00fa"),
	"s": lambda :print(vesp.colors.YELLOW+"\tsee / s : dumps memory, code, register and see breakpoints\n\n\t          Dump code : \n\t                     see code / c <min_address>-<max_address>\n\t                     Example : see code 4-a "+vesp.colors.RESET+"# see code from the address 0004 to 000a.\n\t                               "+vesp.colors.YELLOW+"s c all "+vesp.colors.RESET+"# see all the code"+vesp.colors.YELLOW+"\n\n\t          See Breakpoints : \n\t                           see breakpoint / break / b\n\n\t          See Registers : \n\t                         see registers / reg / r\n\n\t          Dump memory : \n\t                         see memory / mem / m <min_address>-<max_address>\n\t                         Example : see memory 34-fa "+vesp.colors.RESET+"# dump memory from the address 0034 to 00fa"),
	"color": lambda :print(vesp.colors.YELLOW+"\tcolor : toggles color mode.\n\t        Example : color <yes / y> / <no / n>"+vesp.colors.RESET),
	"breakpoint": lambda:print(vesp.colors.YELLOW+"\tbreakpoint / break / b : sets breakpoint.\n\t                         breakpoint / break / b <address>\n\t                         Example : breakpoint 23fe "+vesp.colors.RESET+"# sets breakpoint at address 23fe"),
	"break": lambda:print(vesp.colors.YELLOW+"\tbreakpoint / break / b : sets breakpoint.\n\t                         breakpoint / break / b <address>\n\t                         Example : breakpoint 23fe "+vesp.colors.RESET+"# sets breakpoint at address 23fe"),
	"b": lambda:print(vesp.colors.YELLOW+"\tbreakpoint / break / b : sets breakpoint.\n\t                         breakpoint / break / b <address>\n\t                         Example : breakpoint 23fe "+vesp.colors.RESET+"# sets breakpoint at address 23fe"),
	"del" : lambda:print(vesp.colors.YELLOW+"\tdel : deletes breakpoint.\n\t      del <address>\n\t      Example : del 4af "+vesp.colors.RESET+"# deletes breakpoint set at address 000004af"),
	"quit" : lambda:print(vesp.colors.YELLOW+"\tquit / q : quits the program"+vesp.colors.RESET),
	"q" : lambda:print(vesp.colors.YELLOW+"\tquit / q : quits the program"+vesp.colors.RESET),
	"run" : lambda:print(vesp.colors.YELLOW+"\trun / r : runs the program until a breakpoint is reached or until HLT instruction."+vesp.colors.RESET),
	"r" : lambda:print(vesp.colors.YELLOW+"\trun / r : runs the program until a breakpoint is reached or until HLT instruction."+vesp.colors.RESET),
	"continue" : lambda:print(vesp.colors.YELLOW+"\tcontinue / c : continues the program until a breakpoint is reached or until HLT instruction."+vesp.colors.RESET),
	"c" : lambda:print(vesp.colors.YELLOW+"\tcontinue / c : continues the program until a breakpoint is reached or until HLT instruction."+vesp.colors.RESET),
	"nexti" : lambda:print(vesp.colors.YELLOW+"\tnexti / ni : executes the next instruction following PC register."+vesp.colors.RESET),
	"ni" : lambda:print(vesp.colors.YELLOW+"\tnexti / ni / n: executes the next instruction following PC register."+vesp.colors.RESET),
	"n" : lambda:print(vesp.colors.YELLOW+"\tnexti / ni / n: executes the next instruction following PC register."+vesp.colors.RESET)
	}
	if(len(command) == 1):
		print(vesp.colors.YELLOW+"\tcolor : toggles color mode\n\tclear : clears screen\n\tquit / q : quits the program\n\thelp / h : shows this message\n\tsee / s : dumps memory, sees code, register and breakpoints\n\tbreakpoint / break / b : sets breakpoint\n\tdel : deletes breakpoints\n\trun / r : runs the program\n\tcontinue / c : continues the program\n\tnexti / ni / n : executes the next instruction following PC register."+vesp.colors.RESET)
		return
	if(command[1] in help_command_dict):
		help_command_dict[command[1]]()
	else:
		print(vesp.colors.RED+"\tNo help page for '"+command[1]+"' command. Type 'help' for help."+vesp.colors.RESET)

def decoded_command(command,line):
	overflow = False
	try:
		vesp.code[line+1]
	except IndexError:
		overflow = True
	if(command[0] == '0'):
		return vesp.colors.YELLOW+"ADD A,B "+vesp.colors.RESET+"; A = A+B"
	elif(command[0] == '1'):
		return vesp.colors.YELLOW+"NEG A "+vesp.colors.RESET+"; A = ~A"
	elif(command[0] == '2'):
		if(command[1:] == "000"):
			if(overflow):
				return vesp.colors.YELLOW+"LDA A,A "+vesp.colors.RESET+"; A = A"
			if(vesp.code[line+1] == "0000"):
				return vesp.colors.YELLOW+"LDA A,A "+vesp.colors.RESET+"; A = A"
			elif(vesp.code[line+1] == "0001"):
				return vesp.colors.YELLOW+"LDA A,B "+vesp.colors.RESET+"; A = B"
			else:
				return vesp.colors.YELLOW+"LDA A,M["+str(line+3)+"] "+vesp.colors.RESET+"; A = "+vesp.code[line+1]
		elif(command[1:] == "001"):
			if(overflow):
				return vesp.colors.YELLOW+"LDA B,A "+vesp.colors.RESET+" ; B = A"
			if(vesp.code[line+1] == "0000"):
				return vesp.colors.YELLOW+"LDA B,A"+vesp.colors.RESET+" ; B = A"
			elif(vesp.code[line+1] == "0001"):
				return vesp.colors.YELLOW+"LDA B,B"+vesp.colors.RESET+" ; B = B"
			else:
				return vesp.colors.YELLOW+"LDA B,M["+str(line+3)+"]"+vesp.colors.RESET+" ; B = "+vesp.code[line+1]
		else:
			if(overflow):
				return vesp.colors.YELLOW+"LDA M["+command[1:]+"],A"+vesp.colors.RESET+" ; M["+command[1:]+"] = A"
			return vesp.colors.YELLOW+"LDA M["+command[1:]+"],M["+vesp.code[line+1]+"]"+vesp.colors.RESET+" ; M["+command[1:]+"] = M["+vesp.code[line+1]+"]"
	elif(command[0] == '3'):
		if(command[1:] == "000"):
			if(overflow):
				return vesp.colors.YELLOW+"MOV A,A"+vesp.colors.RESET+" ; A = A"
			if(vesp.code[line+1][1:] == "000"):
				return vesp.colors.YELLOW+"MOV A,A"+vesp.colors.RESET+" ; A = A"
			elif(vesp.code[line+1][1:] == "001"):
				return vesp.colors.YELLOW+"MOV A,B"+vesp.colors.RESET+" ; A = B"
			else:
				return vesp.colors.YELLOW+"MOV A,M[M["+str(line+3)+"]]"+vesp.colors.RESET+" ; A = M["+vesp.code[line+1][1:]+"]"
		elif(command[1:] == "001"):
			if(overflow):
				return vesp.colors.YELLOW+"MOV B,A"+vesp.colors.RESET+" ; B = A"
			if(vesp.code[line+1][1:] == "000"):
				return vesp.colors.YELLOW+"MOV B,A"+vesp.colors.RESET+" ; B = A"
			elif(vesp.code[line+1][1:] == "001"):
				return vesp.colors.YELLOW+"MOV B,B"+vesp.colors.RESET+" ; B = B"
			else:
				return vesp.colors.YELLOW+"MOV B,M[M["+str(line+3)+"]]"+vesp.colors.RESET+" ; B = M["+vesp.code[line+1][1:]+"]"
		else:
			if(overflow):
				return vesp.colors.YELLOW+"MOV M["+command[1:]+"],A"+vesp.colors.RESET+" ; M["+command[1:]+"] = A"
			return vesp.colors.YELLOW+"MOV M["+command[1:]+"],M[M["+str(line+3)+"]]"+vesp.colors.RESET+" ; M["+command[1:]+"] = M["+vesp.code[line+1][1:]+"]"
	elif(command[0] == '4'):
		return vesp.colors.YELLOW+"JMP "+command[1:]+vesp.colors.RESET+" ; PC = "+command[1:]
	elif(command[0] == '5'):
		return vesp.colors.YELLOW+"JEZ "+command[1:]+vesp.colors.RESET+" ; If (A = 0) PC = "+command[1:]
	elif(command[0] == '6'):
		return vesp.colors.YELLOW+"JPS "+command[1:]+vesp.colors.RESET+" ; If (A > 0) PC = "+command[1:]
	elif(command[0] == '7'):
		return vesp.colors.YELLOW+"HLT"+vesp.colors.RESET
	else:
		return "????????"

def see(l):
	if(len(l) < 2):
		print(vesp.colors.RED+"\tInvalid see command. Type 'help see' for help."+vesp.colors.RESET)
		return
	if(l[1] == "code" or l[1] == 'c'):
		if(len(l) < 3):
			print(vesp.colors.RED+"\tInvalid see command. Type 'help see' for help."+vesp.colors.RESET)
			return
		if(l[2].lower() == "all"):
			MIN=2
			MAX=len(vesp.code)+1
		else:
			try:
				splitted = l[2].split("-")
				MIN = min(int(splitted[0],16),int(splitted[1],16))
				MAX = max(int(splitted[0],16),int(splitted[1],16))
				assert MIN>=2 and MAX<(len(vesp.code)+2)
			except AssertionError:
				print(vesp.colors.RED+"\tSee command has invalid address range. Type 'help see' for help."+vesp.colors.RESET)
				return
			except:
				print(vesp.colors.RED+"\tInvalid see command. Type 'help see' for help."+vesp.colors.RESET)
				return
		print("\t###############################################[ CODE ]################################################")
		print("\t PC | "+vesp.colors.RED+"Breakpoint"+vesp.colors.RESET+" | Address | "+vesp.colors.BLUE+"code"+vesp.colors.RESET+" | "+vesp.colors.YELLOW+"decoded instruction"+vesp.colors.RESET)
		print("\t----+------------+---------+------+--------------------------------------------------------------------")
		MAR_needed = False
		count = MIN-2
		overflow = False
		while count <= MAX-2:
			decoded = None
			if(MAR_needed == False):
				decoded = decoded_command(vesp.code[count],count)
				MAR_needed = False
			if(count+2 == vesp.PC and vesp.start == True):
				if(count+2 in vesp.breakpoints):
					print(vesp.colors.GREEN+"\t===>|  set here"+"  |   "+hex(count+2)[2:].rjust(4,'0')+"  | "+str(vesp.code[count]).rjust(4,'0')+" | ",end="")
				else:
					print(vesp.colors.GREEN+"\t===>|            |   "+hex(count+2)[2:].rjust(4,'0')+"  | "+str(vesp.code[count]).rjust(4,'0')+" | ",end="")
				decoded = decoded.replace(vesp.colors.YELLOW,vesp.colors.GREEN)
				decoded = decoded.replace(vesp.colors.RESET,"")
			else:
				if(count+2 in vesp.breakpoints):
					print("\t    |  "+vesp.colors.RED+"set here"+vesp.colors.RESET+"  |   "+hex(count+2)[2:].rjust(4,'0')+"  | "+vesp.colors.BLUE+str(vesp.code[count]).rjust(4,'0')+vesp.colors.RESET+" | ",end="")
				else:
					print("\t    |            |   "+hex(count+2)[2:].rjust(4,'0')+"  | "+vesp.colors.BLUE+str(vesp.code[count]).rjust(4,'0')+vesp.colors.RESET+" | ",end="")
			if(vesp.code[count][0] == '2' or vesp.code[count][0] == '3'):
				print(decoded)
				MAR_needed = True
				count += 1
				print(vesp.colors.RESET,end="")
				continue
			if(decoded == None):
				print()
				count += 1
				MAR_needed = False
				print(vesp.colors.RESET,end="")
				continue
			else:
				print(decoded)
				count += 1
				MAR_needed = False
				print(vesp.colors.RESET,end="")
		print("\t#######################################################################################################")
		return
	elif(l[1] == "breakpoint" or l[1] == "break" or l[1] == 'b'):
		print("\t#############################################[ BREAKPOINTS ]#############################################")
		if(len(vesp.breakpoints) == 0):
			print(vesp.colors.BLUE+"\tNo breakpoints set."+vesp.colors.RESET)
		else:
			for i in vesp.breakpoints:
				print(vesp.colors.BLUE+"\t   "+hex(i)[2:].rjust(4,'0'),end="")
				print(vesp.colors.RESET+" --> "+vesp.colors.YELLOW,end="")
				print(decoded_command(vesp.code[i-2],i-2))
			print(vesp.colors.RESET,end="")
		print("\t#########################################################################################################")
	elif(l[1] == "registers" or l[1] == "reg" or l[1] == 'r'):
		if(vesp.start == False):
			print(vesp.colors.YELLOW+"\tThe program is not started."+vesp.colors.RESET)
			return
		else:
			print("\t#############################################[ REGISTERS ]#############################################")
			print(vesp.colors.BLUE+"\t       A : "+hex(vesp.memory[0])[2:].rjust(4,'0')+"\t\t           B : "+hex(vesp.memory[1])[2:].rjust(4,'0'))
			if(vesp.instructions[vesp.MAR]):
				print(vesp.colors.BLUE+"\t      IR : "+hex(vesp.IR)[2:].rjust(4,'0')+"\t\t          PC : "+hex(vesp.PC)[2:].rjust(4,'0')+" --> "+decoded_command(vesp.code[vesp.PC-2],vesp.PC-2))
				print(vesp.colors.BLUE+"\t   CLOCK : "+hex(vesp.CLOCK)[2:].rjust(4,'0')+"\t\t         MAR : "+hex(vesp.MAR)[2:].rjust(4,'0')+" --> "+decoded_command(vesp.code[vesp.MAR-2],vesp.MAR-2))
			else:
				print(vesp.colors.BLUE+"\t      IR : "+hex(vesp.IR)[2:].rjust(4,'0')+"\t\t          PC : "+hex(vesp.PC)[2:].rjust(4,'0'))
				print(vesp.colors.BLUE+"\t   CLOCK : "+hex(vesp.CLOCK)[2:].rjust(4,'0')+"\t\t         MAR : "+hex(vesp.MAR)[2:].rjust(4,'0'))
			carry = vesp.colors.YELLOW+"CARRY" if vesp.c else vesp.colors.BLUE+"carry"
			overflow = vesp.colors.YELLOW+"OVERFLOW" if vesp.f else vesp.colors.BLUE+"overflow"
			sign = vesp.colors.YELLOW+"SIGN" if vesp.s else vesp.colors.BLUE+"sign"
			zero = vesp.colors.YELLOW+"ZERO" if vesp.z else vesp.colors.BLUE+"zero"
			complement = vesp.colors.YELLOW+"COMPLEMENT" if vesp.complement else vesp.colors.BLUE+"complement"
			add = vesp.colors.YELLOW+"ADD" if vesp.add else vesp.colors.BLUE+"add"
			reset = vesp.colors.YELLOW+"RESET" if vesp.reset else vesp.colors.BLUE+"reset"
			print(vesp.colors.BLUE+"\n\t   FLAGS : ["+carry+" "+overflow+" "+sign+" "+zero+" "+complement+" "+add+" "+reset+vesp.colors.BLUE+"]")
			print(vesp.colors.RESET,end="")
			print("\t#######################################################################################################")
	elif(l[1] == "memory" or l[1] == "mem" or l[1] == 'm'):
		if(len(l) < 3):
			print(vesp.colors.RED+"\tInvalid see command. Type 'help see' for help."+vesp.colors.RESET)
			return
		else:
			try:
				splitted = l[2].split("-")
				MIN = min(int(splitted[0],16),int(splitted[1],16))
				MAX = max(int(splitted[0],16),int(splitted[1],16))
				assert MIN>=0 and MAX<8192
			except AssertionError:
				print(vesp.colors.RED+"\tSee command has invalid address range. Type 'help see' for help."+vesp.colors.RESET)
				return
			except:
				print(vesp.colors.RED+"\tInvalid see command. Type 'help see' for help."+vesp.colors.RESET)
				return
			if(vesp.start == False):
				print(vesp.colors.YELLOW+"\tThe program is not started."+vesp.colors.RESET)
				return
			print("\t#############################################[ MEMORY ]#############################################")
			for i in range(MIN,MAX+1):
				print(vesp.colors.RESET+"\tM["+hex(i)[2:].rjust(4,'0')+"] = "+hex(vesp.memory[i])[2:].rjust(4,'0'),end="")
				try:
					if(vesp.instructions[i]):
						print(" --> "+decoded_command(vesp.code[i-2],i-2))
					else:
						print()
				except KeyError:
					print()
			print("\t####################################################################################################")
	else:
		print(vesp.colors.RED+"\tInvalid see command. Type 'help see' for help."+vesp.colors.RESET)

def breakpoint_command(l):
	if(len(l) < 2):
		print(vesp.colors.RED+"\tInvalid breakpoint command. Type 'help breakpoint' for help."+vesp.colors.RESET)
		return
	try:
		value = int(l[1],16)
	except ValueError:
		print(vesp.colors.RED+"\tInvalid breakpoint address. Type 'help breakpoint' for help."+vesp.colors.RESET)
		return
	if(value < 2 or value > len(vesp.code)+1):
		print(vesp.colors.RED+"\tInvalid breakpoint address. Type 'help breakpoint' for help."+vesp.colors.RESET)
		return
	if(value in vesp.breakpoints):
		print(vesp.colors.YELLOW+"\tBreakpoint is already set at this address."+vesp.colors.RESET)
		return
	if(vesp.instructions[value] == False):
		print(vesp.colors.YELLOW+"\tBreakpoint will never be reached by PC because the address "+hex(value)[2:].rjust(4,'0')+" is not an executable instruction."+vesp.colors.RESET)
		print(vesp.colors.YELLOW+"\tBreakpoint not set."+vesp.colors.RESET)
		return
	vesp.breakpoints.append(value)
	vesp.breakpoints =  sorted(vesp.breakpoints)
	print(vesp.colors.BLUE+"\tBreakpoint set at address "+hex(value)[2:].rjust(4,'0')+vesp.colors.RESET)

def del_breakpoint(l):
	if(len(l) < 2):
		print(vesp.colors.RED+"\tInvalid del command. Type 'help del' for help."+vesp.colors.RESET)
		return
	try:
		value = int(l[1],16)
	except ValueError:
		print(vesp.colors.RED+"\tInvalid breakpoint address. Type 'help del' for help."+vesp.colors.RESET)
		return
	if(value not in vesp.breakpoints):
		print(vesp.colors.RED+"\tNo breakpoints set at this address."+vesp.colors.RESET)
		return
	vesp.breakpoints.remove(value)
	print(vesp.colors.BLUE+"\tBreakpoint at address "+hex(value)[2:].rjust(4,'0')+" successfully deleted."+vesp.colors.RESET)

def fetch():
	if(vesp.code[vesp.PC-2][0] == '2' or vesp.code[vesp.PC-2][0] == '3'):
		vesp.PC += 1
	vesp.PC += 1
	vesp.MAR = vesp.PC
	vesp.CLOCK += 1
	vesp.IR = vesp.memory[vesp.MAR]
	vesp.CLOCK += 1

def decode_and_execute(instruction,line):
	vesp.add = 0
	vesp.complement = 0
	vesp.reset = 0
	if(instruction[0] == '0'):
		temp = vesp.memory[0] + vesp.memory[1]
		vesp.c = 1 if((vesp.memory[0] + vesp.memory[1]) % 0x10000 != temp) else 0;
		temp = (~temp+1) % 0x10000 if(bin(temp).rjust(16,'0')[2:][0] == '1') else temp
		temp1 = (~vesp.memory[0]+1) % 0x10000 if(bin(vesp.memory[0])[2:].rjust(16,'0')[0] == '1') else vesp.memory[0]
		temp2 = (~vesp.memory[1]+1) % 0x10000 if(bin(vesp.memory[1])[2:].rjust(16,'0')[0] == '1') else vesp.memory[1]
		vesp.f = 1 if((temp1+temp2) % 0x10000 != temp) else 0
		vesp.memory[0] = (vesp.memory[0] + vesp.memory[1]) % 0x10000
		vesp.z = 1 if(vesp.memory[0] == 0) else 0
		vesp.s = 1 if(bin(vesp.memory[0]).rjust(16,'0')[-1] == '1') else 0
		vesp.CLOCK += 1
		vesp.add = 1
	elif(instruction[0] == '1'):
		vesp.memory[0] = (~vesp.memory[0]+1) % 0xffff
		vesp.CLOCK += 1
		vesp.complement = 1
	elif(instruction[0] == '2'):
		vesp.memory[vesp.IR & 0x0fff] = vesp.memory[vesp.MAR+1]
		vesp.CLOCK += 1
	elif(instruction[0] == '3'):
		vesp.memory[vesp.IR & 0x0fff] = vesp.memory[vesp.memory[vesp.MAR+1]]
		vesp.CLOCK += 2
	elif(instruction[0] == '4'):
		vesp.PC = vesp.IR & 0x0fff
		vesp.CLOCK += 1
	elif(instruction[0] == '5'):
		if(vesp.memory[0] == 0):
			vesp.PC = vesp.IR & 0x0fff
		vesp.CLOCK += 1
	elif(instruction[0] == '6'):
		if(vesp.memory[0] > 0):
			vesp.PC = vesp.IR & 0x0fff
		vesp.CLOCK += 1
	elif(instruction[0] == '7'):
		vesp.reset = 1
		vesp.CLOCK += 1

def initialize_from_beginning():
	vesp.memory[0] = 0
	vesp.memory[1] = 0
	vesp.complement = 0
	vesp.add = 0
	vesp.reset = 0
	vesp.start = 0
	vesp.c = 0
	vesp.f = 0
	vesp.s = 0
	vesp.z = 0
	vesp.PC = 1
	vesp.IR = 0
	vesp.MAR = 0
	vesp.CLOCK = 0

def run():
	if(vesp.start == True):
		print(vesp.colors.YELLOW+"\tThe program already started but will start again."+vesp.colors.RESET)
	initialize_from_beginning()
	vesp.start = True
	print(vesp.colors.BLUE+"\tThe program started."+vesp.colors.RESET)
	while True:
		fetch()
		decode_and_execute(vesp.code[vesp.PC-2],vesp.PC-2)
		if(vesp.reset):
			vesp.start = False
			print(vesp.colors.BLUE+"\tThe program stopped because of HLT instruction at address "+hex(vesp.PC)[2:].rjust(4,'0')+vesp.colors.RESET)
			return
		if(vesp.PC in vesp.breakpoints):
			see(["see","registers"])
			mini = vesp.PC-2
			maxi = vesp.PC+2
			if(mini < 2):
				mini = 2
			if(maxi > len(vesp.code)):
				maxi = len(vesp.code)+1
			see(["see","code",hex(mini)[2:]+"-"+hex(maxi)[2:]])
			print(vesp.colors.BLUE+"\tBreakpoint reached at address "+hex(vesp.PC)[2:].rjust(4,'0')+vesp.colors.RESET)
			return

def nexti():
	if(vesp.start == False):
		print(vesp.colors.RED+"\tThe program is not started."+vesp.colors.RESET)
		return
	fetch()
	decode_and_execute(vesp.code[vesp.PC-2],vesp.PC-2)
	if(vesp.reset):
		vesp.start = False
		print(vesp.colors.BLUE+"\tThe program stopped because of HLT instruction at address "+hex(vesp.PC)[2:].rjust(4,'0')+vesp.colors.RESET)
		return
	if(vesp.PC in vesp.breakpoints):
		see(["see","registers"])
		mini = vesp.PC-2
		maxi = vesp.PC+2
		if(mini < 2):
			mini = 2
		if(maxi > len(vesp.code)):
			maxi = len(vesp.code)+1
		see(["see","code",hex(mini)[2:]+"-"+hex(maxi)[2:]])
		print(vesp.colors.BLUE+"\tBreakpoint reached at address "+hex(vesp.PC)[2:].rjust(4,'0')+vesp.colors.RESET)
		return
	see(["see","registers"])
	mini = vesp.PC-2
	maxi = vesp.PC+2
	if(mini < 2):
		mini = 2
	if(maxi > len(vesp.code)):
		maxi = len(vesp.code)+1
	see(["see","code",hex(mini)[2:]+"-"+hex(maxi)[2:]])

def continue_function():
	if(vesp.start == False):
		print(vesp.colors.RED+"\tThe program is not started."+vesp.colors.RESET)
		return
	while True:
		fetch()
		decode_and_execute(vesp.code[vesp.PC-2],vesp.PC-2)
		if(vesp.reset):
			vesp.start = False
			print(vesp.colors.BLUE+"\tThe program stopped because of HLT instruction at address "+hex(vesp.PC)[2:].rjust(4,'0')+vesp.colors.RESET)
			return
		if(vesp.PC in vesp.breakpoints):
			see(["see","registers"])
			mini = vesp.PC-2
			maxi = vesp.PC+2
			if(mini < 2):
				mini = 2
			if(maxi > len(vesp.code)):
				maxi = len(vesp.code)+1
			see(["see","code",hex(mini)[2:]+"-"+hex(maxi)[2:]])
			print(vesp.colors.BLUE+"\tBreakpoint reached at address "+hex(vesp.PC)[2:].rjust(4,'0')+vesp.colors.RESET)
			return

COMMANDS = {"clear":lambda _:clear(),"quit":lambda _:exit(),"q":lambda _:exit(),"color": color,"help":help_command,"h":help_command,"see":see,"s":see,"breakpoint":breakpoint_command,"break":breakpoint_command,"b":breakpoint_command,"del":del_breakpoint,"run":lambda _:run(),"r":lambda _:run(),"nexti":lambda _:nexti(),"ni":lambda _:nexti(),"n":lambda _:nexti(),"continue":lambda _:continue_function(),"c":lambda _:continue_function()}

class Vesp_class:
	def __init__(self):
		self.memory = [0]*8192
		self.complement = 0
		self.add = 0
		self.reset = 0
		self.c = 0
		self.f = 0
		self.s = 0
		self.z = 0
		self.PC = 1
		self.IR = 0
		self.MAR = 1
		self.CLOCK = 0
		self.breakpoints = []
		self.start = False
		self.instructions = {}
		self.colors = color_class()
		self.file_errors()
		with open(sys.argv[1],"r") as file:
			self.code = [x.replace('\n','') for x in file.readlines()]
		self.color = True
		self.content_errors()
		self.code_analyzer()
		for i in range(len(self.code)):
			self.memory[i+2] = int(self.code[i],16)
		self.instruction_verification()

	def file_errors(self):
		if(len(sys.argv) < 2):
			print(self.colors.RED+"\n\tUsage : python3 gdb-vesp.py <file.vesp>\n"+self.colors.RESET)
			exit()
		try:
			open(sys.argv[1],"r")
		except FileNotFoundError:
			print(self.colors.RED+"\n\tThe file '"+sys.argv[1]+"' does not exist\n"+self.colors.RESET)
			exit()
		except PermissionError:
			print(self.colors.RED+"\n\tYou have not the permissions to read '"+sys.argv[1]+"'\n"+self.colors.RESET)
			exit()

	def content_errors(self):
		if(len(self.code) == 0):
			print(self.colors.RED+"\n\tThe file '"+sys.argv[1]+"' is empty\n"+self.colors.RESET)
			exit()
		try:
			for i in range(len(self.code)):
				assert len(self.code[i])==4
				int(self.code[i],16)
		except AssertionError:
			print(self.colors.RED+"\n\tThe file '"+sys.argv[1]+"' has invalid VeSP code at line "+str(i+1)+" : "+self.code[i]+"\n"+self.colors.RESET)
			exit()
		except ValueError:
			print(self.colors.RED+"\n\tThe file '"+sys.argv[1]+"' has invalid VeSP code at line "+str(i+1)+" : "+self.code[i]+"\n"+self.colors.RESET)
			exit()

	def code_analyzer(self):
		MAR_needed = False
		count = 0
		while count < len(self.code):
			if(self.code[count][0] == '2' or self.code[count][0] == '3'):
				count += 2
				continue
			if(self.code[count][0] not in "01234567"):
				print(self.colors.RED+"\n\tThe file '"+sys.argv[1]+"' has invalid VeSP code at line "+str(count+1)+" : "+self.code[count]+".\n\tNo instruction with opcode "+self.code[count][0]+".\n"+self.colors.RESET)
				exit()
			count += 1

	def instruction_verification(self):
		MAR_needed = False
		count = 0
		overflow = False
		while count < len(self.code):
			decoded = None
			if(MAR_needed == False):
				decoded = None if self.code[count][0] not in "01234567" else True
				MAR_needed = False
			if(self.code[count][0] == '2' or self.code[count][0] == '3'):
				self.instructions[count+2] = True
				MAR_needed = True
				count += 1
				continue
			if(decoded == None):
				self.instructions[count+2] = False
				count += 1
				MAR_needed = False
				continue
			else:
				self.instructions[count+2] = True
				count += 1
				MAR_needed = False

vesp = Vesp_class()
