# Generated from Calculator.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#AtomExpr.
    def enterAtomExpr(self, ctx:CalculatorParser.AtomExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#AtomExpr.
    def exitAtomExpr(self, ctx:CalculatorParser.AtomExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#ParenExpr.
    def enterParenExpr(self, ctx:CalculatorParser.ParenExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#ParenExpr.
    def exitParenExpr(self, ctx:CalculatorParser.ParenExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#OpExpr.
    def enterOpExpr(self, ctx:CalculatorParser.OpExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#OpExpr.
    def exitOpExpr(self, ctx:CalculatorParser.OpExprContext):
        pass



del CalculatorParser