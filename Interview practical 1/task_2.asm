# Vanessa Joyce Tan
# Global variables: size_prompt, element_prompt, min_str, colon_str, newline_str, size, the_list, i, min, item
# This program reads a list of integers of the size given by the user and computes the minimum element in the list.

   .data
size_prompt:	.asciiz "Enter list size: "
element_prompt:	.asciiz "Enter element "
min_str:	.asciiz "The minimum element in this list is "
colon_str:	.asciiz ": "
newline_str:	.asciiz "\n"
size:		.word 0
the_list:	.word 0
i:		.word 0
min:		.word 0
item:		.word 0

    .text
    # ignore this line, it is for later testing
    la $ra, test

#    ENTER YOUR CODE FOR READING LIST HERE (PYTHON LINES 1-7)
    
    # size = int(input("Enter list size: "))
    addi $v0, $0, 4		# $v0 = 4
    la $a0, size_prompt		# $a0 = size_prompt
    syscall			# print size_prompt
    
    addi $v0, $0, 5		# $v0 = 5
    syscall			# get user input for size
    sw $v0, size		# store user input in size
    
    # the_list = [0] * size
    addi $t0, $0, 4		# $t0 = 4
    lw $t1, size		# $t1 = size
    
    mult $t1, $t0		# size * 4 for amount of space to allocate in heap for elements in array
    mflo $t2			# store result in $t2
    
    addi $v0, $0, 9		# $v0 = 9
    la $a0, 4($t2)		# $a0 = (size * 4) + 4
    syscall			# allocate space in the heap
    sw $v0, the_list		# save address of array in the_list
    sw $t1, ($v0)		# store size of array in the address that $v0 is pointing to
    
input_loop:    
    # for i in range(size):
    lw $t0, i			# $t0 = i
    lw $t1, size		# $t1 = size
    slt $t2, $t0, $t1		# $t2 = 1 if i < size
    beq $t2, $0, compute_min	# jump to compute_min when i = size
    
    # the_list[i] = int(input("Enter element " + str(i) + ": "))
    addi $v0, $0, 4		# $v0 = 4
    la $a0, element_prompt	# $a0 = element_prompt
    syscall			# print element_prompt
    
    addi $v0, $0, 1		# $v0 = 1
    lw $a0, i			# $a0 = i
    syscall			# print index i
    
    addi $v0, $0, 4		# $v0 = 4
    la $a0, colon_str		# $a0 = colon_str
    syscall			# print colon_str
    
    addi $v0, $0, 5		# $v0 = 5
    syscall			# get user input for element
    
    lw $t0, the_list		# $t0 = address of array
    lw $t1, i			# $t1 = i
    addi $t2, $0, 4		# $t2 = 4
    
    mult $t1, $t2		# i * 4
    mflo $t3			# store results in $t3
    
    la $t3, 4($t3)		# $t3 = (i * 4) + 4				
    add $t0, $t0, $t3		# $t0 = address of the_list[i]
    sw $v0, ($t0)		# store input at the_list[i]
    
    lw $t0, i			# $t0 = i
    addi $t0, $t0, 1		# $t0 = $t0 + 1
    sw $t0, i			# i = i + 1
    
    j input_loop		# jump to input_loop

compute_min:
    
#    ENTER YOUR CODE FOR COMPUTING THE MIN (PYTHON LINES 8-15)
    
    # if size > 0:
    lw $t1, size		# $t1 = size
    slt $t0, $0, $t1		# $t0 = 1 if 0 < size
    beq $t0, $0, exit		# jump to exit if $t0 = 0 (size <= 0)
    
    # min = the_list[0]
    lw $t0, the_list		# $t0 = address of the array
    lw $t1, 4($t0)		# $t1 = the_list[0]
    sw $t1, min			# min = the_list[0]
   
    # for i in range(1,size):   
    sw $0, i			# i = 0
min_loop:
    lw $t0, i			# $t0 = i
    addi $t0, $t0, 1		# $t0 = $t0 + 1
    sw $t0, i			# i = i + 1
    
    lw $t0, i			# $t0 = i
    lw $t1, size		# $t1 = size
    slt $t2, $t0, $t1		# $t2 = 1 if i < size
    beq $t2, $0, print		# jump to print if $t2 = 0 (i >= size)
    
    # item = the_list[i]
    lw $t0, the_list		# $t0 = address of array
    lw $t1, i			# $t1 = i
    addi $t2, $0, 4		# $t2 = 4
    
    mult $t1, $t2		# i * 4
    mflo $t3			# store results in $t3
    
    la $t3, 4($t3)		# $t3 = (i * 4) + 4					
    add $t0, $t0, $t3		# $t0 = address of the_list[i]
    
    lw $t4, ($t0)		# $t4 = the_list[i]
    sw $t4, item		# item = the_list[i]
    
    # if min > item:
    lw $t0, min			# $t0 = min
    lw $t1, item		# $t1 = item
    slt $t3, $t1, $t0		# $t3 = 1 if item < min
    beq $t3, $0, min_loop	# jump to min_loop if $t3 = 0 (item >= min)
    
    # min = item
    lw $t0, item  		# $t0 = item
    sw $t0, min			# min = item
    
    j min_loop			# jump to min_loop

print:        
    # print("The minimum element in this list is " + str(min) + "\n")
    addi $v0, $0, 4		# $v0 = 4
    la $a0, min_str		# $a0 = min_str
    syscall			# print min_str
    
    addi $v0, $0, 1		# $v0 = 1
    lw $a0, min			# $a0 = min
    syscall			# print minimum element
    
    addi $v0, $0, 4		# $v0 = 4
    la $a0, newline_str		# $a0 = newline_str
    syscall			# go to next line
    
    
    
    jr $ra
test:   

    # the_list = [2,4,-1] 
    # Allocate the required bytes on the heap via syscall and put the address in the_list
    addi $a0, $0, 16   # 3 elements plus size = 16 bytes
    addi $v0, $0, 9    # allocate the bytes
    syscall
    sw $v0, the_list   # put start address in the_list
    # set global variable size to 3
    addi $t0, $0, 3    # $t0 = 3
    sw $t0, ($v0)      # start of the_list has correct size (3)
    sw $t0, size       # set the global variable size to the correct value so that the rest works
    # write the value of the elements 2, 4, -1
    addi $t0, $0, 2    # $t0 = 2
    sw $t0, 4($v0)     # the_list[0] = 2
    addi $t0, $0, 4    # $t0 = 4
    sw $t0, 8($v0)     # the_list[1] = 4
    addi $t0, $0, -1   # $t0 = -1
    sw $t0, 12($v0)    # the_list[2] = -1

    # go to compute the minimum of the_list = [2,4,-1] and come back
    jal compute_min    # should print -1

    # the_list = [2] 
    # Allocate the required bytes on the heap via syscall and put the address in the_list
    addi $a0, $0, 8    # 1 elements plus size = 8 bytes
    addi $v0, $0, 9    # allocate the bytes
    syscall
    sw $v0, the_list   # put start address in the_list
    # set global variable size to 1
    addi $t0, $0, 1    # $t0 = 1
    sw $t0, ($v0)      # start of the_list has correct size (1)
    sw $t0, size       # set the global variable size to the correct value so that the rest works
    # write the value of the element 2
    addi $t0, $0, 2    # $t0 = 2
    sw $t0, 4($v0)     # the_list[0] = 2
    
    # go to compute the minimum of the_list = [2] and come back
    jal compute_min    # should print 2
    
    # the_list = [0,5] 
    # Allocate the required bytes on the heap via syscall and put the address in the_list
    addi $a0, $0, 12   # 2 elements plus size = 12 bytes
    addi $v0, $0, 9    # allocate the bytes
    syscall
    sw $v0, the_list   # put start address in the_list
    # set global variable size to 2
    addi $t0, $0, 2    # $t0 = 2
    sw $t0, ($v0)      # start of the_list has correct size (2)
    sw $t0, size       # set the global variable size to the correct value so that the rest works
    # write the value of the elements  0,5
    sw $0, 4($v0)      # the_list[0] = 0
    addi $t0, $0, 5    # $t0 = 5
    sw $t0, 8($v0)     # the_list[1] = 5

    # go to compute the minimum of the_list = [0,5] and come back
    jal compute_min    # should print 0

    # the_list = [] 
    # Allocate the required bytes on the heap via syscall and put the address in the_list
    addi $a0, $0, 4    # 0 elements plus size = 4 bytes 
    addi $v0, $0, 9    # allocate the bytes
    syscall
    sw $v0, the_list   # put start address in the_list
    # set global variable size to 0
    sw $0, ($v0)       # start of the_list has correct size (0)
    sw $0, size        # set the global variable size to the correct value so that the rest works
    
    # go to compute the minimum of the_list = [] and come back
    jal compute_min    # should print nothing
        

    
exit:
    # Exit the program
    addi $v0, $0, 10		# $v0 = 10
    syscall			# exit program
