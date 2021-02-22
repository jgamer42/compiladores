import sly

class Lexer(sly.Lexer):
    tokens = {
        NUMBER,
        FLOAT
    }
    literals = '+-*/()'
    ignore = ' \t\r'
    ignore_newline = r'\n+'

    def ignore_newline(self,t):
        self.lineno += t.value.count("\n")

    @_(r'\d+\.?|\d*\.\d+')
    def NUMBER(self,t):
        t.value = int(t.value)
        return t.value

    def FLOAT(self)

    def error(self,t):
        print("%s Caracter es ilegal '%s" % (t.lineno. t.value[0]))
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