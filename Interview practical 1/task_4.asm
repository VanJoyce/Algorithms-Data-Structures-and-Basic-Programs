# Vanessa Joyce Tan
# This program has a function that implements bubble sort


# TEST HARNESS GIVEN PLUS ONE ADDED TEST CASE
	# Author: Maria Garcia de la Banda
# Nine global variables: 3 strings for printing (newline_str, correct, incorrect),
#      3 for the different test cases, and 3 for the expected results
# Aim: Test harness for Task 4 (bubble sort) in Interview prac 1
#      It uses 3 test cases:
#      [4,3,2,1]: should be left as [1,2,3,4]
#      [3,3,1]: should be left as [1,3,3]
#      []: should be left as is
#      [9,-3,0] should be left as [-3,0,9]	
    .data
newline_str:	.asciiz "\n"
correct:	.asciiz "sorted list is correct"
incorrect:	.asciiz "sorted list is incorrect"
test_list1:     .word 4,4,3,2,1
correct_list1:  .word 4,1,2,3,4
test_list2:     .word 3,3,3,1
correct_list2:  .word 3,1,3,3
test_list3:     .word 0
correct_list3:  .word 0
test_list4:	.word 3,9,-3,0
correct_list4:	.word 3,-3,0,9
    .text
test:

    # Call bubble_sort(the_list1)
    addi $sp, $sp, -4 # make space for 1 argument
    la $t0, test_list1# $t0 = test_list1
    sw $t0, 0($sp)    # arg 1
    jal bubble_sort   # call
    addi $sp, $sp, 4  # remove the argument

    # determine if correct (correct_list1)
    la $t0, test_list1    # load address of test_list1
    la $t1, correct_list1 # load address of correct_list1
    jal determine_if_correct # determine if correct sorting or not

    # Call bubble_sort(the_list2)
    addi $sp, $sp, -4 # make space for 1 argument
    la $t0, test_list2# $t0 = test_list2
    sw $t0, 0($sp)    # arg 1
    jal bubble_sort   # call
    addi $sp, $sp, 4  # remove the argument

    # determine if correct (correct_list2)
    la $t0, test_list2     # load address of test_list2
    la $t1, correct_list2  # load address of correct_list2
    jal determine_if_correct # determine if correct sorting or not

    # Call bubble_sort(the_list3)
    addi $sp, $sp, -4 # make space for 1 argument
    la $t0, test_list3# $t0 = test_list3
    sw $t0, 0($sp)    # arg 1
    jal bubble_sort   # call
    addi $sp, $sp, 4  # remove the argument

    # determine if correct (correct_list3)
    la $t0, test_list3    # load address of test_list3
    la $t1, correct_list3 # load address of correct_list3
    jal determine_if_correct # determine if correct sorting or not
    
    # Call bubble_sort(the_list4)
    addi $sp, $sp, -4 # make space for 1 argument
    la $t0, test_list4# $t0 = test_list4
    sw $t0, 0($sp)    # arg 1
    jal bubble_sort   # call
    addi $sp, $sp, 4  # remove the argument

    # determine if correct (correct_list4)
    la $t0, test_list4    # load address of test_list4
    la $t1, correct_list4 # load address of correct_list4
    jal determine_if_correct # determine if correct sorting or not

    # Exit the program
    addi $v0, $0, 10  # $v0 = 10 for exiting the program
    syscall           

determine_if_correct: #address of one list in $t0, the other in $t1
    lw $t2, ($t0) # load the size of the test list 
    lw $t3, ($t1) # load the size of the expected list
    bne $t2, $t3, is_incorrect # if size of array is different go to incorrect
 
loop:    
    beq $t2, $0, is_correct # if all elements compared, go to correct
   
    addi $t0,$t0,4 # compute address of next test_list element
    addi $t1,$t1,4 # compute address of next correct_list element
    lw $t3, ($t0)  # load test_list[i]
    lw $t4, ($t1)  # load correct_list[i]
    bne $t3, $t4, is_incorrect # if elements are different go to incorrect

    addi $t2, $t2, -1 # decrement loop index
    
    j loop

is_correct:    
   la $a0, correct  # $a0 = string that indicates sorting  is correct
   addi $v0, $0, 4  # $v0 = 4 to print the string already loaded in $a0
   syscall 
   # print "\n"
   la $a0, newline_str  # $a0 = newline to print a new line (could have added it to the string, but I might have wanted to print where it fails)
   syscall
   jr $ra            # go back to caller
is_incorrect:    
   la $a0, incorrect  # $a0 = string that indicates sorting is incorrect
   addi $v0, $0, 4  # $v0 = 4 to print the string already loaded in $a0
   syscall 
   # print "\n"
   la $a0, newline_str  # $a0 = newline to print a new line (could have added it to the string, but I might have wanted to print where it fails)
   syscall
   jr $ra            # go back to caller
		
	
bubble_sort:	# Save value of $ra and $fp on stack
		addi $sp, $sp, -8		# move $sp 2 addresses up
		sw $ra, 4($sp)			# save value of $ra in the byte below where $sp is pointing at
		sw $fp, 0($sp)			# save value of $fp in the byte where $sp is pointing at
	
		# Copy $sp to $fp
		addi $fp, $sp, 0		# $fp = $sp
		
		# Allocate local variables on the stack
		addi $sp, $sp, -20		# move $sp 5 addresses up for 5 local variables
		
		# Function body
		# n = len(the_list)
		lw $t0, 8($fp)			# $t0 = address of array
		lw $t1, 0($t0)			# $t1 = len(the_list)
		sw $t1, -4($fp)			# store len(the_list) in local variable n
		
		# Initialize local variable a
		addi $t0, $0, -1		# $t0 = -1
		sw $t0, -8($fp)			# a = -1
		
		# for a in range(n-1):
	a_loop: lw $t0, -8($fp)			# $t0 = a
		addi $t0, $t0, 1		# $t0 = a+1
		sw $t0, -8($fp)			# a = a+1
		
		lw $t1, -4($fp)			# $t1 = n
		addi $t1, $t1, -1		# $t1 = n - 1
		slt $t2, $t0, $t1		# $t2 = 1 if a < n - 1
		beq $t2, $0, exit_func		# jump to exit_func if a >= n - 1
		
		# Initialize local variable i
		addi $t0, $0, -1		# $t0 = -1
		sw $t0, -12($fp)		# i = -1
		
		# for i in range(n-1):
	i_loop: lw $t0, -12($fp)		# $t0 = i
		addi $t0, $t0, 1		# $t0 = i+1
		sw $t0, -12($fp)		# i = i+1
		
		lw $t1, -4($fp)			# $t1 = n
		addi $t1, $t1, -1		# $t1 = n - 1
		slt $t2, $0, $t1 		# $t2 = 1 if i < n - 1
		beq $t0, $t1, a_loop		# jump to a_loop if i >= n - 1
		
		# item = the_list[i]
		lw $t0, 8($fp)			# $t0 = address of array
		lw $t1, -12($fp)		# $t1 = i
		addi $t2, $0, 4			# $t2 = 4
		
		mult $t1, $t2			# i*4
		mflo $t1			# $t1 = i*4
		
		addi $t1, $t1, 4		# $t1 = i*4 + 4
		add $t3, $t0, $t1		# $t3 = address of the_list[i]
		
		lw $t4, ($t3)			# $t4 = the_list[i]
		sw $t4, -16($fp)		# item = the_list[i] 
		
		# item_to_right = the_list[i+1]
		lw $t0, 8($fp)			# $t0 = address of array
		lw $t1, -12($fp)		# $t1 = i
		addi $t1, $t1, 1		# $t1 = i+1
		addi $t2, $0, 4			# $t2 = 4
		
		mult $t1, $t2			# (i+1)*4
		mflo $t1			# $t1 = (i+1)*4
		
		addi $t1, $t1, 4		# $t1 = (i+1)*4 + 4
		add $t3, $t0, $t1		# $t3 = address of the_list[i+1]
		
		lw $t4, ($t3)			# $t4 = the_list[i+1]
		sw $t4, -20($fp)		# item_to_right = the_list[i+1] 
		
		# if item > item_to_right:
		lw $t0, -16($fp)		# $t0 = item
		lw $t1, -20($fp)		# $t1 = item_to_right
		slt $t2, $t1, $t0		# $t2 = 1 if item_to_right < item
		beq $t2, $0, i_loop		# jump to i_loop if $t2 = 0 (item_to_right > item)
		
		# the_list[i] = item_to_right
		lw $t0, 8($fp)			# $t0 = address of array
		lw $t1, -12($fp)		# $t1 = i
		addi $t2, $0, 4			# $t2 = 4
		
		mult $t1, $t2			# i*4
		mflo $t1			# $t1 = i*4
		
		addi $t1, $t1, 4		# $t1 = i*4 + 4
		add $t3, $t0, $t1		# $t3 = address of the_list[i]
		
		lw $t4, -20($fp)		# $t4 = item_to_right
		sw $t4, ($t3)			# the_list[i] = item_to_right
		
		# the_list[i+1] = item
		lw $t0, 8($fp)			# $t0 = address of array
		lw $t1, -12($fp)		# $t1 = i
		addi $t1, $t1, 1		# $t1 = i+1
		addi $t2, $0, 4			# $t2 = 4
		
		mult $t1, $t2			# (i+1)*4
		mflo $t1			# $t1 = (i+1)*4
		
		addi $t1, $t1, 4		# $t1 = (i+1)*4 + 4
		add $t3, $t0, $t1		# $t3 = address of the_list[i+1]
		
		lw $t4, -16($fp)		# $t4 = item
		sw $t4, ($t3)			# the_list[i+1] = item
		
		j i_loop			# jump to i_loop
		
	exit_func:
		# Clear local variables off stack
		addi $sp, $sp, 20		# move $sp 5 addresses down
		
		# Restores saved $fp and $ra off stack
		lw $fp, 0($sp)			# $fp = previous address of $fp before function call
		lw $ra, 4($sp)			# $ra = previous address of $ra before function call
		addi $sp, $sp, 8		# move $sp 2 addresses down
		
		# Return to caller
		jr $ra				# jump back to instruction where function was called
