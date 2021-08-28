# Generated from d:\Assignment_PPL\assignment2\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0215\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\3\3\5\3\u009f\n\3\3\3\6\3\u00a2\n\3\r")
        buf.write("\3\16\3\u00a3\3\3\3\3\3\3\7\3\u00a9\n\3\f\3\16\3\u00ac")
        buf.write("\13\3\3\3\5\3\u00af\n\3\3\3\6\3\u00b2\n\3\r\3\16\3\u00b3")
        buf.write("\3\3\3\3\5\3\u00b8\n\3\3\4\3\4\7\4\u00bc\n\4\f\4\16\4")
        buf.write("\u00bf\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u018f\n\62\f")
        buf.write("\62\16\62\u0192\13\62\3\62\3\62\3\62\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\3")
        buf.write("9\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\5>\u01b2\n>\3?\3?\3")
        buf.write("?\3@\3@\3@\3A\3A\3A\3A\7A\u01be\nA\fA\16A\u01c1\13A\3")
        buf.write("B\3B\3B\3B\7B\u01c7\nB\fB\16B\u01ca\13B\3C\5C\u01cd\n")
        buf.write("C\3C\3C\7C\u01d1\nC\fC\16C\u01d4\13C\3D\3D\3E\3E\5E\u01da")
        buf.write("\nE\3E\6E\u01dd\nE\rE\16E\u01de\3F\3F\3G\3G\3G\3H\6H\u01e7")
        buf.write("\nH\rH\16H\u01e8\3H\3H\3I\3I\7I\u01ef\nI\fI\16I\u01f2")
        buf.write("\13I\3J\3J\3J\3K\3K\7K\u01f9\nK\fK\16K\u01fc\13K\3K\3")
        buf.write("K\3L\3L\7L\u0202\nL\fL\16L\u0205\13L\3L\3L\3L\3L\3M\3")
        buf.write("M\3M\3M\7M\u020f\nM\fM\16M\u0212\13M\3M\3M\4\u0190\u0210")
        buf.write("\2N\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{\2}\2\177\2\u0081?\u0083@\u0085A\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008fB\u0091C\u0093D\u0095E\u0097F")
        buf.write("\u0099G\3\2\21\t\2\n\f\16\17$$))GHQQ^^\t\2))^^ddhhppt")
        buf.write("tvv\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\63;\3\2\62")
        buf.write("9\3\2\62;\4\2GGgg\4\2--//\5\2\13\f\16\17\"\"\3\2c|\6\2")
        buf.write("\62;C\\aac|\r\2))GGQQSSVW^^ddhhppttvv\2\u0223\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u008f\3\2\2\2")
        buf.write("\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\3\u009b\3\2\2\2\5\u00b7\3\2\2")
        buf.write("\2\7\u00b9\3\2\2\2\t\u00c3\3\2\2\2\13\u00c8\3\2\2\2\r")
        buf.write("\u00ce\3\2\2\2\17\u00d7\3\2\2\2\21\u00da\3\2\2\2\23\u00df")
        buf.write("\3\2\2\2\25\u00e6\3\2\2\2\27\u00ee\3\2\2\2\31\u00f4\3")
        buf.write("\2\2\2\33\u00fb\3\2\2\2\35\u0104\3\2\2\2\37\u0108\3\2")
        buf.write("\2\2!\u0111\3\2\2\2#\u0114\3\2\2\2%\u011e\3\2\2\2\'\u0125")
        buf.write("\3\2\2\2)\u012a\3\2\2\2+\u012e\3\2\2\2-\u0134\3\2\2\2")
        buf.write("/\u0139\3\2\2\2\61\u013f\3\2\2\2\63\u0145\3\2\2\2\65\u014a")
        buf.write("\3\2\2\2\67\u014c\3\2\2\29\u014e\3\2\2\2;\u0150\3\2\2")
        buf.write("\2=\u0152\3\2\2\2?\u0154\3\2\2\2A\u0157\3\2\2\2C\u015a")
        buf.write("\3\2\2\2E\u015d\3\2\2\2G\u0160\3\2\2\2I\u0162\3\2\2\2")
        buf.write("K\u0165\3\2\2\2M\u0168\3\2\2\2O\u016b\3\2\2\2Q\u016e\3")
        buf.write("\2\2\2S\u0170\3\2\2\2U\u0172\3\2\2\2W\u0175\3\2\2\2Y\u0178")
        buf.write("\3\2\2\2[\u017c\3\2\2\2]\u017f\3\2\2\2_\u0182\3\2\2\2")
        buf.write("a\u0186\3\2\2\2c\u018a\3\2\2\2e\u0198\3\2\2\2g\u019a\3")
        buf.write("\2\2\2i\u019c\3\2\2\2k\u019e\3\2\2\2m\u01a0\3\2\2\2o\u01a2")
        buf.write("\3\2\2\2q\u01a4\3\2\2\2s\u01a6\3\2\2\2u\u01a8\3\2\2\2")
        buf.write("w\u01aa\3\2\2\2y\u01ac\3\2\2\2{\u01b1\3\2\2\2}\u01b3\3")
        buf.write("\2\2\2\177\u01b6\3\2\2\2\u0081\u01b9\3\2\2\2\u0083\u01c2")
        buf.write("\3\2\2\2\u0085\u01cc\3\2\2\2\u0087\u01d5\3\2\2\2\u0089")
        buf.write("\u01d7\3\2\2\2\u008b\u01e0\3\2\2\2\u008d\u01e2\3\2\2\2")
        buf.write("\u008f\u01e6\3\2\2\2\u0091\u01ec\3\2\2\2\u0093\u01f3\3")
        buf.write("\2\2\2\u0095\u01f6\3\2\2\2\u0097\u01ff\3\2\2\2\u0099\u020a")
        buf.write("\3\2\2\2\u009b\u009c\7\62\2\2\u009c\4\3\2\2\2\u009d\u009f")
        buf.write("\5\67\34\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00a1\3\2\2\2\u00a0\u00a2\5\u0087D\2\u00a1\u00a0\3\2")
        buf.write("\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00aa\5w<\2\u00a6\u00a9")
        buf.write("\5\u0087D\2\u00a7\u00a9\5\u0089E\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3")
        buf.write("\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00b8\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ad\u00af\5\67\34\2\u00ae\u00ad\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00b2\5\u0087")
        buf.write("D\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00b6\5\u0089E\2\u00b6\u00b8\3\2\2\2\u00b7\u009e\3\2")
        buf.write("\2\2\u00b7\u00ae\3\2\2\2\u00b8\6\3\2\2\2\u00b9\u00bd\7")
        buf.write("$\2\2\u00ba\u00bc\5{>\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf")
        buf.write("\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c1\7$\2\2")
        buf.write("\u00c1\u00c2\b\4\2\2\u00c2\b\3\2\2\2\u00c3\u00c4\7D\2")
        buf.write("\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7f\2\2\u00c6\u00c7\7")
        buf.write("{\2\2\u00c7\n\3\2\2\2\u00c8\u00c9\7D\2\2\u00c9\u00ca\7")
        buf.write("t\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7m\2\2\u00cd\f\3\2\2\2\u00ce\u00cf\7E\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\16\3\2\2\2\u00d7\u00d8\7F\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\20\3\2\2\2\u00da\u00db\7G\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7g\2\2\u00de\22")
        buf.write("\3\2\2\2\u00df\u00e0\7G\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2")
        buf.write("\7u\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7K\2\2\u00e4\u00e5")
        buf.write("\7h\2\2\u00e5\24\3\2\2\2\u00e6\u00e7\7G\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7f\2\2\u00e9\u00ea\7D\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7f\2\2\u00ec\u00ed\7{\2\2\u00ed\26")
        buf.write("\3\2\2\2\u00ee\u00ef\7G\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7f\2\2\u00f1\u00f2\7K\2\2\u00f2\u00f3\7h\2\2\u00f3\30")
        buf.write("\3\2\2\2\u00f4\u00f5\7G\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7f\2\2\u00f7\u00f8\7H\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\32\3\2\2\2\u00fb\u00fc\7G\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7f\2\2\u00fe\u00ff\7Y\2\2\u00ff\u0100")
        buf.write("\7j\2\2\u0100\u0101\7k\2\2\u0101\u0102\7n\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\34\3\2\2\2\u0104\u0105\7H\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\u0107\7t\2\2\u0107\36\3\2\2\2\u0108\u0109")
        buf.write("\7H\2\2\u0109\u010a\7w\2\2\u010a\u010b\7p\2\2\u010b\u010c")
        buf.write("\7e\2\2\u010c\u010d\7v\2\2\u010d\u010e\7k\2\2\u010e\u010f")
        buf.write("\7q\2\2\u010f\u0110\7p\2\2\u0110 \3\2\2\2\u0111\u0112")
        buf.write("\7K\2\2\u0112\u0113\7h\2\2\u0113\"\3\2\2\2\u0114\u0115")
        buf.write("\7R\2\2\u0115\u0116\7c\2\2\u0116\u0117\7t\2\2\u0117\u0118")
        buf.write("\7c\2\2\u0118\u0119\7o\2\2\u0119\u011a\7g\2\2\u011a\u011b")
        buf.write("\7v\2\2\u011b\u011c\7g\2\2\u011c\u011d\7t\2\2\u011d$\3")
        buf.write("\2\2\2\u011e\u011f\7T\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write("\7v\2\2\u0121\u0122\7w\2\2\u0122\u0123\7t\2\2\u0123\u0124")
        buf.write("\7p\2\2\u0124&\3\2\2\2\u0125\u0126\7V\2\2\u0126\u0127")
        buf.write("\7j\2\2\u0127\u0128\7g\2\2\u0128\u0129\7p\2\2\u0129(\3")
        buf.write("\2\2\2\u012a\u012b\7X\2\2\u012b\u012c\7c\2\2\u012c\u012d")
        buf.write("\7t\2\2\u012d*\3\2\2\2\u012e\u012f\7Y\2\2\u012f\u0130")
        buf.write("\7j\2\2\u0130\u0131\7k\2\2\u0131\u0132\7n\2\2\u0132\u0133")
        buf.write("\7g\2\2\u0133,\3\2\2\2\u0134\u0135\7V\2\2\u0135\u0136")
        buf.write("\7t\2\2\u0136\u0137\7w\2\2\u0137\u0138\7g\2\2\u0138.\3")
        buf.write("\2\2\2\u0139\u013a\7H\2\2\u013a\u013b\7c\2\2\u013b\u013c")
        buf.write("\7n\2\2\u013c\u013d\7u\2\2\u013d\u013e\7g\2\2\u013e\60")
        buf.write("\3\2\2\2\u013f\u0140\7G\2\2\u0140\u0141\7p\2\2\u0141\u0142")
        buf.write("\7f\2\2\u0142\u0143\7F\2\2\u0143\u0144\7q\2\2\u0144\62")
        buf.write("\3\2\2\2\u0145\u0146\7O\2\2\u0146\u0147\7c\2\2\u0147\u0148")
        buf.write("\7k\2\2\u0148\u0149\7p\2\2\u0149\64\3\2\2\2\u014a\u014b")
        buf.write("\7-\2\2\u014b\66\3\2\2\2\u014c\u014d\7/\2\2\u014d8\3\2")
        buf.write("\2\2\u014e\u014f\7,\2\2\u014f:\3\2\2\2\u0150\u0151\7^")
        buf.write("\2\2\u0151<\3\2\2\2\u0152\u0153\7\'\2\2\u0153>\3\2\2\2")
        buf.write("\u0154\u0155\7-\2\2\u0155\u0156\7\60\2\2\u0156@\3\2\2")
        buf.write("\2\u0157\u0158\7/\2\2\u0158\u0159\7\60\2\2\u0159B\3\2")
        buf.write("\2\2\u015a\u015b\7,\2\2\u015b\u015c\7\60\2\2\u015cD\3")
        buf.write("\2\2\2\u015d\u015e\7^\2\2\u015e\u015f\7\60\2\2\u015fF")
        buf.write("\3\2\2\2\u0160\u0161\7#\2\2\u0161H\3\2\2\2\u0162\u0163")
        buf.write("\7(\2\2\u0163\u0164\7(\2\2\u0164J\3\2\2\2\u0165\u0166")
        buf.write("\7~\2\2\u0166\u0167\7~\2\2\u0167L\3\2\2\2\u0168\u0169")
        buf.write("\7?\2\2\u0169\u016a\7?\2\2\u016aN\3\2\2\2\u016b\u016c")
        buf.write("\7#\2\2\u016c\u016d\7?\2\2\u016dP\3\2\2\2\u016e\u016f")
        buf.write("\7>\2\2\u016fR\3\2\2\2\u0170\u0171\7@\2\2\u0171T\3\2\2")
        buf.write("\2\u0172\u0173\7>\2\2\u0173\u0174\7?\2\2\u0174V\3\2\2")
        buf.write("\2\u0175\u0176\7@\2\2\u0176\u0177\7?\2\2\u0177X\3\2\2")
        buf.write("\2\u0178\u0179\7?\2\2\u0179\u017a\7\61\2\2\u017a\u017b")
        buf.write("\7?\2\2\u017bZ\3\2\2\2\u017c\u017d\7>\2\2\u017d\u017e")
        buf.write("\7\60\2\2\u017e\\\3\2\2\2\u017f\u0180\7@\2\2\u0180\u0181")
        buf.write("\7\60\2\2\u0181^\3\2\2\2\u0182\u0183\7>\2\2\u0183\u0184")
        buf.write("\7?\2\2\u0184\u0185\7\60\2\2\u0185`\3\2\2\2\u0186\u0187")
        buf.write("\7@\2\2\u0187\u0188\7?\2\2\u0188\u0189\7\60\2\2\u0189")
        buf.write("b\3\2\2\2\u018a\u018b\7,\2\2\u018b\u018c\7,\2\2\u018c")
        buf.write("\u0190\3\2\2\2\u018d\u018f\13\2\2\2\u018e\u018d\3\2\2")
        buf.write("\2\u018f\u0192\3\2\2\2\u0190\u0191\3\2\2\2\u0190\u018e")
        buf.write("\3\2\2\2\u0191\u0193\3\2\2\2\u0192\u0190\3\2\2\2\u0193")
        buf.write("\u0194\7,\2\2\u0194\u0195\7,\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0197\b\62\3\2\u0197d\3\2\2\2\u0198\u0199\7.\2\2\u0199")
        buf.write("f\3\2\2\2\u019a\u019b\7=\2\2\u019bh\3\2\2\2\u019c\u019d")
        buf.write("\7<\2\2\u019dj\3\2\2\2\u019e\u019f\7*\2\2\u019fl\3\2\2")
        buf.write("\2\u01a0\u01a1\7+\2\2\u01a1n\3\2\2\2\u01a2\u01a3\7}\2")
        buf.write("\2\u01a3p\3\2\2\2\u01a4\u01a5\7\177\2\2\u01a5r\3\2\2\2")
        buf.write("\u01a6\u01a7\7]\2\2\u01a7t\3\2\2\2\u01a8\u01a9\7_\2\2")
        buf.write("\u01a9v\3\2\2\2\u01aa\u01ab\7\60\2\2\u01abx\3\2\2\2\u01ac")
        buf.write("\u01ad\7?\2\2\u01adz\3\2\2\2\u01ae\u01b2\n\2\2\2\u01af")
        buf.write("\u01b2\5}?\2\u01b0\u01b2\5\177@\2\u01b1\u01ae\3\2\2\2")
        buf.write("\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2|\3\2\2")
        buf.write("\2\u01b3\u01b4\7^\2\2\u01b4\u01b5\t\3\2\2\u01b5~\3\2\2")
        buf.write("\2\u01b6\u01b7\7)\2\2\u01b7\u01b8\7$\2\2\u01b8\u0080\3")
        buf.write("\2\2\2\u01b9\u01ba\7\62\2\2\u01ba\u01bb\t\4\2\2\u01bb")
        buf.write("\u01bf\t\5\2\2\u01bc\u01be\t\6\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3")
        buf.write("\2\2\2\u01c0\u0082\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3")
        buf.write("\7\62\2\2\u01c3\u01c4\t\7\2\2\u01c4\u01c8\t\b\2\2\u01c5")
        buf.write("\u01c7\t\t\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2")
        buf.write("\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u0084\3")
        buf.write("\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cd\5\67\34\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01d2\t\b\2\2\u01cf\u01d1\5\u0087D\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3\u0086\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d5\u01d6\t\n\2\2\u01d6\u0088\3\2\2\2\u01d7\u01d9\t")
        buf.write("\13\2\2\u01d8\u01da\5\u008bF\2\u01d9\u01d8\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01dd\5\u0087")
        buf.write("D\2\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u008a\3\2\2\2\u01e0")
        buf.write("\u01e1\t\f\2\2\u01e1\u008c\3\2\2\2\u01e2\u01e3\7^\2\2")
        buf.write("\u01e3\u01e4\n\3\2\2\u01e4\u008e\3\2\2\2\u01e5\u01e7\t")
        buf.write("\r\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e6")
        buf.write("\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write("\u01eb\bH\3\2\u01eb\u0090\3\2\2\2\u01ec\u01f0\t\16\2\2")
        buf.write("\u01ed\u01ef\t\17\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2")
        buf.write("\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u0092\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3\u01f4\13\2\2")
        buf.write("\2\u01f4\u01f5\bJ\4\2\u01f5\u0094\3\2\2\2\u01f6\u01fa")
        buf.write("\7$\2\2\u01f7\u01f9\5{>\2\u01f8\u01f7\3\2\2\2\u01f9\u01fc")
        buf.write("\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb")
        buf.write("\u01fd\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u01fe\bK\5\2")
        buf.write("\u01fe\u0096\3\2\2\2\u01ff\u0203\7$\2\2\u0200\u0202\5")
        buf.write("{>\2\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205")
        buf.write("\u0203\3\2\2\2\u0206\u0207\7^\2\2\u0207\u0208\n\20\2\2")
        buf.write("\u0208\u0209\bL\6\2\u0209\u0098\3\2\2\2\u020a\u020b\7")
        buf.write(",\2\2\u020b\u020c\7,\2\2\u020c\u0210\3\2\2\2\u020d\u020f")
        buf.write("\13\2\2\2\u020e\u020d\3\2\2\2\u020f\u0212\3\2\2\2\u0210")
        buf.write("\u0211\3\2\2\2\u0210\u020e\3\2\2\2\u0211\u0213\3\2\2\2")
        buf.write("\u0212\u0210\3\2\2\2\u0213\u0214\bM\7\2\u0214\u009a\3")
        buf.write("\2\2\2\30\2\u009e\u00a3\u00a8\u00aa\u00ae\u00b3\u00b7")
        buf.write("\u00bd\u0190\u01b1\u01bf\u01c8\u01cc\u01d2\u01d9\u01de")
        buf.write("\u01e8\u01f0\u01fa\u0203\u0210\b\3\4\2\b\2\2\3J\3\3K\4")
        buf.write("\3L\5\3M\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    REAL_LITERAL = 2
    STRING_LITERAL = 3
    BODY = 4
    BREAK = 5
    CONTINUE = 6
    DO = 7
    ELSE = 8
    ELSEIF = 9
    ENDBODY = 10
    ENDIF = 11
    ENDFOR = 12
    ENDWHILE = 13
    FOR = 14
    FUNCTION = 15
    IF = 16
    PARAMETER = 17
    RETURN = 18
    THEN = 19
    VAR = 20
    WHILE = 21
    TRUE = 22
    FALSE = 23
    ENDDO = 24
    MAIN = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    RMD = 30
    ADDF = 31
    SUBF = 32
    MULF = 33
    DIVF = 34
    NOT = 35
    AND = 36
    OR = 37
    DBEQ = 38
    NEQ = 39
    LT = 40
    GT = 41
    LTE = 42
    GTE = 43
    NEQF = 44
    LTF = 45
    GTF = 46
    LTEF = 47
    GTEF = 48
    BLOCK_COMMENT = 49
    COMMA = 50
    SEMI = 51
    COLON = 52
    LP = 53
    RP = 54
    LCB = 55
    RCB = 56
    LSB = 57
    RSB = 58
    DOT = 59
    EQ = 60
    HEXADECIMAL = 61
    OCTALDECIMAL = 62
    NUM = 63
    WS = 64
    ID = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68
    UNTERMINATED_COMMENT = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'0'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'True'", "'False'", "'EndDo'", "'Main'", 
            "'+'", "'-'", "'*'", "'\\'", "'%'", "'+.'", "'-.'", "'*.'", 
            "'\\.'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "','", 
            "';'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'.'", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "REAL_LITERAL", "STRING_LITERAL", "BODY", "BREAK", "CONTINUE", 
            "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
            "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
            "WHILE", "TRUE", "FALSE", "ENDDO", "MAIN", "ADD", "SUB", "MUL", 
            "DIV", "RMD", "ADDF", "SUBF", "MULF", "DIVF", "NOT", "AND", 
            "OR", "DBEQ", "NEQ", "LT", "GT", "LTE", "GTE", "NEQF", "LTF", 
            "GTF", "LTEF", "GTEF", "BLOCK_COMMENT", "COMMA", "SEMI", "COLON", 
            "LP", "RP", "LCB", "RCB", "LSB", "RSB", "DOT", "EQ", "HEXADECIMAL", 
            "OCTALDECIMAL", "NUM", "WS", "ID", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "REAL_LITERAL", "STRING_LITERAL", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "MAIN", "ADD", "SUB", "MUL", "DIV", "RMD", "ADDF", "SUBF", 
                  "MULF", "DIVF", "NOT", "AND", "OR", "DBEQ", "NEQ", "LT", 
                  "GT", "LTE", "GTE", "NEQF", "LTF", "GTF", "LTEF", "GTEF", 
                  "BLOCK_COMMENT", "COMMA", "SEMI", "COLON", "LP", "RP", 
                  "LCB", "RCB", "LSB", "RSB", "DOT", "EQ", "CHAR", "ESC_CHAR", 
                  "QUOTE", "HEXADECIMAL", "OCTALDECIMAL", "NUM", "DIGIT", 
                  "EXPONENT", "SIGN", "ILLEGAL_ESC", "WS", "ID", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.STRING_LITERAL_action 
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text=self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                            raise ErrorToken(self.text)
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
                   
                            raise UncloseString(self.text[1:])
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
                   
                            raise IllegalEscape(self.text[1:])
                    
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                            raise UnterminatedComment()
                    
     


