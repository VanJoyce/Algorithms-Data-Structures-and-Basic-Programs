# Vanessa Joyce Tan
# Global variables: strlabel1
# This program prints out "I like MIPS"

	.data
strlabel1:	.asciiz "I like MIPS"
	
	.text
	
# print("I like MIPS")
addi $v0, $0, 4		# stores 4 in $v0. 4 is the call code for the system call that prints strings
la $a0, strlabel1	# stores the string with label strlabel1 in the register $a0
syscall

# Exit program
addi $v0, $0, 10	# stores 10 in $v0. 10 is the call code for the system call that exits a program
syscall
