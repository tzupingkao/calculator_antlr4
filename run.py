import sys
from antlr4 import *
from Calculator.CalculatorLexer import CalculatorLexer
from Calculator.CalculatorParser import CalculatorParser
from Calculator.CalculatorVisitor import CalculatorVisitor


class CalcVisitor(CalculatorVisitor):
    def visitAtomExpr(self, ctx:CalculatorParser.AtomExprContext):
        return int(ctx.getText())

    def visitParenExpr(self, ctx:CalculatorParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitOpExpr(self, ctx:CalculatorParser.OpExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            if r == 0:
                print('divide by zero!')
                return 0
            return l / r



def calc(line) -> float:
    input_stream = InputStream(line)

    # lexing
    lexer = CalculatorLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # parsing
    parser = CalculatorParser(stream)
    tree = parser.expr()

    # use customized visitor to traverse AST
    visitor = CalcVisitor()
    return visitor.visit(tree)



if __name__ == '__main__':
    while True:
        print(">>> ", end='')
        line = input()
        print(calc(line))