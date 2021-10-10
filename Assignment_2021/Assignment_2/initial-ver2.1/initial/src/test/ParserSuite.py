import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # Test var declare
    def test_var_decl_1(self):
        input = """
            class program {
                int a;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_var_decl_2(self):
        input = """class program {
                int a, c, d, e, f;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_var_decl_3(self):
        input = """class program {
                float a = 1 + 2 + 3;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_var_decl_4(self):
        input = """class program {
                float a = 0, b = 1, c = 2, d = 10 + a;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_var_decl_5(self):
        input = """class program {
                int a;
                float b;
                string e = "abcdef", b, c, d = "";
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_var_decl_6(self):
        input = """class program {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                string e = "abcdef", b, c, d = "";
                int[5] b = {123,45};
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_var_decl_7(self):
        input = """class program {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                string e = "abcdef", b, c, d = "";
                int[5] b = {123,45};
                float[2] d = {123, "'", 12345, "12", 0};
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_var_decl_8(self):
        input = """class program {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                string e = "abcdef", b, c, d = "";
                int[5] b = {123,45};
                float[2] d = {123, "'", 12345, "12", 0};
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_var_decl_9(self):
        input = """class program {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                string e = "abcdef", b, c, d = "";
                int[5] b = {123,45};
                float[2] d = {123, "'", 12345, "12", 0};
                string[12] aeE = {"12", "0012321", 12E-5, 20e+8};
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_var_decl_10(self):
        input = """class program {
                float b, c ,d ,e ,f = 5.0, g = 12E-10;
                string e = "abcdef", b, c, d = "";
                int[5] b = {123,45};
                float[2] d = {123, "'", 12345, "12", 0};
                string[12] stringA = {"12", "0012321", 12E-5, 20e+8};
                /* This is a comment string[45] abd */
                # string c = "abcdef", d = "", e = "\"";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    # Test assign statement
    def test_assign_1(self):
        input = """
        class program {
            int a = 0;
            int b = 0;
            float c = 0;
            int func(int a, b; float c) {
                a := b + c * this.c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_assign_9(self):
        input = """
        class program {
            program() {
                a[b[2] + c] := 0;
                c[2 * this.foo(3) + x.g(2)] := 0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_assign_10(self):
        input = """
        class program {
            program() {
                a[b[2] + c] := 0;
                c[2 * this.foo(3) + x.g(2)] := b[ab[2] * 5 + 10];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))


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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

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
                    a := 0;
                    d := d * b;
                    c := c ^ d;
                    e := e * f;
                    g := g + h;
                else return 0;
            } 
        }
        """
        expect = "Error on line 16 col 16: else"
        self.assertTrue(TestParser.test(input, expect, 236))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

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
                    return x.foo(2);
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

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
                if a = b / 2 * 5 then
                    c := c - 1;
                else
                    c := c % a;
            } 
        }
        """
        expect = "Error on line 14 col 21: ="
        self.assertTrue(TestParser.test(input, expect, 239))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    # Test for statement
    def test_for_1(self):
        input = """
        class program {
            program(int a, b, c; string d) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    b := b + 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_for_8(self):
        input = """
        program(int a, b, c; string d; boolean e) {
                a = 0;
                b = 0;
                for a = 5 to 10 do 
                    for b = 15 downto 1 do
                        for c = 0 downto -10 do
                            if c == 0 then
                                if d == "" then
                                    if e == false then
                                        d = d ^ "abc";
                                    else
                                        c = 1;
        }
        """
        expect = "Error on line 2 col 8: program"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_for_9(self):
        input = """
        program(int a, b, c; string d; boolean e) {
                a = 0;
                b = 0;
                for a = 5 to 10 do 
                    for b = 15 downto 1 do
                        for c = 0 downto -10 do
                            if c == 0 then
                                if d == "" then
                                    if e == false then
                                        if a == b + c % c then
                                            c = -1;
        }
        """
        expect = "Error on line 2 col 8: program"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_for_10(self):
        input = """
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
        """
        expect = "Error on line 2 col 8: program"
        self.assertTrue(TestParser.test(input, expect, 250))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_break_3(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        for b := 5 to 10 do 
                            break;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_break_5(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    break
            }
        }
        """
        expect = "Error on line 8 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 255))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_continue_3(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        for c := 10 to 15 do
                           if c == 12 then
                                continue;
                            else 
                                c := c + 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_continue_4(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    for b := 5 to 10 do 
                        for c := 10 to 15 do
                           if c == 12 then
                                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_continue_5(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    continue
            }
        }
        """
        expect = "Error on line 8 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 260))

    # Test return statement

    def test_return_1(self):
        input = """
        class program {
            program() {
                return a[b[2]] + 3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_return_2(self):
        input = """
        class program {
            program() {
                return a[b[2]]*a[b]+this.length;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_return_3(self):
        input = """
        class program {
            program() {
                return a[b[2]]*a[b]+this.length+this.width / 2 * x.foo(3,4,5);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_return_4(self):
        input = """
        class program {
            string func() {
                return "";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_return_5(self):
        input = """
        class program {
            program() {
                return a[b[2]]*a[b]+this.length+this.width / 2 * x.foo(3,4,5)
            }
        }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_return_6(self):
        input = """
        class program {
            program() {
                return a[b[2]]*a[b]+this.length+this.width / 2 * x.foo(a,b,c,d) + this.foo(2,3,4);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_return_7(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    return a[b[c[2]]] + 3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_return_8(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    if b == 0 then
                        return a[b[c[2]]] + 3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_return_10(self):
        input = """
        class program {
            program(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do 
                    if b == 0 then
                        return a[b[c[2]]] + 3;
                    else
                        return a[b + x.foo(a)] + 3
            }
        }
        """
        expect = "Error on line 11 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 270))

    # Test random
    def test_random_1(self):
        input = """
        clas program {
                   
        }
        """
        expect = "Error on line 2 col 8: clas"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_random_2(self):
        input = """
        class program 

        }
        """
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_random_3(self):
        input = """
        class program {
            program a;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_random_4(self):
        input = """
        class program {
            final int b
        }
        """
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_random_5(self):
        input = """
        class program {
            int[2] ;
        }
        """
        expect = "Error on line 3 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_random_6(self):
        input = """
        class program {
            void func(int a,b) {
                return a == b % 2;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

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
        class program2 {
            int width = 0;
            int length = 0;
            program2() {
                program pg1 = new program();
                return this.width * this.length;
            }
        }
        """
        expect = "Error on line 23 col 28: ="
        self.assertTrue(TestParser.test(input, expect, 280))

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
                program pg1 = new program();
                return this.width * this.length;
            }
            static int func() {
                return "";
            }
        }
        """
        expect = "Error on line 23 col 28: ="
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_random_12(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_random_13(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000 a, b;
        }
        """
        expect = "Error on line 4 col 26: a"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_random_14(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000 a, b;
        }
        """
        expect = "Error on line 4 col 26: a"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_random_15(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_random_17(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_random_21(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                return 0
            }
        }
        """
        expect = "Error on line 8 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_random_22(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b, float c) {
                return 0;
            }
        }
        """
        expect = "Error on line 6 col 34: float"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_random_23(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b, float c) {
                return 0;
            }
        }
        """
        expect = "Error on line 6 col 34: float"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_random_24(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b; float c) {
                if a == 0 then
                    b := b + 1;
                if b == 0 then
                    b := b - a;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_random_25(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string funcint a, b, float c) {
                if a == 0 then
                    b = b + 1;
                if b == 0 then
                    b = b - a;
                else
                    c = d - 5 * 9 % 3;
                if d == 0 then
                    a = 0;
                else
                    c = 12E-8 + 5;
            }
        }
        """
        expect = "Error on line 6 col 27: a"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_random_26(self):
        input = """
        class program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b, float c) {
                return 0;
            }
        }
        """
        expect = "Error on line 6 col 34: float"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_random_27(self):
        input = """
        clas program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b, float c) {
                for a = 5 to 10 do 
                    for b = 5 to 10 do 
                        for b = 5 to 10 do 
                            for c = 15 downto 10 do 
                                break;
            }
        }
        """
        expect = "Error on line 2 col 8: clas"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_random_28(self):
        input = """
        clas program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b, float c) {
                for a = 5 to 10 do 
                    for b = 5 to 10 do 
                        for b = 5 to 10 do 
                            for c = 15 downto 10 do 
                                break;
            }
        }
        """
        expect = "Error on line 2 col 8: clas"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_random_29(self):
        input = """
        clas program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b, float c) {
                for a = 5 to 10 do 
                    for b = 5 to 10 do 
            }
        }
        """
        expect = "Error on line 2 col 8: clas"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_random_30(self):
        input = """
        clas program {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b, float c) {
                return 0;
            }
        }
        """
        expect = "Error on line 2 col 8: clas"
        self.assertTrue(TestParser.test(input, expect, 300))





