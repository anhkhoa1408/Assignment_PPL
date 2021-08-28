import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program_1(self):
        """Simple program: int main() {} """
        input = """
        Var: x;
        Function: main
            Body:

            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_simple_program_2(self):
        """Simple program: int main() {} """
        input = """
        Var: z,a=5,b,c,s,esa;
        Function: main
            Body:
                foo(a,b,c);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_declare_variable_1(self):
        input = """
        Var: b,a[3],c[123][22],e=5,r=6,a;
        Function: main
            Body:
                foo(3*5);
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_declare_variable_2(self):
        input = """
        Var: a[3]={12,3,0} , c[1][1] = {{"abc","ab"},{"xt","z"}}, e = 5 , r = 6, a;
        Function: main
            Body:

            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_parameter_declare_1(self):
        input = """
        Function: foo
            Parameter: b,a[12],a[2][3][4];
            Body:

            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_assign_stmt_1(self):
        input = """
        Function: foo
            Parameter: b,a[12],a[2][3][4];
            Body:
                Var: a = 5, b = 10;
                c = 10. +. 25 * 40 \\ 3 && 15;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_assign_stmt_2(self):
        input = """
        Function: foo
            Parameter: b,a[12],a[2][3][4];
            Body:
                Var: a = 5, b = 10;
                d = "ancn";
                e = 10e+12;
                g = 0x123AF;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    # def test_index_operator_1(self):
    #     input = """
    #     Function: foo
    #         Body:
    #             Var: a = 5, b = 10;
    #             a[3+2] = 
    #         EndBody.
    #     """
    #     expect ="successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_if_stmt_1(self):
        input = """
        Function: foo
            Parameter: a;
            Body:
                If a == 1 Then
                a = a + 1;
                Else
                a = a - 1;
                EndIf.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_if_stmt_2(self):
        input = """
        Function: foo
            Parameter: a, b;
            Body:
                If a == 1 Then
                a = a + 1;
                ElseIf (a == 2) || (b == 3) Then
                a = a + 2;
                Else
                a = a - 1;
                EndIf.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_if_stmt_5(self):
        input = """
        Function: foo
            Parameter: a, b, c, d;
            Body:
                If (a + 1 > a*b) Then
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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_while_stmt_1(self):
        input = """
        Function: foo
            Body:
                Var: i = 0;
                While (i<1) Do
                EndWhile.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_while_stmt_2(self):
        input = """
        Function: foo
            Body:
                Var: i = 0,a;
                While (i<1) Do
                a = 15 * a +5;
                EndWhile.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    
    def test_while_stmt_3(self):
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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_while_stmt_4(self):
        input = """
        Function: foo
            Body:
                Var: i = 0,a,b;
                While ((i<1) && (a>2) && b+a<i+12) Do
                a = 15*a +5;
                i = a + 1;
                b=i;
                EndWhile.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_while_stmt_5(self):
        input = """
        Function: foo
            Body:
                Var: i = 0,a,b;
                a = 15 * 9 +29;
                While ((i<1) && (a>2) && b+a<i+12) Do
                    If (a>100) Then
                        a = 15 * a +5;
                    EndIf.
                    i = a + 1;
                    b=i;
                EndWhile.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_while_stmt_7(self):
        input = """
        Function: foo
            Body:
                Var:i=0,j=0;
                While (2) Do
                    While (j>1) Do
                        j=j+1;
                    EndWhile.
                    i=i+1;
                EndWhile.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_while_stmt_9(self):
        input = """
        Function: foo
            Body:
                Var:i=0,j=0;
                If(i==j) Then
                    While(2) Do
                        i=j+1;
                        While(3) Do
                            j=j+1;
                        EndWhile.
                    EndWhile.
                EndIf.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_DoWhile_stmt_1(self):
        input = """
        Function: foo
            Body:
                Do a=a+11;
                While (a<1)
                EndDo.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_DoWhile_stmt_2(self):
        input = """
        Function: foo
            Body:
                Do 
                    a=a+11;
                    
                While (a<1)
                EndDo.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_DoWhile_stmt_3(self):
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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_DoWhile_stmt_4(self):
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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_DoWhile_stmt_5(self):
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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_DoWhile_stmt_8(self):
        input = """
        Function: foo
            Body:
                Do 
                    foo(a,2+3);
                    Do
                        a=a+1;
                        Return a;
                    While (a<1)
                    EndDo.
                While (a<1)
                EndDo.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_For_stmt_1(self):
        input = """
        Function: foo
            Parameter: a,b;
            Body:
                Var: i;
                For (i=0,i<5,2) Do
                EndFor.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_For_stmt_2(self):
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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_For_stmt_3(self):
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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_For_stmt_4(self):
        input = """
        Function: foo
            Parameter: a,b;
            Body:
                Var: i;
                For (i=0,i<5,2) Do
                EndFor.
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_Return_stmt_1(self):
        input = """
        Function: foo
            Body:
                Var: a,b,c;
                a= b*b;
                b= c*c;
                c= a*a;
                Return a*b*c;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_Return_stmt_2(self):
        input = """
        Function: foo
            Body:
                Var: a,b,c;
                a = 0xABCD;
                Return a;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_Return_stmt_3(self):
        input = """
        Function: foo
            Body:
                Return foo(a+x1);
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_Return_stmt_4(self):
        input = """
        Function: foo
            Body:
                Return a(a*99+12);
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_Return_stmt_5(self):
        input = """
        Function: foo
            Body:
                Return 1+2*6;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_Return_stmt_6(self):
        input = """
        Function: foo
            Body:
                Return "A";
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_Return_stmt_7(self):
        input = """
        Function: foo
            Body:
                Return "A";
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_Return_stmt_8(self):
        input = """
        Function: foo
            Body:
                Return "ammqmwd";
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_Return_stmt_9(self):
        input = """
        Function: foo
            Body:
                Return 0xABCD1234;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_Return_stmt_10(self):
        input = """
        Function: foo
            Body:
                Return 12E+12;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_random_2(self):
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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_random_3(self):
        input = """
        Var: a,b,c;
        Function: foo
            Body:

            EndBody.
        Function: sum
            Parameter: n;
            Body:
               
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_random_5(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                n = n + 1 - 2 * 9;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_random_9(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                a = (2+3) * 100 ;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_random_11(self):
        input = """
        Function: sum
            Parameter: n;
            Body:
                a = (2+3) * 100 - 100E+34 ;
            EndBody.
        """
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_random_12(self):
        input = """
        Function: sum
            Parameter: ;
            Body:
                
            EndBody.
        """
        expect ="Error on line 3 col 23: ;"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_random_13(self):
        input = """
        Function: foo
            Parameter: ;
            Body:
                While(
            EndBody.
        """
        expect ="Error on line 3 col 23: ;"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_random_14(self):
        """Miss variable"""
        input = """
        Var: ;
        Function: Main
            Body:

            EndBody.
        """
        expect = "Error on line 2 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_random_15(self):
        input = """
        Function: ucln
            Parameter:a ;
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
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_random_16(self):
        """Miss variable"""
        input = """
        Var:a,b,c,a;
        Function: main
            Body:

            EndBody
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    
    def test_random_17(self):
        input = """
        Var:a,b,c,a;
        Function: main
            If(x%5 == 0 && x > 3) Then

            EndIf.

            EndBody
        """
        expect = "Error on line 4 col 12: If"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_random_18(self):
        input = """
        Var:a,b,c,a;
        Function: main
            body
                foo(x,1000+23*5);
            EndIf.

            EndBody
        """
        expect = "Error on line 4 col 12: body"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_random_19(self):
        input = """
        Var:a,b,c,a,a[;
        """
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_random_20(self):
        input = """
        Var:a,b,c;
        Function: main
            While (a&&b || c+5>2

            EndWhile.

            EndBody
        """
        expect = "Error on line 4 col 12: While"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_random_21(self):
        input = """
        Function main
        Body:
        EndBody.
        """
        expect = "Error on line 2 col 17: main"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_random_22(self):
        input = """
        Var:x;
        Function: main
            If(x == 0 || x > 3) Then
                Return x
            EndIf.
            EndBody
        """
        expect = "Error on line 4 col 12: If"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_random_23(self):
        input = """
        Function: main
            Body:
            Var:a,b,c;
            If (a>b) && (a>c) Then
                Return a;
            ElseIf (b>a) && (b>c) Then
                Return b;
            Else
                Return c;
            EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_random_24(self):
        input = """
        Var:x=2,a[2][3]={"x,t,z",12,2,3," ",12};
        Function: main
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_random_25(self):
        input = """
        Var:x;
        Function: main
            Body:
            If( Then
                Return x;
            EndIf.
            EndBody.
        """
        expect = "Error on line 5 col 16: Then"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_random_26(self):
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
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    
    def test_random_27(self):
        input = """
        Var:x;
        Function: foo1
            Parameter:x,a,b,c,y[5];
            Body:
                Break;
                Return;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_random_28(self):
        input = """
        Function: main
            Body:
            Var: result;
            If (a > 12E-4) Then
                Return result+a;
            EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_random_29(self):
        input = """
        Function: main
            Body:
            if (a>b) Then
                Return x;
            EndIf.
            EndBody.
        """
        expect = "Error on line 4 col 21: Then"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_random_30(self):
        input = """
        Var:x;
        Function: main
            Body:
            If Then
                Return x;
            EndIf.
            EndBody.
        """
        expect = "Error on line 5 col 15: Then"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_random_31(self):
        input = """
        Var:x;
        Function: 12main
            Body:
            
            EndBody.
        """
        expect = "Error on line 3 col 18: 12"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_random_32(self):
        input = """
        Function: main
            Body:
            Body:
            EndBody.
        """
        expect = "Error on line 4 col 12: Body"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_random_33(self):
        input = """
        Function: 12main
            Body:
            
            Endody.
        """
        expect = "Error on line 2 col 18: 12"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_random_34(self):
        input = """
                If a == 1 Then
                a = a + 1;
                ElseIf (a == 2) || (b == 3) Then
                a = a + 2;
                Else
                a = a - 1;
                EndIf.
        """
        expect = "Error on line 2 col 16: If"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_random_35(self):
        input = """
        Var:x;
        Function: main
            Body:
                Break
            EndBody.
        """
        expect = "Error on line 6 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_random_36(self):
        input = """
        Function: foo
            Parameter: ba[12],a[2][3][4;
            Body:

            EndBody.
        """
        expect = "Error on line 3 col 39: ;"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_random_37(self):
        input = """
       Function: foo
            Body:
                Var: i = 0,a,b;
                a = 15 * 9 +29;
                While ((i<1) && (a>2) && acb+a<i+12) Do
                    If (a>100) Then
                        a  15 * a +5;
                    EndIf.
                    i = a + 1;
                    b=i;
                EndWhile.
            EndBody.
        """
        expect = "Error on line 8 col 27: 15"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_random_38(self):
        input = """
       Function: foo
            Body:
               
                While ((i=1) && (a>2)) Do
                    i = a + 1;
                    b=i;
                EndWhile.
            EndBody.
        """
        expect = "Error on line 5 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_random_39(self):
        input = """
        Function: foo
            Body:
                Return "Bai tap lon 1";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_random_40(self):
        input = """
        Function: foo
            Body:
                Return "Bai tap lon 1";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_random_41(self):
        input = """
        Function: foo
            Body:
                Var:i;
                For(i=12i<1000,12) Do
                    Return 5*foo(i);
                EndFor.
            EndBody.
        """
        expect = "Error on line 5 col 24: i"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_random_42(self):
        input = """
        Function: foo
            Body:
                Var:i;
                For(i="x",i<1000,12) Do
                    Return 5*foo(i);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_random_43(self):
        input = """
        Function: foo
            Body:
                Var:i;
                    Return 5*fooi);
            EndBody.
        """
        expect = "Error on line 5 col 33: )"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_random_44(self):
        input = """
        Function: foo
            Body:
                Var:i;
                Var:i;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_random_45(self):
        input = """
        Function: foo
            Body:
                Var: i[2],i[3];
            EndBody.
            EndBody.
        """
        expect = "Error on line 6 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_random_46(self):
        input = """
        Function: foo
            Body:
            EndBody..
        """
        expect = "Error on line 4 col 20: ."
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_random_47(self):
        input = """
        Function: foo
            Body:
                foo(a,x,s,a,f,31,34);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_random_48(self):
        input = """
        Function: foo
            Body:
                Var:i,j;
                For (i=0,i<=9122,23) Do
                   While(j>10) Do
                    foo(2+x);
                   EndWhile.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_random_49(self):
        input = """
        Function: foo
            Body:
                Var:i,j;
                For (i=0,i<=9122,23) Do
                Break;
                EndFor
            EndBody.
        """
        expect = "Error on line 8 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    
    def test_random_50(self):
        input = """
        Function: foo
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,300))

    

    

    

    



    

    



    