# Vanessa Joyce Tan
# global variables: strenter, space, m, n, a, b, c
# This program takes two positive integers from user inputs and calculates the pythagorean triple

	.data
strenter:	.asciiz "Enter two positive integers\n"
space:		.asciiz "\n"
m:	.word 0
n:	.word 0
a:	.word 0
b:	.word 0
c:	.word 0
	
	.text
# printing strenter
addi $v0, $0, 4		# $v0 = 4
la $a0, strenter	# load strenter into $a0
syscall			# print strenter string

# user input for m
addi $v0, $0, 5		# $v0 = 5
syscall			# read int value
sw $v0, m		# storing user input in m

# user input for n
addi $v0, $0, 5		# $v0 = 5
syscall			# read int value
sw $v0, n		# storing user input in n

# calculating a = m^2 - n^2
lw $t0, m		# $t0 = m
lw $t1, n		# $t1 = n

mult $t0, $t0		# to get m^2
mflo $t2		# store result in $t2

mult $t1, $t1		# to get n^2
mflo $t3		# store result in $t3

sub $t4, $t2, $t3	# m^2 - n^2
sw $t4, a		# store result in a

# calculating b = 2mn
addi $t5, $0, 2		# $t5 = 2

mult $t5, $t0		# 2*m
mflo $t6		# store result in $t6

mult $t6, $t1		# 2*m*n
mflo $t7		# store result in register $t7

sw $t7, b		# store result in b

# calculating c = m^2 + n^2
add $t5, $t2, $t3	# adding m^2 and n^2
sw $t5, c		# store result at c

# printing a
addi, $v0, $0, 1	# $v0 = 1
lw $a0, a		# load contents of a into $a0
syscall			# print value stored in a

# next line
addi $v0, $0, 4		# $v0 = 4
la $a0, space		# load "\n" into $a0
syscall			# print space

# printing b
addi, $v0, $0, 1	# $v0 = 1
lw $a0, b		# load contents of b into $a0
syscall			# print value stored in b

# next line
addi $v0, $0, 4		# $v0 = 4
la $a0, space		# load "\n" into $a0
syscall			# print space

# printing c		
addi, $v0, $0, 1	# $v0 = 1
lw $a0, c		# load contents of c into $a0
syscall			# print value stored in c

# exiting program
addi $v0, $0, 10	# $v0 = 10
syscall			# exit program
