import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_1(self):
    #     input = """
    #         class BKoolClass {
    #             static final int z = 22;
                

    #             int foo(int a; int b) {
    #                 int t = 0;
    #                 string abc = "avkjn";
    #                 z := +1;
    #                 abc := "1";
    #             }
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))

    # def test_2(self):
    #     input = """
    #         class BKoolClass {
                
    #             static final int a = 12123;
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))



    # def test_3(self):
    #     input = """
    #         class BKoolClass {
    #             static final int z = 22;
    #             static int l = 1;
    #             int j, k, p, q, r;
    #             static int c = 100;
    #             final int l = 1000;
    #             string a = "lll";
    #             int b = 10;
    #             final boolean qwew = true;
    #             final boolean wf9ekp = false;

    #             static int foo() {
    #                 int afnalfjoi = 0;
    #                 qwew := !wf9ekp;
    #                 b := -b + l;
    #             }
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))

    # def test_4(self):
    #     input = """
    #         class BKoolClass {
    #             static final int z = 22;
    #             static int l = 1;
    #             int j, k, p, q, r;
    #             static int c = 100;
    #             final int l = 1000;
    #             string a = "lll";
    #             int b = 10;
    #             final boolean qwew = true;
    #             final boolean wf9ekp = false;

    #             static int foo() {
    #                 int afnalfjoi = 0;
    #                 qwew := !wf9ekp;
    #                 b := -b + l;
    #             }

    #             int foo2() {
    #                 a := "woewoii";
    #                 b := b / 10;
    #             }
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))

    # def test_5(self):
    #     input = """
    #         class BKoolClass {
    #             static final int z = 22;
    #             static int l = 1;
    #             int j, k, p, q, r;
    #             static int c = 100;
    #             final int l = 1000;
    #             string a = "lll";
    #             int b = 10;
    #             final boolean qwew = true;
    #             final boolean wf9ekp = false;

    #             static int foo() {
    #                 int afnalfjoi = 0;
    #                 qwew := !wf9ekp;
    #                 b := -b + l;
    #             }
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))

    # def test_6(self):
    #     input = """
    #         class BKoolClass {
    #             BkoolClass bk = new BkoolClass();
    #             int c = 0;
    #             int d = e.foo(1, 2 * 2) + 1;
    #             static int sjoefij = 1;
    #             D e = new D(1,2);

    #             int foo1() {
    #                 int aeopw, uriuwm;
    #                 BKoolClass basd = new BKoolClass();
    #                 c := D.c;
    #                 return c * this.d;
    #             }

    #             float foo2() {
    #                 return this.c + this.d - sjoefij;
    #             }
    #         }

    #         class D {
    #             int z = 0;
    #             static int c = 1;
    #             static int foo() {
    #                 return 0;
    #             }


               
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_7(self):
    #     input = """
    #         class BKoolClass {
    #             BkoolClass bk = new BkoolClass();
    #             int c = 0;
    #             int d = e.foo(1, 2 * 2) + 1;
    #             static int sjoefij = 1;
    #             D e = new D(1,2);
    #             BKoolClass bas = new BKoolClass();

    #             int foo1() {
    #                 int aeopw, uriuwm;
    #                 BKoolClass basd = new BKoolClass();
    #                 c := D.c;
    #                 return c * this.d;
    #             }

    #             float foo2() {
    #                 c := this.bas.e.z;
    #                 c := bas.c;
    #                 return 0;
    #             }   
    #         }

    #         class D {
    #             int z = 0;
    #             static int c = 1;
    #             static int foo() {
    #                 return 0;
    #             }
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))


    # def test_8(self):
    #     input = """
    #         class BKoolClass {
    #             BkoolClass bk = new BkoolClass();
    #             int c = 0;
    #             int d = e.foo(1, 2 * 2) + 1;
    #             static int sjoefij = 1;
    #             D e = new D(1,2);
    #             BKoolClass bas = new BKoolClass();

    #             int foo1() {
    #                 int aeopw, uriuwm;
    #                 BKoolClass basd = new BKoolClass();
    #                 c := D.c;
    #                 return c * this.d;
    #             }

    #             float foo2() {
    #                 c := this.bas.e.z;
    #                 c := bas.c;
    #                 return 0;
    #             }   
    #         }

    #         class D {
    #             int z = 0;
    #             static int c = 1;
    #             static int foo() {
    #                 return 0;
    #             }
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_9(self):
        input = """
            class BKoolClass {
                BkoolClass bk = new BkoolClass();
                int c = 0;
                int d = e.foo(1, 2 * 2) + 1;
                static int sjoefij = 1;
                D e = new D(1,2);
                BKoolClass bas = new BKoolClass();

                int foo1() {
                    int aeopw, uriuwm;
                    BKoolClass basd = new BKoolClass();
                    c := D.c;
                    return c * this.d;
                }

                float foo2() {
                    c := this.bas.e.z;
                    return 0;
                }   
            }

            class D {
                int z = 0;
                static int c = 1;
                static BKoolClass bk2 = new BKoolClass();
                static int foo() {
                    return 0;
                }

                int foo2() {
                    return 0;
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,509))


    
    