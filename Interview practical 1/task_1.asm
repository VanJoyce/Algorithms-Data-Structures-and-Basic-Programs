# Vanessa Joyce Tan
# Global variables: new_line, x, y, result, more_than_0
# This program takes in two integers and calculates one of b//a, a*b, or b//2 depending on which conditions are satisfied.

	.data
new_line:	.asciiz "\n"
x:		.word 5
y:		.word 5
result:		.word 0
more_than_0:	.word 0

	.text
		# x > 0 
cond1:		lw $t0, x		# $t0 = x
		slt $t1, $0, $t0	# $t1 = 1 if 0 < x
		sw $t1, more_than_0	# more_than_0 = 1
		beq $t1, $0, cond2	# jump to cond2 if $t1 = 0 (x < 0)
		
		# x < y
		lw $t0, x		# $t0 = x
		lw $t1, y		# $t1 = y
		
		slt $t2, $t0, $t1	# $t2 = 1 if x < y
		beq $t2, $0, cond2	# jump to cond2 if $t2 = 0 (x > y)
		
		j result1		# jump to result1 if $t0 = 1 (x > 0 and x < y)
		
		# x == y
cond2:		lw $t0, x		# $t0 = x
		lw $t1, y		# $t1 = y
		bne $t0, $t1, cond3	# jump to cond3 if x != y
		
		lw $t2, more_than_0	# $t2 = more_than_0
		and $t3, $t1, $t2	# $t3 = 1 if (x > 0) and (x == y)
		beq $t3, $0, result2	# jump to result2 if $t3 = 0 ((x < 0) and (x == y))
		
		j result1		# jump to result1 if $t3 = 1 ((x > 0) and (x == y))
		
		# y < 0
cond3:		lw $t0, y		# $t0 = y
		slt $t1, $t0, $0	# $t1 = 1 if y < 0
		beq $t1, $0, result3 	# jump to result3 if $t1 == 0 (none of the conditions met)
		
		j result2		# jump to result2 if $t1 == 1 (y < 0)
		

		# result = y//x
result1:	lw $t0, x		# $t0 = x
		lw $t1, y		# $t1 = y
		
		div $t1, $t0		# y divide by x
		mflo $t2		# $t2 = y//x
		sw $t2, result		# result = y//x
		
		j print			# jump to label print
		
		# result = x * y
result2:	lw $t0, x		# $t0 = x
		lw $t1, y		# $t1 = y
		
		mult $t0, $t1		# x multiply with y
		mflo $t2		# $t2 = x * y
		sw $t2, result		# result = x * y
		
		j print			# jump to label print
		
		# result = y//2
result3:	addi $t0, $0, 2		# $t0 = 2
		lw $t1, y		# $t1 = y
		
		div $t1, $t0		# y divide by 2
		mflo $t2		# $t2 = y//2
		sw $t2, result		# result = y//2
		
		j print			# jump to label print
	
		# print(result)
print:		addi $v0, $0, 1		# $v0 = 1
		lw $a0, result		# $a0 = result
		syscall			# print integer stored in label result
		
		# go to next line
		addi $v0, $0, 4		# $v0 = 4
		la $a0, new_line	# $a0 = new_line
		syscall			# go to next line
		
		# terminate program
		addi $v0, $0, 10	# $v0 = 10
		syscall			# terminate program
