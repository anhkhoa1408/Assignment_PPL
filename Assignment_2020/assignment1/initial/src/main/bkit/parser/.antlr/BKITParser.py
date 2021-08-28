# Generated from d:\Assignment_PPL\assignment2-v1.1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u019a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\6\2T\n\2\r\2\16\2U\3\2\3\2\3")
        buf.write("\3\3\3\5\3\\\n\3\3\4\3\4\3\4\3\4\3\4\6\4c\n\4\r\4\16\4")
        buf.write("d\3\5\3\5\3\5\7\5j\n\5\f\5\16\5m\13\5\3\6\3\6\3\6\3\6")
        buf.write("\5\6s\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7}\n\7\3\b")
        buf.write("\3\b\3\b\3\b\5\b\u0083\n\b\3\t\3\t\5\t\u0087\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0091\n\n\3\13\3\13\3\13")
        buf.write("\7\13\u0096\n\13\f\13\16\13\u0099\13\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\7\f\u00a3\n\f\f\f\16\f\u00a6\13\f\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00ac\n\r\3\r\3\r\3\r\5\r\u00b1\n\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\7\17\u00bf\n\17\f\17\16\17\u00c2\13\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00cd\n\20\3\21")
        buf.write("\7\21\u00d0\n\21\f\21\16\21\u00d3\13\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00de\n\23\3\23\3")
        buf.write("\23\7\23\u00e2\n\23\f\23\16\23\u00e5\13\23\3\23\3\23\5")
        buf.write("\23\u00e9\n\23\3\23\5\23\u00ec\n\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u00f5\n\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u0105\n\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\5")
        buf.write("\26\u010f\n\26\3\26\3\26\3\26\3\26\3\27\3\27\5\27\u0117")
        buf.write("\n\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\5\32\u0128\n\32\3\32\3\32\3")
        buf.write("\32\3\33\3\33\5\33\u012f\n\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u0137\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u013e")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0146\n\36\f")
        buf.write("\36\16\36\u0149\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7")
        buf.write("\37\u0151\n\37\f\37\16\37\u0154\13\37\3 \3 \3 \3 \3 \3")
        buf.write(" \7 \u015c\n \f \16 \u015f\13 \3!\3!\3!\5!\u0164\n!\3")
        buf.write("\"\3\"\3\"\5\"\u0169\n\"\3#\3#\3#\3#\3#\7#\u0170\n#\f")
        buf.write("#\16#\u0173\13#\3$\3$\5$\u0177\n$\3%\3%\3%\3%\3%\3%\5")
        buf.write("%\u017f\n%\3&\3&\3\'\3\'\3\'\7\'\u0186\n\'\f\'\16\'\u0189")
        buf.write("\13\'\3(\3(\3(\3(\6(\u018f\n(\r(\16(\u0190\3)\3)\3)\5")
        buf.write(")\u0196\n)\3)\3)\3)\2\6:<>D*\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNP\2\t\3\2")
        buf.write(")\63\3\2\'(\4\2\35\36\"#\4\2\37!$%\4\2\36\36##\3\2<=\3")
        buf.write("\2\3\6\2\u01a1\2S\3\2\2\2\4[\3\2\2\2\6]\3\2\2\2\bf\3\2")
        buf.write("\2\2\nr\3\2\2\2\f|\3\2\2\2\16\u0082\3\2\2\2\20\u0086\3")
        buf.write("\2\2\2\22\u0090\3\2\2\2\24\u0092\3\2\2\2\26\u009a\3\2")
        buf.write("\2\2\30\u00a7\3\2\2\2\32\u00b6\3\2\2\2\34\u00bb\3\2\2")
        buf.write("\2\36\u00cc\3\2\2\2 \u00d1\3\2\2\2\"\u00d4\3\2\2\2$\u00d9")
        buf.write("\3\2\2\2&\u00f0\3\2\2\2(\u00f8\3\2\2\2*\u010a\3\2\2\2")
        buf.write(",\u0114\3\2\2\2.\u011e\3\2\2\2\60\u0121\3\2\2\2\62\u0124")
        buf.write("\3\2\2\2\64\u012c\3\2\2\2\66\u0136\3\2\2\28\u013d\3\2")
        buf.write("\2\2:\u013f\3\2\2\2<\u014a\3\2\2\2>\u0155\3\2\2\2@\u0163")
        buf.write("\3\2\2\2B\u0168\3\2\2\2D\u016a\3\2\2\2F\u0176\3\2\2\2")
        buf.write("H\u017e\3\2\2\2J\u0180\3\2\2\2L\u0182\3\2\2\2N\u018e\3")
        buf.write("\2\2\2P\u0192\3\2\2\2RT\5\4\3\2SR\3\2\2\2TU\3\2\2\2US")
        buf.write("\3\2\2\2UV\3\2\2\2VW\3\2\2\2WX\7\2\2\3X\3\3\2\2\2Y\\\5")
        buf.write("\6\4\2Z\\\5\30\r\2[Y\3\2\2\2[Z\3\2\2\2\\\5\3\2\2\2]^\7")
        buf.write("\27\2\2^b\7\67\2\2_`\5\b\5\2`a\7\66\2\2ac\3\2\2\2b_\3")
        buf.write("\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2e\7\3\2\2\2fk\5\n")
        buf.write("\6\2gh\7\65\2\2hj\5\n\6\2ig\3\2\2\2jm\3\2\2\2ki\3\2\2")
        buf.write("\2kl\3\2\2\2l\t\3\2\2\2mk\3\2\2\2ns\5\f\7\2os\7A\2\2p")
        buf.write("q\7A\2\2qs\5N(\2rn\3\2\2\2ro\3\2\2\2rp\3\2\2\2s\13\3\2")
        buf.write("\2\2tu\7A\2\2uv\7?\2\2v}\5\20\t\2wx\7A\2\2xy\5N(\2yz\7")
        buf.write("?\2\2z{\5\20\t\2{}\3\2\2\2|t\3\2\2\2|w\3\2\2\2}\r\3\2")
        buf.write("\2\2~\u0083\7A\2\2\177\u0080\58\35\2\u0080\u0081\5N(\2")
        buf.write("\u0081\u0083\3\2\2\2\u0082~\3\2\2\2\u0082\177\3\2\2\2")
        buf.write("\u0083\17\3\2\2\2\u0084\u0087\5J&\2\u0085\u0087\5\22\n")
        buf.write("\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087\21\3")
        buf.write("\2\2\2\u0088\u0089\7:\2\2\u0089\u008a\5\24\13\2\u008a")
        buf.write("\u008b\7;\2\2\u008b\u0091\3\2\2\2\u008c\u008d\7:\2\2\u008d")
        buf.write("\u008e\5\26\f\2\u008e\u008f\7;\2\2\u008f\u0091\3\2\2\2")
        buf.write("\u0090\u0088\3\2\2\2\u0090\u008c\3\2\2\2\u0091\23\3\2")
        buf.write("\2\2\u0092\u0097\5J&\2\u0093\u0094\7\65\2\2\u0094\u0096")
        buf.write("\5J&\2\u0095\u0093\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\25\3\2\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u009a\u009b\7:\2\2\u009b\u009c\5\24\13\2\u009c")
        buf.write("\u00a4\7;\2\2\u009d\u009e\7\65\2\2\u009e\u009f\7:\2\2")
        buf.write("\u009f\u00a0\5\24\13\2\u00a0\u00a1\7;\2\2\u00a1\u00a3")
        buf.write("\3\2\2\2\u00a2\u009d\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\27\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a7\u00a8\7\22\2\2\u00a8\u00a9\7\67\2")
        buf.write("\2\u00a9\u00ab\7A\2\2\u00aa\u00ac\5\32\16\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00ae\7\7\2\2\u00ae\u00b0\7\67\2\2\u00af\u00b1\5\6\4")
        buf.write("\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b3\5 \21\2\u00b3\u00b4\7\r\2\2\u00b4")
        buf.write("\u00b5\7>\2\2\u00b5\31\3\2\2\2\u00b6\u00b7\7\24\2\2\u00b7")
        buf.write("\u00b8\7\67\2\2\u00b8\u00b9\5\34\17\2\u00b9\u00ba\7\66")
        buf.write("\2\2\u00ba\33\3\2\2\2\u00bb\u00c0\5\n\6\2\u00bc\u00bd")
        buf.write("\7\65\2\2\u00bd\u00bf\5\n\6\2\u00be\u00bc\3\2\2\2\u00bf")
        buf.write("\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\35\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00cd\5\"")
        buf.write("\22\2\u00c4\u00cd\5$\23\2\u00c5\u00cd\5(\25\2\u00c6\u00cd")
        buf.write("\5*\26\2\u00c7\u00cd\5,\27\2\u00c8\u00cd\5.\30\2\u00c9")
        buf.write("\u00cd\5\60\31\2\u00ca\u00cd\5\62\32\2\u00cb\u00cd\5\64")
        buf.write("\33\2\u00cc\u00c3\3\2\2\2\u00cc\u00c4\3\2\2\2\u00cc\u00c5")
        buf.write("\3\2\2\2\u00cc\u00c6\3\2\2\2\u00cc\u00c7\3\2\2\2\u00cc")
        buf.write("\u00c8\3\2\2\2\u00cc\u00c9\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cb\3\2\2\2\u00cd\37\3\2\2\2\u00ce\u00d0\5\36")
        buf.write("\20\2\u00cf\u00ce\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2!\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d4\u00d5\5\16\b\2\u00d5\u00d6\7?\2\2\u00d6")
        buf.write("\u00d7\58\35\2\u00d7\u00d8\7\66\2\2\u00d8#\3\2\2\2\u00d9")
        buf.write("\u00da\7\23\2\2\u00da\u00db\58\35\2\u00db\u00dd\7\26\2")
        buf.write("\2\u00dc\u00de\5\6\4\2\u00dd\u00dc\3\2\2\2\u00dd\u00de")
        buf.write("\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e3\5 \21\2\u00e0")
        buf.write("\u00e2\5&\24\2\u00e1\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00eb\3")
        buf.write("\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e8\7\13\2\2\u00e7")
        buf.write("\u00e9\5\6\4\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3\2\2\2")
        buf.write("\u00e9\u00ea\3\2\2\2\u00ea\u00ec\5 \21\2\u00eb\u00e6\3")
        buf.write("\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee")
        buf.write("\7\16\2\2\u00ee\u00ef\7>\2\2\u00ef%\3\2\2\2\u00f0\u00f1")
        buf.write("\7\f\2\2\u00f1\u00f2\58\35\2\u00f2\u00f4\7\26\2\2\u00f3")
        buf.write("\u00f5\5\6\4\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\u00f7\5 \21\2\u00f7\'\3\2\2")
        buf.write("\2\u00f8\u00f9\7\21\2\2\u00f9\u00fa\78\2\2\u00fa\u00fb")
        buf.write("\7A\2\2\u00fb\u00fc\7?\2\2\u00fc\u00fd\58\35\2\u00fd\u00fe")
        buf.write("\7\65\2\2\u00fe\u00ff\58\35\2\u00ff\u0100\7\65\2\2\u0100")
        buf.write("\u0101\58\35\2\u0101\u0102\79\2\2\u0102\u0104\7\n\2\2")
        buf.write("\u0103\u0105\5\6\4\2\u0104\u0103\3\2\2\2\u0104\u0105\3")
        buf.write("\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\5 \21\2\u0107\u0108")
        buf.write("\7\17\2\2\u0108\u0109\7>\2\2\u0109)\3\2\2\2\u010a\u010b")
        buf.write("\7\30\2\2\u010b\u010c\58\35\2\u010c\u010e\7\n\2\2\u010d")
        buf.write("\u010f\5\6\4\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0110\3\2\2\2\u0110\u0111\5 \21\2\u0111\u0112\7")
        buf.write("\20\2\2\u0112\u0113\7>\2\2\u0113+\3\2\2\2\u0114\u0116")
        buf.write("\7\n\2\2\u0115\u0117\5\6\4\2\u0116\u0115\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\5 \21\2")
        buf.write("\u0119\u011a\7\30\2\2\u011a\u011b\58\35\2\u011b\u011c")
        buf.write("\7\33\2\2\u011c\u011d\7>\2\2\u011d-\3\2\2\2\u011e\u011f")
        buf.write("\7\b\2\2\u011f\u0120\7\66\2\2\u0120/\3\2\2\2\u0121\u0122")
        buf.write("\7\t\2\2\u0122\u0123\7\66\2\2\u0123\61\3\2\2\2\u0124\u0125")
        buf.write("\7A\2\2\u0125\u0127\78\2\2\u0126\u0128\5L\'\2\u0127\u0126")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write("\u012a\79\2\2\u012a\u012b\7\66\2\2\u012b\63\3\2\2\2\u012c")
        buf.write("\u012e\7\25\2\2\u012d\u012f\5\66\34\2\u012e\u012d\3\2")
        buf.write("\2\2\u012e\u012f\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131")
        buf.write("\7\66\2\2\u0131\65\3\2\2\2\u0132\u0137\58\35\2\u0133\u0134")
        buf.write("\58\35\2\u0134\u0135\5\66\34\2\u0135\u0137\3\2\2\2\u0136")
        buf.write("\u0132\3\2\2\2\u0136\u0133\3\2\2\2\u0137\67\3\2\2\2\u0138")
        buf.write("\u0139\5:\36\2\u0139\u013a\t\2\2\2\u013a\u013b\5:\36\2")
        buf.write("\u013b\u013e\3\2\2\2\u013c\u013e\5:\36\2\u013d\u0138\3")
        buf.write("\2\2\2\u013d\u013c\3\2\2\2\u013e9\3\2\2\2\u013f\u0140")
        buf.write("\b\36\1\2\u0140\u0141\5<\37\2\u0141\u0147\3\2\2\2\u0142")
        buf.write("\u0143\f\4\2\2\u0143\u0144\t\3\2\2\u0144\u0146\5<\37\2")
        buf.write("\u0145\u0142\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3")
        buf.write("\2\2\2\u0147\u0148\3\2\2\2\u0148;\3\2\2\2\u0149\u0147")
        buf.write("\3\2\2\2\u014a\u014b\b\37\1\2\u014b\u014c\5> \2\u014c")
        buf.write("\u0152\3\2\2\2\u014d\u014e\f\4\2\2\u014e\u014f\t\4\2\2")
        buf.write("\u014f\u0151\5> \2\u0150\u014d\3\2\2\2\u0151\u0154\3\2")
        buf.write("\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153=\3")
        buf.write("\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156\b \1\2\u0156\u0157")
        buf.write("\5@!\2\u0157\u015d\3\2\2\2\u0158\u0159\f\4\2\2\u0159\u015a")
        buf.write("\t\5\2\2\u015a\u015c\5@!\2\u015b\u0158\3\2\2\2\u015c\u015f")
        buf.write("\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("?\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\7&\2\2\u0161")
        buf.write("\u0164\5@!\2\u0162\u0164\5B\"\2\u0163\u0160\3\2\2\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164A\3\2\2\2\u0165\u0166\t\6\2\2\u0166")
        buf.write("\u0169\5B\"\2\u0167\u0169\5D#\2\u0168\u0165\3\2\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169C\3\2\2\2\u016a\u016b\b#\1\2\u016b")
        buf.write("\u016c\5F$\2\u016c\u0171\3\2\2\2\u016d\u016e\f\4\2\2\u016e")
        buf.write("\u0170\t\7\2\2\u016f\u016d\3\2\2\2\u0170\u0173\3\2\2\2")
        buf.write("\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172E\3\2\2")
        buf.write("\2\u0173\u0171\3\2\2\2\u0174\u0177\5P)\2\u0175\u0177\5")
        buf.write("H%\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177G\3")
        buf.write("\2\2\2\u0178\u0179\78\2\2\u0179\u017a\58\35\2\u017a\u017b")
        buf.write("\79\2\2\u017b\u017f\3\2\2\2\u017c\u017f\5J&\2\u017d\u017f")
        buf.write("\7A\2\2\u017e\u0178\3\2\2\2\u017e\u017c\3\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017fI\3\2\2\2\u0180\u0181\t\b\2\2\u0181")
        buf.write("K\3\2\2\2\u0182\u0187\58\35\2\u0183\u0184\7\65\2\2\u0184")
        buf.write("\u0186\58\35\2\u0185\u0183\3\2\2\2\u0186\u0189\3\2\2\2")
        buf.write("\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188M\3\2\2")
        buf.write("\2\u0189\u0187\3\2\2\2\u018a\u018b\7<\2\2\u018b\u018c")
        buf.write("\58\35\2\u018c\u018d\7=\2\2\u018d\u018f\3\2\2\2\u018e")
        buf.write("\u018a\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191O\3\2\2\2\u0192\u0193\7A\2\2")
        buf.write("\u0193\u0195\78\2\2\u0194\u0196\5L\'\2\u0195\u0194\3\2")
        buf.write("\2\2\u0195\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198")
        buf.write("\79\2\2\u0198Q\3\2\2\2)U[dkr|\u0082\u0086\u0090\u0097")
        buf.write("\u00a4\u00ab\u00b0\u00c0\u00cc\u00d1\u00dd\u00e3\u00e8")
        buf.write("\u00eb\u00f4\u0104\u010e\u0116\u0127\u012e\u0136\u013d")
        buf.write("\u0147\u0152\u015d\u0163\u0168\u0171\u0176\u017e\u0187")
        buf.write("\u0190\u0195")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Body'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
                     "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
                     "'Return'", "'Then'", "'Var'", "'While'", "'True'", 
                     "'False'", "'EndDo'", "'Main'", "'+'", "'-'", "'*'", 
                     "'\\'", "'%'", "'+.'", "'-.'", "'*.'", "'\\.'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "<INVALID>", "','", "';'", "':'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN_LITERAL", "INTEGER_LITERAL", 
                      "REAL_LITERAL", "STRING_LITERAL", "BODY", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                      "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
                      "ENDDO", "MAIN", "ADD", "SUB", "MUL", "DIV", "RMD", 
                      "ADDF", "SUBF", "MULF", "DIVF", "NOT", "AND", "OR", 
                      "DBEQ", "NEQ", "LT", "GT", "LTE", "GTE", "NEQF", "LTF", 
                      "GTF", "LTEF", "GTEF", "BLOCK_COMMENT", "COMMA", "SEMI", 
                      "COLON", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "DOT", 
                      "EQ", "WS", "ID", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_declare = 1
    RULE_var_declare = 2
    RULE_var_list = 3
    RULE_var_stmt = 4
    RULE_init_stmt = 5
    RULE_lhs = 6
    RULE_init_val = 7
    RULE_array_init = 8
    RULE_one_dimension = 9
    RULE_multi_dimension = 10
    RULE_func_declare = 11
    RULE_parameter_declare = 12
    RULE_parameter_list = 13
    RULE_stmt_list = 14
    RULE_compound_stmt = 15
    RULE_assign_stmt = 16
    RULE_if_stmt = 17
    RULE_elseif_stmt = 18
    RULE_for_stmt = 19
    RULE_while_stmt = 20
    RULE_dowhile_stmt = 21
    RULE_break_stmt = 22
    RULE_continue_stmt = 23
    RULE_call_stmt = 24
    RULE_return_stmt = 25
    RULE_return_expression = 26
    RULE_expression = 27
    RULE_expression1 = 28
    RULE_expression2 = 29
    RULE_expression3 = 30
    RULE_expression4 = 31
    RULE_expression5 = 32
    RULE_expression6 = 33
    RULE_expression7 = 34
    RULE_operand = 35
    RULE_literal = 36
    RULE_exp_list = 37
    RULE_index_operator = 38
    RULE_function_call = 39

    ruleNames =  [ "program", "declare", "var_declare", "var_list", "var_stmt", 
                   "init_stmt", "lhs", "init_val", "array_init", "one_dimension", 
                   "multi_dimension", "func_declare", "parameter_declare", 
                   "parameter_list", "stmt_list", "compound_stmt", "assign_stmt", 
                   "if_stmt", "elseif_stmt", "for_stmt", "while_stmt", "dowhile_stmt", 
                   "break_stmt", "continue_stmt", "call_stmt", "return_stmt", 
                   "return_expression", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "operand", "literal", "exp_list", "index_operator", 
                   "function_call" ]

    EOF = Token.EOF
    BOOLEAN_LITERAL=1
    INTEGER_LITERAL=2
    REAL_LITERAL=3
    STRING_LITERAL=4
    BODY=5
    BREAK=6
    CONTINUE=7
    DO=8
    ELSE=9
    ELSEIF=10
    ENDBODY=11
    ENDIF=12
    ENDFOR=13
    ENDWHILE=14
    FOR=15
    FUNCTION=16
    IF=17
    PARAMETER=18
    RETURN=19
    THEN=20
    VAR=21
    WHILE=22
    TRUE=23
    FALSE=24
    ENDDO=25
    MAIN=26
    ADD=27
    SUB=28
    MUL=29
    DIV=30
    RMD=31
    ADDF=32
    SUBF=33
    MULF=34
    DIVF=35
    NOT=36
    AND=37
    OR=38
    DBEQ=39
    NEQ=40
    LT=41
    GT=42
    LTE=43
    GTE=44
    NEQF=45
    LTF=46
    GTF=47
    LTEF=48
    GTEF=49
    BLOCK_COMMENT=50
    COMMA=51
    SEMI=52
    COLON=53
    LP=54
    RP=55
    LCB=56
    RCB=57
    LSB=58
    RSB=59
    DOT=60
    EQ=61
    WS=62
    ID=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66
    UNTERMINATED_COMMENT=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.DeclareContext)
            else:
                return self.getTypedRuleContext(BKITParser.DeclareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.declare()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.FUNCTION or _la==BKITParser.VAR):
                    break

            self.state = 85
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(BKITParser.Func_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_declare




    def declare(self):

        localctx = BKITParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declare)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.var_declare()
                pass
            elif token in [BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.func_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_listContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SEMI)
            else:
                return self.getToken(BKITParser.SEMI, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declare




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(BKITParser.VAR)
            self.state = 92
            self.match(BKITParser.COLON)
            self.state = 96 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 93
                    self.var_list()
                    self.state = 94
                    self.match(BKITParser.SEMI)

                else:
                    raise NoViableAltException(self)
                self.state = 98 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_stmtContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_list




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.var_stmt()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 101
                self.match(BKITParser.COMMA)
                self.state = 102
                self.var_stmt()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_stmt(self):
            return self.getTypedRuleContext(BKITParser.Init_stmtContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_stmt




    def var_stmt(self):

        localctx = BKITParser.Var_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_stmt)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.init_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(BKITParser.ID)
                self.state = 111
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def init_val(self):
            return self.getTypedRuleContext(BKITParser.Init_valContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_stmt




    def init_stmt(self):

        localctx = BKITParser.Init_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_init_stmt)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(BKITParser.ID)
                self.state = 115
                self.match(BKITParser.EQ)
                self.state = 116
                self.init_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(BKITParser.ID)
                self.state = 118
                self.index_operator()
                self.state = 119
                self.match(BKITParser.EQ)
                self.state = 120
                self.init_val()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_lhs




    def lhs(self):

        localctx = BKITParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lhs)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.expression()
                self.state = 126
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def array_init(self):
            return self.getTypedRuleContext(BKITParser.Array_initContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_val




    def init_val(self):

        localctx = BKITParser.Init_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_init_val)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.BOOLEAN_LITERAL, BKITParser.INTEGER_LITERAL, BKITParser.REAL_LITERAL, BKITParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.literal()
                pass
            elif token in [BKITParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.array_init()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def one_dimension(self):
            return self.getTypedRuleContext(BKITParser.One_dimensionContext,0)


        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def multi_dimension(self):
            return self.getTypedRuleContext(BKITParser.Multi_dimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_init




    def array_init(self):

        localctx = BKITParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_init)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(BKITParser.LCB)
                self.state = 135
                self.one_dimension()
                self.state = 136
                self.match(BKITParser.RCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(BKITParser.LCB)
                self.state = 139
                self.multi_dimension()
                self.state = 140
                self.match(BKITParser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_dimensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKITParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_one_dimension




    def one_dimension(self):

        localctx = BKITParser.One_dimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_one_dimension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.literal()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 145
                self.match(BKITParser.COMMA)
                self.state = 146
                self.literal()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_dimensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LCB)
            else:
                return self.getToken(BKITParser.LCB, i)

        def one_dimension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.One_dimensionContext)
            else:
                return self.getTypedRuleContext(BKITParser.One_dimensionContext,i)


        def RCB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RCB)
            else:
                return self.getToken(BKITParser.RCB, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_multi_dimension




    def multi_dimension(self):

        localctx = BKITParser.Multi_dimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_multi_dimension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(BKITParser.LCB)
            self.state = 153
            self.one_dimension()
            self.state = 154
            self.match(BKITParser.RCB)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 155
                self.match(BKITParser.COMMA)
                self.state = 156
                self.match(BKITParser.LCB)
                self.state = 157
                self.one_dimension()
                self.state = 158
                self.match(BKITParser.RCB)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def compound_stmt(self):
            return self.getTypedRuleContext(BKITParser.Compound_stmtContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def parameter_declare(self):
            return self.getTypedRuleContext(BKITParser.Parameter_declareContext,0)


        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declare




    def func_declare(self):

        localctx = BKITParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(BKITParser.FUNCTION)
            self.state = 166
            self.match(BKITParser.COLON)
            self.state = 167
            self.match(BKITParser.ID)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 168
                self.parameter_declare()


            self.state = 171
            self.match(BKITParser.BODY)
            self.state = 172
            self.match(BKITParser.COLON)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 173
                self.var_declare()


            self.state = 176
            self.compound_stmt()
            self.state = 177
            self.match(BKITParser.ENDBODY)
            self.state = 178
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(BKITParser.Parameter_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_parameter_declare




    def parameter_declare(self):

        localctx = BKITParser.Parameter_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(BKITParser.PARAMETER)
            self.state = 181
            self.match(BKITParser.COLON)
            self.state = 182
            self.parameter_list()
            self.state = 183
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_stmtContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_parameter_list




    def parameter_list(self):

        localctx = BKITParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.var_stmt()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 186
                self.match(BKITParser.COMMA)
                self.state = 187
                self.var_stmt()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def dowhile_stmt(self):
            return self.getTypedRuleContext(BKITParser.Dowhile_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_list




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt_list)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 197
                self.dowhile_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 199
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 200
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 201
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_compound_stmt




    def compound_stmt(self):

        localctx = BKITParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_compound_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 204
                    self.stmt_list() 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKITParser.LhsContext,0)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.lhs()
            self.state = 211
            self.match(BKITParser.EQ)
            self.state = 212
            self.expression()
            self.state = 213
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def compound_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Compound_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Compound_stmtContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def elseif_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Elseif_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Elseif_stmtContext,i)


        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(BKITParser.IF)
            self.state = 216
            self.expression()
            self.state = 217
            self.match(BKITParser.THEN)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 218
                self.var_declare()


            self.state = 221
            self.compound_stmt()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 222
                self.elseif_stmt()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 228
                self.match(BKITParser.ELSE)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.VAR:
                    self.state = 229
                    self.var_declare()


                self.state = 232
                self.compound_stmt()


            self.state = 235
            self.match(BKITParser.ENDIF)
            self.state = 236
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def compound_stmt(self):
            return self.getTypedRuleContext(BKITParser.Compound_stmtContext,0)


        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_stmt




    def elseif_stmt(self):

        localctx = BKITParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_elseif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(BKITParser.ELSEIF)
            self.state = 239
            self.expression()
            self.state = 240
            self.match(BKITParser.THEN)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 241
                self.var_declare()


            self.state = 244
            self.compound_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def compound_stmt(self):
            return self.getTypedRuleContext(BKITParser.Compound_stmtContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(BKITParser.FOR)
            self.state = 247
            self.match(BKITParser.LP)
            self.state = 248
            self.match(BKITParser.ID)
            self.state = 249
            self.match(BKITParser.EQ)
            self.state = 250
            self.expression()
            self.state = 251
            self.match(BKITParser.COMMA)
            self.state = 252
            self.expression()
            self.state = 253
            self.match(BKITParser.COMMA)
            self.state = 254
            self.expression()
            self.state = 255
            self.match(BKITParser.RP)
            self.state = 256
            self.match(BKITParser.DO)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 257
                self.var_declare()


            self.state = 260
            self.compound_stmt()
            self.state = 261
            self.match(BKITParser.ENDFOR)
            self.state = 262
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def compound_stmt(self):
            return self.getTypedRuleContext(BKITParser.Compound_stmtContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(BKITParser.WHILE)
            self.state = 265
            self.expression()
            self.state = 266
            self.match(BKITParser.DO)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 267
                self.var_declare()


            self.state = 270
            self.compound_stmt()
            self.state = 271
            self.match(BKITParser.ENDWHILE)
            self.state = 272
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def compound_stmt(self):
            return self.getTypedRuleContext(BKITParser.Compound_stmtContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dowhile_stmt




    def dowhile_stmt(self):

        localctx = BKITParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dowhile_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(BKITParser.DO)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 275
                self.var_declare()


            self.state = 278
            self.compound_stmt()
            self.state = 279
            self.match(BKITParser.WHILE)
            self.state = 280
            self.expression()
            self.state = 281
            self.match(BKITParser.ENDDO)
            self.state = 282
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(BKITParser.BREAK)
            self.state = 285
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(BKITParser.CONTINUE)
            self.state = 288
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(BKITParser.ID)
            self.state = 291
            self.match(BKITParser.LP)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BOOLEAN_LITERAL) | (1 << BKITParser.INTEGER_LITERAL) | (1 << BKITParser.REAL_LITERAL) | (1 << BKITParser.STRING_LITERAL) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.ID))) != 0):
                self.state = 292
                self.exp_list()


            self.state = 295
            self.match(BKITParser.RP)
            self.state = 296
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def return_expression(self):
            return self.getTypedRuleContext(BKITParser.Return_expressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(BKITParser.RETURN)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BOOLEAN_LITERAL) | (1 << BKITParser.INTEGER_LITERAL) | (1 << BKITParser.REAL_LITERAL) | (1 << BKITParser.STRING_LITERAL) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.ID))) != 0):
                self.state = 299
                self.return_expression()


            self.state = 302
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def return_expression(self):
            return self.getTypedRuleContext(BKITParser.Return_expressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_expression




    def return_expression(self):

        localctx = BKITParser.Return_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_return_expression)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.expression()
                self.state = 306
                self.return_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expression1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Expression1Context,i)


        def DBEQ(self):
            return self.getToken(BKITParser.DBEQ, 0)

        def NEQ(self):
            return self.getToken(BKITParser.NEQ, 0)

        def GT(self):
            return self.getToken(BKITParser.GT, 0)

        def LT(self):
            return self.getToken(BKITParser.LT, 0)

        def LTE(self):
            return self.getToken(BKITParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKITParser.GTE, 0)

        def NEQF(self):
            return self.getToken(BKITParser.NEQF, 0)

        def GTF(self):
            return self.getToken(BKITParser.GTF, 0)

        def LTF(self):
            return self.getToken(BKITParser.LTF, 0)

        def GTEF(self):
            return self.getToken(BKITParser.GTEF, 0)

        def LTEF(self):
            return self.getToken(BKITParser.LTEF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.expression1(0)
                self.state = 311
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.DBEQ) | (1 << BKITParser.NEQ) | (1 << BKITParser.LT) | (1 << BKITParser.GT) | (1 << BKITParser.LTE) | (1 << BKITParser.GTE) | (1 << BKITParser.NEQF) | (1 << BKITParser.LTF) | (1 << BKITParser.GTF) | (1 << BKITParser.LTEF) | (1 << BKITParser.GTEF))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 312
                self.expression1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.expression1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(BKITParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(BKITParser.Expression1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression1



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expression1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 320
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 321
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 322
                    self.expression2(0) 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(BKITParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(BKITParser.Expression2Context,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADDF(self):
            return self.getToken(BKITParser.ADDF, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.SUB) | (1 << BKITParser.ADDF) | (1 << BKITParser.SUBF))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 333
                    self.expression3(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(BKITParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(BKITParser.Expression3Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def MULF(self):
            return self.getToken(BKITParser.MULF, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def DIVF(self):
            return self.getToken(BKITParser.DIVF, 0)

        def RMD(self):
            return self.getToken(BKITParser.RMD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.expression4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.DIV) | (1 << BKITParser.RMD) | (1 << BKITParser.MULF) | (1 << BKITParser.DIVF))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 344
                    self.expression4() 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def expression4(self):
            return self.getTypedRuleContext(BKITParser.Expression4Context,0)


        def expression5(self):
            return self.getTypedRuleContext(BKITParser.Expression5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression4




    def expression4(self):

        localctx = BKITParser.Expression4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expression4)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(BKITParser.NOT)
                self.state = 351
                self.expression4()
                pass
            elif token in [BKITParser.BOOLEAN_LITERAL, BKITParser.INTEGER_LITERAL, BKITParser.REAL_LITERAL, BKITParser.STRING_LITERAL, BKITParser.SUB, BKITParser.SUBF, BKITParser.LP, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.expression5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(BKITParser.Expression5Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def expression6(self):
            return self.getTypedRuleContext(BKITParser.Expression6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression5




    def expression5(self):

        localctx = BKITParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 356
                self.expression5()
                pass
            elif token in [BKITParser.BOOLEAN_LITERAL, BKITParser.INTEGER_LITERAL, BKITParser.REAL_LITERAL, BKITParser.STRING_LITERAL, BKITParser.LP, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(BKITParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(BKITParser.Expression6Context,0)


        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression6



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.LSB or _la==BKITParser.RSB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression7




    def expression7(self):

        localctx = BKITParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression7)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operand




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_operand)
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(BKITParser.LP)
                self.state = 375
                self.expression()
                self.state = 376
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.BOOLEAN_LITERAL, BKITParser.INTEGER_LITERAL, BKITParser.REAL_LITERAL, BKITParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.literal()
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
                self.match(BKITParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BKITParser.INTEGER_LITERAL, 0)

        def REAL_LITERAL(self):
            return self.getToken(BKITParser.REAL_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(BKITParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(BKITParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BOOLEAN_LITERAL) | (1 << BKITParser.INTEGER_LITERAL) | (1 << BKITParser.REAL_LITERAL) | (1 << BKITParser.STRING_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_exp_list




    def exp_list(self):

        localctx = BKITParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.expression()
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 385
                self.match(BKITParser.COMMA)
                self.state = 386
                self.expression()
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_index_operator




    def index_operator(self):

        localctx = BKITParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_index_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 392
                self.match(BKITParser.LSB)
                self.state = 393
                self.expression()
                self.state = 394
                self.match(BKITParser.RSB)
                self.state = 398 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LSB):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(BKITParser.ID)
            self.state = 401
            self.match(BKITParser.LP)
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BOOLEAN_LITERAL) | (1 << BKITParser.INTEGER_LITERAL) | (1 << BKITParser.REAL_LITERAL) | (1 << BKITParser.STRING_LITERAL) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.ID))) != 0):
                self.state = 402
                self.exp_list()


            self.state = 405
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.expression1_sempred
        self._predicates[29] = self.expression2_sempred
        self._predicates[30] = self.expression3_sempred
        self._predicates[33] = self.expression6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




