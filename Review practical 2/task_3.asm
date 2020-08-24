# Vanessa Joyce Tan
# Global variables: strenter, strquotient, strremainder, a, b, quotient, remainder
# This program takes two integers and finds the quotient and remainder

	.data
strenter:	.asciiz "Enter two integers\n"
strquotient:	.asciiz "\nQuotient is "
strremainder:	.asciiz "\nRemainder is "
a: 		.word 0
b:		.word 0
quotient:	.word 0
remainder:	.word 0
	
	.text
# print("Enter two integers")
addi $v0, $0, 4
la $a0, strenter
syscall

# a = int(input())
addi $v0, $0, 5			# call code 5 is for inputting integers
syscall
sw $v0, a			# store contents of $v0 into a

# b = int(input())
addi $v0, $0, 5			# call code 5 is for inputting integers
syscall
sw $v0, b			# store contents of $v0 into b

# dividing a by b
lw $t0, a			# load contents of a into $t0
lw $t1, b			# load contents of b into $t1
div $t0, $t1			# a divide by b

# quotient = a//b
mflo $t2			# $t2 = LO
sw $t2, quotient		# store results in quotient

# remainder = a%b
mfhi $t3			# $t3 = HI
sw $t3, remainder		# sotre remainder in label remainder

# print("Quotient is " + str(quotient))
addi $v0, $0, 4
la $a0, strquotient
syscall

addi $v0, $0, 1
lw $a0, quotient
syscall

# print("Remainder is " + str(remainder))
addi $v0, $0, 4
la $a0, strremainder
syscall

addi $v0, $0, 1
lw $a0, remainder
syscall

# exiting program
addi $v0, $0, 10		# call code 10 is for exiting the program
syscall
