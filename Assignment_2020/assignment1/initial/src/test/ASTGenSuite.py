import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program_1(self):
        input = """
        Var: x;
        """
        expect = "Program([VarDecl(Id(x))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_simple_program_2(self):
        input = """
        Var: x,y,z,t;
        """
        expect = "Program([VarDecl(Id(x)),VarDecl(Id(y)),VarDecl(Id(z)),VarDecl(Id(t))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_simple_program_3(self):
        input = """
        Var: x=0x1AF12,y=2,z=3.55,t=4E-10;
        """
        expect = "Program([VarDecl(Id(x),IntLiteral(110354)),VarDecl(Id(y),IntLiteral(2)),VarDecl(Id(z),FloatLiteral(3.55)),VarDecl(Id(t),FloatLiteral(4e-10))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_simple_program_4(self):
        input = """
        Var: x[2],y[2][3];
        """
        expect = "Program([VarDecl(Id(x),[2]),VarDecl(Id(y),[2,3])])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_simple_program_5(self):
        input = """
        Function: foo
            Body:
        EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_simple_program_6(self):
        input = """
        Var: a,b,c;
        Function: foo
            Body:
        EndBody.
        """
        expect = "Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(foo)[],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_simple_program_7(self):
        input = """
        Var: w = "a",c =0o12,d = 12.46;
        Function: foo
            Body:
        EndBody.
        """
        expect = "Program([VarDecl(Id(w),StringLiteral(a)),VarDecl(Id(c),IntLiteral(10)),VarDecl(Id(d),FloatLiteral(12.46)),FuncDecl(Id(foo)[],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_simple_program_8(self):
        input = """
        Function: foo
            Parameter: a, b, c, d;
            Body:
        EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d))],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_simple_program_9(self):
        input = """
        Function: foo
            Parameter: a[1],b[2];
            Body:
        EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[1]),VarDecl(Id(b),[2])],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_simple_program_10(self):
        input = """
        Function: foo
            Parameter: b[2][3][4];
            Body:
        EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(b),[2,3,4])],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_if_stmt_1(self):
        input = """
        Function: foo
            Body:
                If a==9 Then
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][If(BinaryOp(==,Id(a),IntLiteral(9)),[],[])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_if_stmt_2(self):
        input = """
        Function: foo
            Parameter: a, b;
            Body:
                If a == 1 Then
                a = foo(a) + 1;
                ElseIf (a == 2) || (b == 3) Then
                a = foo(a) + foo(2);
                Else
                a = a - 1;
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([][If(BinaryOp(==,Id(a),IntLiteral(1)),[],[Assign(Id(a),BinaryOp(+,CallExpr(Id(foo),[Id(a)]),IntLiteral(1)))])ElseIf(BinaryOp(||,BinaryOp(==,Id(a),IntLiteral(2)),BinaryOp(==,Id(b),IntLiteral(3))),[],[Assign(Id(a),BinaryOp(+,CallExpr(Id(foo),[Id(a)]),CallExpr(Id(foo),[IntLiteral(2)])))])Else([],[Assign(Id(a),BinaryOp(-,Id(a),IntLiteral(1)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_if_stmt_3(self):
        input = """
        Function: foo
            Parameter: a, b;
            Body:
                If a >= 1 Then
                a = 15 + 1 - 20 *. 9;
                ElseIf (a <= 2) || (b == 3) || (c == 5) Then
                a = b + 2;
                Else
                a = c - 1;
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([][If(BinaryOp(>=,Id(a),IntLiteral(1)),[],[Assign(Id(a),BinaryOp(-,BinaryOp(+,IntLiteral(15),IntLiteral(1)),BinaryOp(*.,IntLiteral(20),IntLiteral(9))))])ElseIf(BinaryOp(||,BinaryOp(||,BinaryOp(<=,Id(a),IntLiteral(2)),BinaryOp(==,Id(b),IntLiteral(3))),BinaryOp(==,Id(c),IntLiteral(5))),[],[Assign(Id(a),BinaryOp(+,Id(b),IntLiteral(2)))])Else([],[Assign(Id(a),BinaryOp(-,Id(c),IntLiteral(1)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_if_stmt_4(self):
        input = """
        Function: foo
            Parameter: a, b, c, d;
            Body:
                If (a + b > 1) Then
                    a = 15 + 1 - 20 *. 9;
                ElseIf ( a - c + d <= 2) || (b == 3) || (c == 5 * 5.0) Then
                    a = b + c + d + 2;
                ElseIf (a==b) && (b==c) Then
                    a = (a+b+c+d)\\4;
                Else
                    a = c + d - 1;
                EndIf.
            EndBody.
        """
        expect =  "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d))],([][If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),IntLiteral(1)),[],[Assign(Id(a),BinaryOp(-,BinaryOp(+,IntLiteral(15),IntLiteral(1)),BinaryOp(*.,IntLiteral(20),IntLiteral(9))))])ElseIf(BinaryOp(||,BinaryOp(||,BinaryOp(<=,BinaryOp(+,BinaryOp(-,Id(a),Id(c)),Id(d)),IntLiteral(2)),BinaryOp(==,Id(b),IntLiteral(3))),BinaryOp(==,Id(c),BinaryOp(*,IntLiteral(5),FloatLiteral(5.0)))),[],[Assign(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(b),Id(c)),Id(d)),IntLiteral(2)))])ElseIf(BinaryOp(&&,BinaryOp(==,Id(a),Id(b)),BinaryOp(==,Id(b),Id(c))),[],[Assign(Id(a),BinaryOp(\,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),Id(d)),IntLiteral(4)))])Else([],[Assign(Id(a),BinaryOp(-,BinaryOp(+,Id(c),Id(d)),IntLiteral(1)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_if_stmt_5(self):
        input = """
        Function: foo
                Parameter: a, b, c, d;
                Body:
                    If a == True Then
                        a = 15 + 1 - 20 *. 9;
                    ElseIf ( a - c + d <= 2) || (b == 3) || (c == 5 * 5.0) Then
                        a = b + c + d + 2;
                    ElseIf (a==b) && (b==c) Then
                        a = (a+b+c+d)\\.4.0;
                    ElseIf (a!=b) && ((b!=c)||(b!=d)) Then
                        Return 0; 
                    Else
                        a = c + d - 1;
                    EndIf.
                EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d))],([][If(BinaryOp(==,Id(a),BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(-,BinaryOp(+,IntLiteral(15),IntLiteral(1)),BinaryOp(*.,IntLiteral(20),IntLiteral(9))))])ElseIf(BinaryOp(||,BinaryOp(||,BinaryOp(<=,BinaryOp(+,BinaryOp(-,Id(a),Id(c)),Id(d)),IntLiteral(2)),BinaryOp(==,Id(b),IntLiteral(3))),BinaryOp(==,Id(c),BinaryOp(*,IntLiteral(5),FloatLiteral(5.0)))),[],[Assign(Id(a),BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(b),Id(c)),Id(d)),IntLiteral(2)))])ElseIf(BinaryOp(&&,BinaryOp(==,Id(a),Id(b)),BinaryOp(==,Id(b),Id(c))),[],[Assign(Id(a),BinaryOp(\.,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),Id(d)),FloatLiteral(4.0)))])ElseIf(BinaryOp(&&,BinaryOp(!=,Id(a),Id(b)),BinaryOp(||,BinaryOp(!=,Id(b),Id(c)),BinaryOp(!=,Id(b),Id(d)))),[],[Return(IntLiteral(0))])Else([],[Assign(Id(a),BinaryOp(-,BinaryOp(+,Id(c),Id(d)),IntLiteral(1)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_while_stmt_1(self):
        input = """
        Function: foo
            Body:
                Var: i = 0,a;
                While (i<1) Do
                a = 15 * a +5;
                EndWhile.
            EndBody.  
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i),IntLiteral(0)),VarDecl(Id(a))][While(BinaryOp(<,Id(i),IntLiteral(1)),[],[Assign(Id(a),BinaryOp(+,BinaryOp(*,IntLiteral(15),Id(a)),IntLiteral(5)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_while_stmt_2(self):
        input = """
        Function: foo
            Body:
                Var: i = 0,a;
                While ((i<1) && (a>2)) Do
                a = 15*a +5;
                i = a + 1;
                EndWhile.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i),IntLiteral(0)),VarDecl(Id(a))][While(BinaryOp(&&,BinaryOp(<,Id(i),IntLiteral(1)),BinaryOp(>,Id(a),IntLiteral(2))),[],[Assign(Id(a),BinaryOp(+,BinaryOp(*,IntLiteral(15),Id(a)),IntLiteral(5))),Assign(Id(i),BinaryOp(+,Id(a),IntLiteral(1)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_while_stmt_3(self):
        input = """
        Function: foo
            Body:
                While True Do
                    While True Do
                    EndWhile
                EndWhile.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][While(BooleanLiteral(true),[],[While(BooleanLiteral(true),[],[])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_while_stmt_4(self):
        input = """
        Var: a,b,c;
        Function: foo
            Body:
                While a<0 Do
                a = a+1;
                EndWhile.
            EndBody.
        """
        expect = "Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(foo)[],([][While(BinaryOp(<,Id(a),IntLiteral(0)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_while_stmt_5(self):
        input = """
        Function: foo
            Body:
                Var: i = 0;
                While (i<1) Do
                    While i == True Do
                        While i + 10 >= 25 Do
                            While 3*i == False Do
                                While 10*i - 27*i > 90 Do
                                EndWhile.
                            EndWhile.
                        EndWhile.
                    EndWhile.
                EndWhile.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i),IntLiteral(0))][While(BinaryOp(<,Id(i),IntLiteral(1)),[],[While(BinaryOp(==,Id(i),BooleanLiteral(true)),[],[While(BinaryOp(>=,BinaryOp(+,Id(i),IntLiteral(10)),IntLiteral(25)),[],[While(BinaryOp(==,BinaryOp(*,IntLiteral(3),Id(i)),BooleanLiteral(false)),[],[While(BinaryOp(>,BinaryOp(-,BinaryOp(*,IntLiteral(10),Id(i)),BinaryOp(*,IntLiteral(27),Id(i))),IntLiteral(90)),[],[])])])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_while_stmt_6(self):
        input = """
        Function: foo
            Body:
                Var:a[2], i = 0,b;
                a[0] = 9 + 29;
                While ((i<1) && (a>2) && b+a<i+12) Do
                    If (a>100) Then
                        a[1] = 15 * a +5;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(a),[2]),VarDecl(Id(i),IntLiteral(0)),VarDecl(Id(b))][Assign(ArrayCell(Id(a),[IntLiteral(0)]),BinaryOp(+,IntLiteral(9),IntLiteral(29))),While(BinaryOp(<,BinaryOp(&&,BinaryOp(&&,BinaryOp(<,Id(i),IntLiteral(1)),BinaryOp(>,Id(a),IntLiteral(2))),BinaryOp(+,Id(b),Id(a))),BinaryOp(+,Id(i),IntLiteral(12))),[],[If(BinaryOp(>,Id(a),IntLiteral(100)),[],[Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(+,BinaryOp(*,IntLiteral(15),Id(a)),IntLiteral(5)))])Else([],[])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_while_stmt_7(self):
        input = """
        Function: foo
            Body:
                Var:i=0,j=0;
                While (2) Do
                    While (j>1) Do
                        j=j+1;
                    EndWhile.
                EndWhile.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i),IntLiteral(0)),VarDecl(Id(j),IntLiteral(0))][While(IntLiteral(2),[],[While(BinaryOp(>,Id(j),IntLiteral(1)),[],[Assign(Id(j),BinaryOp(+,Id(j),IntLiteral(1)))])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_while_stmt_8(self):
        input = """
        Function: foo
            Body:
                Var:i=0,j=0;
                If(i==j) Then
                    While(2) Do
                        i=j+1;
                    EndWhile.
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i),IntLiteral(0)),VarDecl(Id(j),IntLiteral(0))][If(BinaryOp(==,Id(i),Id(j)),[],[While(IntLiteral(2),[],[Assign(Id(i),BinaryOp(+,Id(j),IntLiteral(1)))])])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_while_stmt_9(self):
        input = """
        Function: foo
            Body:
                Var:i=0,j=0;
                If(i==-j) Then
                    While(2) Do
                        i=j+1;
                        While(3) Do
                            j=j+1;
                        EndWhile.
                    EndWhile.
                EndIf.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i),IntLiteral(0)),VarDecl(Id(j),IntLiteral(0))][If(BinaryOp(==,Id(i),UnaryOp(-,Id(j))),[],[While(IntLiteral(2),[],[Assign(Id(i),BinaryOp(+,Id(j),IntLiteral(1))),While(IntLiteral(3),[],[Assign(Id(j),BinaryOp(+,Id(j),IntLiteral(1)))])])])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_while_stmt_10(self):
        input = """
        Var: a[4] = {"aasdasd","rrb","adc","asdd"}
        Function: foo
            Body:
            Var:i=0,j=0;
            While(2) Do
            i=j+1;
                While(3) Do
                j=j+1;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = "Program([VarDecl(Id(a),[4],ArrayLiteral(StringLiteral(aasdasd),StringLiteral(rrb),StringLiteral(adc),StringLiteral(asdd))),FuncDecl(Id(foo)[],([VarDecl(Id(i),IntLiteral(0)),VarDecl(Id(j),IntLiteral(0))][While(IntLiteral(2),[],[Assign(Id(i),BinaryOp(+,Id(j),IntLiteral(1))),While(IntLiteral(3),[],[Assign(Id(j),BinaryOp(+,Id(j),IntLiteral(1)))])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_For_stmt_1(self):
        input = """
        Function: foo
        Body:
            For(i=0,i>5,100) Do
            i = i*i;
            EndFor.
        EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][For(Id(i),IntLiteral(0),BinaryOp(>,Id(i),IntLiteral(5)),IntLiteral(100),[],[Assign(Id(i),BinaryOp(*,Id(i),Id(i)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_For_stmt_2(self):
        input = """
        Function: foo
            Parameter: a,b;
            Body:
                Var: i;
                For (i=0,i<5,2) Do
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(i))][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(5)),IntLiteral(2),[],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_For_stmt_3(self):
        input = """
        Function: foo
            Parameter: a,b;
            Body:
                Var: i;
                For (i=0,i<5,2) Do
                    a=b+9;
                    b=b*9;
                    i=i+1;
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(i))][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(5)),IntLiteral(2),[],[Assign(Id(a),BinaryOp(+,Id(b),IntLiteral(9))),Assign(Id(b),BinaryOp(*,Id(b),IntLiteral(9))),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_For_stmt_4(self):
        input = """
        Function: foo
            Parameter: a,b;
            Body:
                Var: i;
                For (i=0,i<5,2) Do
                    If(i % 2 == 0) Then
                    i = i * i;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(i))][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(5)),IntLiteral(2),[],[If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id(i),BinaryOp(*,Id(i),Id(i)))])Else([],[])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_For_stmt_5(self):
        input = """
        Function: maxNum
            Parameter: a[10];
            Body:
                Var:i;
                max=a[0];
                For (i=0,i<=9,1) Do
                    If (max > a[i]) Then
                    max = a[i];
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(maxNum)[VarDecl(Id(a),[10])],([VarDecl(Id(i))][Assign(Id(max),ArrayCell(Id(a),[IntLiteral(0)])),For(Id(i),IntLiteral(0),BinaryOp(<=,Id(i),IntLiteral(9)),IntLiteral(1),[],[If(BinaryOp(>,Id(max),ArrayCell(Id(a),[Id(i)])),[],[Assign(Id(max),ArrayCell(Id(a),[Id(i)]))])Else([],[])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_For_stmt_6(self):
        input = """
        Function: foo
            Parameter: a[10];
            Body:
                Var:i,j;
                For (i=0,i<=9,1.5) Do
                   While(j>10) Do
                    foo(2);
                   EndWhile.
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[10])],([VarDecl(Id(i)),VarDecl(Id(j))][For(Id(i),IntLiteral(0),BinaryOp(<=,Id(i),IntLiteral(9)),FloatLiteral(1.5),[],[While(BinaryOp(>,Id(j),IntLiteral(10)),[],[CallStmt(Id(foo),[IntLiteral(2)])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_For_stmt_7(self):
        input = """
        Function: foo
            Parameter: a[10];
            Body:
                Var:i,j;
                For (i=0,i<=9,1.5) Do
                   While(j>10) Do
                        foo(2);
                        While(k<15) Do
                        foo(3+i);
                        EndWhile.
                   EndWhile.
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[10])],([VarDecl(Id(i)),VarDecl(Id(j))][For(Id(i),IntLiteral(0),BinaryOp(<=,Id(i),IntLiteral(9)),FloatLiteral(1.5),[],[While(BinaryOp(>,Id(j),IntLiteral(10)),[],[CallStmt(Id(foo),[IntLiteral(2)]),While(BinaryOp(<,Id(k),IntLiteral(15)),[],[CallStmt(Id(foo),[BinaryOp(+,IntLiteral(3),Id(i))])])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_For_stmt_8(self):
        input = """
        Function: foo
            Parameter: a[10];
            Body:
                Var:i,j;
                For(i=12,i<1000,12) Do
                    Continue;
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[10])],([VarDecl(Id(i)),VarDecl(Id(j))][For(Id(i),IntLiteral(12),BinaryOp(<,Id(i),IntLiteral(1000)),IntLiteral(12),[],[Continue()])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_For_stmt_9(self):
        input = """
        Function: foo
            Body:
                Var:i;
                For(i=12,i<1000,12) Do
                    Continue;
                    foo(i+1);
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i))][For(Id(i),IntLiteral(12),BinaryOp(<,Id(i),IntLiteral(1000)),IntLiteral(12),[],[Continue(),CallStmt(Id(foo),[BinaryOp(+,Id(i),IntLiteral(1))])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_For_stmt_10(self):
        input = """
         Function: foo
            Body:
                Var:i;
                For(i=12,i<1000,12) Do
                    Return 5*foo(i);
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i))][For(Id(i),IntLiteral(12),BinaryOp(<,Id(i),IntLiteral(1000)),IntLiteral(12),[],[Return(BinaryOp(*,IntLiteral(5),CallExpr(Id(foo),[Id(i)])))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_Return_stmt_1(self):
        input = """
        Function: foo
            Parameter: a,b,c;
            Body:
                Var: a,b,c;
                a= b*b;
                b= c*c;
                c= a*a;
                Return foo(2+a,3*b,4*c);
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))][Assign(Id(a),BinaryOp(*,Id(b),Id(b))),Assign(Id(b),BinaryOp(*,Id(c),Id(c))),Assign(Id(c),BinaryOp(*,Id(a),Id(a))),Return(CallExpr(Id(foo),[BinaryOp(+,IntLiteral(2),Id(a)),BinaryOp(*,IntLiteral(3),Id(b)),BinaryOp(*,IntLiteral(4),Id(c))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_Return_stmt_2(self):
        input = """
        Function: foo
            Parameter: a,b,c;
            Body:
                Do a=a+11;
                While (a<1)
                    Return foo(3*a);
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([][Dowhile([],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(11)))],BinaryOp(<,Id(a),IntLiteral(1))),Return(CallExpr(Id(foo),[BinaryOp(*,IntLiteral(3),Id(a))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_Return_stmt_3(self):
        input = """
        Function: foo
            Parameter: a,b,c;
            Body:
                Do a=a+11;
                While (a<1)
                    Return foo(3*a);
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([][Dowhile([],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(11)))],BinaryOp(<,Id(a),IntLiteral(1))),Return(CallExpr(Id(foo),[BinaryOp(*,IntLiteral(3),Id(a))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_Return_stmt_4(self):
        input = """
        Function: foo
            Body:
                Return ;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))


    def test_Return_stmt_5(self):
        input = """
        Function: foo
            Body:
                Return 1+2*6*foo(3,4,5,6);
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(BinaryOp(+,IntLiteral(1),BinaryOp(*,BinaryOp(*,IntLiteral(2),IntLiteral(6)),CallExpr(Id(foo),[IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6)]))))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))


    def test_Return_stmt_6(self):
        input = """
        Function: foo
            Body:
                Return "Auvqnciwnqcini"+"vokosv,o";
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(BinaryOp(+,StringLiteral(Auvqnciwnqcini),StringLiteral(vokosv,o)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_Return_stmt_7(self):
        input = """
        Function: foo
            Body:
                Return 0xABCD1234;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(IntLiteral(2882343476))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))


    def test_Return_stmt_8(self):
        input = """
        Function: foo
            Body:
                Return 12E+12;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(FloatLiteral(12000000000000.0))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_Return_stmt_9(self):
        input = """
        Function: foo
            Body:
                Return foo()[4];
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(ArrayCell(CallExpr(Id(foo),[]),[IntLiteral(4)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_Return_stmt_10(self):
        input = """
        Function: foo
            Body:
                Return foo()[4];
            EndBody.
        Function: foo1
            Body:
                Return foo1()[5];
            EndBody.
        Function: foo2
            Body:
                Return foo2()[6];
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(ArrayCell(CallExpr(Id(foo),[]),[IntLiteral(4)]))])),FuncDecl(Id(foo1)[],([][Return(ArrayCell(CallExpr(Id(foo1),[]),[IntLiteral(5)]))])),FuncDecl(Id(foo2)[],([][Return(ArrayCell(CallExpr(Id(foo2),[]),[IntLiteral(6)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_DoWhile_stmt_1(self):
        input = """
        Function: foo
            Body:
                Do 
                    a=a*.9 \\.12;
                    Do
                        a[2]=12;
                    While (a<1)
                    EndDo.
                While (a<1)
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Dowhile([],[Assign(Id(a),BinaryOp(\.,BinaryOp(*.,Id(a),IntLiteral(9)),IntLiteral(12))),Dowhile([],[Assign(ArrayCell(Id(a),[IntLiteral(2)]),IntLiteral(12))],BinaryOp(<,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_DoWhile_stmt_2(self):
        input = """
        Function: foo
            Body:
                Do a=a+11;
                While (a<1)
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Dowhile([],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(11)))],BinaryOp(<,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_DoWhile_stmt_3(self):
        input = """
        Function: foo
            Body:
                Do 
                    a=a+11;
                    
                While (a<1)
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Dowhile([],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(11)))],BinaryOp(<,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_DoWhile_stmt_4(self):
        input = """
        Function: foo
            Body:
                Do 
                    a=12900 * 12 + 4e4;
                    Do
                        a=a+1;
                    While (a<1)
                    EndDo.
                While (a<1)
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Dowhile([],[Assign(Id(a),BinaryOp(+,BinaryOp(*,IntLiteral(12900),IntLiteral(12)),FloatLiteral(40000.0))),Dowhile([],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_DoWhile_stmt_5(self):
        input = """
        Function: foo
            Body:
                Do 
                    a=a*.9 \\.12;
                    Do
                        a=a+1;
                    While (a<1)
                    EndDo.
                While (a<1)
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Dowhile([],[Assign(Id(a),BinaryOp(\.,BinaryOp(*.,Id(a),IntLiteral(9)),IntLiteral(12))),Dowhile([],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_DoWhile_stmt_6(self):
        input = """
        Function: foo
            Body:
                Do 
                    a = 12 * 9 + 8 - 4;
                    Do
                        a=a+1;
                    While (a<1)
                    EndDo.
                While (a<1)
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Dowhile([],[Assign(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLiteral(12),IntLiteral(9)),IntLiteral(8)),IntLiteral(4))),Dowhile([],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_DoWhile_stmt_7(self):
        input = """
        Function: foo
            Body:
                Do 
                    a=a*.9 \\.12;
                    Do
                        a=a+1;
                    While (a<1)
                    EndDo.
                While (a<1)
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Dowhile([],[Assign(Id(a),BinaryOp(\.,BinaryOp(*.,Id(a),IntLiteral(9)),IntLiteral(12))),Dowhile([],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_DoWhile_stmt_8(self):
        input = """
        Function: foo
            Body:
                Do 
                    a=a*.9 \\.12;
                    Do
                        a=a+1;
                    While (a<1)
                    EndDo.
                While (a<1)
                EndDo.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Dowhile([],[Assign(Id(a),BinaryOp(\.,BinaryOp(*.,Id(a),IntLiteral(9)),IntLiteral(12))),Dowhile([],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_DoWhile_stmt_9(self):
        input = """
        Function: foo
            Parameter: a,b;
            Body:
                Var: x,y;
                If (x<y) Then
                    Do
                        x=x+1;
                        Break;
                    While (x>y)
                    EndDo.
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x)),VarDecl(Id(y))][If(BinaryOp(<,Id(x),Id(y)),[],[Dowhile([],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1))),Break()],BinaryOp(>,Id(x),Id(y)))])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_DoWhile_stmt_10(self):
        input = """
        Function: foo
            Parameter: a,b;
            Body:
                Var: x,y;
                If (x==True) Then
                    Do
                        x=x+1;
                        Break;
                    While (x>y)
                    EndDo.
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(x)),VarDecl(Id(y))][If(BinaryOp(==,Id(x),BooleanLiteral(true)),[],[Dowhile([],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1))),Break()],BinaryOp(>,Id(x),Id(y)))])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_random_1(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                Var: i,s=0;
                For(i=0,i<n,1) Do
                s = s + i;
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(sum)[VarDecl(Id(n))],([VarDecl(Id(i)),VarDecl(Id(s),IntLiteral(0))][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),Id(n)),IntLiteral(1),[],[Assign(Id(s),BinaryOp(+,Id(s),Id(i)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_random_2(self):
        input = """
        Function: foo
            Body:
                Return 12E+12;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(FloatLiteral(12000000000000.0))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_random_3(self):
        input = """
        Var: a,b,c;
        Function: foo
            Body:

            EndBody.
        Function: sum
            Parameter: n;
            Body:
            a[3+foo(2)] = a[b[2][3]];
            EndBody.
        """
        expect = "Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),FuncDecl(Id(foo)[],([][])),FuncDecl(Id(sum)[VarDecl(Id(n))],([][Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))]),ArrayCell(Id(a),[ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_random_4(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                Var: i,s=0;
                For(i=0,i<n,1) Do
                s = s + i;
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(sum)[VarDecl(Id(n))],([VarDecl(Id(i)),VarDecl(Id(s),IntLiteral(0))][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),Id(n)),IntLiteral(1),[],[Assign(Id(s),BinaryOp(+,Id(s),Id(i)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_random_5(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                n = n + 1 - 2 * 9;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(sum)[VarDecl(Id(n))],([][Assign(Id(n),BinaryOp(-,BinaryOp(+,Id(n),IntLiteral(1)),BinaryOp(*,IntLiteral(2),IntLiteral(9))))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_random_6(self):
        input = """
        Var: a = "camc";
        Function: a
            Parameter: a;
            Body:
                If(a==a) Then
                Return a;
                EndIf.
            EndBody.
        """
        expect = "Program([VarDecl(Id(a),StringLiteral(camc)),FuncDecl(Id(a)[VarDecl(Id(a))],([][If(BinaryOp(==,Id(a),Id(a)),[],[Return(Id(a))])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_random_7(self):
        input = """
        Function: foo
        Body:
            Return x*x*x+2;
        EndBody.
        Function: sum
            Parameter: n;
            Body:
                foo(x) ;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(BinaryOp(+,BinaryOp(*,BinaryOp(*,Id(x),Id(x)),Id(x)),IntLiteral(2)))])),FuncDecl(Id(sum)[VarDecl(Id(n))],([][CallStmt(Id(foo),[Id(x)])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_random_8(self):
        input = """
        Function: fibo
            Parameter: n;
            Body:
                If (n<2) Then
                    Return 1;
                Else
                    Return fibo(n - 2) + fibo(n - 1);
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(fibo)[VarDecl(Id(n))],([][If(BinaryOp(<,Id(n),IntLiteral(2)),[],[Return(IntLiteral(1))])Else([],[Return(BinaryOp(+,CallExpr(Id(fibo),[BinaryOp(-,Id(n),IntLiteral(2))]),CallExpr(Id(fibo),[BinaryOp(-,Id(n),IntLiteral(1))])))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_random_9(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                a = (2+3) * 100 ;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(sum)[VarDecl(Id(n))],([][Assign(Id(a),BinaryOp(*,BinaryOp(+,IntLiteral(2),IntLiteral(3)),IntLiteral(100)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_random_10(self):
        input = """
        Function: fooo
            Parameter: n;
            Body:
                While (a == n) Do
                    Break;
                    Continue;
                EndWhile.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(fooo)[VarDecl(Id(n))],([][While(BinaryOp(==,Id(a),Id(n)),[],[Break(),Continue()])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_random_11(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                a = (2+3) * 100 - 100E+34 ;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(sum)[VarDecl(Id(n))],([][Assign(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLiteral(2),IntLiteral(3)),IntLiteral(100)),FloatLiteral(1e+36)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_random_12(self):
        input = """
        Function: sum
            Parameter: a,b,c;
            Body:
                
            EndBody.
        """
        expect = "Program([FuncDecl(Id(sum)[VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_random_13(self):
        input = """
        Function: foo
            Body:
            Var: a[2][3] = {{1,2,3},{4,5,6}}
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(a),[2,3],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6))))][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_random_14(self):
        input = """
        Function: foo
            Body:
            Var: a[2][3] = {{1E+9,22.0,33.0},{4.123,0.5,.6}}
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(a),[2,3],ArrayLiteral(ArrayLiteral(FloatLiteral(1000000000.0),FloatLiteral(22.0),FloatLiteral(33.0)),ArrayLiteral(FloatLiteral(4.123),FloatLiteral(0.5),IntLiteral(6))))][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_random_15(self):
        input = """
        Function: foo
            Body:
            Var: a[2][3] = {{1E+9,22.0,33.0},{4.123,0.5,.6}} , x,y,z;
            x = 23*y +z - 9E+10;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(a),[2,3],ArrayLiteral(ArrayLiteral(FloatLiteral(1000000000.0),FloatLiteral(22.0),FloatLiteral(33.0)),ArrayLiteral(FloatLiteral(4.123),FloatLiteral(0.5),IntLiteral(6)))),VarDecl(Id(x)),VarDecl(Id(y)),VarDecl(Id(z))][Assign(Id(x),BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLiteral(23),Id(y)),Id(z)),FloatLiteral(90000000000.0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_random_16(self):
        input = """
        Function: ucln
            Parameter:a,m,m ;
            Body:
                If(m==n) Then
                    Return m;
                EndIf.
                If(m>n) Then
                    ucln(m - n, m);
                Else
                    ucln(n, n - m);
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(ucln)[VarDecl(Id(a)),VarDecl(Id(m)),VarDecl(Id(m))],([][If(BinaryOp(==,Id(m),Id(n)),[],[Return(Id(m))])Else([],[]),If(BinaryOp(>,Id(m),Id(n)),[],[CallStmt(Id(ucln),[BinaryOp(-,Id(m),Id(n)),Id(m)])])Else([],[CallStmt(Id(ucln),[Id(n),BinaryOp(-,Id(n),Id(m))])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_random_17(self):
        input = """
        Var:a,b,c,a;
        Function: main
            Body:
            a[b[2] + foo(a,b,c)] = 2*9+2-9.0;
            EndBody.
        """
        expect = "Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(a)),FuncDecl(Id(main)[],([][Assign(ArrayCell(Id(a),[BinaryOp(+,ArrayCell(Id(b),[IntLiteral(2)]),CallExpr(Id(foo),[Id(a),Id(b),Id(c)]))]),BinaryOp(+,BinaryOp(*,IntLiteral(2),IntLiteral(9)),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_random_18(self):
        input = """
        Var:a,b,c,a;
        Function: main
            Body:
            a[b[2] + foo(a,b,c)] = 2*9+2-9.0;
            c[d[e[f]]] = 4;
            EndBody.
        """
        expect = "Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(a)),FuncDecl(Id(main)[],([][Assign(ArrayCell(Id(a),[BinaryOp(+,ArrayCell(Id(b),[IntLiteral(2)]),CallExpr(Id(foo),[Id(a),Id(b),Id(c)]))]),BinaryOp(+,BinaryOp(*,IntLiteral(2),IntLiteral(9)),IntLiteral(2))),Assign(ArrayCell(Id(c),[ArrayCell(Id(d),[ArrayCell(Id(e),[Id(f)])])]),IntLiteral(4))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_random_19(self):
        input = """
        Var: z,a=5,b,c,s,esa;
        Function: main
            Body:
                foo(a,b,c);
                a[2+x] = 2;
            EndBody.
        """
        expect = "Program([VarDecl(Id(z)),VarDecl(Id(a),IntLiteral(5)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(s)),VarDecl(Id(esa)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[Id(a),Id(b),Id(c)]),Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(2),Id(x))]),IntLiteral(2))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_random_20(self):
        input = """
        Var: b,a[3],c[123][22],e=5,r=6,a;
        Function: main
            Body:
                foo(3*5);
            EndBody.
        """
        expect = "Program([VarDecl(Id(b)),VarDecl(Id(a),[3]),VarDecl(Id(c),[123,22]),VarDecl(Id(e),IntLiteral(5)),VarDecl(Id(r),IntLiteral(6)),VarDecl(Id(a)),FuncDecl(Id(main)[],([][CallStmt(Id(foo),[BinaryOp(*,IntLiteral(3),IntLiteral(5))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_random_21(self):
        input = """
        Var: a[3]={12,3,0} , c[2][2] = {{1,4},{1,7}}, e = 5 , r = 6, a;
        Function: main
            Body:
            a[2 + foo(3)] = b[c[2][3]] + 5;
            EndBody.
        """
        expect = "Program([VarDecl(Id(a),[3],ArrayLiteral(IntLiteral(12),IntLiteral(3),IntLiteral(0))),VarDecl(Id(c),[2,2],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(4)),ArrayLiteral(IntLiteral(1),IntLiteral(7)))),VarDecl(Id(e),IntLiteral(5)),VarDecl(Id(r),IntLiteral(6)),VarDecl(Id(a)),FuncDecl(Id(main)[],([][Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(2),CallExpr(Id(foo),[IntLiteral(3)]))]),BinaryOp(+,ArrayCell(Id(b),[ArrayCell(Id(c),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(5)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_random_22(self):
        input = """
        Function: foo
            Parameter: b,a[12],a[2][3][4];
            Body:

            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(b)),VarDecl(Id(a),[12]),VarDecl(Id(a),[2,3,4])],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_random_23(self):
        input = """
        Function: foo
            Parameter: b,a[12],a[2][3][4];
            Body:
                Var: a = 5, b = 10;
                c = 10. +. 25 * 40 \\ 3 && 15;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(b)),VarDecl(Id(a),[12]),VarDecl(Id(a),[2,3,4])],([VarDecl(Id(a),IntLiteral(5)),VarDecl(Id(b),IntLiteral(10))][Assign(Id(c),BinaryOp(&&,BinaryOp(+.,FloatLiteral(10.0),BinaryOp(\,BinaryOp(*,IntLiteral(25),IntLiteral(40)),IntLiteral(3))),IntLiteral(15)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_random_24(self):
        input = """
        Function: foo
            Parameter: a;
            Body:
                Var: a = False;
                If a == False Then
                a = a + 1;
                ElseIf a == True Then
                a = a - 1;
                Else
                a = a * a
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a))],([VarDecl(Id(a),BooleanLiteral(false))][If(BinaryOp(==,Id(a),BooleanLiteral(false)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])ElseIf(BinaryOp(==,Id(a),BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(-,Id(a),IntLiteral(1)))])Else([],[Assign(Id(a),BinaryOp(*,Id(a),Id(a)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_random_25a(self):
        input = """
        Function: foo
            Parameter: a;
            Body:
                Var: a = False;
                If a == False Then
                a = a + 1;
                ElseIf a == True Then
                a = a - 1;
                Else
                a = a * a
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a))],([VarDecl(Id(a),BooleanLiteral(false))][If(BinaryOp(==,Id(a),BooleanLiteral(false)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])ElseIf(BinaryOp(==,Id(a),BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(-,Id(a),IntLiteral(1)))])Else([],[Assign(Id(a),BinaryOp(*,Id(a),Id(a)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_random_25b(self):
        input = """
        Function: foo
            Parameter: a;
            Body:
                Var: a = False;
                If a == False Then
                a = a + 1;
                ElseIf a == True Then
                a = a - 1;
                ElseIf a!=0 Then
                a = 0;
                Else
                a = a * a
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a))],([VarDecl(Id(a),BooleanLiteral(false))][If(BinaryOp(==,Id(a),BooleanLiteral(false)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])ElseIf(BinaryOp(==,Id(a),BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(-,Id(a),IntLiteral(1)))])ElseIf(BinaryOp(!=,Id(a),IntLiteral(0)),[],[Assign(Id(a),IntLiteral(0))])Else([],[Assign(Id(a),BinaryOp(*,Id(a),Id(a)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_random_26(self):
        input = """
        Function: foo
            Parameter: a;
            Body:
                Var: a = False;
                If a == False Then
                a = a + 1;
                ElseIf a == True Then
                a = a - 1;
                ElseIf a!=0 Then
                a = 0;
                ElseIf a==a*9+19\\2 Then
                a = foo(3,4,5,6);
                EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a))],([VarDecl(Id(a),BooleanLiteral(false))][If(BinaryOp(==,Id(a),BooleanLiteral(false)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])ElseIf(BinaryOp(==,Id(a),BooleanLiteral(true)),[],[Assign(Id(a),BinaryOp(-,Id(a),IntLiteral(1)))])ElseIf(BinaryOp(!=,Id(a),IntLiteral(0)),[],[Assign(Id(a),IntLiteral(0))])ElseIf(BinaryOp(==,Id(a),BinaryOp(+,BinaryOp(*,Id(a),IntLiteral(9)),BinaryOp(\,IntLiteral(19),IntLiteral(2)))),[],[Assign(Id(a),CallExpr(Id(foo),[IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6)]))])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_random_27(self):
        input = """
        Var: x;
        Function: main
            Body:

            EndBody.
        """
        expect = "Program([VarDecl(Id(x)),FuncDecl(Id(main)[],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_random_28(self):
        input = """
        Function: foo
            Body:
                Var:i,j;
                For (i=0,i<=9122,23) Do
                Break;
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i)),VarDecl(Id(j))][For(Id(i),IntLiteral(0),BinaryOp(<=,Id(i),IntLiteral(9122)),IntLiteral(23),[],[Break()])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_random_29(self):
        input = """
        Function: foo
            Body:
                Var:i;
                    Return 5*foo(i);
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(i))][Return(BinaryOp(*,IntLiteral(5),CallExpr(Id(foo),[Id(i)])))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_random_30(self):
        input = """
        Function: foo
            Body:
                Return "Bai tap lon 2";
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(StringLiteral(Bai tap lon 2))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_random_31(self):
        input = """
        Function: foo
            Body:
                While i == 1 Do
                    i = i + 1;
                    i=i;
                EndWhile.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][While(BinaryOp(==,Id(i),IntLiteral(1)),[],[Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1))),Assign(Id(i),Id(i))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_random_32(self):
        input = """
        Var:x;
        Function: main
            Body:
            If True Then
                Return x;
            EndIf.
            EndBody.
        """
        expect = "Program([VarDecl(Id(x)),FuncDecl(Id(main)[],([][If(BooleanLiteral(true),[],[Return(Id(x))])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_random_33(self):
        input = """
        Function: main
            Body:
            Var: result;
            If (a > 12E-4) Then
                Return result+a;
            EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(main)[],([VarDecl(Id(result))][If(BinaryOp(>,Id(a),FloatLiteral(0.0012)),[],[Return(BinaryOp(+,Id(result),Id(a)))])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_random_34(self):
        input = """
        Function: main
            Body:
            If (a>b) Then
                Return x;
            EndIf.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(main)[],([][If(BinaryOp(>,Id(a),Id(b)),[],[Return(Id(x))])Else([],[])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_random_35(self):
        input = """
        Function: foo1
            Body:
            EndBody.
        Function: foo2
            Body:
            EndBody.
        Function: main
            Body:
            EndBody.
        Function: foo3
            Body:
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo1)[],([][])),FuncDecl(Id(foo2)[],([][])),FuncDecl(Id(main)[],([][])),FuncDecl(Id(foo3)[],([][]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_random_36(self):
        input = """
        Var:x;
        Function: foo1
            Parameter:x,a,b,c,y[5];
            Body:
                Break;
                Return;
            EndBody.
        """
        expect = "Program([VarDecl(Id(x)),FuncDecl(Id(foo1)[VarDecl(Id(x)),VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(y),[5])],([][Break(),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_random_37(self):
        input = """
        Var:x;
        Function: foo1
            Parameter:x,a,b,c,y[5];
            Body:
                Break;
                Return;
            EndBody.
        """
        expect = "Program([VarDecl(Id(x)),FuncDecl(Id(foo1)[VarDecl(Id(x)),VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(y),[5])],([][Break(),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_random_38(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                a = (2+3) * 100 - 100E+34 ;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(sum)[VarDecl(Id(n))],([][Assign(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLiteral(2),IntLiteral(3)),IntLiteral(100)),FloatLiteral(1e+36)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_random_39(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                a = (2+3) * 100 - 100E+34 ;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(sum)[VarDecl(Id(n))],([][Assign(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLiteral(2),IntLiteral(3)),IntLiteral(100)),FloatLiteral(1e+36)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_random_40(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                Var: i,s=0;
                While (i>0) Do
                    If (i%2 == 0) Then
                        Continue;
                    Else
                        s=s+i;
                        i=i+1;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(sum)[VarDecl(Id(n))],([VarDecl(Id(i)),VarDecl(Id(s),IntLiteral(0))][While(BinaryOp(>,Id(i),IntLiteral(0)),[],[If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),[],[Continue()])Else([],[Assign(Id(s),BinaryOp(+,Id(s),Id(i))),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_random_41(self):
        input = """
        Function: foo
            Body:
                Return foo(a+x1);
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([][Return(CallExpr(Id(foo),[BinaryOp(+,Id(a),Id(x1))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_random_42(self):
        input = """
        Function: foo
            Body:
                Var: a,b,c;
                a = 0xABCD;
                Return a;
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[],([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c))][Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_random_43(self):
        input = """
        Var: a,b,c,d,w,e,f,a[2][3][4][5][6];
        Function: foo
            Parameter: a[10];
            Body:
                Var:i,j;
                For(i=12,i<1000,12) Do
                    Continue;
                EndFor.
            EndBody.
        """
        expect = "Program([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c)),VarDecl(Id(d)),VarDecl(Id(w)),VarDecl(Id(e)),VarDecl(Id(f)),VarDecl(Id(a),[2,3,4,5,6]),FuncDecl(Id(foo)[VarDecl(Id(a),[10])],([VarDecl(Id(i)),VarDecl(Id(j))][For(Id(i),IntLiteral(12),BinaryOp(<,Id(i),IntLiteral(1000)),IntLiteral(12),[],[Continue()])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_random_44(self):
        input = """
        Function: foo
            Parameter: a[10];
            Body:
                Var:i,j;
                For (i=0,i<=9,1.5) Do
                   While(j>10) Do
                        foo(2);
                        While(k<15) Do
                        foo(3+i);
                        EndWhile.
                   EndWhile.
                EndFor.
            EndBody.
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),[10])],([VarDecl(Id(i)),VarDecl(Id(j))][For(Id(i),IntLiteral(0),BinaryOp(<=,Id(i),IntLiteral(9)),FloatLiteral(1.5),[],[While(BinaryOp(>,Id(j),IntLiteral(10)),[],[CallStmt(Id(foo),[IntLiteral(2)]),While(BinaryOp(<,Id(k),IntLiteral(15)),[],[CallStmt(Id(foo),[BinaryOp(+,IntLiteral(3),Id(i))])])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
































