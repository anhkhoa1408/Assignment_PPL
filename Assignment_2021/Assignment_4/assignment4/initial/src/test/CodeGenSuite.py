from dataclasses import Field
import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_0(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myCar"),
                                        ClassType(Id("Main")),
                                        NewExpr(Id("Main"), []),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("myCar"),
                                        Id("fullThrottle"),
                                        [],
                                    ),
                                    CallStmt(
                                        Id("myCar"),
                                        Id("speed"),
                                        [StringLiteral('"200"')],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                ClassDecl(
                    Id("Main"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("fullThrottle"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStrLn"),
                                        [
                                            StringLiteral(
                                                '"The car is going as fast as it can!"'
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Instance(),
                            Id("speed"),
                            [VarDecl(Id("maxSpeed"), StringType())],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStrLn"),
                                        [
                                            BinaryOp(
                                                "^",
                                                StringLiteral('"Max speed is: "'),
                                                Id("maxSpeed"),
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "The car is going as fast as it can!\nMax speed is: 200\n"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
    def test_1(self):
        input = """
            class BKoolClass {
                int x=5;
                static void main(){
                    BkoolClass myObj1 = new BKoolClass();
                    BkoolClass myObj2 = new BKoolClass();
                    int a=100;
                    myObj2.x := 25;
                    io.writeInt(myObj2.x+myObj1.x+a);
                }
            }
        """
        expect = "130"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_2(self):
        input = """
            class BKoolClass{
                int b=1;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    io.writeInt(bk.b);
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_3(self):
        input = """
            class BKoolClass{
                int a=10;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if 1 < 17 then {
                        io.writeInt(bk.a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_4(self):
        input = """
            class BKoolClass{
                int a=10;
                float b=2.5;
                string c="bk";
                boolean d= true;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if 1 < 17 then {
                        io.writeInt(bk.a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_5(self):
        input = """
            class BKoolClass{
                int a=10;
                float b=2.5;
                string c="bk";
                boolean d= true;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if bk.d then {
                        io.writeInt(bk.a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_6(self):
        input = """
            class BKoolClass{
                int a=10;
                float b=2.5;
                string c="bk";
                boolean d= true;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if bk.d then {
                        io.writeStr(bk.c);
                    }
                }
            }
        """
        expect = "bk"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_7(self):
        input = """
            class BKoolClass{
                int value = 100;
                void foo(int x){
                    io.writeInt(x);
                }
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    bk.foo(100);
                    
                }
            }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_8(self):
        input = """
            class BKoolClass{
                int a=10;
                int b=20;
                int foo(int x){
                    return x;
                }
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    if bk.a < bk.b then
                        bk.a := bk.b;             
                    io.writeInt(bk.a);       
                }
            }
        """
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_9(self):
        input = """
            class BKoolClass{
                
                static void main(){ 
                    int a=0;
                    for a := 5 to 10 do
                        io.writeInt(a);
                }
            }
        """
        expect = "5678910"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_10(self):
        input = """
            class BKoolClass{
                int z=0;                
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    int a=0;
                    for a := 5 to 10 do
                        bk.z := bk.z +1;
                    io.writeInt(bk.z);
                }
            }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_11(self):
        input = """
            class BKoolClass{
                int z=6;   
                void foo(){
                    io.writeInt(this.z);
                }             
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    bk.foo();
                }
            }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_12(self):
        input = """
            class A {
                int e;
            }
            class BKoolClass {
                int x = 0;
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    bk.x := 25;
                    io.writeInt(bk.x);   
                }
            }
        """
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    
    def test_13(self):
        input = """class BKoolClass {static void main() {io.writeBool(true);}}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    
    def test_14(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    
    def test_15(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    
    def test_16(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 19\\10;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    
    def test_17(self):
        input = """
        class BKoolClass {
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    def test_18(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    
    def test_19(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 50\\47;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    
    def test_20(self):
        input = """
        class BKoolClass {
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    
    def test_21(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    
    def test_22(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 50\\47;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,522))
        
    def test_23(self):
        input = """
        class BKoolClass {
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    
    def test_24(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    
    def test_25(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 50\\47;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_26(self):
        input = """
        class BKoolClass {
            int foo(){
                return 100;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                int zoo=bk.foo();
                io.writeInt(zoo);
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,526))
        
    def test_27(self):
        input = """
        class BKoolClass {
            int foo(){
                return 100;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                io.writeInt(bk.foo());
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,527))
        
    def test_28(self):
        input = """
        class BKoolClass {
            int foo(){
                return 100;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                BKoolClass spkt = new BKoolClass();
                int zoo=bk.foo();
                io.writeInt(zoo+spkt.foo());
            }
        }
        """
        expect = "200"
        self.assertTrue(TestCodeGen.test(input,expect,528))
        
    def test_29(self):
        input = """
        class BKoolClass {
            static int foo(){
                return 100;
            }
            static void main(){
                io.writeInt(BKoolClass.foo());
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    
    def test_30(self):
        input = """
        class BKoolClass {
            static void foo(){
                io.writeFloat(2.51);
            }
            static void main(){
                BKoolClass.foo();
            }
        }
        """
        expect = "2.51"
        self.assertTrue(TestCodeGen.test(input,expect,530))
    
    def test_31(self):
        input = """
        class BKoolClass {
            void foo(){
                io.writeInt(100);
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,531))
    
    def test_32(self):
        input = """
        class BKoolClass {
            int att=20;
            void foo(){
                this.att := 30;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
                io.writeInt(bk.att);
            }
        }
        """
        expect = "30"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    
    def test_33(self):
        input = """
        class BKoolClass {
            int z=10;
            static void main(){
                BKoolClass bk = new BKoolClass();
                io.writeInt(bk.z);
            }
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    
    def test_34(self):
        input = """
        class BKoolClass {
            int att=20;
            void foo(){
                this.att := 70;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
                io.writeInt(bk.att);
            }
        }
        """
        expect = "70"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    
    def test_35(self):
        input = """
        class BKoolClass {
            void foo(){
                io.writeInt(101);
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
            }
        }
        """
        expect = "101"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    def test_36(self):
        input = """
        class BKoolClass {
            void foo(){
                io.writeInt(1);
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                int i=0;
                for i:=1 to 5 do
                    bk.foo();
            }
        }
        """
        expect = "11111"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    def test_37(self):
        input = """
        class BKoolClass {
            static void main(){
                int i=7;
                io.writeBool(i==7);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    def test_38(self):
        input = """
            class BKoolClass{
                static void main(){
                    int a;
                    boolean e;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 2 then {
                            e := 1 < 1;
                            break;
                        }
                    }
                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    
    def test_39(self):
        input = """
            class BKoolClass{
                static void main(){
                    int p = (5%2);
                    io.writeInt(p);
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,539))
    
    def test_40(self):
        input = """
            class BKoolClass{
                static void main(){
                    int i=0;
                    for i:=0 to 10 do{
                        if i%2==0 then{
                            io.writeInt(i);
                        }
                    }
                }
            }
        """
        expect = "0246810"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    def test_41(self):
        input = """
            class BKoolClass {
                int[4] total={0,0,0,0};
                string name;
            
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    bk.total[0] := 9;
                    io.writeInt(bk.total[0]);
                    io.writeInt(bk.total[1]);
                    io.writeInt(bk.total[2]);
                    io.writeInt(bk.total[3]);
            }
        }
        """
        expect = "9000"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test_42(self):
        input = """
            class BKoolClass {
                int[4] total={0,0,0,0};
                void change(int i){
                    this.total[i] := 100;
                }
            
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    int i=0;
                    for i:=0 to 3 do{
                        io.writeInt(bk.total[i]);
                    }
            }
        }
        """
        expect = "0000"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test_43(self):
        input = """
            class BKoolClass {
                int[4] total={0,0,0,0};
                void change(int i){
                    this.total[i] := 7;
                }
            
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    bk.change(2);
                    io.writeInt(bk.total[0]);
                    io.writeInt(bk.total[1]);
                    io.writeInt(bk.total[2]);
                    io.writeInt(bk.total[3]);
                }
            }
        """
        expect = "0070"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    
    def test_44(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(5+10);
                }
            }
            
        """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    
    def test_45(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(88-44);
                }
            }
            
        """
        expect = "44"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    
    def test_46(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(5*10);
                }
            }
            
        """
        expect = "50"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    
    def test_47(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(14%7);
                }
            }
            
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    
    def test_48(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeStr("a"^"bb");
                }
            }
            
        """
        expect = "abb"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    
    def test_49(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeBool((5<7));
                }
            }
            
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,549))
    
    def test_50(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeFloat(10/5);
                }
            }
            
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    
    
    def test_51(self):
        input = """
            class BKoolClass {
                int x=5;
                static void main(){
                    BkoolClass myObj1 = new BKoolClass();
                    BkoolClass myObj2 = new BKoolClass();
                    int a=100;
                    myObj2.x := 25;
                    io.writeInt(myObj2.x+myObj1.x+a);
                }
            }
        """
        expect = "130"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test_52(self):
        input = """
            class BKoolClass{
                int b=1;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    io.writeInt(bk.b);
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    def test_53(self):
        input = """
            class BKoolClass{
                int a=10;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if 1 < 17 then {
                        io.writeInt(bk.a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,553))
    def test_54(self):
        input = """
            class BKoolClass{
                int a=10;
                float b=2.5;
                string c="bk";
                boolean d= true;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if 1 < 17 then {
                        io.writeInt(bk.a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,554))
    def test_55(self):
        input = """
            class BKoolClass{
                int a=10;
                float b=2.5;
                string c="bk";
                boolean d= true;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if bk.d then {
                        io.writeInt(bk.a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,555))
    def test_56(self):
        input = """
            class BKoolClass{
                int a=10;
                float b=2.5;
                string c="bk";
                boolean d= true;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if bk.d then {
                        io.writeStr(bk.c);
                    }
                }
            }
        """
        expect = "bk"
        self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_57(self):
        input = """
            class BKoolClass{
                int value = 100;
                void foo(int x){
                    io.writeInt(x);
                }
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    bk.foo(100);
                    
                }
            }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    def test_58(self):
        input = """
            class BKoolClass{
                int a=10;
                int b=20;
                int foo(int x){
                    return x;
                }
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    if bk.a < bk.b then
                        bk.a := bk.b;             
                    io.writeInt(bk.a);       
                }
            }
        """
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_59(self):
        input = """
            class BKoolClass{
                
                static void main(){ 
                    int a=0;
                    for a := 5 to 10 do
                        io.writeInt(a);
                }
            }
        """
        expect = "5678910"
        self.assertTrue(TestCodeGen.test(input,expect,559))
    def test_60(self):
        input = """
            class BKoolClass{
                int z=0;                
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    int a=0;
                    for a := 5 to 10 do
                        bk.z := bk.z +1;
                    io.writeInt(bk.z);
                }
            }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_60(self):
        input = """
            class BKoolClass{
                int z=6;   
                void foo(){
                    io.writeInt(this.z);
                }             
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    bk.foo();
                }
            }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_61(self):
        input = """
            class A {
                int e;
            }
            class BKoolClass {
                int x = 0;
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    bk.x := 25;
                    io.writeInt(bk.x);   
                }
            }
        """
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    
    def test_62(self):
        input = """class BKoolClass {static void main() {io.writeBool(true);}}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,562))
    
    def test_63(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,563))
    
    def test_64(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,564))
    
    def test_65(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 19\\10;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    
    def test_66(self):
        input = """
        class BKoolClass {
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,566))
    
    def test_67(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    
    def test_68(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 50\\47;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,568))
    
    def test_69(self):
        input = """
        class BKoolClass {
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,569))
    
    def test_70(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    
    def test_71(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 50\\47;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,571))
        
    def test_72(self):
        input = """
        class BKoolClass {
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    
    def test_73(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,573))
    
    def test_74(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 50\\47;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_75(self):
        input = """
        class BKoolClass {
            int foo(){
                return 100;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                int zoo=bk.foo();
                io.writeInt(zoo);
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,575))
        
    def test_76(self):
        input = """
        class BKoolClass {
            int foo(){
                return 100;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                io.writeInt(bk.foo());
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,576))
        
    def test_77(self):
        input = """
        class BKoolClass {
            int foo(){
                return 100;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                BKoolClass spkt = new BKoolClass();
                int zoo=bk.foo();
                io.writeInt(zoo+spkt.foo());
            }
        }
        """
        expect = "200"
        self.assertTrue(TestCodeGen.test(input,expect,577))
        
    def test_78(self):
        input = """
        class BKoolClass {
            static int foo(){
                return 100;
            }
            static void main(){
                io.writeInt(BKoolClass.foo());
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,578))
    
    def test_79(self):
        input = """
        class BKoolClass {
            static void foo(){
                io.writeFloat(2.51);
            }
            static void main(){
                BKoolClass.foo();
            }
        }
        """
        expect = "2.51"
        self.assertTrue(TestCodeGen.test(input,expect,579))
    
    def test_80(self):
        input = """
        class BKoolClass {
            void foo(){
                io.writeInt(100);
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,580))
    
    def test_81(self):
        input = """
        class BKoolClass {
            int att=20;
            void foo(){
                this.att := 30;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
                io.writeInt(bk.att);
            }
        }
        """
        expect = "30"
        self.assertTrue(TestCodeGen.test(input,expect,581))
    
    def test_82(self):
        input = """
        class BKoolClass {
            int z=10;
            static void main(){
                BKoolClass bk = new BKoolClass();
                io.writeInt(bk.z);
            }
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,582))
    
    def test_83(self):
        input = """
        class BKoolClass {
            int att=20;
            void foo(){
                this.att := 70;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
                io.writeInt(bk.att);
            }
        }
        """
        expect = "70"
        self.assertTrue(TestCodeGen.test(input,expect,583))
    
    def test_84(self):
        input = """
        class BKoolClass {
            void foo(){
                io.writeInt(101);
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
            }
        }
        """
        expect = "101"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    def test_85(self):
        input = """
        class BKoolClass {
            void foo(){
                io.writeInt(1);
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                int i=0;
                for i:=1 to 5 do
                    bk.foo();
            }
        }
        """
        expect = "11111"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    def test_86(self):
        input = """
        class BKoolClass {
            static void main(){
                int i=7;
                io.writeBool(i==7);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    def test_87(self):
        input = """
            class BKoolClass{
                static void main(){
                    int a;
                    boolean e;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 2 then {
                            e := 1 < 1;
                            break;
                        }
                    }
                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,587))
    
    
    def test_88(self):
        input = """
            class BKoolClass {
                int[4] total={0,0,0,0};
                string name;
            
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    bk.total[0] := 9;
                    io.writeInt(bk.total[0]);
                    io.writeInt(bk.total[1]);
                    io.writeInt(bk.total[2]);
                    io.writeInt(bk.total[3]);
            }
        }
        """
        expect = "9000"
        self.assertTrue(TestCodeGen.test(input,expect,588))
    def test_89(self):
        input = """
            class BKoolClass {
                int[4] total={0,0,0,0};
                void change(int i){
                    this.total[i] := 100;
                }
            
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    int i=0;
                    for i:=0 to 3 do{
                        io.writeInt(bk.total[i]);
                    }
            }
        }
        """
        expect = "0000"
        self.assertTrue(TestCodeGen.test(input,expect,589))
    def test_90(self):
        input = """
            class BKoolClass {
                int[4] total={0,0,0,0};
                void change(int i){
                    this.total[i] := 7;
                }
            
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    bk.change(2);
                    io.writeInt(bk.total[0]);
                    io.writeInt(bk.total[1]);
                    io.writeInt(bk.total[2]);
                    io.writeInt(bk.total[3]);
                }
            }
        """
        expect = "0070"
        self.assertTrue(TestCodeGen.test(input,expect,590))
    
    def test_91(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(5+10);
                }
            }
            
        """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,591))
    
    def test_92(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(88-44);
                }
            }
            
        """
        expect = "44"
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test_93(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(5*10);
                }
            }
            
        """
        expect = "50"
        self.assertTrue(TestCodeGen.test(input,expect,593))
    
    def test_94(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(14%7);
                }
            }
            
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,594))
    
    def test_95(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeStr("a"^"bb");
                }
            }
            
        """
        expect = "abb"
        self.assertTrue(TestCodeGen.test(input,expect,595))
    
    def test_96(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeBool((5<7));
                }
            }
            
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,596))
    
    def test_97(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeFloat(10/5);
                }
            }
            
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,597))
    
    def test_98(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeBool((1<2) || (5<7));
                }
            }
            
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,598))
    
    def test_99(self):
        input = """
            class MP{
                int a=11;
                void foo(){
                    io.writeInt(11);
                }
            }
            class BKoolClass extends MP{
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    bk.foo();
                }
            }
            
        """
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,599))

    
        
    