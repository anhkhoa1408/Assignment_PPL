import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """
        class a {
            int a = 0;
            final float b = 0.2;
            int c = 0;
            boolean d = false;
            static boolean e = false;
            int foo(int b) {
                this.foo2();
            }
            void foo2() {
            }
        }

        

        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,401))

    