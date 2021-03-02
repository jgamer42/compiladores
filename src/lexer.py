import sly
import site
site.addsitedir("../")
import sys
from errors.base import BaseError 
class Lexer(sly.Lexer):
    tokens = {
        #palabras resevadas
        IF,FOR,WHILE,DEF,DIM,RETURN,END,BREAK,CONTINUE,STOP,
        TO, STEP,NEXT,GOSUB,GOTO,THEN,LET,PRINT,DATA,READ,REM,
        #operadores
        EQ,NE,LT,GT,LE,GE,
        #identificadores
        NAMES,
        #constantes
       NUMBER,STRING
    }
    literals = '+-*/()^:,;='
    ignore = r' \t\r'

    #PALABRAS RESERVADAS
    NAMES = r"[a-zA-Z][a-zA-Z0-9]*"
    NAMES["IF"] = IF
    NAMES["FOR"] = FOR
    NAMES["WHILE"] = WHILE
    NAMES["RETURN"] = RETURN
    NAMES["END"] = END 
    NAMES["BREAK"] = BREAK 
    NAMES["CONTINUE"] = CONTINUE
    NAMES["DEF"] = DEF
    NAMES["DIM"] = DIM
    NAMES["STOP"] = STOP
    NAMES["TO"] = TO 
    NAMES["STEP"] = STEP
    NAMES["NEXT"] = NEXT
    NAMES["GOSUB"] = GOSUB
    NAMES["GOTO"] = GOTO
    NAMES["THEN"] = THEN
    NAMES["LET"] = LET 
    NAMES["PRINT"] = PRINT
    NAMES["DATA"] = DATA
    NAMES["READ"] = READ
    NAMES["REM"] = REM

    #OPERADORES
    LE = r"<="
    LT = r"<"
    EQ = r"="
    GE = r">="
    GT = r">"
    NE = r"<>"

    @_(r'-?(\d+(\.\d+)?(E-?\d+)?)',r'-?(\.\d+)(E-?\d+)?')
    def NUMBER(self,t):
        try:
            t.value = int(t.value)
        except ValueError:
            t.value = float(t.value)
        return t


    @_(r'"[^"]*"')
    def STRING(self,t):
        return t

    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count("\n")

    def error(self,t):
        print(f" Caracter es ilegal {t}")
        self.index += 1


#para correr el lexer con los datos que lee desde un archivo
def main_archivo():
	if len(sys.argv) != 2:
		print('uso: baslex.py filename')
		sys.exit(1)

	data = open(sys.argv[1]).read()

	lex = Lexer()
	for tok in lex.tokenize(data):
		print(tok)
        
#para probar el lexer manualmente
def main_consola():
    lex = Lexer()
    text = input()
    while True:
        for tok in lex.tokenize(text):
            print(tok)
        break

if __name__ == '__main__':
    #main_consola()
    main_archivo()