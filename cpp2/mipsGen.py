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
......arith string.......
arith a = b s== c
arith a = b s!= c
......arith bool........
arith a = b b== c
arith a = b b!= c
arith a = b b! // a = not(b)
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

arith a = b + 10
arith a = 10 + b
arith a = 4 * b
arith a = b * 4
--------arith convert-----------
arith a c= itob b
arith a c= btoi b
arith a c= itod b
arith a c= dtoi b
---------function call format----------
pushra
push input1 (optional)
.
.
.
Lcall lable
pop output (optional)
popra
--------------------------------
lable:
.
.
.
return from lable
return
----------------------
Ifz a goto lable
#pushaddressof... gooya nadarim ino
jumpto lable
---------print---------
Printf a
Printb a
Printi a
Prints a //the address of first byte of our string is in a
Printe
--------read----------
ReadInt t = ReadInt()
ReadLine t = ReadLine()
----------one word instructions-----------
pushra
popra
Printe
lable:
return
'''
def mipsGen(input_code):
    def check_int(x):
        if x[0] == '+' or x[0] == '-':
            return x[1:].isdigit()
        return x.isdigit()
    vars = {}
    myLableCount = 0
    MAX_SIZE = 1010
    instructions = input_code.split('\n')
    mipsDataCode = '.data\n'
    mipsDataCode += '____true____: .asciiz \"true\"\n'
    mipsDataCode += '____false____: .asciiz \"false\"\n'
    mipsTextCode = '.text\nmain:\nb ___main___\n'
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
        if instruction[0] == 'arith':#arith
            if instruction[2] == '=':#arith a = b Xop c
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
                    if instruction[4] == 'f==':#arith a = b f== c
                        if not instruction[1] in vars.keys():
                            mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                            vars[instruction[1]] = 0
                        ceqtrueLable = '____ceqstrue' + str(myLableCount) + '____'
                        ceqfalseLable = '____ceqsfalse' + str(myLableCount) + '____'
                        ceqendLable = '____ceqsend' + str(myLableCount) + '____'
                        myLableCount += 1
                        mipsTextCode += 'l.s $f1, ' + instruction[3] + '\n'
                        mipsTextCode += 'l.s $f2, ' + instruction[5] + '\n'
                        mipsTextCode += 'c.eq.s $t1, $t2\n'
                        mipsTextCode += 'bc1f ' + ceqfalseLable + '\n'
                        mipsTextCode += ceqtrueLable + ':\n'
                        mipsTextCode += 'li $t3, 1\n'
                        mipsTextCode += 'j ' + ceqendLable + '\n'
                        mipsTextCode += ceqfalseLable + ':\n'
                        mipsTextCode += 'li $t3, 0\n'
                        mipsTextCode += ceqendLable + ':\n'
                        mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                    if instruction[4] == 'f!=':#arith a = b f!= c
                        if not instruction[1] in vars.keys():
                            mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                            vars[instruction[1]] = 0
                        ceqtrueLable = '____ceqstrue' + str(myLableCount) + '____'
                        ceqfalseLable = '____ceqsfalse' + str(myLableCount) + '____'
                        ceqendLable = '____ceqsend' + str(myLableCount) + '____'
                        myLableCount += 1
                        mipsTextCode += 'l.s $f1, ' + instruction[3] + '\n'
                        mipsTextCode += 'l.s $f2, ' + instruction[5] + '\n'
                        mipsTextCode += 'c.eq.s $t1, $t2\n'
                        mipsTextCode += 'bc1f ' + ceqfalseLable + '\n'
                        mipsTextCode += ceqtrueLable + ':\n'
                        mipsTextCode += 'li $t3, 0\n'
                        mipsTextCode += 'j ' + ceqendLable + '\n'
                        mipsTextCode += ceqfalseLable + ':\n'
                        mipsTextCode += 'li $t3, 1\n'
                        mipsTextCode += ceqendLable + ':\n'
                        mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                    if instruction[4] == 'f<=':#arith a = b f<= c
                        if not instruction[1] in vars.keys():
                            mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                            vars[instruction[1]] = 0
                        ceqtrueLable = '____ceqstrue' + str(myLableCount) + '____'
                        ceqfalseLable = '____ceqsfalse' + str(myLableCount) + '____'
                        ceqendLable = '____ceqsend' + str(myLableCount) + '____'
                        myLableCount += 1
                        mipsTextCode += 'l.s $f1, ' + instruction[3] + '\n'
                        mipsTextCode += 'l.s $f2, ' + instruction[5] + '\n'
                        mipsTextCode += 'c.le.s $f1, $f2\n'
                        mipsTextCode += 'bc1f ' + ceqfalseLable + '\n'
                        mipsTextCode += ceqtrueLable + ':\n'
                        mipsTextCode += 'li $t3, 1\n'
                        mipsTextCode += 'j ' + ceqendLable + '\n'
                        mipsTextCode += ceqfalseLable + ':\n'
                        mipsTextCode += 'li $t3, 0\n'
                        mipsTextCode += ceqendLable + ':\n'
                        mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                    if instruction[4] == 'f<':#arith a = b f< c
                        if not instruction[1] in vars.keys():
                            mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                            vars[instruction[1]] = 0
                        ceqtrueLable = '____ceqstrue' + str(myLableCount) + '____'
                        ceqfalseLable = '____ceqsfalse' + str(myLableCount) + '____'
                        ceqendLable = '____ceqsend' + str(myLableCount) + '____'
                        myLableCount += 1
                        mipsTextCode += 'l.s $f1, ' + instruction[3] + '\n'
                        mipsTextCode += 'l.s $f2, ' + instruction[5] + '\n'
                        mipsTextCode += 'c.lt.s $f1, $f2\n'
                        mipsTextCode += 'bc1f ' + ceqfalseLable + '\n'
                        mipsTextCode += ceqtrueLable + ':\n'
                        mipsTextCode += 'li $t3, 1\n'
                        mipsTextCode += 'j ' + ceqendLable + '\n'
                        mipsTextCode += ceqfalseLable + ':\n'
                        mipsTextCode += 'li $t3, 0\n'
                        mipsTextCode += ceqendLable + ':\n'
                        mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                if instruction[4][0] == 's':#arith a = s1 s== s2
                    if not instruction[1] in vars.keys():
                        mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                        vars[instruction[1]] = 0
                    loopLable = '____loop' + str(myLableCount) + '____'
                    missmatchLable = '____missmatch' + str(myLableCount) + '____'
                    endfunctionLable = '____endfunction' + str(myLableCount) + '____'
                    checkt2Lable = '____checkt2' + str(myLableCount) + '____'
                    myLableCount += 1
                    mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                    mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                    mipsTextCode += loopLable + ':\n'
                    mipsTextCode += 'lb $t3($t1)  #load a byte from each string\n'
                    mipsTextCode += 'lb $t4($t2)\n'
                    mipsTextCode += 'beqz $t3, '+checkt2Lable+' #str1 end\n'
                    mipsTextCode += 'beqz $t4, '+missmatchLable+'\n'
                    mipsTextCode += 'seq $t5,$t3,$t4  #compare two bytes\n'
                    mipsTextCode += 'beqz $t5, '+missmatchLable+'\n'
                    mipsTextCode += 'addi $t1,$t1,1  #t1 points to the next byte of str1\n'
                    mipsTextCode += 'addi $t2,$t2,1\n'
                    mipsTextCode += 'j '+loopLable+'\n'
                    mipsTextCode += missmatchLable + ':\n'
                    mipsTextCode += 'add $v0, $zero, $zero\n'
                    mipsTextCode += 'addi $v1, $zero, 1\n'
                    mipsTextCode += 'j '+ endfunctionLable +'\n'
                    mipsTextCode += checkt2Lable + ':\n'
                    mipsTextCode += 'bnez $t4, ' + missmatchLable + '\n'
                    mipsTextCode += 'addi $v0, $zero, 1\n'
                    mipsTextCode += 'add $v1, $zero, $zero\n'
                    mipsTextCode += endfunctionLable + ':\n'
                    if instruction[4] == 's==':
                        mipsTextCode += 'sw $v0, ' + instruction[1] + '\n'
                    if instruction[4] == 's!=':
                        mipsTextCode += 'sw $v1, ' + instruction[1] + '\n'
                if instruction[4][0] == 'b':
                    if not instruction[1] in vars.keys():
                        mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                        vars[instruction[1]] = 0
                    if instruction[4] == 'b==':#arith a = b b== c
                        mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                        mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                        mipsTextCode += 'seq $t3, $t1, $t2\n'
                        mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                    if instruction[4] == 'b!=':#arith a = b b!= c
                        mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                        mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                        mipsTextCode += 'sne $t3, $t1, $t2\n'
                        mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                    if instruction[4] == 'b!':#arith a = b b! // a = not(b)
                        mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                        mipsTextCode += 'li $t2, 1\n'
                        mipsTextCode += 'sub $t3, $t2, $t1\n'
                        mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                if not instruction[1] in vars.keys():
                    mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                    vars[instruction[1]] = 0
                if instruction[4] == '+':#add
                    if check_int(instruction[3]):
                        if instruction[3][0] == '-':
                            numberLable = '______'+instruction[3][1:]+'_____'
                        else:
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
                        if instruction[5][0] == '-':
                            numberLable = '______'+instruction[5][1:]+'_____'
                        else:
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
                        if instruction[3][0] == '-':
                            numberLable = '______'+instruction[3][1:]+'_____'
                        else:
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
                        if instruction[5][0] == '-':
                            numberLable = '______'+instruction[5][1:]+'_____'
                        else:
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
                    Arg1Is0Lable = '___Arg1Is0_' + str(myLableCount) + '___'
                    endOrOrLable = '___endOrOr_' + str(myLableCount) + '___'
                    Arg2IsAlso0Lable = '___Arg2IsAlso0_' + str(myLableCount) + '___'
                    myLableCount += 1
                    mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                    mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                    mipsTextCode += 'beqz $t1, ' + Arg1Is0Lable+ '\n'
                    mipsTextCode += 'li $t3, 1\nb '+endOrOrLable+'\n'
                    mipsTextCode += Arg1Is0Lable + ':\n'
                    mipsTextCode += 'beqz $t2, ' + Arg2IsAlso0Lable + '\n'
                    mipsTextCode += 'li $t3, 1\nb ' + endOrOrLable + '\n'
                    mipsTextCode += Arg2IsAlso0Lable + ':\n'
                    mipsTextCode += 'li $t3, 0\n' + endOrOrLable + ':\n'
                    mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
                if instruction[4] == '&&':#
                    Arg1Is1Lable = '___Arg1Is1_' + str(myLableCount) + '___'
                    endAndAndLable = '___endAndAnd_' + str(myLableCount) + '___'
                    Arg2IsAlso1Lable = '___Arg2IsAlso1_' + str(myLableCount) + '___'
                    myLableCount += 1
                    mipsTextCode += 'lw $t1, ' + instruction[3] + '\n'
                    mipsTextCode += 'lw $t2, ' + instruction[5] + '\n'
                    mipsTextCode += 'bnez $t1, ' + Arg1Is1Lable+ '\n'
                    mipsTextCode += 'li $t3, 0\nb '+endAndAndLable+'\n'
                    mipsTextCode += Arg1Is1Lable + ':\n'
                    mipsTextCode += 'bnez $t2, ' + Arg2IsAlso1Lable + '\n'
                    mipsTextCode += 'li $t3, 0\nb ' + endAndAndLable + '\n'
                    mipsTextCode += Arg2IsAlso1Lable + ':\n'
                    mipsTextCode += 'li $t3, 1\n' + endAndAndLable + ':\n'
                    mipsTextCode += 'sw $t3, ' + instruction[1] + '\n'
            elif instruction[2] == 'c=':#arith a c= xtoy b
                if not instruction[1] in vars.keys():
                    mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                    vars[instruction[1]] = 0
                if instruction[3] == 'itod':#arith ad c= itod bi
                    mipsTextCode += 'l.s $f9, ' + instruction[4]  +'\n'
                    mipsTextCode += 'cvt.s.w $f9, $f9\n'
                    mipsTextCode += 's.s $f9, ' + instruction[1]  +'\n'
                if instruction[3] == 'dtoi':#arith ai c= dtoi bd
                    mipsTextCode += 'l.s $f9, ' + instruction[4]  +'\n'
                    mipsTextCode += 'cvt.w.s $f9, $f9\n'
                    mipsTextCode += 's.s $f9, ' + instruction[1]  +'\n'
                if instruction[3] == 'itob':#arith ab c= itob bi
                    convertZeroLable = '____convertZero' + myLableCount + '____'
                    myLableCount += 1
                    convertEndLable = '____convertEnd' + myLableCount + '____'
                    myLableCount += 1
                    mipsTextCode += 'lw $t9, ' + instruction[4]  +'\n'
                    mipsTextCode += 'beq $t9, $zero, ' + convertZeroLable + '\n'
                    mipsTextCode += 'li $t9, 1\n'
                    mipsTextCode += 'b convertEndLable\n'
                    mipsTextCode += convertZeroLable + ':\n'
                    mipsTextCode += 'li $t9, 0\n'
                    mipsTextCode += convertEndLable + ':\n'
                    mipsTextCode += 'sw $t9, ' + instruction[1] + '\n'
                if instruction[3] == 'btoi':#arith ai c= btoi bb
                    mipsTextCode += 'lw $t9, ' + instruction[4] + '\n'
                    mipsTextCode += 'sw $t9, ' + instruction[1] + '\n'
        if len(instruction) == 1:#pushra or #popra or #a:
            if instruction[0] == 'pushra':#pushra
                mipsTextCode += 'addi $sp, $sp, -4\n'
                mipsTextCode += 'sw $ra, ($sp)\n'
            elif instruction[0] == 'popra':#popra
                mipsTextCode += 'lw $ra, ($sp)\n'
                mipsTextCode += 'addi $sp, $sp, 4\n'
            elif instruction[0] == 'Printe':#Printe
                mipsTextCode += 'li	$v0, 11\nli	$a0, 10\nsyscall\n'
            elif instruction[0] == 'return':
                mipsTextCode += 'jr $ra\n'
            else:#lable:
                if instruction[0] == 'main:':
                    mipsTextCode += '___main___:\nla $ra, _____EndOfWorld_____\n'
                else:
                    mipsTextCode += instruction[0] + '\n'
        if instruction[0] == 'push':#push a
            mipsTextCode += 'lw $t9, ' + instruction[1] + '\n'
            mipsTextCode += 'addi $sp, $sp, -4\n'
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
            printFalseLable = '____printFalse' + str(myLableCount) + '____'
            printTrueLable = '____printTrue' + str(myLableCount) + '____'
            printEndLable = '____printEnd' + str(myLableCount) + '____'
            myLableCount += 1
            mipsTextCode += 'beqz $t9, ' + printFalseLable + '\n'
            mipsTextCode += printTrueLable + ':\n'
            mipsTextCode += 'la $a0, ____true____\n'
            mipsTextCode += 'li $v0, 4\n'
            mipsTextCode += 'syscall\n'
            mipsTextCode += 'j ' + printEndLable + '\n'
            mipsTextCode += printFalseLable +':\n'
            mipsTextCode += 'la $a0, ____false____\n'
            mipsTextCode += 'li $v0, 4\n'
            mipsTextCode += 'syscall\n'
            mipsTextCode += printEndLable + ':\n'
        if instruction[0] == 'assign':
            if instruction[2] == 'f=':#assign a f= 1.2
                mipsDataCode += instruction[1] + ': ' + '.float ' + instruction[3] + '\n'
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
        if instruction[0] == 'ReadInt':#ReadInt t = ReadInt()
            if not instruction[1] in vars.keys():
                mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                vars[instruction[1]] = 0
            mipsTextCode += 'li	$v0, 5\nsyscall\nmove	$t9, $v0\n'
            mipsTextCode += 'sw $t9, ' + instruction[1] + '\n'
        if instruction[0] == 'ReadLine':#ReadLine t = ReadLine()
            if not instruction[1] in vars.keys():
                mipsDataCode += '___' + instruction[1] + '___: ' + '.space ' + str(MAX_SIZE) + '\n'
                mipsDataCode += instruction[1] + ': ' + '.word 0\n'
                vars['___' + instruction[1] + '___'] = 0
                vars[instruction[1]] = 0
                mipsTextCode += 'la $t9, ' + '___' + instruction[1] + '___\n'
                mipsTextCode += 'sw $t9, ' + instruction[1] + '\n'
            len_to_new_lineLable = '____len_to_new_line' + str(myLableCount) + '____'
            endofreadlineLable = '____endofreadline' + str(myLableCount) + '____'
            endfunctionLable = '____endfunction' + str(myLableCount) + '____'
            myLableCount += 1

            mipsTextCode += 'li	$v0, 8\nli	$a1, ' + str(MAX_SIZE) + '  #MAX_String_Read_SIZE==1000\nmove	$a0, $t9\nsyscall\n'
            mipsTextCode += len_to_new_lineLable + ':\n'
            mipsTextCode += 'lb $t2, ($a0)\n'
            mipsTextCode += 'li $t3, 10\n'
            mipsTextCode += 'beq $t2, $t3, ' + endofreadlineLable + '\n'
            mipsTextCode += 'addi $a0, $a0, 1\n'
            mipsTextCode += 'b ' + len_to_new_lineLable + '\n'
            mipsTextCode += endofreadlineLable + ':\n'
            mipsTextCode += 'sb $zero, ($a0)\n'
        if instruction[0] == 'jumpto':# jumpto lable
            mipsTextCode += 'j ' + instruction[1] + '\n'
        if instruction[0] == 'Ifz':#Ifz a goto lable
            mipsTextCode += 'lw $t9, ' + instruction[1] + '\n'
            mipsTextCode += 'beqz $t9, ' + instruction[3] + '\n'
    mipsTextCode += '_____EndOfWorld_____:\nli	$v0, 10\nsyscall\n'
    return  mipsDataCode + '\n' + mipsTextCode
