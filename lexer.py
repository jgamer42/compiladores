import sly
class Lexer(sly.Lexer):
    tokens = {
        #palabras resevadas
        IF,FOR,WHILE,FUNCTION,RETURN,END,NOT,BREAK,ELIF,OR,AND,CONTINUE,
        #operadores
        EQ,NE,LT,GT,LE,GE,
        #identificadores
        NAMES,
        #constantes
        NIL,NUMBER,TRUE,FALSE,STRING,BOOLEAN
    }
    literals = '+-*/(){}:'
    ignore = ' \t\r'
    ignore_newline = r'\n+'
    #PALABRAS RESERVADAS
    NAMES = r"[a-zA-Z_][a-zA-Z_\-0-9]*"
    NAMES["if"] = IF
    NAMES["for"] = FOR
    NAMES["while"] = WHILE
    NAMES["return"] = RETURN
    NAMES["end"] = END
    NAMES["not"] = NOT 
    NAMES["break"] = BREAK 
    NAMES["elif"] = ELIF
    NAMES["or"] = OR 
    NAMES["and"] = AND 
    NAMES["continue"] = CONTINUE
    #OPERADORES
    LE = r"<="
    LT = r"<"
    EQ = r"=="
    GE = r">="
    GT = r">"
    NE = r"!="

    def ignore_newline(self,t):
        self.lineno += t.value.count("\n")

    @_(r'\d+(\.\d+)?')
    def NUMBER(self,t):
        try:
            t.value = int(t.value)
        except ValueError:
            t.value = float(t.value)
        return t

    @_(r"'[^']*'",r'"[^"]"')
    def STRING(self,t):
        return t

    def error(self,t):
        print(f" Caracter es ilegal {t}")
        self.index += 1

def main():
    l = Lexer()
    while True:
        try:
            text = input("$ ")
            for tok in l.tokenize(text):
                print(tok)
        except EOFError:
            break
main()