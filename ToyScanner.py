import os
import sys
charClass = 0
lexeme=[]
nextChar = ''
lexLen = 0
token = 0
#Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99
#Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MUL_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1
nextToken = 0
seekval = 0
def addChar():
    #print "AddChar"
    global lexeme
    global nextChar
    if len(lexeme)<=98:
        lexeme.append(nextChar)
    else:
        print ("Error: lexeme is too long.")
        sys.exit(0)
    return 0


def getChar():
    #print "GetChar"
    global seekval
    global charClass
    with open("C:\Users\gani\Desktop\InputFile.txt","r") as f:
        global nextChar
        f.seek(seekval)
        nextChar = f.read(1)
        seekval+=1
        
        if nextChar<>EOF:
            if nextChar.isalpha():
                charClass = LETTER
            elif nextChar.isdigit():
                charClass = DIGIT
            else:
                charClass = UNKNOWN
        else:
            charClass = EOF

            
def getNonBlank():
    #print "getNonBlank"
    global nextChar
    while nextChar.isspace():
        getChar()

        
def lex():
    #print "Lex"
    global nextToken
    global nextChar
    #lexLen = 0
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()
        while (charClass == LETTER or charClass == DIGIT): 
            addChar()
            getChar()
            nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
            nextToken = IDENT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[0] = 'E'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = '\0'
    #global nextToken
    print ('Next token is : '+str(nextToken)+',Next lexeme is : '+''.join(lexeme))
    del lexeme[:]
    return nextToken


def lookup(ch):
    #print "LookUp"
    global nextToken
    global nextChar
    if ch=='(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MUL_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
        lexeme.append('EOF')
    return nextToken


def main():
    global EOF
    global nextToken
    global nextChar
    #print "Main"
    #cwd=[]
    if open("C:\Users\gani\Desktop\InputFile.txt","r"):
        getChar()
        #do-while logic
        while True:
            lex()
            if nextToken == EOF:
                break
main()
        
