import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """
        class a {
            int c;
            final int a = 1;
            b b = new b();
            int foo() {
                b.foo();
            }
        }

        class b {
            b() {

            }
            void foo() {

            }
        }

        class c {

        }

        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,401))

    