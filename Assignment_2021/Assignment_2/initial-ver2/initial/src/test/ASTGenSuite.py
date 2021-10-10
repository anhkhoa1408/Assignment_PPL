import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_class_declare_1(self):
        """Simple program: class main {} """
        input = """
            class main {
                float a, b = 0.5E-10;
                int[10] b = {1, 2, 3};
                foo foo() {
                    for i:= 0 to 10 do
                        return a[b[3] + 2];
                }
            }
            class a {}
            """
        expect = "Program([ClassDecl(Id(main),[]),ClassDecl(Id(A),[]),ClassDecl(Id(B),Id(A),[]),ClassDecl(Id(C),[]),ClassDecl(Id(D),[])])"
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_declare_2(self):
        """Simple program: class main {} """
        input = """class main {

            
        }"""
        expect = "Program([ClassDecl(Id(main),[]),ClassDecl(Id(A),[]),ClassDecl(Id(B),Id(A),[]),ClassDecl(Id(C),[]),ClassDecl(Id(D),[])])"
        self.assertTrue(TestAST.test(input, expect, 301))

