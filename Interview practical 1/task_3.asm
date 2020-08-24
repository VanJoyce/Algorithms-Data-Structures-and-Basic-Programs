# Vanessa Joyce Tan
# Global variables: three strings to be printed - size_prompt, element_prompt, colon_str, newline_str
#		    four test arrays - list_1, list_2, list_3, list_4
#		    for testing - the_list, size
# This program contains three functions - read_list(), get_minimum() and main() to compute the minimum element in a list that has been input by the user

	.data
size_prompt:	.asciiz "Enter list size: "
element_prompt:	.asciiz "Enter element "
colon_str:	.asciiz ": "
newline_str:	.asciiz "\n"
the_list:	.word 0
size:		.word 0
list_1:		.word 3,2,4,-1
list_2:		.word 1,2
list_3:		.word 2,0,5
list_4:		.word 0

	.text	
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
    # Pass arguments on stack
    addi $sp, $sp, -4	# move $sp one address space up
    lw $t0, the_list	# $t0 = the_list
    sw $t0, ($sp)	# store address of the_list where $sp is pointing at
    # go to compute the minimum of the_list = [2,4,-1] and come back
    jal get_minimum    # should print -1
    # Clear arguments off stack
    addi $sp, $sp, 4		# move $sp one address down
    # Use return value of get_minimum in $v0
    add $a0, $0, $v0		# $a0 = return of get_minimum(the_list)
    addi $v0, $0, 1		# $v0 = 1
    syscall			# print return of get_minimum(the_list)
    # go to next line
    addi $v0, $0, 4		# $v0 = 4
    la $a0, newline_str		# $a0 = newline_str
    syscall			


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
    # Pass arguments on stack
    addi $sp, $sp, -4	# move $sp one address space up
    lw $t0, the_list	# $t0 = the_list
    sw $t0, ($sp)	# store address of the_list where $sp is pointing at
    # go to compute the minimum of the_list = [2] and come back
    jal get_minimum    # should print 2
    # Clear arguments off stack
    addi $sp, $sp, 4	# move $sp one address down	
    # Use return value of get_minimum in $v0
    add $a0, $0, $v0		# $a0 = return of get_minimum(the_list)
    addi $v0, $0, 1		# $v0 = 1
    syscall			# print return of get_minimum(the_list)
    # go to next line
    addi $v0, $0, 4		# $v0 = 4
    la $a0, newline_str		# $a0 = newline_str
    syscall	
    
    
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
    # Pass arguments on stack
    addi $sp, $sp, -4	# move $sp one address space up
    lw $t0, the_list	# $t0 = the_list
    sw $t0, ($sp)	# store address of the_list where $sp is pointing at
    # go to compute the minimum of the_list = [0,5] and come back
    jal get_minimum    # should print 0 
    # Clear arguments off stack
    addi $sp, $sp, 4	# move $sp one address down		
    # Use return value of get_minimum in $v0
    add $a0, $0, $v0		# $a0 = return of get_minimum(the_list)
    addi $v0, $0, 1		# $v0 = 1
    syscall			# print return of get_minimum(the_list)
    # go to next line
    addi $v0, $0, 4		# $v0 = 4
    la $a0, newline_str		# $a0 = newline_str
    syscall	
    

    # the_list = [] 
    # Allocate the required bytes on the heap via syscall and put the address in the_list
    addi $a0, $0, 4    # 0 elements plus size = 4 bytes 
    addi $v0, $0, 9    # allocate the bytes
    syscall
    sw $v0, the_list   # put start address in the_list
    # set global variable size to 0
    sw $0, ($v0)       # start of the_list has correct size (0)
    sw $0, size        # set the global variable size to the correct value so that the rest works
    # Pass arguments on stack
    addi $sp, $sp, -4	# move $sp one address space up
    lw $t0, the_list	# $t0 = the_list
    sw $t0, ($sp)	# store address of the_list where $sp is pointing at
    # go to compute the minimum of the_list = [] and come back
    jal get_minimum    # should print 0
    # Clear arguments off stack
    addi $sp, $sp, 4	# move $sp one address down	
    # Use return value of get_minimum in $v0
    add $a0, $0, $v0		# $a0 = return of get_minimum(the_list)
    addi $v0, $0, 1		# $v0 = 1
    syscall			# print return of get_minimum(the_list)
    # go to next line
    addi $v0, $0, 4		# $v0 = 4
    la $a0, newline_str		# $a0 = newline_str
    syscall	
    
    # Call function main
    jal main

    # Exit the program
    addi $v0, $0, 10		# $v0 = 10
    syscall			# exit program
		
read_list:	# Save value of $ra and $fp on stack
		addi $sp, $sp, -8		# move $sp two addresses up
		sw $ra,	4($sp)			# store $ra in address below where $sp is pointing at
		sw $fp, 0($sp)			# store $fp in address where $sp is pointing at
		
		# Copy $sp to $fp
		addi $fp, $sp, 0		# $fp = address $sp is pointing at
		
		# Allocate local variables on stack
		addi $sp, $sp, -12		# move $sp three addresses up
		
		# Function body
		# size = int(input("Enter list size: "))
		addi $v0, $0, 4			# $v0 = 4
    		la $a0, size_prompt		# $a0 = size_prompt
    		syscall				# print size_prompt
    
    		addi $v0, $0, 5			# $v0 = 5
    		syscall				# get user input for size
    		sw $v0, -4($fp)			# store user input in size
		
		# the_list = [0] * size
		addi $t0, $0, 4			# $t0 = 4
		lw $t1, -4($fp)			# $t1 = size
    
    		mult $t1, $t0			# size * 4 for amount of space to allocate in heap for elements in array
    		mflo $t2			# store result in $t2
    
    		addi $v0, $0, 9			# $v0 = 9
    		addi $a0, $t2, 4		# $a0 = (size * 4) + 4
    		syscall				# allocate space in the heap
    		sw $v0, -8($fp)			# save address of array in the_list
    		sw $t1, ($v0)			# store size of array in the address that $v0 is pointing to
		
	read_loop:
		# for i in range(size):
		lw $t0, -12($fp)		# $t0 = i
    		lw $t1, -4($fp)			# $t1 = size
    		slt $t2, $t0, $t1		# $t2 = 1 if i < size
    		beq $t2, $0, read_return	# jump to read_return when i >= size
    
		# the_list[i] = int(input("Enter element "+ str(i) + ": "))
		addi $v0, $0, 4			# $v0 = 4
    		la $a0, element_prompt		# $a0 = element_prompt
    		syscall				# print element_prompt
    
    		addi $v0, $0, 1			# $v0 = 1
    		lw $a0, -12($fp)		# $a0 = i
    		syscall				# print index i
    
    		addi $v0, $0, 4			# $v0 = 4
    		la $a0, colon_str		# $a0 = colon_str
    		syscall				# print colon_str
    
    		addi $v0, $0, 5			# $v0 = 5
    		syscall				# get user input for element
    
    		lw $t0, -8($fp)			# $t0 = address of array
    		lw $t1, -12($fp)		# $t1 = i
    		addi $t2, $0, 4			# $t2 = 4
    
    		mult $t1, $t2			# i * 4
    		mflo $t3			# store results in $t3
    
    		addi $t3, $t3, 4		# $t3 = (i * 4) + 4
    		add $t0, $t0, $t3		# $t0 = address of the_list[i]
    		sw $v0, ($t0)			# store input at the_list[i]
    
		lw $t0, -12($fp)		# $t0 = i
    		addi $t0, $t0, 1		# $t0 = $t0 + 1
    		sw $t0, -12($fp)		# i = i + 1
    
    		j read_loop			# jump to read_loop
    		
		# return the_list
	read_return:
		# Set $v0 to return value
		lw $v0, -8($fp)			# $v0 = the_list

		# Clear local variables off stack
		addi $sp, $sp, 12		# move $sp three addresses down
		
		# Restores saved $fp and $ra off stack
		lw $fp, 0($sp)			# $fp = previous address of $fp before function call
		lw $ra, 4($sp)			# $ra = previous address of $ra before function call
		addi $sp, $sp, 8		# move $sp 2 addresses down
		
		# Returns to caller
		jr $ra
		
		
get_minimum:	# Save value of $ra and $fp on stack
		addi $sp, $sp, -8		# move $sp two addresses up
		sw $ra,	4($sp)			# store $ra in address below where $sp is pointing at
		sw $fp, 0($sp)			# store $fp in address where $sp is pointing at
		
		# Copy $sp to $fp
		addi $fp, $sp, 0		# $fp = address $sp is pointing at
		
		# Allocate local variables on stack
		addi $sp, $sp, -16		# move $sp four addresses up
		
		# Function body
		# size = len(the_list)
		lw $t0, 8($fp)			# $t0 = the_list
		lw $t1, 0($t0)			# $t1 = len(the_list)
		sw $t1, -4($fp)			# size = len(the_list)
		
		# if size > 0:
		lw $t1, -4($fp)			# $t1 = size
    		slt $t0, $0, $t1		# $t0 = 1 if 0 < size
    		beq $t0, $0, get_minimum_else	# jump to exit if $t0 = 0 (size < 0)
		
		# min = the_list[0]
		lw $t0, 8($fp)			# $t0 = the_list
    		lw $t1, 4($t0)			# $t1 = the_list[0]
    		sw $t1, -8($fp)			# min = the_list[0]
		
		# for i in range(1, size):
		sw $0, -12($fp)			# i = 0
	get_minimum_loop:
		lw $t0, -12($fp)		# $t0 = i
    		addi $t0, $t0, 1		# $t0 = $t0 + 1
    		sw $t0, -12($fp)		# i = i + 1
    
    		lw $t0, -12($fp)		# $t0 = i
    		lw $t1, -4($fp)			# $t1 = size
    		slt $t2, $t0, $t1		# $t2 = 1 if i < size
    		beq $t2, $0, return_min		# jump to return_min if $t2 = $t0 (i >= size)
		
		# item = the_list[i]
		lw $t0, 8($fp)			# $t0 = the_list
    		lw $t1, -12($fp)		# $t1 = i
    		addi $t2, $0, 4			# $t2 = 4
    
    		mult $t1, $t2			# i * 4
    		mflo $t3			# store results in $t3
    
    		addi $t3, $t3, 4		# $t3 = (i * 4) + 4
    		add $t0, $t0, $t3		# $t0 = address of the_list[i]
    
    		lw $t4, ($t0)			# $t4 = the_list[i]
    		sw $t4, -16($fp)		# item = the_list[i]
    
		# if min > item
		lw $t0, -8($fp)			# $t0 = min
    		lw $t1, -16($fp)		# $t1 = item
    		slt $t3, $t1, $t0		# $t3 = 1 if item < min
    		beq $t3, $0, get_minimum_loop	# jump to get_minimum_loop if $t3 = 0 (item >= min)
    		
		# min = item
		lw $t0, -16($fp)  		# $t0 = item
    		sw $t0, -8($fp)			# min = item
		
		j get_minimum_loop		# jump to get_minimum_loop
		
		# return min
	return_min:
		# Set $v0 to return value
		lw $v0, -8($fp)			# $v0 = min
		
		# Clear local variable off stack
		addi $sp, $sp, 16		# move $sp four addresses down
		
		# Restores $fp and $ra off stack
		lw $fp, 0($sp)			# $fp = previous address of $fp before function call
		lw $ra, 4($sp)			# $ra = previous address of $ra before function call
		addi $sp, $sp, 8		# move $sp two addresses down
		
		# Return to caller
		jr $ra				# jump back to instruction where function was called
		
		# else:
	get_minimum_else:
		# return 0
		add $v0, $0, $0			# $v0 = 0
		
		# Clear local variable off stack
		addi $sp, $sp, 16		# move $sp four addresses down
		
		# Restores $fp and $ra off stack
		lw $fp, 0($sp)			# $fp = previous address of $fp before function call
		lw $ra, 4($sp)			# $ra = previous address of $ra before function call
		addi $sp, $sp, 8		# move $sp two addresses down
		
		# Return to caller
		jr $ra				# jump back to instruction where function was called
		
		
main:		# Save value of $ra and $fp on stack
		addi $sp, $sp, -8		# move $sp two addresses up
		sw $ra,	4($sp)			# store $ra in address below where $sp is pointing at
		sw $fp, 0($sp)			# store $fp in address where $sp is pointing at
		
		# Copy $sp to $fp
		addi $fp, $sp, 0		# $fp = address $sp is pointing at
		
		# Allocate local variables on stack
		addi $sp, $sp, -4		# move $sp one address up
		
		# Function body
		# my_list = read_list()
		# Call function read_list
		jal read_list
		
		# Use return value of read_list in $v0
		sw $v0, -4($fp)			# my_list = return value of read_list()
	
		# print(get_minimum(my_list))
		# Pass arguments of get_minimum on stack
		addi $sp, $sp, -4		# move $sp one address up
		
		lw $t0, -4($fp)			# $t0 = my_list
		sw $t0, 0($sp)			# store my_list in the address $sp is pointing to
		
		# Call function get_minimum
		jal get_minimum
		
		# Clear arguments off stack
		addi $sp, $sp, 4		# move $sp one address down
		
		# Use return value of get_minimum in $v0
		add $a0, $0, $v0		# $a0 = return of get_minimum(my_list)
		addi $v0, $0, 1			# $v0 = 1
		syscall				# print return of get_minimum(my_list)
		
		# Clear local variable off stack
		addi $sp, $sp, 4		# move $sp one addresses down
		
		# Restores $fp and $ra off stack
		lw $fp, 0($sp)			# $fp = previous address of $fp before function call
		lw $ra, 4($sp)			# $ra = previous address of $ra before function call
		addi $sp, $sp, 8		# move $sp two addresses down
		
		# Return to caller
		jr $ra				# jump back to instruction where function was called
