import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_1(self):
        input = """
        class ABC{
            int x;
            static int y;
        }
        class DEF{
            int main(){
                string[5] s = {"a", "b", "c"};
                s[5] := "a";
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(s),IntLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """
        class Shape {
            int y() {return 0;}
            int calc() {
                Shape s;
                s.y()[1] := 0;
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(s),Id(y),[]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """
        class Shape {
            int y() {int[5] t; return t;}
            int c() {
                Shape s;
                s.y() := 0.5;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(CallExpr(Id(s),Id(y),[]),FloatLit(0.5))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """
        class Test {
            float mult(int a; float b) {
                return a*b;
            }
            void calc() {
                int c;
                c := this.mult(3, 4.5);
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),CallExpr(Self(),Id(mult),[IntLit(3),FloatLit(4.5)]))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        input = """
        class Test {
            final int a = a;
            
        }
        """
        expect = "Illegal Constant Expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        input = """
        class Test {
            int a = 1 + true;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_7(self):
        input = """
        class Test {
            int foo(int a){
                int a;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """
        class Test {
            int foo(int a){
                b := 9;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        input = """
        class Test {
            final int c = 9;
            int foo(int a){
                a := 0;
                this.c := 7;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(c)),IntLit(7))"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self):
        input = """
        class Test {
            final int c = 9;
            foo(int a){}
            int fun(){
                Test a;
                a := new Test(9);
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """
        class main{
            final int n = 0;
            int main() {
                final int x = 2;
                int i;
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        """Simple program: int main() {} """
        input = """
        class main extends B{
            B a;
            static int j;
            int m  = this.m + 5;
            int c ;
            int main() {
                this.a.b := 5;
                continue;
            }
        }
        class B{
            int b;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """
        class main extends B{
            B a;
            static int j;
            int m  = this.m + 5 + this.c;
        }
        
        """
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        input = """
        class B extends B{
            B a;
            static int j;
            int m  = this.m + 5 + this.c;
            int c ;
            int main() {
                this.a.b := 5;
                this.j := 7;
            }
        }
        """
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """
        class main extends B{}
        """
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        input = """
        class main extends A{}
        class A{}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
        class main {
            int m  = this.c + this.c;
            int c ;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """
        class main extends B{
            int ma() {
                final int x = x;
                continue;
            }
        }
        class B{
            int b;
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """
        class main {
            static int a;
            int t = main.z;
        }
        """
        expect = "Undeclared Attribute: z"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
        class main {
            static int a;
            int foo(){
                int i;
                main.a := 5;
                for i := 0 to 5 do
                   i := 1;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        # this.a.b not constant
        input = """
        class X {
            float b = 0;
            X a;
            final int c = this.a.b;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(c),IntType,FieldAccess(FieldAccess(Self(),Id(a)),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        # type coerc int c = ...
        input = """
        class X {
            final int c = "a";
        }
        """
        expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(c),IntType,StringLit("a"))"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        # static boo and this
        input = """
        class X {
            int foo(){

            }
            int a = this.foo();
            int b = this.foo() / 2;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,CallExpr(Self(),Id(foo),[]),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """
        class X extends B{
            int foo(){}
            static int boo(){}
            final X bin = nil;
        }
        class B{
            int n;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        # this.a not in classtype
        input = """
        class A{
            A a;
            int foo() {}
            int b = 1 + this.a.foo() * 2; 
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """
        class main {
            int a;
            int b;
            float a;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """
        class main {
            int a;
            int b;
            int foo(int foo,c,c){}
        }
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """
        class main {
            int foo(int foo, c){
                float c;
            }
        }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = """
        class main {
            final float k = 8;
            int foo(int foo,c){
                return this.k;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """
        class main {
            static final int k = 8;
            float foo(int foo,c){
                return this.k;
            }
        }
        """
        expect = "Type Mismatch In Statement: FieldAccess(Self(),Id(k))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        input = """
        class main {
            final int k = 8;
            float foo(int foo,c){
                f := 5;
            }
        }
        """
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """
        class main {
            final int k = 8;
            float foo(int foo,c){
                final int f = 2.0;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(f),IntType,FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """
        class main{
            final int k = 8;
            final B x = 0;
        }
        class B{
            int e;
            B() {

            }
        }
        """
        expect = "Type Mismatch In Expression: IntLit(0)"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        input = """
        class main extends B{
            B x = nil;
            int c = this.x.e;
        }
        class B{
            int e;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        input = """
        class main{
            final int k = 8;
            int foo(){
                return k % 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(k),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input = """
        class X{
            static final int k = 8;
            int foo(){
                X X;
                return X.k;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(X),Id(k))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """
        class X{
            int foo(){
                int[5] a = {true, 1.2};
            }
        }
        """
        expect = "Illegal Array Literal: [BooleanLit(True),FloatLit(1.2)]"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """
        class X{
            final float[3] k = {4.5,2.3,4.6,true};
        }
        """
        expect = "Illegal Array Literal: [FloatLit(4.5),FloatLit(2.3),FloatLit(4.6),BooleanLit(True)]"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """
        class X{
            final float[3] k = {4.5,2.3,4.6, "a"};
        }
        """
        expect = """Illegal Array Literal: [FloatLit(4.5),FloatLit(2.3),FloatLit(4.6),StringLit("a")]"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """
        class X{
            final int[3] k = {4,6,7};
            final float[3] e = this.k;
            int e;
        }
        """
        expect = "Redeclared Attribute: e"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """
        class X{
            final int a = 1 + this.b;
            final int b = 9 && 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLit(9),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """
        class X{
            int main(){
                int i;
                float a;
                boolean b;
                string s;
                io.writeBool(b);
                io.writeBoolLn(b);
                s := io.readStr();
                io.writeStr(s);
                io.writeStrLn(s);
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
        class A {
            int get(int a; float b) {} 
        }
        class B {
            int get; 
        }
        class C {
            B b = new B(); 
            int get = b.get();
        }
        """
        expect = "Undeclared Method: get"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """
        class B{
            final int e = 5 && 2;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLit(5),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """
        class A{
            A A;
            static int c;
            int a;
            int b = this.A.a;
            int d = this.A.c;
        }
        """
        expect = "Type Mismatch In Statement: FieldAccess(FieldAccess(Self(),Id(A)),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        input = """
        class A{
            A d;
            int a;
            int k = A.a;
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """
        class A{
            final int x;
        }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        input = """
        class Test {
            int fun(){
                Test a;
                a := new Test(9);
                a.b := 0;
            }
        }
        """
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        input = """
        class Test {
            final int c = 9;
            int fun(){
                this.c := 0;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(c)),IntLit(0))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """
        class A{
            int foo() {
                B x;
                int a = x.c;
            }
        }
        class B{
            int b;
        }
        """
        expect = "Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        input = """
        class x {
            int foo(){
                int b = io.readBool();
                int a;
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(io),Id(readBool),[])"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_52(self):
        input = """
        class x {
            int foo(){
                int a;
                a := 1 + 2.2;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLit(1),FloatLit(2.2)))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """
        class hello {
            int foo(){
                this.a := 2;
            }

        }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_54(self):
        input = """
        class A{
            final int[3] a = {1, 2, 3};
            int foo(){
                a[1] := 3;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),IntLit(1)),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_55(self):
        input = """
        class A{}
        class B extends A{}
        class B{}
        """
        expect = "Redeclared Class: B"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_56(self):
        input = """
        class main{
            boolean q,w,r,t,a;
            int b(int a,b,c; float d) {
                int x;
                string b;
            } 
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input = """
        class main{
            foo(){}
            foo(int a){}
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        input = """
        class B{
            A x;
            int boo(){
                return this.x.foo(5,4, this.x);
            }
        }
        class A{
            void foo(float c,d; A n){}
        }
        """
        expect = "Type Mismatch In Statement: CallExpr(FieldAccess(Self(),Id(x)),Id(foo),[IntLit(5),IntLit(4),FieldAccess(Self(),Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_59(self):
        input = """
        class x {
            int a,b;
        }
        class y {
            x a,b;
            static x m;
            final x x = nil;
            int foo() {
                x := new x();
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(x),NewExpr(Id(x),[]))"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_60(self):
        input = """
        class hello {
                int foo(){
                    x := x && 3;
                }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = """
        class x {}
        class y {
            C a;
        }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        input = """
        class y {
            int main(int a,b; float c){
                ABC x;
            }
        }
        """
        expect = "Undeclared Class: ABC"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        input = """
        class y {
            int main(int[5] a,b; float c){
                A d;
            }
        }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_64(self):
        input = """
        class y {
            int main(int[5] b; float c){
                b := {1.3, 2.4, 3.2, 4.4, 5.6};
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),[FloatLit(1.3),FloatLit(2.4),FloatLit(3.2),FloatLit(4.4),FloatLit(5.6)])"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_65(self):
        input = """
        class C{
            int c;
            final int k = true;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(k),IntType,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_66(self):
        input = """
        class hello {
            int a = -"aa";
        }
        """
        expect = """Type Mismatch In Expression: UnaryOp(-,StringLit("aa"))"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        input = """
        class hello {
              int foo(){
              this.a();
              }
        }
        """
        expect = "Undeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        input = """
        class A{
            static int k;
            int foo(){
                int c = A.k % 12.2;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,FieldAccess(Id(A),Id(k)),FloatLit(12.2))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = """
        class  A extends  B{
            int foo(){
                A  x;
                int a = x.c  ;
            }
        }
        class  B{
            static int  c;
        }

        """
        expect = "Illegal Member Access: FieldAccess(Id(x),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = """
        class A{
            int  foo(){
                return this.boo;
            }
        }
        

        """
        expect = "Undeclared Attribute: boo"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_71(self):
        input = """
        class A extends B{
            int  foo(){
                A A;
                return A.b;
            }
        }
        class  B{
            static final int b = 0;
        }

        """
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = """
        class hello {
            int b(){}
            int foo(){
                int a;
                if 1 then a:=0;
            }
        }
        """
        expect = "Type Mismatch In Statement: If(IntLit(1),AssignStmt(Id(a),IntLit(0)))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_73(self):
        input = """
         class x {
            int a,b;
            final int c=0;
            int foo() {
                x m;
                int a = 7;
                float n;
                m.a := 6;
                if 1+2==3 then m.a := 6; else m.b := 7;
                for a := 1+22*3+2 to m.c do m.a := 1;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_74(self):
        input = """
         class x {
            int foo() {
                x m;
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_75(self):
        input = """
        class x{
            XA a;
        }
        """
        expect = "Undeclared Class: XA"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_76(self):
        input = """
         class x {
            final int c=15*152-151;
            int foo(int a,v,b) {
            }
            void main() {
                x d;
                d.foo(1,2,3);
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(d),Id(foo),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_77(self):
        input = """
        class hello extends A {
            int foo(){
                int a = this.boo();
            }
        }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_78(self):
        input = """
        class hello {
            static int foo;
            int main(){
                int hello;
                int b = hello.foo ^ "aaa";
            }
        }
        """
        expect = "Type Mismatch In Expression: FieldAccess(Id(hello),Id(foo))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_79(self):
        input = """
        class hello {
            static int foo;
            int main(){
                return this.man;
            }
        }
        """
        expect = "Undeclared Attribute: man"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_80(self):
        input = """
        class hello {
            static int foo;
            int main(){
                return this.man && 2;
            }
        }
        """
        expect = "Undeclared Attribute: man"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_81(self):
        input = """
        class hello {
        int b(){}
        int foo(){
            int x;
            int i;
        for i := 1 to 100 do 
            io.writeIntLn(i);
    
        for x := 5 downto 2 do
            io.writeIntLn(x);

        this.d := 0;
        """
        expect = "Undeclared Attribute: d"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_82(self):
        input = """class hello {
            int b(){}
            int foo(){
                int x;
                int i;
                for i := 1 to 100 do
                continue;
                io.writeIntLn(x);
                this.d := 0;
            }
        }
          """
        expect = """Undeclared Attribute: d"""

        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = """
        class D{
            static int foo(int a){}
            float main(){
                return 5 + 3;
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_84(self):
        input = """
        class X{
            int[5] abiwe = {1,2,3,true};
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),IntLit(3),BooleanLit(True)]"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_85(self):
        input = """
        class X{
            int foo(){
                int i;
                for i := 5 to true do
                    break;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(5),BooleanLit(True),True,Break])"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        input = """
        class A{
            static int get(){}
        }
        class B extends A{
            int get;
            void foo(){
                B x;
                int a = x.get();
            }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(x),Id(get),[])"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_87(self):
        input = """
         class x extends y{
            int a,b;
            final int c = 2;
            static int m;
        }
        
        """
        expect = "Undeclared Class: y"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_88(self):
        input = """
        class a {
            final int x = 3 / 2;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,BinaryOp(/,IntLit(3),IntLit(2)))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_89(self):
        input = """
         class a extends b{
            final b y = x;
        }
        class b{}
        class c{}
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_90(self):
        input = """
         class A{
            B x;
            int n = this.x.m;
        }
        class B{
            int m;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_91(self):
        input = """
         class a {
            int b;
            void main(){
                int a;
                for a := this.b to 7 do 
                    continue;
                a := a.b;
            }
        }
        """
        expect = "Type Mismatch In Expression: FieldAccess(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_92(self):
        input = """
        class A{
            int a;
        }
        class B extends A{
            void foo(){
                A.a();
            }
        }
        """
        expect = "Undeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_93(self):
        input = """
        class A{
            int a = io.readInt();
            int c = io.readStr();
            void main(){
                int k;
                boolean b;
                io.writeFloat(k);
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(io),Id(readStr),[])"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_94(self):
        input = """
        class A{
            void main(){
                int a = io.writeFloat();
            }
        }
        """
        expect = "Type Mismatch In Statement: CallExpr(Id(io),Id(writeFloat),[])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_95(self):
        input = """
        class A{
            void main(){
                int a;
                for a := 8 downto 9.5 do
                    io.writeInt(a);
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(a),IntLit(8),FloatLit(9.5),False,Call(Id(io),Id(writeInt),[Id(a)])])"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_96(self):
        input = """
        class b {
            final float z = 6.5;
            final int c = 5 + this.z;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(c),IntType,BinaryOp(+,IntLit(5),FieldAccess(Self(),Id(z))))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_97(self):
        input = """
         class x extends y{
            int a,b;
            int foo(int a,v,b) {
                x d;
            }
            void main() {
                x d;
                int m;
                d.foo(2,3,4);
            }
        }
        class y {
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(d),Id(foo),[IntLit(2),IntLit(3),IntLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_98(self):
        input = """
         class x extends y{
            int a,b;
            static int m;
            int foo(int a,v,b) {
                return m ^ "a";
            }
        }
        class y {
        }
        """
        expect = """Type Mismatch In Expression: BinaryOp(^,Id(m),StringLit("a"))"""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_99(self):
        input = """
        class x extends A{
            final int a = this.x + this.g;
        }
        class A{
            final int g = 0;
        }
        """
        expect = "Undeclared Attribute: x"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_100(self):
        input = """
        class A{
            int[4] foo(){
                int[3] a;
                return a;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,500))

