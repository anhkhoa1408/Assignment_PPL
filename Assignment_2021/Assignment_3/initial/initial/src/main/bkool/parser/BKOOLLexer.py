# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01c4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$")
        buf.write("\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\64\7\64\u014c\n\64\f\64\16")
        buf.write("\64\u014f\13\64\5\64\u0151\n\64\3\65\6\65\u0154\n\65\r")
        buf.write("\65\16\65\u0155\3\65\3\65\5\65\u015a\n\65\3\65\5\65\u015d")
        buf.write("\n\65\3\66\3\66\7\66\u0161\n\66\f\66\16\66\u0164\13\66")
        buf.write("\3\66\3\66\3\67\3\67\5\67\u016a\n\67\3\67\7\67\u016d\n")
        buf.write("\67\f\67\16\67\u0170\13\67\38\38\38\38\78\u0176\n8\f8")
        buf.write("\168\u0179\138\38\38\38\38\38\39\39\79\u0182\n9\f9\16")
        buf.write("9\u0185\139\39\39\3:\3:\3;\6;\u018c\n;\r;\16;\u018d\3")
        buf.write(";\3;\3<\3<\3=\3=\7=\u0196\n=\f=\16=\u0199\13=\3>\3>\3")
        buf.write(">\5>\u019e\n>\3>\6>\u01a1\n>\r>\16>\u01a2\3?\3?\3@\3@")
        buf.write("\3@\3A\3A\5A\u01ac\nA\3B\3B\3B\3C\3C\7C\u01b3\nC\fC\16")
        buf.write("C\u01b6\13C\3C\3C\3D\3D\7D\u01bc\nD\fD\16D\u01bf\13D\3")
        buf.write("D\3D\3D\3D\2\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u<w\2y\2{\2}\2\177\2\u0081\2\u0083=\u0085")
        buf.write(">\u0087?\3\2\f\3\2\63;\6\2\62;C\\aac|\4\2GHQQ\5\2\f\f")
        buf.write("GHQQ\5\2\13\f\16\17\"\"\3\2\62;\4\2GGgg\4\2C\\c|\t\2$")
        buf.write("$^^ddhhppttvv\6\2\n\f\16\17$$^^\2\u01cf\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\3\u0089\3\2\2\2\5\u0091\3\2\2\2\7\u0097\3\2\2")
        buf.write("\2\t\u009d\3\2\2\2\13\u00a6\3\2\2\2\r\u00a9\3\2\2\2\17")
        buf.write("\u00ae\3\2\2\2\21\u00b6\3\2\2\2\23\u00bc\3\2\2\2\25\u00bf")
        buf.write("\3\2\2\2\27\u00c3\3\2\2\2\31\u00c7\3\2\2\2\33\u00ce\3")
        buf.write("\2\2\2\35\u00d3\3\2\2\2\37\u00d7\3\2\2\2!\u00de\3\2\2")
        buf.write("\2#\u00e3\3\2\2\2%\u00e9\3\2\2\2\'\u00ee\3\2\2\2)\u00f2")
        buf.write("\3\2\2\2+\u00f7\3\2\2\2-\u00fd\3\2\2\2/\u0104\3\2\2\2")
        buf.write("\61\u0107\3\2\2\2\63\u010e\3\2\2\2\65\u0110\3\2\2\2\67")
        buf.write("\u0112\3\2\2\29\u0114\3\2\2\2;\u0116\3\2\2\2=\u0118\3")
        buf.write("\2\2\2?\u011a\3\2\2\2A\u011d\3\2\2\2C\u0120\3\2\2\2E\u0122")
        buf.write("\3\2\2\2G\u0124\3\2\2\2I\u0127\3\2\2\2K\u012a\3\2\2\2")
        buf.write("M\u012d\3\2\2\2O\u0130\3\2\2\2Q\u0132\3\2\2\2S\u0134\3")
        buf.write("\2\2\2U\u0136\3\2\2\2W\u0138\3\2\2\2Y\u013a\3\2\2\2[\u013c")
        buf.write("\3\2\2\2]\u013e\3\2\2\2_\u0140\3\2\2\2a\u0142\3\2\2\2")
        buf.write("c\u0144\3\2\2\2e\u0146\3\2\2\2g\u0150\3\2\2\2i\u0153\3")
        buf.write("\2\2\2k\u015e\3\2\2\2m\u0169\3\2\2\2o\u0171\3\2\2\2q\u017f")
        buf.write("\3\2\2\2s\u0188\3\2\2\2u\u018b\3\2\2\2w\u0191\3\2\2\2")
        buf.write("y\u0193\3\2\2\2{\u019a\3\2\2\2}\u01a4\3\2\2\2\177\u01a6")
        buf.write("\3\2\2\2\u0081\u01ab\3\2\2\2\u0083\u01ad\3\2\2\2\u0085")
        buf.write("\u01b0\3\2\2\2\u0087\u01b9\3\2\2\2\u0089\u008a\7d\2\2")
        buf.write("\u008a\u008b\7q\2\2\u008b\u008c\7q\2\2\u008c\u008d\7n")
        buf.write("\2\2\u008d\u008e\7g\2\2\u008e\u008f\7c\2\2\u008f\u0090")
        buf.write("\7p\2\2\u0090\4\3\2\2\2\u0091\u0092\7d\2\2\u0092\u0093")
        buf.write("\7t\2\2\u0093\u0094\7g\2\2\u0094\u0095\7c\2\2\u0095\u0096")
        buf.write("\7m\2\2\u0096\6\3\2\2\2\u0097\u0098\7e\2\2\u0098\u0099")
        buf.write("\7n\2\2\u0099\u009a\7c\2\2\u009a\u009b\7u\2\2\u009b\u009c")
        buf.write("\7u\2\2\u009c\b\3\2\2\2\u009d\u009e\7e\2\2\u009e\u009f")
        buf.write("\7q\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2")
        buf.write("\7k\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5")
        buf.write("\7g\2\2\u00a5\n\3\2\2\2\u00a6\u00a7\7f\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\f\3\2\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab")
        buf.write("\7n\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7g\2\2\u00ad\16")
        buf.write("\3\2\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7z\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4")
        buf.write("\7f\2\2\u00b4\u00b5\7u\2\2\u00b5\20\3\2\2\2\u00b6\u00b7")
        buf.write("\7h\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba")
        buf.write("\7c\2\2\u00ba\u00bb\7v\2\2\u00bb\22\3\2\2\2\u00bc\u00bd")
        buf.write("\7k\2\2\u00bd\u00be\7h\2\2\u00be\24\3\2\2\2\u00bf\u00c0")
        buf.write("\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\26")
        buf.write("\3\2\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7y\2\2\u00c6\30\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7i\2\2\u00cd\32\3\2\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\u00d0\7j\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\34\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7t\2\2\u00d6\36\3\2\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7w\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7p\2\2\u00dd \3")
        buf.write("\2\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7w\2\2\u00e1\u00e2\7g\2\2\u00e2\"\3\2\2\2\u00e3\u00e4")
        buf.write("\7h\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7")
        buf.write("\7u\2\2\u00e7\u00e8\7g\2\2\u00e8$\3\2\2\2\u00e9\u00ea")
        buf.write("\7x\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed")
        buf.write("\7f\2\2\u00ed&\3\2\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7k\2\2\u00f0\u00f1\7n\2\2\u00f1(\3\2\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7j\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6")
        buf.write("\7u\2\2\u00f6*\3\2\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7n\2\2\u00fc,\3\2\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7v\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7e\2\2\u0103.\3\2\2\2\u0104\u0105")
        buf.write("\7v\2\2\u0105\u0106\7q\2\2\u0106\60\3\2\2\2\u0107\u0108")
        buf.write("\7f\2\2\u0108\u0109\7q\2\2\u0109\u010a\7y\2\2\u010a\u010b")
        buf.write("\7p\2\2\u010b\u010c\7v\2\2\u010c\u010d\7q\2\2\u010d\62")
        buf.write("\3\2\2\2\u010e\u010f\7-\2\2\u010f\64\3\2\2\2\u0110\u0111")
        buf.write("\7/\2\2\u0111\66\3\2\2\2\u0112\u0113\7,\2\2\u01138\3\2")
        buf.write("\2\2\u0114\u0115\7\61\2\2\u0115:\3\2\2\2\u0116\u0117\7")
        buf.write("^\2\2\u0117<\3\2\2\2\u0118\u0119\7\'\2\2\u0119>\3\2\2")
        buf.write("\2\u011a\u011b\7#\2\2\u011b\u011c\7?\2\2\u011c@\3\2\2")
        buf.write("\2\u011d\u011e\7?\2\2\u011e\u011f\7?\2\2\u011fB\3\2\2")
        buf.write("\2\u0120\u0121\7>\2\2\u0121D\3\2\2\2\u0122\u0123\7@\2")
        buf.write("\2\u0123F\3\2\2\2\u0124\u0125\7>\2\2\u0125\u0126\7?\2")
        buf.write("\2\u0126H\3\2\2\2\u0127\u0128\7@\2\2\u0128\u0129\7?\2")
        buf.write("\2\u0129J\3\2\2\2\u012a\u012b\7~\2\2\u012b\u012c\7~\2")
        buf.write("\2\u012cL\3\2\2\2\u012d\u012e\7(\2\2\u012e\u012f\7(\2")
        buf.write("\2\u012fN\3\2\2\2\u0130\u0131\7#\2\2\u0131P\3\2\2\2\u0132")
        buf.write("\u0133\7`\2\2\u0133R\3\2\2\2\u0134\u0135\7]\2\2\u0135")
        buf.write("T\3\2\2\2\u0136\u0137\7_\2\2\u0137V\3\2\2\2\u0138\u0139")
        buf.write("\7}\2\2\u0139X\3\2\2\2\u013a\u013b\7\177\2\2\u013bZ\3")
        buf.write("\2\2\2\u013c\u013d\7*\2\2\u013d\\\3\2\2\2\u013e\u013f")
        buf.write("\7+\2\2\u013f^\3\2\2\2\u0140\u0141\7=\2\2\u0141`\3\2\2")
        buf.write("\2\u0142\u0143\7<\2\2\u0143b\3\2\2\2\u0144\u0145\7\60")
        buf.write("\2\2\u0145d\3\2\2\2\u0146\u0147\7.\2\2\u0147f\3\2\2\2")
        buf.write("\u0148\u0151\7\62\2\2\u0149\u014d\t\2\2\2\u014a\u014c")
        buf.write("\5w<\2\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u0150\u0148\3\2\2\2\u0150\u0149\3\2\2\2")
        buf.write("\u0151h\3\2\2\2\u0152\u0154\5w<\2\u0153\u0152\3\2\2\2")
        buf.write("\u0154\u0155\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3")
        buf.write("\2\2\2\u0156\u015c\3\2\2\2\u0157\u0159\5y=\2\u0158\u015a")
        buf.write("\5{>\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015d")
        buf.write("\3\2\2\2\u015b\u015d\5{>\2\u015c\u0157\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015dj\3\2\2\2\u015e\u0162\7$\2\2\u015f\u0161")
        buf.write("\5\u0081A\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0165\u0166\7$\2\2\u0166l\3\2\2\2")
        buf.write("\u0167\u016a\5}?\2\u0168\u016a\7a\2\2\u0169\u0167\3\2")
        buf.write("\2\2\u0169\u0168\3\2\2\2\u016a\u016e\3\2\2\2\u016b\u016d")
        buf.write("\t\3\2\2\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016fn\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0171\u0172\7\61\2\2\u0172\u0173\7,\2\2")
        buf.write("\u0173\u0177\3\2\2\2\u0174\u0176\n\4\2\2\u0175\u0174\3")
        buf.write("\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u0177\3\2\2\2\u017a")
        buf.write("\u017b\7,\2\2\u017b\u017c\7\61\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d\u017e\b8\2\2\u017ep\3\2\2\2\u017f\u0183\7%\2\2")
        buf.write("\u0180\u0182\n\5\2\2\u0181\u0180\3\2\2\2\u0182\u0185\3")
        buf.write("\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\b9\2\2\u0187")
        buf.write("r\3\2\2\2\u0188\u0189\7?\2\2\u0189t\3\2\2\2\u018a\u018c")
        buf.write("\t\6\2\2\u018b\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0190\b;\2\2\u0190v\3\2\2\2\u0191\u0192\t\7\2\2")
        buf.write("\u0192x\3\2\2\2\u0193\u0197\5c\62\2\u0194\u0196\5w<\2")
        buf.write("\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3")
        buf.write("\2\2\2\u0197\u0198\3\2\2\2\u0198z\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u019a\u019d\t\b\2\2\u019b\u019e\5\65\33\2\u019c")
        buf.write("\u019e\5\63\32\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2")
        buf.write("\2\u019d\u019e\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u01a1")
        buf.write("\5w<\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3|\3\2\2\2\u01a4\u01a5")
        buf.write("\t\t\2\2\u01a5~\3\2\2\2\u01a6\u01a7\7^\2\2\u01a7\u01a8")
        buf.write("\t\n\2\2\u01a8\u0080\3\2\2\2\u01a9\u01ac\n\13\2\2\u01aa")
        buf.write("\u01ac\5\177@\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa\3\2\2")
        buf.write("\2\u01ac\u0082\3\2\2\2\u01ad\u01ae\13\2\2\2\u01ae\u01af")
        buf.write("\bB\3\2\u01af\u0084\3\2\2\2\u01b0\u01b4\7$\2\2\u01b1\u01b3")
        buf.write("\5\u0081A\2\u01b2\u01b1\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2")
        buf.write("\u01b6\u01b4\3\2\2\2\u01b7\u01b8\bC\4\2\u01b8\u0086\3")
        buf.write("\2\2\2\u01b9\u01bd\7$\2\2\u01ba\u01bc\5\u0081A\2\u01bb")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01bd\u01be\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf\u01bd\3")
        buf.write("\2\2\2\u01c0\u01c1\7^\2\2\u01c1\u01c2\n\n\2\2\u01c2\u01c3")
        buf.write("\bD\5\2\u01c3\u0088\3\2\2\2\24\2\u014d\u0150\u0155\u0159")
        buf.write("\u015c\u0162\u0169\u016e\u0177\u0183\u018d\u0197\u019d")
        buf.write("\u01a2\u01ab\u01b4\u01bd\6\b\2\2\3B\2\3C\3\3D\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEAN = 1
    BREAK = 2
    CLASS = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    EXTENDS = 7
    FLOAT = 8
    IF = 9
    INT = 10
    NEW = 11
    STRING = 12
    THEN = 13
    FOR = 14
    RETURN = 15
    TRUE = 16
    FALSE = 17
    VOID = 18
    NIL = 19
    THIS = 20
    FINAL = 21
    STATIC = 22
    TO = 23
    DOWNTO = 24
    ADD = 25
    SUB = 26
    MUL = 27
    FLOAT_DIV = 28
    INT_DIV = 29
    MOD = 30
    NOT_EQ = 31
    DBEQ = 32
    LT = 33
    GT = 34
    LTEQ = 35
    GTEQ = 36
    OR = 37
    AND = 38
    NOT = 39
    CONCAT = 40
    LSB = 41
    RSB = 42
    LP = 43
    RP = 44
    LB = 45
    RB = 46
    SEMI = 47
    COLON = 48
    DOT = 49
    COMMA = 50
    INT_LIT = 51
    FLOAT_LIT = 52
    STRING_LIT = 53
    ID = 54
    BLOCKCOMMENT = 55
    LINECOMMENT = 56
    EQ = 57
    WS = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", 
            "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "'['", 
            "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", "'.'", "','", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
            "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
            "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", 
            "DOWNTO", "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", "MOD", 
            "NOT_EQ", "DBEQ", "LT", "GT", "LTEQ", "GTEQ", "OR", "AND", "NOT", 
            "CONCAT", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", "COLON", 
            "DOT", "COMMA", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "ID", 
            "BLOCKCOMMENT", "LINECOMMENT", "EQ", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                  "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", 
                  "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                  "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", 
                  "FLOAT_DIV", "INT_DIV", "MOD", "NOT_EQ", "DBEQ", "LT", 
                  "GT", "LTEQ", "GTEQ", "OR", "AND", "NOT", "CONCAT", "LSB", 
                  "RSB", "LP", "RP", "LB", "RB", "SEMI", "COLON", "DOT", 
                  "COMMA", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "ID", "BLOCKCOMMENT", 
                  "LINECOMMENT", "EQ", "WS", "DIGIT", "DECIMAL", "EXPONENT", 
                  "LETTER", "ESC_CHAR", "CHAR", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[64] = self.ERROR_CHAR_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
                   
                    raise UncloseString(self.text[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
                   
                    raise IllegalEscape(self.text[0:])

     


