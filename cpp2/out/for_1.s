.data
____true____: .asciiz "true"
____false____: .asciiz "false"
tempo0: .word 0
x1: .word 0
tempo1: .word 2
tempo2: .word 5
tempo3: .word 0
tempo4: .word 1
tempo5: .word 0

.text
main:
b ___main___
___main___:
la $ra, _____EndOfWorld_____
lw $t9, tempo0
sw $t9, x1
lw $t9, tempo1
sw $t9, x1
l0:
lw $t1, x1
lw $t2, tempo2
slt $t3, $t1, $t2
sw $t3, tempo3
lw $t9, tempo3
beqz $t9, l2
j l1
l3:
lw $t1, x1
lw $t2, tempo4
add $t3, $t1, $t2
sw $t3, tempo5
lw $t9, tempo5
sw $t9, x1
j l0
l1:
lw $t9, x1
li	$v0, 1
move 	$a0, $t9
syscall
li	$v0, 11
li	$a0, 10
syscall
j l3
l2:
jr $ra
_____EndOfWorld_____:
li	$v0, 10
syscall
li	$v0, 8
li	$v0, 8
li	$v0, 8
