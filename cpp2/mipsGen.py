#gets a TAC like string input and outputs a MIPS code
'''
u better go to page 54 of SPIM_Manual.pdf contains mips manual too
there are also instructions for double and single
================================================================================
-----------assign----------
//constant
assign a f= 1.2
assign a i= 12
assign a s= "fwrefwerf"
assign a b= false
//regular
assign a = b
assign *(a) = b
assign a = *(b)
assign a = allocate 6
assign a = allocate t
----------arith-------------
.........arith float.......
arith a = b f+ c
arith a = b f* c
arith a = b f/ c
arith a = b f- c
arith a = b f== c
arith a = b f!= c
arith a = b f<= c
arith a = b f< c
arith a = b f>= c
arith a = b f> c
......arith string.......
arith a = b s== c
arith a = b s!= c
......arith bool........
arith a = b b== c
arith a = b b!= c
......arith int........
arith a = b + c
arith a = b * c
arith a = b / c
arith a = b - c
arith a = b % c
arith a = b == c
arith a = b != c
arith a = b <= c
arith a = b < c
arith a = b >= c
arith a = b > c

arith a = b + 10
arith a = 10 + b
arith a = 4 * b
arith a = b * 4
--------arith convert-----------
arith a c= itod b
arith a c= btoi b
arith a c= itod b
arith a c= dtoi b
-----------function call-----------
pushra
push input1 (optional)
.
.
.
Lcall lable
pop output (optional)
popra

lable:
.
.
.
return from lable
----------------------
Ifz a goto lable
#pushaddressof... gooya nadarim ino
jumpto lable
---------print---------
Printf lable
Printb lable
Printi lable
Prints lable
Printe
--------read----------
ReadInt t = ReadInt()
ReadLine t = ReadLine()
----------one word instructs-----------
pushra
popra
Printe
lable:
'''
def mipsGen(input_code):
    def check_int(x):
        if x[0] == '+':
            return x[1:].isdigit()
        return x.isdigit()
    vars = {}
    instructions = input_code.split('\n')
    mipsDataCode = '.data\n'
    mipsDataCode += '____true____: .asciiz \"true\"\n'
    mipsDataCode += '____false____: .asciiz \"false\"\n'
    mipsTextCode = '.text\n'
    # mipsTextCode += '################ MACROS ################\n'
    # mipsTextCode += '.macro read_int($dReg)\nli	$v0, 5\nsyscall\nmove	$dReg, $v0\n.end_macro\n'
    # mipsTextCode += '.macro read_string($string_address)\nli	$v0, 8\nli	$a1, 1000  #MAX_SIZE==999\nmove	$a0, $string_address\nsyscall\n.end_macro\n'
    # mipsTextCode += '.macro print_int($reg)\nli	$v0, 1\nmove 	$a0, $reg\nsyscall\n.end_macro\n'
    # mipsTextCode += '.macro print_float($reg)\nli	$v0, 2\nmov.s 	$f12, $reg\nsyscall\n.end_macro\n'
    # mipsTextCode += '.macro	print_string($string_address)\nli	$v0, 4\nmove	$a0, $string_address\nsyscall\n.end_macro\n'
    # mipsTextCode += '.macro	Exit()\nli	$v0, 10\nsyscall\n.end_macro\n'
    # mipsTextCode += '.macro	print_enter()\nli	$v0, 11\nli	$a0, 10\nsyscall\n.end_macro\n'
    # mipsTextCode += '########################################\n'
    for instruction in instructions:
        if instruction == '':
            continue
        # mipsTextCode += '#' + instruction + '\n'
        instruction = instruction.split(' ')
        if instruction[0] == 'arith':#arith a = b Xop c
            if instruction[4][0] == 'f':
                if instruction[4] == 'f+':#add
                    if not instruction[1] in vars.keys():
                        mipsDataCode += instruction[1] + ': ' + '.float 0.0\n'
                        vars[instruction[1]] = 0
                    mipsTextCode += 'l.s $f1, ' + instruction[3] + '\n'
                    mipsTextCode += 'l.s $f2, ' + instruction[5] + '\n'
                    mipsTextCode += 'add.s $f3, $f1, $f2\n'
                    mipsTextCode += 's.s $f3, ' + instruction[1] + '\n'
                if instruction[4] == 'f-':#sub
                    if not instruction[1] in vars.keys():
                        mipsDataCode += instruction[1] + ': ' + '.float 0.0\n'
                        vars[instruction[1]] = 0
                    mipsTextCode += 'l.s $f1, ' + instruction[3] + '\n'
                    mipsTextCode += 'l.s $f2, ' + instruction[5] + '\n'
                    mipsTextCode += 'sub.s $f3, $f1, $f2\n'
                    mipsTextCode += 's.s $f3, ' + instruction[1] + '\n'
                if instruction[4] == 'f*':#mul
                    if not instruction[1] in vars.keys():
                        mipsDataCode += instruction[1] + ': ' + '.float 0.0\n'
                        vars[instruction[1]] = 0
                    mipsTextCode += 'l.s $f1, ' + instruction[3] + '\n'
                    mipsTextCode += 'l.s $f2, ' + instruction[5] + '\n'
                    mipsTextCode += 'mul.s $f3, $f1, $f2\n'
                    mipsTextCode += 's.s $f3, ' + instruction[1] + '\n'
                if instruction[4] == 'f/':#div
                    if not instruction[1] in vars.keys():
                        mipsDataCode += instruction[1] + ': ' + '.float 0.0\n'
                        vars[instruction[1]] = 0
                    mipsTextCode += 'l.s $f1, ' + instruction[3] + '\n'
                    mipsTextCode += 'l.s $f2, ' + instruction[5] + '\n'
                    mipsTextCode += 'div.s $f3, $f1, $f2\n'
                    mipsTextCode += 's.s $f3, ' + instruction[1] + '\n'
            if instruction[4][0] == 's':
                if instruction[4] == 's==':
                    pass
                if instruction[4] == 's!=':
                    pass
            if instruction[4][0] == 'b':
                if instruction[4] == 'b==':
                    pass
                if instruction[4] == 'b!=':
                    pass
            if instruction[2] == 'c=':#arith a c= xtoy b
                if instruction[3] == 'xtoy':#arith a c= itod b
                    pass
                if instruction[3] == 'xtoy':#arith a c= dtoi b
                    pass
                if instruction[3] == 'xtoy':#arith a c= btoi b
                    pass
                if instruction[3] == 'xtoy':#arith a c= itob b
                    pass
            if not instruction[1] in vars.keys():
                mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                vars[instruction[1]] = 0
            if instruction[4] == '+':#add
                if check_int(instruction[3]):
                    numberLable = '_____'+instruction[3]+'_____'
                    if not numberLable in vars.keys():
                        mipsDataCode += numberLable + ': .word ' + instruction[3] + '\n'
                        vars[numberLable] = 0
                    mipsTextCode += 'lw $t1, ' + numberLable + '\n'
                    mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                    mipsTextCode += 'add $t3, $t1, $t2\n'
                    mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                elif check_int(instruction[5]):
                    mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                    numberLable = '_____'+instruction[5]+'_____'
                    if not numberLable in vars.keys():
                        mipsDataCode += numberLable + ': .word ' + instruction[5] + '\n'
                        vars[numberLable] = 0
                    mipsTextCode += 'lw $t2, ' + numberLable + '\n'
                    mipsTextCode += 'add $t3, $t1, $t2\n'
                    mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                else:
                    mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                    mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                    mipsTextCode += 'add $t3, $t1, $t2\n'
                    mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '-':#sub
                mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                mipsTextCode += 'sub $t3, $t1, $t2\n'
                mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '*':#mul
                if check_int(instruction[3]):
                    numberLable = '_____'+instruction[3]+'_____'
                    if not numberLable in vars.keys():
                        mipsDataCode += numberLable + ': .word ' + instruction[3] + '\n'
                        vars[numberLable] = 0
                    mipsTextCode += 'lw $t1, ' + numberLable + '\n'
                    mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                    mipsTextCode += 'mul $t3, $t1, $t2\n'
                    mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                elif check_int(instruction[5]):
                    mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                    numberLable = '_____'+instruction[5]+'_____'
                    if not numberLable in vars.keys():
                        mipsDataCode += numberLable + ': .word ' + instruction[5] + '\n'
                        vars[numberLable] = 0
                    mipsTextCode += 'lw $t2, ' + numberLable + '\n'
                    mipsTextCode += 'mul $t3, $t1, $t2\n'
                    mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                else:
                    mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                    mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                    mipsTextCode += 'mul $t3, $t1, $t2\n'
                    mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '/':#div
                mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                mipsTextCode += 'div $t3, $t1, $t2\n'
                mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '%':#rem
                mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                mipsTextCode += 'rem $t3, $t1, $t2\n'
                mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '==':#seq
                mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                mipsTextCode += 'seq $t3, $t1, $t2\n'
                mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '!=':#sne
                mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                mipsTextCode += 'sne $t3, $t1, $t2\n'
                mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '<':#slt
                mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                mipsTextCode += 'slt $t3, $t1, $t2\n'
                mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '<=':#sle
                mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                mipsTextCode += 'sle $t3, $t1, $t2\n'
                mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '||':#
                mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                mipsTextCode += 'beqz $t1, __branch__here__if__arg1__is__0__\n'
                mipsTextCode += 'li $t3, 1\nb __branch__here__to__end__oror__\n'
                mipsTextCode += '__branch__here__if__arg1__is__0__:\n'
                mipsTextCode += 'beqz $t2, __branch__here__if__arg2__isAlso__0__\n'
                mipsTextCode += 'li $t3, 1\nb __branch__here__to__end__oror__\n'
                mipsTextCode += '__branch__here__if__arg2__isAlso__0__:\n'
                mipsTextCode += 'li $t3, 0\n__branch__here__to__end__oror__:\n'
                mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            if instruction[4] == '&&':#
                mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                mipsTextCode += 'bnez $t1, __branch__here__if__arg1__is__1__\n'
                mipsTextCode += 'li $t3, 0\nb __branch__here__to__end__andand__\n'
                mipsTextCode += '__branch__here__if__arg1__is__1__:\n'
                mipsTextCode += 'bnez $t2, __branch__here__if__arg2__isAlso__1__\n'
                mipsTextCode += 'li $t3, 0\nb __branch__here__to__end__andand__\n'
                mipsTextCode += '__branch__here__if__arg2__isAlso__1__:\n'
                mipsTextCode += 'li $t3, 1\n__branch__here__to__end__andand__:\n'
                mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
        if len(instruction) == 1:#pushra or #popra or #a:
            if instruction[0] == 'pushra':#pushra
                mipsTextCode += 'subi $sp, $sp, 4\n'
                mipsTextCode += 'sw $ra, ($sp)\n'
            elif instruction[0] == 'popra':#popra
                mipsTextCode += 'lw $ra, ($sp)\n'
                mipsTextCode += 'addi $sp, $sp, 4\n'
            elif instruction[0] == 'Printe':#Printe
                mipsTextCode += 'li	$v0, 11\nli	$a0, 10\nsyscall\n'
            else:#lable:
                mipsTextCode += instruction[0] + '\n'
                if instruction[0] == 'main:':
                    mipsTextCode += 'la $ra, _______End_Of_The_World_______\n'
        if instruction[0] == 'push':#push a
            mipsTextCode += 'lw $t9, ' + instruction[1] + '\n'
            mipsTextCode += 'subi $sp, $sp, 4\n'
            mipsTextCode += 'sw $t9, ($sp)\n'
        if instruction[0] == 'pop':#pop a
            if not instruction[1] in vars.keys():
                mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                vars[instruction[1]] = 0
            mipsTextCode += 'lw $t9, ($sp)\n'
            mipsTextCode += 'addi $sp, $sp, 4\n'
            mipsTextCode += 'sw $t9, ' + instruction[1] + '\n'
        if instruction[0] == 'Lcall':#Lcall lable
            mipsTextCode += 'jal ' + instruction[1] + '\n'
        if instruction[0] == 'return': #return from folan
            mipsTextCode += 'jr $ra\n'
        if instruction[0] == 'Printf':#Printf a
            mipsTextCode += 'l.s $f9, ' + instruction[1] + '\n'
            mipsTextCode += 'li	$v0, 2\nmov.s 	$f12, $f9\nsyscall\n'
        if instruction[0] == 'Prints':#Prints a
            mipsTextCode += 'lw $t9, ' + instruction[1] + '\n'
            mipsTextCode += 'li	$v0, 4\nmove	$a0, $t9\nsyscall\n\n'
        if instruction[0] == 'Printi':#Printi a
            mipsTextCode += 'lw $t9, ' + instruction[1] + '\n'
            mipsTextCode += 'li	$v0, 1\nmove 	$a0, $t9\nsyscall\n'
        if instruction[0] == 'Printb':#Printb a
            mipsTextCode += 'lw $t9, ' + instruction[1] + '\n'
            mipsTextCode += 'beqz $t9, ____printFalse____\n'
            mipsTextCode += '____printTrue____:\n'
            mipsTextCode += 'la $a0, ____true____\n'
            mipsTextCode += 'li $v0, 4\n'
            mipsTextCode += 'syscall\n'
            mipsTextCode += 'j ____printbEnd____\n'
            mipsTextCode += '____printFalse____:\n'
            mipsTextCode += 'la $a0, ____false____\n'
            mipsTextCode += 'li $v0, 4\n'
            mipsTextCode += 'syscall\n'
            mipsTextCode += '____printbEnd____:\n'
        if instruction[0] == 'assign':
            if instruction[2] == 'f=':#assign a f= 1.2
                mipsDataCode += instruction[1] + ': ' + '.double ' + instruction[3] + '\n'
                vars[instruction[1]] = 0
            if instruction[2] == 'i=':#assign a i= 12
                mipsDataCode += instruction[1] + ': ' + '.word ' + instruction[3] + '\n'
                vars[instruction[1]] = 0
            if instruction[2] == 's=':#assign a s= "fwrefwerf"
                s = ''
                for i in instruction[3:]:
                    s += ' ' + i
                mipsDataCode += '___' + instruction[1] + '___: ' + '.asciiz ' + s + '\n'
                mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                mipsTextCode += 'la $t9, ' + '___' + instruction[1] + '___\n'
                mipsTextCode += 'sw $t9, ' + instruction[1] + '\n'
                vars['___' + instruction[1] + '___'] = 0
                vars[instruction[1]] = 0
            if instruction[2] == 'b=':#assign a b= false
                if instruction[3] == 'false':
                    instruction[3] = '0'
                if instruction[3] == 'true':
                    instruction[3] = '1'
                mipsDataCode += instruction[1] + ': ' + '.word ' + instruction[3] + '\n'
                vars[instruction[1]] = 0
            if instruction[2] == '=':
                if instruction[3] == 'allocate':
                    if check_int(instruction[4]):#assign t1 = allocate 6
                        if not instruction[1] in vars.keys():
                            mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                            vars[instruction[1]] = 0
                        allocLable = '___' + instruction[1] + '___'
                        mipsDataCode += allocLable + ': .word ' + instruction[4] + '\n'
                        mipsTextCode += 'lw	$t9, ' + allocLable + '\n'
                        mipsTextCode += 'li	$v0, 9\n'
                        mipsTextCode += 'move	$a0, $t9\n'
                        mipsTextCode += 'syscall\n'
                        mipsTextCode += 'sw $v0, ' + instruction[1] + '\n'
                    else:#assign t1 = allocate b
                        if not instruction[1] in vars.keys():
                            mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                            vars[instruction[1]] = 0
                        mipsTextCode += 'lw	$t9, ' + instruction[4] + '\n'
                        mipsTextCode += 'li	$v0, 9\n'
                        mipsTextCode += 'move	$a0, $t9\n'
                        mipsTextCode += 'syscall\n'
                        mipsTextCode += 'sw $v0, ' + instruction[1] + '\n'
                elif instruction[1][0] == '*':#assign *(t1) = t2
                    mipsTextCode += 'lw $t9, ' + instruction[1][2:-1] + '\n'
                    mipsTextCode += 'lw $t8, ' + instruction[3] + '\n'
                    mipsTextCode += 'sw $t8, ($t9)\n'
                elif instruction[3][0] == '*':#assign t1 = *(t2)
                    if not instruction[1] in vars.keys():
                        mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                        vars[instruction[1]] = 0
                    mipsTextCode += 'lw $t9, ' + instruction[3][2:-1] + '\n'
                    mipsTextCode += 'lw $t9, ($t9)\n'
                    mipsTextCode += 'sw $t9, ' + instruction[1] + '\n'
                else:#assign t1 = t2
                    if not instruction[1] in vars.keys():
                        mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                        vars[instruction[1]] = 0
                    mipsTextCode += "lw $t9, " + instruction[3] + '\n'
                    mipsTextCode += "sw $t9, " + instruction[1] + '\n'
        if instruction[0] == 'getAddress':
            pass
        if instruction[0] == 'ReadInt':#ReadInt t = ReadInt()
            mipsDataCode += instruction[1] + ': ' + '.word 0\n'
            mipsTextCode += 'li	$v0, 5\nsyscall\nmove	$t9, $v0\n'
            mipsTextCode += 'sw $t9, ' + instruction[1] + '\n'
        if instruction[0] == 'ReadLine':#ReadLine t = ReadLine()
            mipsDataCode += instruction[1] + ': ' + '.asciiz\n'
            mipsTextCode += 'la $t9, ' + instruction[1] + '\n'
            mipsTextCode += 'li	$v0, 8\nli	$a1, 1000  #MAX_SIZE==999\nmove	$a0, $t9\nsyscall\n\n'
        if instruction[0] == 'jumpto':# jumpto lable
            mipsTextCode += 'j ' + instruction[1] + '\n'
        if instruction[0] == 'Ifz':#Ifz a goto lable
            mipsTextCode += 'lw $t9, ' + instruction[1] + '\n'
            mipsTextCode += 'beqz $t9, ' + instruction[3] + '\n'
    mipsTextCode += '_______End_Of_The_World_______:\nli	$v0, 10\nsyscall\n'
    return '=============mipsGen under construction===============\n' + mipsDataCode + '\n' + mipsTextCode
