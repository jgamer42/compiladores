import unittest
import site
site.addsitedir("../")
from src.lexer import Lexer

class TestLexer(unittest.TestCase):
    def Test_number(self):
        l = Lexer()
        caso1 = False
        for token in l.tokenize("10"):
            if token.type == "NUMBER":
                caso1 = True
        self.assertAlmostEqual(caso1,True)
        self.assertAlmostEqual(False,True)