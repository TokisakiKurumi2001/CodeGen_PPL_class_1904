from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class ASTGeneration(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program([FuncDecl(Id("main"),
                        [],
                        self.visit(ctx.mptype()),
                        Block([], [self.visit(ctx.body())] if ctx.body() else []))])

    def visitMptype(self, ctx: BKOOLParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        else:
            return VoidType()

    def visitBody(self, ctx: BKOOLParser.BodyContext):
        return self.visit(ctx.funcall())

    def visitFuncall(self, ctx: BKOOLParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self, ctx: BKOOLParser.ExpContext):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.LB():
            return ctx.exp().accept(self)
        else:
            op = ctx.getChild(1).getText()
            left = ctx.exp(0).accept(self)
            right = ctx.exp(1).accept(self)
            return BinaryOp(op, left, right)
