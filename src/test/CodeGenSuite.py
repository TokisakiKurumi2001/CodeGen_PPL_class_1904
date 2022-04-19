import unittest
from TestUtils import TestCodeGen, TestAST
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_int_ast(self):
        input = Program([
            FuncDecl(Id("main"), [], VoidType(), Block([], [
                CallExpr(Id("putInt"), [IntLiteral(5)])]))])
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_float_ast(self):
        input = """void main() {putFloatLn(10.0);}"""
        expect = "10.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_bin_ast_1(self):
        input = """void main() {putIntLn(10 + 1);}"""
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_bin_ast_2(self):
        input = """void main() {putFloatLn(10.0 + 1.5);}"""
        expect = "11.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
