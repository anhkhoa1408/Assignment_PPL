import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_decl_1(self):
        input = """
            class program {
                int a;
                int foo(int a) {
                    final Shape a = new Shape(3,4);
                }
            }
        """
        expect = "Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),MethodDecl(Id(foo),Instance,[param(Id(a),IntType)],IntType,Block([ConstDecl(Id(a),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(3),IntLit(4)]))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,301))

    def test_var_decl_2(self):
        input = """class program {
                int a, c, d, e, f;
            }"""
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(d),IntType)),AttributeDecl(Instance,VarDecl(Id(e),IntType)),AttributeDecl(Instance,VarDecl(Id(f),IntType))])])"""
        self.assertTrue(TestAST.test(input,expect,302))

    def test_var_decl_3(self):
        input = """class program {
                float a = 1 + 2 + 3;
            }"""
        expect = "Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))))])])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_var_decl_4(self):
        input = """class program {
                float a = 0, b = 1, c = 2, d = 10 + a;
            }"""
        expect = "Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,BinaryOp(+,IntLit(10),Id(a))))])])"
        self.assertTrue(TestAST.test(input,expect,304))
        
    def test_var_decl_5(self):
        input = """class program {
                int a;
                float b;
                string e = "abcdef", b, c, d = "";
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(e),StringType,StringLit("abcdef"))),AttributeDecl(Instance,VarDecl(Id(b),StringType)),AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Instance,VarDecl(Id(d),StringType,StringLit("")))])])"""
        self.assertTrue(TestAST.test(input,expect,305))

    def test_var_decl_6(self):
        input = """class program {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                string e = "abcdef", b, c, d = "";
                int[5] b = {123,45};
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType)),AttributeDecl(Instance,VarDecl(Id(d),FloatType)),AttributeDecl(Instance,VarDecl(Id(e),FloatType)),AttributeDecl(Instance,VarDecl(Id(f),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(g),FloatType,FloatLit(1.2e-09))),AttributeDecl(Instance,VarDecl(Id(e),StringType,StringLit("abcdef"))),AttributeDecl(Instance,VarDecl(Id(b),StringType)),AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Instance,VarDecl(Id(d),StringType,StringLit(""))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType),[IntLit(123),IntLit(45)]))])])"""
        self.assertTrue(TestAST.test(input,expect,306))

    def test_var_decl_7(self):
        input = """class program {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                string e = "abcdef", b, c, d = "";
                int[5] b = {123,45};
                float[2] d = {123, "'", 12345, "12", 0};
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType)),AttributeDecl(Instance,VarDecl(Id(d),FloatType)),AttributeDecl(Instance,VarDecl(Id(e),FloatType)),AttributeDecl(Instance,VarDecl(Id(f),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(g),FloatType,FloatLit(1.2e-09))),AttributeDecl(Instance,VarDecl(Id(e),StringType,StringLit("abcdef"))),AttributeDecl(Instance,VarDecl(Id(b),StringType)),AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Instance,VarDecl(Id(d),StringType,StringLit(""))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType),[IntLit(123),IntLit(45)])),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(2,FloatType),[IntLit(123),StringLit("'"),IntLit(12345),StringLit("12"),IntLit(0)]))])])"""
        self.assertTrue(TestAST.test(input,expect,307))
        
    def test_var_decl_8(self):
        input = """class program {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                string e = "abcdef", b, c, d = "";
                int[5] b = {123,45};
                float[2] d = {123, "'", 12345, "12", 0};
            }"""
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType)),AttributeDecl(Instance,VarDecl(Id(d),FloatType)),AttributeDecl(Instance,VarDecl(Id(e),FloatType)),AttributeDecl(Instance,VarDecl(Id(f),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(g),FloatType,FloatLit(1.2e-09))),AttributeDecl(Instance,VarDecl(Id(e),StringType,StringLit("abcdef"))),AttributeDecl(Instance,VarDecl(Id(b),StringType)),AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Instance,VarDecl(Id(d),StringType,StringLit(""))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType),[IntLit(123),IntLit(45)])),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(2,FloatType),[IntLit(123),StringLit("'"),IntLit(12345),StringLit("12"),IntLit(0)]))])])"""
        self.assertTrue(TestAST.test(input,expect,308))

    def test_var_decl_9(self):
        input = """class program {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                string e = "abcdef", b, c, d = "";
                int[5] b = {123,45};
                float[2] d = {123, "'", 12345, "12", 0};
                string[12] aeE = {"12", "0012321", 12E-5, 20e+8};
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType)),AttributeDecl(Instance,VarDecl(Id(d),FloatType)),AttributeDecl(Instance,VarDecl(Id(e),FloatType)),AttributeDecl(Instance,VarDecl(Id(f),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(g),FloatType,FloatLit(1.2e-09))),AttributeDecl(Instance,VarDecl(Id(e),StringType,StringLit("abcdef"))),AttributeDecl(Instance,VarDecl(Id(b),StringType)),AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Instance,VarDecl(Id(d),StringType,StringLit(""))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType),[IntLit(123),IntLit(45)])),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(2,FloatType),[IntLit(123),StringLit("'"),IntLit(12345),StringLit("12"),IntLit(0)])),AttributeDecl(Instance,VarDecl(Id(aeE),ArrayType(12,StringType),[StringLit("12"),StringLit("0012321"),FloatLit(0.00012),FloatLit(2000000000.0)]))])])"""
        self.assertTrue(TestAST.test(input,expect,309))

    def test_var_decl_10(self):
        input = """class program extends props {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                final string e = "abcdef", b, c, d = "";
                final int[5] b = {123,45};
                float[2] d = {123, "'", 12345, "12", 0};
                static final string[12] stringA = {"12", "0012321", 12E-5, 20e+8};
                /* This is a comment string[45] abd */
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = """Program([ClassDecl(Id(program),Id(props),[AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType)),AttributeDecl(Instance,VarDecl(Id(d),FloatType)),AttributeDecl(Instance,VarDecl(Id(e),FloatType)),AttributeDecl(Instance,VarDecl(Id(f),FloatType,FloatLit(5.0))),AttributeDecl(Instance,VarDecl(Id(g),FloatType,FloatLit(1.2e-09))),AttributeDecl(Instance,ConstDecl(Id(e),StringType,StringLit("abcdef"))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(c),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(d),StringType,StringLit(""))),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(5,IntType),[IntLit(123),IntLit(45)])),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(2,FloatType),[IntLit(123),StringLit("'"),IntLit(12345),StringLit("12"),IntLit(0)])),AttributeDecl(Static,ConstDecl(Id(stringA),ArrayType(12,StringType),[StringLit("12"),StringLit("0012321"),FloatLit(0.00012),FloatLit(2000000000.0)]))])])"""
        self.assertTrue(TestAST.test(input,expect,310))

    # Test method declare
    def test_method_decl_1(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                int func() {
                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(func),Instance,[],IntType,Block([],[]))])])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_method_decl_2(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                static int funcA() {
                }
                static int funcB() {
                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[],IntType,Block([],[])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[]))])])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_method_decl_3(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                static int funcA(int a; int b) {
                }
                static int funcB() {
                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[]))])])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_method_decl_4(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                static int funcA(int a; int b) {
                    return this.length;
                }
                static int funcB() {
                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[Return(FieldAccess(Self(),Id(length)))])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[]))])])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_method_decl_5(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                static int funcA(int a,b,c) {
                    return a*b+c;
                }
                static int funcB() {
                    a[3+x.foo(2)] := a[b] * 2;
                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],IntType,Block([],[Return(BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)))])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(*,ArrayCell(Id(a),Id(b)),IntLit(2)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_method_decl_6(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                static int funcA(int a,b,c) {
                    return a*b+c;
                }
                static int funcB() {
                    a[3+x.foo(2)] := a[b] * 2;
                }
                string func() {
                    this.a := 5;
                    this.a[0] := 1;
                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],IntType,Block([],[Return(BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)))])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(*,ArrayCell(Id(a),Id(b)),IntLit(2)))])),MethodDecl(Id(func),Instance,[],StringType,Block([],[AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),IntLit(0)),IntLit(1))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_method_decl_7(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                static int funcA(int a,b,c) {
                    return a*b+c;
                }
                static int funcB() {
                    a[3+x.foo(2)] := a[b] * 2;
                }
                string func() {
                    this.a := 5;
                    this.a[0] := 1;
                }
            }
            class program2 {
                static final int a = 0;
                program a = new program();
                int funcA() {

                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],IntType,Block([],[Return(BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)))])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(*,ArrayCell(Id(a),Id(b)),IntLit(2)))])),MethodDecl(Id(func),Instance,[],StringType,Block([],[AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),IntLit(0)),IntLit(1))]))]),ClassDecl(Id(program2),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(program)),NewExpr(Id(program),[]))),MethodDecl(Id(funcA),Instance,[],IntType,Block([],[]))])])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_method_decl_8(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                static int funcA(int a,b,c) {
                    return a*b+c;
                }
                static int funcB() {
                    a[3+x.foo(2)] := a[b] * 2;
                }
                string func() {
                    this.a := 5;
                    this.a[0] := 1;
                }
            }
            class program2 {
                static final int a = 0;
                program a = new program();
                int funcA() {
                    c := 5 * d - e + f /2000;
                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],IntType,Block([],[Return(BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)))])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(*,ArrayCell(Id(a),Id(b)),IntLit(2)))])),MethodDecl(Id(func),Instance,[],StringType,Block([],[AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),IntLit(0)),IntLit(1))]))]),ClassDecl(Id(program2),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(program)),NewExpr(Id(program),[]))),MethodDecl(Id(funcA),Instance,[],IntType,Block([],[AssignStmt(Id(c),BinaryOp(+,BinaryOp(-,BinaryOp(*,IntLit(5),Id(d)),Id(e)),BinaryOp(/,Id(f),IntLit(2000))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_method_decl_9(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                static int funcA(int a,b,c) {
                    return a*b+c;
                }
                static int funcB() {
                    a[3+x.foo(2)] := a[b] * 2;
                }
                string func() {
                    this.a := 5;
                    this.a[0] := 1;
                }
            }

            class program2 {
                static final int a = 0;
                program a = new program();
                int funcA() {
                    c := 5 * d - e + f /2000;
                }
            }

            class program3 {
                static final int a = 0;
                program a = new program();
                int funcA() {
                    c := 5 * d - e + f /2000;
                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],IntType,Block([],[Return(BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)))])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(*,ArrayCell(Id(a),Id(b)),IntLit(2)))])),MethodDecl(Id(func),Instance,[],StringType,Block([],[AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),IntLit(0)),IntLit(1))]))]),ClassDecl(Id(program2),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(program)),NewExpr(Id(program),[]))),MethodDecl(Id(funcA),Instance,[],IntType,Block([],[AssignStmt(Id(c),BinaryOp(+,BinaryOp(-,BinaryOp(*,IntLit(5),Id(d)),Id(e)),BinaryOp(/,Id(f),IntLit(2000))))]))]),ClassDecl(Id(program3),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(program)),NewExpr(Id(program),[]))),MethodDecl(Id(funcA),Instance,[],IntType,Block([],[AssignStmt(Id(c),BinaryOp(+,BinaryOp(-,BinaryOp(*,IntLit(5),Id(d)),Id(e)),BinaryOp(/,Id(f),IntLit(2000))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_method_decl_10(self):
        input = """
            class program {
                static final int a = 0;
                float b = 0;
                static int funcA(int a,b,c) {
                    return a*b+c;
                }
                static int funcB() {
                    a[3+x.foo(2)] := a[b] * 2;
                }
                string func() {
                    this.a := 5;
                    this.a[0] := 1;
                }
            }

            class program2 {
                static final int a = 0;
                program a = new program();
                int funcA() {
                    c := 5 * d - e + f /2000;
                }
            }

            class program3 {
                static final int a = 0;
                program a = new program();
                program3(string a,c,c; float e,f,g) {
                    a := b * f / g;
                }
            }
            """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],IntType,Block([],[Return(BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)))])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(*,ArrayCell(Id(a),Id(b)),IntLit(2)))])),MethodDecl(Id(func),Instance,[],StringType,Block([],[AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),IntLit(0)),IntLit(1))]))]),ClassDecl(Id(program2),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(program)),NewExpr(Id(program),[]))),MethodDecl(Id(funcA),Instance,[],IntType,Block([],[AssignStmt(Id(c),BinaryOp(+,BinaryOp(-,BinaryOp(*,IntLit(5),Id(d)),Id(e)),BinaryOp(/,Id(f),IntLit(2000))))]))]),ClassDecl(Id(program3),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(program)),NewExpr(Id(program),[]))),MethodDecl(Id(program3),Instance,[param(Id(a),StringType),param(Id(c),StringType),param(Id(c),StringType),param(Id(e),FloatType),param(Id(f),FloatType),param(Id(g),FloatType)],Block([],[AssignStmt(Id(a),BinaryOp(/,BinaryOp(*,Id(b),Id(f)),Id(g)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    # Test assign statement
    def test_assign_1(self):
        input = """
        class program {
            int a = 0;
            int b = nil;
            float c = 0;
            int func(int a, b; float c) {
                a := b + c * this.c;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType,NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(0))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],IntType,Block([],[AssignStmt(Id(a),BinaryOp(+,Id(b),BinaryOp(*,Id(c),FieldAccess(Self(),Id(c)))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_assign_2(self):
        input = """
        class program {
            int a = 0;
            int b = 0;
            float c = 0;
            int func(int a, b; float c) {
                float d,e;
                a := b + c * this.c;
                d := 0;
                e := 0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(0))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],IntType,Block([VarDecl(Id(d),FloatType),VarDecl(Id(e),FloatType)],[AssignStmt(Id(a),BinaryOp(+,Id(b),BinaryOp(*,Id(c),FieldAccess(Self(),Id(c))))),AssignStmt(Id(d),IntLit(0)),AssignStmt(Id(e),IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_assign_3(self):
        input = """
        class program {
            int a = 0;
            int b = 0;
            float c = 0;
            int func(int a, b; float c) {

            }
        }
        """
        expect = "Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(0))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],IntType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_assign_4(self):
        input = """
        class program {
            int a = 0;
            int b = 0;
            float c = 0;
            int func(int a, b; float c) {
                string e;
                final float[1] arr;
                arr[2 + this.foo(2)] := 0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(0))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],IntType,Block([VarDecl(Id(e),StringType),ConstDecl(Id(arr),ArrayType(1,FloatType),None)],[AssignStmt(ArrayCell(Id(arr),BinaryOp(+,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(2)]))),IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_assign_5(self):
        input = """
        class program {
            int a = 0;
            int b = 0;
            float c = 0;
            int func(int a, b; float c) {
                string e;
                final float[1] arr;
                float f;
                arr[2 + this.foo(2)] := 0;
                e := "avc" ^ "jlacsjl";
                f := 12E10 - 20.0003;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(0))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],IntType,Block([VarDecl(Id(e),StringType),ConstDecl(Id(arr),ArrayType(1,FloatType),None),VarDecl(Id(f),FloatType)],[AssignStmt(ArrayCell(Id(arr),BinaryOp(+,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(2)]))),IntLit(0)),AssignStmt(Id(e),BinaryOp(^,StringLit("avc"),StringLit("jlacsjl"))),AssignStmt(Id(f),BinaryOp(-,FloatLit(120000000000.0),FloatLit(20.0003)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_assign_6(self):
        input = """
        class program {
            int a = 0;
            int b = 0;
            float c = 0;
            int func(int a, b; float c) {
                string e;
                final float[1] arr;
                float f;
                arr[2 + this.foo(2)] := 0;
                e := "avc" ^ "jlacsjl";
                f := 12E10 - 20.0003;

            }
        }

        class program2 {
            int program(int a, b; float c; program a) {
                a := new program();
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(0))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],IntType,Block([VarDecl(Id(e),StringType),ConstDecl(Id(arr),ArrayType(1,FloatType),None),VarDecl(Id(f),FloatType)],[AssignStmt(ArrayCell(Id(arr),BinaryOp(+,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(2)]))),IntLit(0)),AssignStmt(Id(e),BinaryOp(^,StringLit("avc"),StringLit("jlacsjl"))),AssignStmt(Id(f),BinaryOp(-,FloatLit(120000000000.0),FloatLit(20.0003)))]))]),ClassDecl(Id(program2),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType),param(Id(a),ClassType(Id(program)))],IntType,Block([],[AssignStmt(Id(a),NewExpr(Id(program),[]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_assign_7(self):
        input = """
        class program {
            int a = 0;
            int b = 0;
            float c = 0;
            int func(int a, b; float c) {
                string e;
                final float[1] arr;
                float f;
                arr[2 + this.foo(2)] := 0;
                e := "avc" ^ "jlacsjl";
                f := 12E10 - 20.0003;

            }
        }

        class program2 {
            int program(int a, b; float c; program a) {
                a := new program();
            }
        }

        class program3 {
            program2 test = new program2();
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(0))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],IntType,Block([VarDecl(Id(e),StringType),ConstDecl(Id(arr),ArrayType(1,FloatType),None),VarDecl(Id(f),FloatType)],[AssignStmt(ArrayCell(Id(arr),BinaryOp(+,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(2)]))),IntLit(0)),AssignStmt(Id(e),BinaryOp(^,StringLit("avc"),StringLit("jlacsjl"))),AssignStmt(Id(f),BinaryOp(-,FloatLit(120000000000.0),FloatLit(20.0003)))]))]),ClassDecl(Id(program2),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType),param(Id(a),ClassType(Id(program)))],IntType,Block([],[AssignStmt(Id(a),NewExpr(Id(program),[]))]))]),ClassDecl(Id(program3),[AttributeDecl(Instance,VarDecl(Id(test),ClassType(Id(program2)),NewExpr(Id(program2),[])))])])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_assign_8(self):
        input = """
        class program {
            int a = 0;
            int b = 0;
            float c = 0;
            int func(int a, b; float c) {
                string e;
                final float[1] arr;
                float f;
                arr[2 + this.foo(2)] := 0;
                e := "avc" ^ "jlacsjl";
                f := 12E10 - 20.0003;

            }
        }

        class program2 {
            int program(int a, b; float c; program a) {
                a := new program();
            }
        }

        class program3 {
            program2 test = new program2();
            program2 testfunc(program test) {
                a[b[2] + c] := 0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(0))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],IntType,Block([VarDecl(Id(e),StringType),ConstDecl(Id(arr),ArrayType(1,FloatType),None),VarDecl(Id(f),FloatType)],[AssignStmt(ArrayCell(Id(arr),BinaryOp(+,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(2)]))),IntLit(0)),AssignStmt(Id(e),BinaryOp(^,StringLit("avc"),StringLit("jlacsjl"))),AssignStmt(Id(f),BinaryOp(-,FloatLit(120000000000.0),FloatLit(20.0003)))]))]),ClassDecl(Id(program2),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType),param(Id(a),ClassType(Id(program)))],IntType,Block([],[AssignStmt(Id(a),NewExpr(Id(program),[]))]))]),ClassDecl(Id(program3),[AttributeDecl(Instance,VarDecl(Id(test),ClassType(Id(program2)),NewExpr(Id(program2),[]))),MethodDecl(Id(testfunc),Instance,[param(Id(test),ClassType(Id(program)))],ClassType(Id(program2)),Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,ArrayCell(Id(b),IntLit(2)),Id(c))),IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_assign_9(self):
        input = """
        class program {
            program() {
                a[b[2] + c] := 0;
                c[2 * this.foo(3) + x.g(2)] := 0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[],Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,ArrayCell(Id(b),IntLit(2)),Id(c))),IntLit(0)),AssignStmt(ArrayCell(Id(c),BinaryOp(+,BinaryOp(*,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(3)])),CallExpr(Id(x),Id(g),[IntLit(2)]))),IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_assign_10(self):
        input = """
        class program {
            program() {
                a[b[2] + c] := 0;
                c[2 * this.foo(3) + x.g(2)] := b[ab[2] * 5 + 10];
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[],Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,ArrayCell(Id(b),IntLit(2)),Id(c))),IntLit(0)),AssignStmt(ArrayCell(Id(c),BinaryOp(+,BinaryOp(*,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(3)])),CallExpr(Id(x),Id(g),[IntLit(2)]))),ArrayCell(Id(b),BinaryOp(+,BinaryOp(*,ArrayCell(Id(ab),IntLit(2)),IntLit(5)),IntLit(10))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    # Test if statement
    def test_if_1(self):
        input = """
        class program {
            int func(int a,b) {
                if a == 0 then
                    b := b + 1;

            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_if_2(self):
        input = """
        class program {
            int func(int a,b) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                if d == 0 then
                    d := d * b;
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a)))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(d),BinaryOp(*,Id(d),Id(b))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_if_3(self):
        input = """
        class program {
            int func(int a,b) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                if d == 0 then
                    d := d * b;
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a)))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(d),BinaryOp(*,Id(d),Id(b))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_if_4(self):
        input = """
        class program {
            int func(int a,b) {
                if a == 0 then
                    b := b + 1;
                    c := c + 2;
                if b == 0 then
                    b := b - a;
                if d == 0 then
                    d := d * b;
                else
                    f := a[2] + 5;
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),AssignStmt(Id(c),BinaryOp(+,Id(c),IntLit(2))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a)))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(d),BinaryOp(*,Id(d),Id(b))),AssignStmt(Id(f),BinaryOp(+,ArrayCell(Id(a),IntLit(2)),IntLit(5))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_if_5(self):
        input = """
        class program {
            int func(int a,b; string c,d) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                else
                    c := d - 5 * 9 % 3;
                if d == 0 then
                    d := d * b;
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),StringType),param(Id(d),StringType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a))),AssignStmt(Id(c),BinaryOp(-,Id(d),BinaryOp(%,BinaryOp(*,IntLit(5),IntLit(9)),IntLit(3))))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(d),BinaryOp(*,Id(d),Id(b))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_if_6(self):
        input = """
        class program {
            int func(int a,b; string c,d) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                else
                    c := d - 5 * 9 % 3;
                if d == 0 then
                    for i := 0 to 10 do
                        i := i - 1;
                else return 0;
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),StringType),param(Id(d),StringType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a))),AssignStmt(Id(c),BinaryOp(-,Id(d),BinaryOp(%,BinaryOp(*,IntLit(5),IntLit(9)),IntLit(3))))),If(BinaryOp(==,Id(d),IntLit(0)),For(Id(i),IntLit(0),IntLit(10),True,AssignStmt(Id(i),BinaryOp(-,Id(i),IntLit(1)))]),Return(IntLit(0)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_if_7(self):
        input = """
        class program {
            int func(int a,b; string c,d) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                else
                    c := d - 5 * 9 % 3;
                if d == 0 then
                    a := 0;
                    d := d * b;
                    c := c ^ d;
                    e := e * f;
                    g := g + h;   
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),StringType),param(Id(d),StringType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a))),AssignStmt(Id(c),BinaryOp(-,Id(d),BinaryOp(%,BinaryOp(*,IntLit(5),IntLit(9)),IntLit(3))))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(a),IntLit(0))),AssignStmt(Id(d),BinaryOp(*,Id(d),Id(b))),AssignStmt(Id(c),BinaryOp(^,Id(c),Id(d))),AssignStmt(Id(e),BinaryOp(*,Id(e),Id(f))),AssignStmt(Id(g),BinaryOp(+,Id(g),Id(h)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_if_8(self):
        input = """
        class program {
            int func(int a,b; string c,d) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                else
                    c := d - 5 * 9 % 3;
                if d == 0 then
                    a := 0;
                else
                    for i : = 1000 downto 10 do
                        x[a[bc[2]]] := c * 9 && 1;
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),StringType),param(Id(d),StringType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a))),AssignStmt(Id(c),BinaryOp(-,Id(d),BinaryOp(%,BinaryOp(*,IntLit(5),IntLit(9)),IntLit(3))))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(a),IntLit(0)),For(Id(i),IntLit(1000),IntLit(10),False,AssignStmt(ArrayCell(Id(x),ArrayCell(Id(a),ArrayCell(Id(bc),IntLit(2)))),BinaryOp(&&,BinaryOp(*,Id(c),IntLit(9)),IntLit(1)))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_if_9(self):
        input = """
        class program {
            int func(int a,b; string c,d) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                else
                    c := d - 5 * 9 % 3;
                if d == 0 then
                    a := 0;
                else
                    c := 12E-8 + 5;
                if a == b / 2 * 5 then
                    c := c - 1;
                else
                    c := c % a;
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),StringType),param(Id(d),StringType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a))),AssignStmt(Id(c),BinaryOp(-,Id(d),BinaryOp(%,BinaryOp(*,IntLit(5),IntLit(9)),IntLit(3))))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(c),BinaryOp(+,FloatLit(1.2e-07),IntLit(5)))),If(BinaryOp(==,Id(a),BinaryOp(*,BinaryOp(/,Id(b),IntLit(2)),IntLit(5))),AssignStmt(Id(c),BinaryOp(-,Id(c),IntLit(1))),AssignStmt(Id(c),BinaryOp(%,Id(c),Id(a))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_if_10(self):
        input = """
        class program {
            int func(int a,b; string c,d) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                else
                    c := d - 5 * 9 % 3;
                if d == 0 then
                    a := 0;
                else
                    c := 0;
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),StringType),param(Id(d),StringType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a))),AssignStmt(Id(c),BinaryOp(-,Id(d),BinaryOp(%,BinaryOp(*,IntLit(5),IntLit(9)),IntLit(3))))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(c),IntLit(0)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 340))
        
# Test for statement
    def test_for_1(self):
        input = """
        class program {
            program(int a, b, c; string d) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    b := b + (a + d);
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,AssignStmt(Id(b),BinaryOp(+,Id(b),BinaryOp(+,Id(a),Id(d))))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_for_2(self):
        input = """
        class program {
            program(int a, b, c; string d) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    b := b + 1;
                for b := 10 downto 3 do
                    a := a * b % a;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))]),For(Id(b),IntLit(10),IntLit(3),False,AssignStmt(Id(a),BinaryOp(%,BinaryOp(*,Id(a),Id(b)),Id(a)))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_for_3(self):
        input = """
        class program {
            program(int a, b, c; string d) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    if a % 2 then
                        b := b + 2;
                    else 
                        b := b * 2;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,If(BinaryOp(%,Id(a),IntLit(2)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(2))),AssignStmt(Id(b),BinaryOp(*,Id(b),IntLit(2))))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_for_4(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    if a % 2 then
                        if b == 0 then
                            a := a * b;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,If(BinaryOp(%,Id(a),IntLit(2)),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(a),BinaryOp(*,Id(a),Id(b)))))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_for_5(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    if a % 2 then
                        if b == 0 then
                            if e == true then
                                e := false;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,If(BinaryOp(%,Id(a),IntLit(2)),If(BinaryOp(==,Id(b),IntLit(0)),If(BinaryOp(==,Id(e),BooleanLit(True)),AssignStmt(Id(e),BooleanLit(False)))))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_for_6(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 15 downto 1 do
                        for c := 0 downto -10 do
                            if c == 0 then
                                c := 1;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(15),IntLit(1),False,For(Id(c),IntLit(0),UnaryOp(-,IntLit(10)),False,If(BinaryOp(==,Id(c),IntLit(0)),AssignStmt(Id(c),IntLit(1)))])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_for_7(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 15 downto 1 do
                        for c := 0 downto -10 do
                            if c == 0 then
                                if d == "" then
                                    if e == false then
                                        d := d ^ "abc";
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(15),IntLit(1),False,For(Id(c),IntLit(0),UnaryOp(-,IntLit(10)),False,If(BinaryOp(==,Id(c),IntLit(0)),If(BinaryOp(==,Id(d),StringLit("")),If(BinaryOp(==,Id(e),BooleanLit(False)),AssignStmt(Id(d),BinaryOp(^,Id(d),StringLit("abc"))))))])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_for_8(self):
        input = """
        class a extends b {
        program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 15 downto 1 do
                        for c := 0 downto -10 do
                            if c == 0 then
                                c := c + 3;
                            else
                                if d == "" then
                                    if e == false then
                                        d := d ^ "abc";
                                    else
                                        c := 1;
            }
        }
        """
        expect = """Program([ClassDecl(Id(a),Id(b),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(15),IntLit(1),False,For(Id(c),IntLit(0),UnaryOp(-,IntLit(10)),False,If(BinaryOp(==,Id(c),IntLit(0)),AssignStmt(Id(c),BinaryOp(+,Id(c),IntLit(3))),If(BinaryOp(==,Id(d),StringLit("")),If(BinaryOp(==,Id(e),BooleanLit(False)),AssignStmt(Id(d),BinaryOp(^,Id(d),StringLit("abc"))),AssignStmt(Id(c),IntLit(1)))))])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_for_9(self):
        input = """
        class a extends b {
            program(int a, b, c; string d; boolean e) {
                    a := 0;
                    b := 0;
                    for a := 5 to 10 do 
                        for b := 15 downto 1 do
                            for c := 0 downto -10 do
                                if c == 0 then
                                    c := c + 3;
                                else
                                    if d == "" then
                                        if e == false then
                                            d := d ^ "abc";
                                        else
                                            for i := 1 downto 0 do
                                                c[a[b + i[2]]] := 5;
                                    
            }
        }
        """
        expect = """Program([ClassDecl(Id(a),Id(b),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(15),IntLit(1),False,For(Id(c),IntLit(0),UnaryOp(-,IntLit(10)),False,If(BinaryOp(==,Id(c),IntLit(0)),AssignStmt(Id(c),BinaryOp(+,Id(c),IntLit(3))),If(BinaryOp(==,Id(d),StringLit("")),If(BinaryOp(==,Id(e),BooleanLit(False)),AssignStmt(Id(d),BinaryOp(^,Id(d),StringLit("abc"))),For(Id(i),IntLit(1),IntLit(0),False,AssignStmt(ArrayCell(Id(c),ArrayCell(Id(a),BinaryOp(+,Id(b),ArrayCell(Id(i),IntLit(2))))),IntLit(5))]))))])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_for_10(self):
        input = """
        class a extends b {
            program(int a, b, c; string d; boolean e) {
                    a := 0;
                    b := 0;
                    for a := 5 to 10 do 
                        for b := 15 downto 1 do
                            for c := 0 downto -10 do
                                if c == 0 then
                                    c := c + 3;
                                else
                                    if d == "" then
                                        if e == false then
                                            d := d ^ "abc";
                                        else
                                            for i := 1 downto 0 do
                                                c[a[b + i[2]]] := 5;
            }

            void foo() {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 15 downto 1 do
                        for c := 0 downto -10 do
                            if c == 0 then
                                c := c + 3;
                            else 
                                return this.foo(a, b, c, a + 2, a && x);
            }
        }
        """
        expect = """Program([ClassDecl(Id(a),Id(b),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(15),IntLit(1),False,For(Id(c),IntLit(0),UnaryOp(-,IntLit(10)),False,If(BinaryOp(==,Id(c),IntLit(0)),AssignStmt(Id(c),BinaryOp(+,Id(c),IntLit(3))),If(BinaryOp(==,Id(d),StringLit("")),If(BinaryOp(==,Id(e),BooleanLit(False)),AssignStmt(Id(d),BinaryOp(^,Id(d),StringLit("abc"))),For(Id(i),IntLit(1),IntLit(0),False,AssignStmt(ArrayCell(Id(c),ArrayCell(Id(a),BinaryOp(+,Id(b),ArrayCell(Id(i),IntLit(2))))),IntLit(5))]))))])])])])),MethodDecl(Id(foo),Instance,[],VoidType,Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(15),IntLit(1),False,For(Id(c),IntLit(0),UnaryOp(-,IntLit(10)),False,If(BinaryOp(==,Id(c),IntLit(0)),AssignStmt(Id(c),BinaryOp(+,Id(c),IntLit(3))),Return(CallExpr(Self(),Id(foo),[Id(a),Id(b),Id(c),BinaryOp(+,Id(a),IntLit(2)),BinaryOp(&&,Id(a),Id(x))])))])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    # Test break statement
    def test_break_1(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    break;
            }
        }
        """
        expect = "Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,Break])]))])])"
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_break_2(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        break;
            }
        }
        """
        expect = "Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,Break])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_break_3(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        for b := 5 to 10 do 
                            if (a == 0) && (b == 0) && (c <= 0) then
                                x := x + 1;
                            else
                                break; 
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,If(BinaryOp(&&,BinaryOp(&&,BinaryOp(==,Id(a),IntLit(0)),BinaryOp(==,Id(b),IntLit(0))),BinaryOp(<=,Id(c),IntLit(0))),AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(1))),Break)])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_break_4(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        for b := 5 to 10 do 
                            for c := 15 downto 10 do 
                                break;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,For(Id(c),IntLit(15),IntLit(10),False,Break])])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_break_5(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    break;
            }
        }

        class program1 extends program {
            program1(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    break;
                for a := 0 downto -14 do
                    break;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,Break])]))]),ClassDecl(Id(program1),Id(program),[MethodDecl(Id(program1),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,Break]),For(Id(a),IntLit(0),UnaryOp(-,IntLit(14)),False,Break])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    # Test continue statement

    def test_continue_1(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        continue;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,Continue])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_continue_2(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        for c := 10 to 15 do
                            continue;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,For(Id(c),IntLit(10),IntLit(15),True,Continue])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_continue_3(self):
        input = """
        class program {
            program() {
                a := a != 0 && b;
                break;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[],Block([],[AssignStmt(Id(a),BinaryOp(!=,Id(a),BinaryOp(&&,IntLit(0),Id(b)))),Break]))])])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_continue_4(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                for a := 5 to 10 do 
                    if c == 12 then
                        continue;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[For(Id(a),IntLit(5),IntLit(10),True,If(BinaryOp(==,Id(c),IntLit(12)),Continue)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_continue_5(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    continue;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,Continue])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    # Test return statement

    def test_return_1(self):
        input = """
        class program {
            program() {
                return a[b[2]] + 3;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[],Block([],[Return(BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_return_2(self):
        input = """
        class program {
            program() {
                return a[b[2]]*a[b]+this.length;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[],Block([],[Return(BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),ArrayCell(Id(a),Id(b))),FieldAccess(Self(),Id(length))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_return_3(self):
        input = """
        class program {
            program() {
                return a[b[2]]*a[b]+this.length+this.width / 2 * x.foo(3,4,5);
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[],Block([],[Return(BinaryOp(+,BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),ArrayCell(Id(a),Id(b))),FieldAccess(Self(),Id(length))),BinaryOp(*,BinaryOp(/,FieldAccess(Self(),Id(width)),IntLit(2)),CallExpr(Id(x),Id(foo),[IntLit(3),IntLit(4),IntLit(5)]))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_return_4(self):
        input = """
        class program {
            string func() {
                return "";
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[],StringType,Block([],[Return(StringLit(""))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_return_5(self):
        input = """
        class program {
            static void foo() {
                return this.a[2];
            }
        } 
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(foo),Static,[],VoidType,Block([],[Return(ArrayCell(FieldAccess(Self(),Id(a)),IntLit(2)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_return_6(self):
        input = """
        class program {
            program() {
                return a[b[2]]*a[b]+this.length+this.width / 2 * x.foo(a,b,c,d) + this.foo(2,3,4);
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[],Block([],[Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),ArrayCell(Id(a),Id(b))),FieldAccess(Self(),Id(length))),BinaryOp(*,BinaryOp(/,FieldAccess(Self(),Id(width)),IntLit(2)),CallExpr(Id(x),Id(foo),[Id(a),Id(b),Id(c),Id(d)]))),CallExpr(Self(),Id(foo),[IntLit(2),IntLit(3),IntLit(4)])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_return_7(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    return a[b[c[2]]] + 3;
                return -1 && -2;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,Return(BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),ArrayCell(Id(c),IntLit(2)))),IntLit(3)))]),Return(BinaryOp(&&,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_return_8(self):
        input = """
        class program {
            void program(int a, b, c; string d; boolean e) {
                return a && "c" || d != e;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],VoidType,Block([],[Return(BinaryOp(!=,BinaryOp(||,BinaryOp(&&,Id(a),StringLit("c")),Id(d)),Id(e)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_return_9(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    if b == 0 then
                        return a[b[c[2]]] + 3;
                    else
                        return a[b + x.foo(a)] + 3;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(program),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),StringType),param(Id(e),BoolType)],Block([],[AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),IntLit(0)),For(Id(a),IntLit(5),IntLit(10),True,If(BinaryOp(==,Id(b),IntLit(0)),Return(BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),ArrayCell(Id(c),IntLit(2)))),IntLit(3))),Return(BinaryOp(+,ArrayCell(Id(a),BinaryOp(+,Id(b),CallExpr(Id(x),Id(foo),[Id(a)]))),IntLit(3))))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_return_10(self):
        input = """
        class program {
            foo() {
                b.a := 5;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(foo),Instance,[],Block([],[AssignStmt(FieldAccess(Id(b),Id(a)),IntLit(5))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    # Test random
    def test_random_1(self):
        input = """
        class program {
                   
        }

        class program1 {

        }
        class program2 {

        }
        """
        expect = """Program([ClassDecl(Id(program),[]),ClassDecl(Id(program1),[]),ClassDecl(Id(program2),[])])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_random_2(self):
        input = """
        class program {
            int[2] a = {5, 5};
            string[2] b = {"", " "};
            float[2] a = {5E10, 22E9, 5.5};


        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(2,IntType),[IntLit(5),IntLit(5)])),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(2,StringType),[StringLit(""),StringLit(" ")])),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(2,FloatType),[FloatLit(50000000000.0),FloatLit(22000000000.0),FloatLit(5.5)]))])])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_random_3(self):
        input = """
        class program {
            program a = this.a;
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(program)),FieldAccess(Self(),Id(a))))])])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_random_4(self):
        input = """
        class program {
            final int b = a[x] + 12 - 4 * 5 / 23 ^ "c" || x;
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(||,BinaryOp(-,BinaryOp(+,ArrayCell(Id(a),Id(x)),IntLit(12)),BinaryOp(/,BinaryOp(*,IntLit(4),IntLit(5)),BinaryOp(^,IntLit(23),StringLit("c")))),Id(x))))])])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_random_5(self):
        input = """
        class program {
            boolean[2] b = {true, false};
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Instance,VarDecl(Id(b),ArrayType(2,BoolType),[BooleanLit(True),BooleanLit(False)]))])])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_random_6(self):
        input = """
        class program {
            void func(int a,b) {
                return a == b % 2;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType)],VoidType,Block([],[Return(BinaryOp(==,Id(a),BinaryOp(%,Id(b),IntLit(2))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_random_7(self):
        input = """
        class program {
            void func(int a,b,c,d) {
                if a == b + c then
                    for d := 0 to 10 do 
                        c := c + 1;
                else
                    for d := 0 to 10 do 
                        c := c - 1;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType)],VoidType,Block([],[If(BinaryOp(==,Id(a),BinaryOp(+,Id(b),Id(c))),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(+,Id(c),IntLit(1)))]),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(-,Id(c),IntLit(1)))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_random_8(self):
        input = """
        class program {
            void func(int a,b,c,d) {
                if a == b + c then
                    for d := 0 to 10 do 
                        c := c + 1 / 3 % d;
                else
                    for d := 0 to 10 do 
                        c := c - 1 * 2018E+10;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType)],VoidType,Block([],[If(BinaryOp(==,Id(a),BinaryOp(+,Id(b),Id(c))),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(+,Id(c),BinaryOp(%,BinaryOp(/,IntLit(1),IntLit(3)),Id(d))))]),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(-,Id(c),BinaryOp(*,IntLit(1),FloatLit(20180000000000.0))))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_random_9(self):
        input = """
        class program {
            void func(int a,b,c,d) {
                if a == b + c then
                    for d := 0 to 10 do 
                        c := c + 1 / 3 % d;
                else
                    for d := 0 to 10 do 
                        c := c - 1 * 2018E+10;
            }
            void func2(string e, f) {
                return e ^ f ^ "c" ^ "";
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType)],VoidType,Block([],[If(BinaryOp(==,Id(a),BinaryOp(+,Id(b),Id(c))),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(+,Id(c),BinaryOp(%,BinaryOp(/,IntLit(1),IntLit(3)),Id(d))))]),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(-,Id(c),BinaryOp(*,IntLit(1),FloatLit(20180000000000.0))))]))])),MethodDecl(Id(func2),Instance,[param(Id(e),StringType),param(Id(f),StringType)],VoidType,Block([],[Return(BinaryOp(^,BinaryOp(^,BinaryOp(^,Id(e),Id(f)),StringLit("c")),StringLit("")))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_random_10(self):
        input = """
        class program {
            void func(int a,b,c,d) {
                if a == b + c then
                    for d := 0 to 10 do 
                        c := c + 1 / 3 % d;
                else
                    for d := 0 to 10 do 
                        c := c - 1 * 2018E+10;
            }
            void func2(string e, f) {
                return e ^ f ^ "c" ^ "";
            }
            boolean func3(boolean g, h) {
                h := false;
                return g == true;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType)],VoidType,Block([],[If(BinaryOp(==,Id(a),BinaryOp(+,Id(b),Id(c))),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(+,Id(c),BinaryOp(%,BinaryOp(/,IntLit(1),IntLit(3)),Id(d))))]),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(-,Id(c),BinaryOp(*,IntLit(1),FloatLit(20180000000000.0))))]))])),MethodDecl(Id(func2),Instance,[param(Id(e),StringType),param(Id(f),StringType)],VoidType,Block([],[Return(BinaryOp(^,BinaryOp(^,BinaryOp(^,Id(e),Id(f)),StringLit("c")),StringLit("")))])),MethodDecl(Id(func3),Instance,[param(Id(g),BoolType),param(Id(h),BoolType)],BoolType,Block([],[AssignStmt(Id(h),BooleanLit(False)),Return(BinaryOp(==,Id(g),BooleanLit(True)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_random_11(self):
        input = """
        class program {
            void func(int a,b,c,d) {
                if a == b + c then
                    for d := 0 to 10 do 
                        c := c + 1 / 3 % d;
                else
                    for d := 0 to 10 do 
                        c := c - 1 * 2018E+10;
                for i := 10 downto 2 do
                    i := x*3;
            }
            void func2(string e, f) {
                return e ^ f ^ "c" ^ "";
            }
            boolean func3(boolean g, h) {
                h := false;
                return g == true;
            }
        }
        class program2 {
            int width = 0;
            int length = 0;
            program2() {
                program pg1;
                return this.width * this.length;
            }
            static int func() {
                return "";
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType)],VoidType,Block([],[If(BinaryOp(==,Id(a),BinaryOp(+,Id(b),Id(c))),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(+,Id(c),BinaryOp(%,BinaryOp(/,IntLit(1),IntLit(3)),Id(d))))]),For(Id(d),IntLit(0),IntLit(10),True,AssignStmt(Id(c),BinaryOp(-,Id(c),BinaryOp(*,IntLit(1),FloatLit(20180000000000.0))))])),For(Id(i),IntLit(10),IntLit(2),False,AssignStmt(Id(i),BinaryOp(*,Id(x),IntLit(3)))])])),MethodDecl(Id(func2),Instance,[param(Id(e),StringType),param(Id(f),StringType)],VoidType,Block([],[Return(BinaryOp(^,BinaryOp(^,BinaryOp(^,Id(e),Id(f)),StringLit("c")),StringLit("")))])),MethodDecl(Id(func3),Instance,[param(Id(g),BoolType),param(Id(h),BoolType)],BoolType,Block([],[AssignStmt(Id(h),BooleanLit(False)),Return(BinaryOp(==,Id(g),BooleanLit(True)))]))]),ClassDecl(Id(program2),[AttributeDecl(Instance,VarDecl(Id(width),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType,IntLit(0))),MethodDecl(Id(program2),Instance,[],Block([VarDecl(Id(pg1),ClassType(Id(program)))],[Return(BinaryOp(*,FieldAccess(Self(),Id(width)),FieldAccess(Self(),Id(length))))])),MethodDecl(Id(func),Static,[],IntType,Block([],[Return(StringLit(""))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_random_12(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType)))])])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_random_13(self):
        input = """
        class program {
            void foo(int a) {
                return b.foo(b) * a.foo(c) * c.foo(a-2) + x.foo(10);
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType)],VoidType,Block([],[Return(BinaryOp(+,BinaryOp(*,BinaryOp(*,CallExpr(Id(b),Id(foo),[Id(b)]),CallExpr(Id(a),Id(foo),[Id(c)])),CallExpr(Id(c),Id(foo),[BinaryOp(-,Id(a),IntLit(2))])),CallExpr(Id(x),Id(foo),[IntLit(10)])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_random_14(self):
        input = """
        class program {
                static final int a = 0;
                float b = 0;
                static int funcA(int a,b,c) {
                    return a*b+c;
                }
                static int funcB() {
                    a[3+x.foo(2)] := a[b] * 2;
                }
                string func() {
                    this.a := 5;
                    this.a[0] := 1;
                    if (b == a) && (c == d) then
                        b := b && a;
                    else
                        b := b || 1;
                }
            }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(0))),MethodDecl(Id(funcA),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],IntType,Block([],[Return(BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)))])),MethodDecl(Id(funcB),Static,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(*,ArrayCell(Id(a),Id(b)),IntLit(2)))])),MethodDecl(Id(func),Instance,[],StringType,Block([],[AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),IntLit(0)),IntLit(1)),If(BinaryOp(&&,BinaryOp(==,Id(b),Id(a)),BinaryOp(==,Id(c),Id(d))),AssignStmt(Id(b),BinaryOp(&&,Id(b),Id(a))),AssignStmt(Id(b),BinaryOp(||,Id(b),IntLit(1))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_random_15(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True)))])])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_random_16(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            int func(int a, b; float c) {
                string e;
                final float[1] arr;
                float f;
                arr[2 + this.foo(2)] := 0;
                e := "avc" ^ "jlacsjl";
                f := 12E10 - 20.0003; 
            }

            int foo() {
                for i := 1 to 10 do
                    for j := 1 downto -10 do
                        for k := 100 to 10000 do
                            if (i == j) && (i == k) then
                                i := j * k -1 / 2;
                            else
                                i := j * j - j / 2;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],IntType,Block([VarDecl(Id(e),StringType),ConstDecl(Id(arr),ArrayType(1,FloatType),None),VarDecl(Id(f),FloatType)],[AssignStmt(ArrayCell(Id(arr),BinaryOp(+,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(2)]))),IntLit(0)),AssignStmt(Id(e),BinaryOp(^,StringLit("avc"),StringLit("jlacsjl"))),AssignStmt(Id(f),BinaryOp(-,FloatLit(120000000000.0),FloatLit(20.0003)))])),MethodDecl(Id(foo),Instance,[],IntType,Block([],[For(Id(i),IntLit(1),IntLit(10),True,For(Id(j),IntLit(1),UnaryOp(-,IntLit(10)),False,For(Id(k),IntLit(100),IntLit(10000),True,If(BinaryOp(&&,BinaryOp(==,Id(i),Id(j)),BinaryOp(==,Id(i),Id(k))),AssignStmt(Id(i),BinaryOp(-,BinaryOp(*,Id(j),Id(k)),BinaryOp(/,IntLit(1),IntLit(2)))),AssignStmt(Id(i),BinaryOp(-,BinaryOp(*,Id(j),Id(j)),BinaryOp(/,Id(j),IntLit(2)))))])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_random_17(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            static void foo() {
                return a.foo(a, b, c, d && 2);
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(foo),Static,[],VoidType,Block([],[Return(CallExpr(Id(a),Id(foo),[Id(a),Id(b),Id(c),BinaryOp(&&,Id(d),IntLit(2))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_random_18(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                string e;
                final float[1] arr;
                float f;
                arr[2 + this.foo(2)] := 0;
                e := "avc" ^ "jlacsjl";
                f := 12E10 - 20.0003;
                return 0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([VarDecl(Id(e),StringType),ConstDecl(Id(arr),ArrayType(1,FloatType),None),VarDecl(Id(f),FloatType)],[AssignStmt(ArrayCell(Id(arr),BinaryOp(+,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(2)]))),IntLit(0)),AssignStmt(Id(e),BinaryOp(^,StringLit("avc"),StringLit("jlacsjl"))),AssignStmt(Id(f),BinaryOp(-,FloatLit(120000000000.0),FloatLit(20.0003))),Return(IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_random_19(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                string e;
                final float[1] arr;
                float f;
                arr[2 + this.foo(2)] := 0;
                e := "avc" ^ "jlacsjl";
                f := 12E10 - 20.0003;
                return 0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([VarDecl(Id(e),StringType),ConstDecl(Id(arr),ArrayType(1,FloatType),None),VarDecl(Id(f),FloatType)],[AssignStmt(ArrayCell(Id(arr),BinaryOp(+,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(2)]))),IntLit(0)),AssignStmt(Id(e),BinaryOp(^,StringLit("avc"),StringLit("jlacsjl"))),AssignStmt(Id(f),BinaryOp(-,FloatLit(120000000000.0),FloatLit(20.0003))),Return(IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_random_20(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                return 0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([],[Return(IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    
    def test_random_21(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                return 0;
            }
        }
        class program2 extends program {
            program a = new program(a, b, c);
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([],[Return(IntLit(0))]))]),ClassDecl(Id(program2),Id(program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(program)),NewExpr(Id(program),[Id(a),Id(b),Id(c)])))])])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_random_22(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                string e;
                final float[1] arr;
                float f;
                arr[2 + this.foo(2)] := 0;
                e := "avc" ^ "jlacsjl";
                f := 12E10 - 20.0003;
                return 0;
            }

            static boolean foo() {
                return a.foo() % b.foo();
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([VarDecl(Id(e),StringType),ConstDecl(Id(arr),ArrayType(1,FloatType),None),VarDecl(Id(f),FloatType)],[AssignStmt(ArrayCell(Id(arr),BinaryOp(+,IntLit(2),CallExpr(Self(),Id(foo),[IntLit(2)]))),IntLit(0)),AssignStmt(Id(e),BinaryOp(^,StringLit("avc"),StringLit("jlacsjl"))),AssignStmt(Id(f),BinaryOp(-,FloatLit(120000000000.0),FloatLit(20.0003))),Return(IntLit(0))])),MethodDecl(Id(foo),Static,[],BoolType,Block([],[Return(BinaryOp(%,CallExpr(Id(a),Id(foo),[]),CallExpr(Id(b),Id(foo),[])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_random_23(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                return 0;
                break;
                continue;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([],[Return(IntLit(0)),Break,Continue]))])])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_random_24(self):
        input = """
        class program {
            int func(int a,b; string c,d) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                else
                    c := d - 5 * 9 % 3;
                if d == 0 then
                    a := 0;
                else
                    c := 0;
                for i := 10 - 3 + 5 to 1000 do
                    i := 100 % 2;
            } 
        }
        """
        expect = """Program([ClassDecl(Id(program),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),StringType),param(Id(d),StringType)],IntType,Block([],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a))),AssignStmt(Id(c),BinaryOp(-,Id(d),BinaryOp(%,BinaryOp(*,IntLit(5),IntLit(9)),IntLit(3))))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(c),IntLit(0))),For(Id(i),BinaryOp(+,BinaryOp(-,IntLit(10),IntLit(3)),IntLit(5)),IntLit(1000),True,AssignStmt(Id(i),BinaryOp(%,IntLit(100),IntLit(2)))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_random_25(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                final int a;
                final int b;
                int c;
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
                else
                    c := d - 5 * 9 % 3;
                if d == 0 then
                    a := 0;
                else
                    c := 12E-8 + 5;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),IntType,None),VarDecl(Id(c),IntType)],[If(BinaryOp(==,Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))),If(BinaryOp(==,Id(b),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,Id(b),Id(a))),AssignStmt(Id(c),BinaryOp(-,Id(d),BinaryOp(%,BinaryOp(*,IntLit(5),IntLit(9)),IntLit(3))))),If(BinaryOp(==,Id(d),IntLit(0)),AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(c),BinaryOp(+,FloatLit(1.2e-07),IntLit(5))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_random_26(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                return 0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([],[Return(IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_random_27(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            boolean a = true;
            string func(int a, b; float c) {
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        for b := 5 to 10 do 
                            for c := 15 downto 10 do 
                                break;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),BoolType,BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([],[For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,For(Id(c),IntLit(15),IntLit(10),False,Break])])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_random_28(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            boolean a = true;
            string func(int a, b; float c) {
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        for b := 5 to 10 do 
                            for c := 15 downto 10 do 
                                break;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),BoolType,BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([],[For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,For(Id(c),IntLit(15),IntLit(10),False,Break])])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_random_29(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        continue;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([],[For(Id(a),IntLit(5),IntLit(10),True,For(Id(b),IntLit(5),IntLit(10),True,Continue])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_random_30(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                return 0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(program),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(10000,BoolType))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(bool)),BooleanLit(True))),MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],StringType,Block([],[Return(IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 400))

