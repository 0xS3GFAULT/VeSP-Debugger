# VeSP Language

VeSP (VEry Simple Processor) is a simple instruction set & simulator made by [A. Yavuz Oruc](https://user.eng.umd.edu/~yavuz/)

The VeSP simulator takes in machine code and runs it. There is no 'print' functionality, all data
is either in registers or memory. See [VeSP Documentation](https://user.eng.umd.edu/~yavuz/teaching/courses/enee350/vesp-source-code/vesp1.0.htm) for more info.

This language was used for two reverse engineering challenges in [Nahamcon CTF 2023](https://ctftime.org/event/2023/) (*writeright* and *ur_a_wizard*)

## Note

I probably found a bug at this line
```
case 4:   vesp.PC = vesp.IR & 0x1FFF;
```
in the `void execute(void)` function inside [VeSP Documentation](https://user.eng.umd.edu/~yavuz/teaching/courses/enee350/vesp-source-code/vesp1.0.htm), where the bit mask should be `0x0FFF` instead of `0x1FFF` according to the documentation where it is written : 
```
JMP  Jump        Opcode: 100  ----- PC = IR[4:15]
```
This bug has been patched in my debugger.

# VeSP Debugger

![title](images/title.png)

This tool created by myself could be considered as a new version of *VeSP 1.1* which allows you to :
  - Set breakpoints and continue the program execution until breakpoint is reached
  - Dump memory, see registers, breakpoints and code in the style of [gdb-peda](https://github.com/longld/peda) / [gdb-gef](https://github.com/hugsy/gef)   
  - Decode each instruction in a human readable way

# How to use VeSP Debugger ?
## Debugging color
Is the debugging color annoying you ? You can disable/enable it by typing
```
color <yes/no>
```
Example : `color yes` enables debugging color and `color no` disables color

## Breakpoints
To set breakpoints, you can type
```
breakpoint <address>
```
Example : `breakpoint ff` sets a breakpoint at address 0xff.

To delete breakpoints, you can type
```
del <address>
```
Example : `del fa` dletes a breakpoint previously set at address 0xfa.

*Note : The code instructions always start at address 0x0002* 

## Run the program
To run the program type
```
run
```
It will execute instructions until **HLT** instruction is reached or until a breakpoint is reached.

## Quit the debugger
Simply type
```
quit
```
It is simple as that.
