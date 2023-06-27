# VeSP Language

VeSP (VEry Simple Processor) is a simple instruction set & simulator made by [A. Yavuz Oruc](https://user.eng.umd.edu/~yavuz/)

The VeSP simulator takes in machine code and runs it. There is no 'print' functionality, all data
is either in registers or memory. See [VeSP Documentation](https://user.eng.umd.edu/~yavuz/teaching/courses/enee350/vesp-source-code/vesp1.0.htm) for more info.

This language was used for two reverse engineering challenges in [Nahamcon CTF 2023](https://ctftime.org/event/2023/) (*writeright* and *ur_a_wizard*)

# VeSP Debugger

This tool created by myself could be considered as a new version of *VeSP 1.1* which allows you to :
  - Set breakpoints and continue the execution until breakpoint is reached
  - Dump memory, see registers, breakpoints and code in the style of [gdb-peda](https://github.com/longld/peda) / [gdb-gef](https://github.com/hugsy/gef)   
  - Decode each instruction in a human readable way
