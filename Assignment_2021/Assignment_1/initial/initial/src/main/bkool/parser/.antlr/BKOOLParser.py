# Generated from d:\Assignment_PPL\Assignment_2021\Assignment_1\initial\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u019c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\6\2V\n\2\r\2\16\2W\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\5\3`\n\3\3\3\3\3\3\3\3\3\3\4\5\4")
        buf.write("g\n\4\3\4\3\4\5\4k\n\4\7\4m\n\4\f\4\16\4p\13\4\3\5\5\5")
        buf.write("s\n\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6{\n\6\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u0087\n\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u008e\n\t\5\t\u0090\n\t\3\n\5\n\u0093\n\n\3\n")
        buf.write("\3\n\3\n\5\n\u0098\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00a5\n\13\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00ab\n\f\3\r\3\r\5\r\u00af\n\r\3\r\5\r\u00b2\n\r\3")
        buf.write("\r\3\r\3\16\5\16\u00b7\n\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00bf\n\16\3\16\3\16\3\16\3\16\5\16\u00c5\n\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00cf\n")
        buf.write("\17\3\20\3\20\3\20\3\20\5\20\u00d5\n\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u00e1\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e9\n\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\5\30\u0100\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\5\31\u0107\n\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u0111\n\32\3\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u011b\n\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u0122\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\7\35\u012a\n\35\f\35\16\35\u012d\13\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\7\36\u0135\n\36\f\36\16\36")
        buf.write("\u0138\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0140")
        buf.write("\n\37\f\37\16\37\u0143\13\37\3 \3 \3 \3 \3 \3 \7 \u014b")
        buf.write("\n \f \16 \u014e\13 \3!\3!\3!\3!\3!\5!\u0155\n!\3\"\3")
        buf.write("\"\3\"\5\"\u015a\n\"\3#\3#\3#\3#\3#\3#\5#\u0162\n#\3$")
        buf.write("\3$\3$\3$\3$\3$\7$\u016a\n$\f$\16$\u016d\13$\3%\3%\3%")
        buf.write("\3%\5%\u0173\n%\3%\3%\3%\5%\u0178\n%\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\5&\u0182\n&\3\'\3\'\3\'\3\'\3\'\5\'\u0189\n\'")
        buf.write("\3(\3(\5(\u018d\n(\3)\3)\3*\3*\3*\3*\7*\u0195\n*\f*\16")
        buf.write("*\u0198\13*\3*\3*\3*\2\78:<>F+\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR\2\13")
        buf.write("\7\2\3\3\n\n\f\f\16\16\24\24\6\2\3\3\n\n\f\f\16\16\3\2")
        buf.write("\31\32\3\2#&\3\2!\"\3\2\'(\3\2\33\34\3\2\35 \3\2\658\2")
        buf.write("\u01a3\2U\3\2\2\2\4[\3\2\2\2\6n\3\2\2\2\br\3\2\2\2\nz")
        buf.write("\3\2\2\2\f|\3\2\2\2\16~\3\2\2\2\20\u008f\3\2\2\2\22\u0092")
        buf.write("\3\2\2\2\24\u00a4\3\2\2\2\26\u00aa\3\2\2\2\30\u00ac\3")
        buf.write("\2\2\2\32\u00c4\3\2\2\2\34\u00ce\3\2\2\2\36\u00d4\3\2")
        buf.write("\2\2 \u00d6\3\2\2\2\"\u00e0\3\2\2\2$\u00e2\3\2\2\2&\u00ea")
        buf.write("\3\2\2\2(\u00f3\3\2\2\2*\u00f6\3\2\2\2,\u00f9\3\2\2\2")
        buf.write(".\u00ff\3\2\2\2\60\u0101\3\2\2\2\62\u010b\3\2\2\2\64\u011a")
        buf.write("\3\2\2\2\66\u0121\3\2\2\28\u0123\3\2\2\2:\u012e\3\2\2")
        buf.write("\2<\u0139\3\2\2\2>\u0144\3\2\2\2@\u0154\3\2\2\2B\u0159")
        buf.write("\3\2\2\2D\u0161\3\2\2\2F\u0163\3\2\2\2H\u0177\3\2\2\2")
        buf.write("J\u0181\3\2\2\2L\u0188\3\2\2\2N\u018c\3\2\2\2P\u018e\3")
        buf.write("\2\2\2R\u0190\3\2\2\2TV\5\4\3\2UT\3\2\2\2VW\3\2\2\2WU")
        buf.write("\3\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\2\2\3Z\3\3\2\2\2[\\\7")
        buf.write("\5\2\2\\_\79\2\2]^\7\t\2\2^`\79\2\2_]\3\2\2\2_`\3\2\2")
        buf.write("\2`a\3\2\2\2ab\7-\2\2bc\5\6\4\2cd\7.\2\2d\5\3\2\2\2eg")
        buf.write("\7\30\2\2fe\3\2\2\2fg\3\2\2\2gj\3\2\2\2hk\5\b\5\2ik\5")
        buf.write("\22\n\2jh\3\2\2\2ji\3\2\2\2km\3\2\2\2lf\3\2\2\2mp\3\2")
        buf.write("\2\2nl\3\2\2\2no\3\2\2\2o\7\3\2\2\2pn\3\2\2\2qs\7\27\2")
        buf.write("\2rq\3\2\2\2rs\3\2\2\2st\3\2\2\2tu\5\n\6\2uv\5\20\t\2")
        buf.write("vw\7\61\2\2w\t\3\2\2\2x{\5\f\7\2y{\5\16\b\2zx\3\2\2\2")
        buf.write("zy\3\2\2\2{\13\3\2\2\2|}\t\2\2\2}\r\3\2\2\2~\177\t\3\2")
        buf.write("\2\177\u0080\7+\2\2\u0080\u0081\7\65\2\2\u0081\u0082\7")
        buf.write(",\2\2\u0082\17\3\2\2\2\u0083\u0086\79\2\2\u0084\u0085")
        buf.write("\7<\2\2\u0085\u0087\5\64\33\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7\64\2")
        buf.write("\2\u0089\u0090\5\20\t\2\u008a\u008d\79\2\2\u008b\u008c")
        buf.write("\7<\2\2\u008c\u008e\5\64\33\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u0083\3\2\2\2")
        buf.write("\u008f\u008a\3\2\2\2\u0090\21\3\2\2\2\u0091\u0093\5\f")
        buf.write("\7\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\u0095\79\2\2\u0095\u0097\7/\2\2\u0096\u0098")
        buf.write("\5\24\13\2\u0097\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009a\7\60\2\2\u009a\u009b\5\30\r")
        buf.write("\2\u009b\23\3\2\2\2\u009c\u009d\5\f\7\2\u009d\u009e\5")
        buf.write("\26\f\2\u009e\u009f\7\61\2\2\u009f\u00a0\5\24\13\2\u00a0")
        buf.write("\u00a5\3\2\2\2\u00a1\u00a2\5\f\7\2\u00a2\u00a3\5\26\f")
        buf.write("\2\u00a3\u00a5\3\2\2\2\u00a4\u009c\3\2\2\2\u00a4\u00a1")
        buf.write("\3\2\2\2\u00a5\25\3\2\2\2\u00a6\u00a7\79\2\2\u00a7\u00a8")
        buf.write("\7\64\2\2\u00a8\u00ab\5\26\f\2\u00a9\u00ab\79\2\2\u00aa")
        buf.write("\u00a6\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\27\3\2\2\2\u00ac")
        buf.write("\u00ae\7-\2\2\u00ad\u00af\5\32\16\2\u00ae\u00ad\3\2\2")
        buf.write("\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00b2")
        buf.write("\5\36\20\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b4\7.\2\2\u00b4\31\3\2\2\2\u00b5")
        buf.write("\u00b7\7\27\2\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2")
        buf.write("\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\5\f\7\2\u00b9\u00ba")
        buf.write("\5\26\f\2\u00ba\u00bb\7\61\2\2\u00bb\u00bc\5\32\16\2\u00bc")
        buf.write("\u00c5\3\2\2\2\u00bd\u00bf\7\27\2\2\u00be\u00bd\3\2\2")
        buf.write("\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1")
        buf.write("\5\f\7\2\u00c1\u00c2\5\26\f\2\u00c2\u00c3\7\61\2\2\u00c3")
        buf.write("\u00c5\3\2\2\2\u00c4\u00b6\3\2\2\2\u00c4\u00be\3\2\2\2")
        buf.write("\u00c5\33\3\2\2\2\u00c6\u00cf\5 \21\2\u00c7\u00cf\5$\23")
        buf.write("\2\u00c8\u00cf\5&\24\2\u00c9\u00cf\5(\25\2\u00ca\u00cf")
        buf.write("\5*\26\2\u00cb\u00cf\5,\27\2\u00cc\u00cf\5,\27\2\u00cd")
        buf.write("\u00cf\5.\30\2\u00ce\u00c6\3\2\2\2\u00ce\u00c7\3\2\2\2")
        buf.write("\u00ce\u00c8\3\2\2\2\u00ce\u00c9\3\2\2\2\u00ce\u00ca\3")
        buf.write("\2\2\2\u00ce\u00cb\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd")
        buf.write("\3\2\2\2\u00cf\35\3\2\2\2\u00d0\u00d1\5\34\17\2\u00d1")
        buf.write("\u00d2\5\36\20\2\u00d2\u00d5\3\2\2\2\u00d3\u00d5\5\34")
        buf.write("\17\2\u00d4\u00d0\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\37")
        buf.write("\3\2\2\2\u00d6\u00d7\5\"\22\2\u00d7\u00d8\7<\2\2\u00d8")
        buf.write("\u00d9\5\64\33\2\u00d9\u00da\7\61\2\2\u00da!\3\2\2\2\u00db")
        buf.write("\u00e1\79\2\2\u00dc\u00dd\79\2\2\u00dd\u00de\7+\2\2\u00de")
        buf.write("\u00df\7\65\2\2\u00df\u00e1\7,\2\2\u00e0\u00db\3\2\2\2")
        buf.write("\u00e0\u00dc\3\2\2\2\u00e1#\3\2\2\2\u00e2\u00e3\7\13\2")
        buf.write("\2\u00e3\u00e4\5\64\33\2\u00e4\u00e5\7\17\2\2\u00e5\u00e8")
        buf.write("\5\34\17\2\u00e6\u00e7\7\b\2\2\u00e7\u00e9\5\34\17\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9%\3\2\2\2\u00ea")
        buf.write("\u00eb\7\20\2\2\u00eb\u00ec\79\2\2\u00ec\u00ed\7<\2\2")
        buf.write("\u00ed\u00ee\5\64\33\2\u00ee\u00ef\t\4\2\2\u00ef\u00f0")
        buf.write("\5\64\33\2\u00f0\u00f1\7\7\2\2\u00f1\u00f2\5\34\17\2\u00f2")
        buf.write("\'\3\2\2\2\u00f3\u00f4\7\4\2\2\u00f4\u00f5\7\61\2\2\u00f5")
        buf.write(")\3\2\2\2\u00f6\u00f7\7\6\2\2\u00f7\u00f8\7\61\2\2\u00f8")
        buf.write("+\3\2\2\2\u00f9\u00fa\7\21\2\2\u00fa\u00fb\5\64\33\2\u00fb")
        buf.write("\u00fc\7\61\2\2\u00fc-\3\2\2\2\u00fd\u0100\5\60\31\2\u00fe")
        buf.write("\u0100\5\62\32\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe\3\2\2")
        buf.write("\2\u0100/\3\2\2\2\u0101\u0102\5\64\33\2\u0102\u0103\7")
        buf.write("\63\2\2\u0103\u0104\79\2\2\u0104\u0106\7/\2\2\u0105\u0107")
        buf.write("\5L\'\2\u0106\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108\u0109\7\60\2\2\u0109\u010a\7\61\2")
        buf.write("\2\u010a\61\3\2\2\2\u010b\u010c\79\2\2\u010c\u010d\7\63")
        buf.write("\2\2\u010d\u010e\79\2\2\u010e\u0110\7/\2\2\u010f\u0111")
        buf.write("\5L\'\2\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u0112\u0113\7\60\2\2\u0113\u0114\7\61\2")
        buf.write("\2\u0114\63\3\2\2\2\u0115\u0116\5\66\34\2\u0116\u0117")
        buf.write("\t\5\2\2\u0117\u0118\5\66\34\2\u0118\u011b\3\2\2\2\u0119")
        buf.write("\u011b\5\66\34\2\u011a\u0115\3\2\2\2\u011a\u0119\3\2\2")
        buf.write("\2\u011b\65\3\2\2\2\u011c\u011d\58\35\2\u011d\u011e\t")
        buf.write("\6\2\2\u011e\u011f\58\35\2\u011f\u0122\3\2\2\2\u0120\u0122")
        buf.write("\58\35\2\u0121\u011c\3\2\2\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\67\3\2\2\2\u0123\u0124\b\35\1\2\u0124\u0125\5:\36\2\u0125")
        buf.write("\u012b\3\2\2\2\u0126\u0127\f\4\2\2\u0127\u0128\t\7\2\2")
        buf.write("\u0128\u012a\5:\36\2\u0129\u0126\3\2\2\2\u012a\u012d\3")
        buf.write("\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c9")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f\b\36\1\2\u012f")
        buf.write("\u0130\5<\37\2\u0130\u0136\3\2\2\2\u0131\u0132\f\4\2\2")
        buf.write("\u0132\u0133\t\b\2\2\u0133\u0135\5<\37\2\u0134\u0131\3")
        buf.write("\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137;\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a")
        buf.write("\b\37\1\2\u013a\u013b\5> \2\u013b\u0141\3\2\2\2\u013c")
        buf.write("\u013d\f\4\2\2\u013d\u013e\t\t\2\2\u013e\u0140\5> \2\u013f")
        buf.write("\u013c\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142=\3\2\2\2\u0143\u0141\3\2\2")
        buf.write("\2\u0144\u0145\b \1\2\u0145\u0146\5@!\2\u0146\u014c\3")
        buf.write("\2\2\2\u0147\u0148\f\4\2\2\u0148\u0149\7*\2\2\u0149\u014b")
        buf.write("\5@!\2\u014a\u0147\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a")
        buf.write("\3\2\2\2\u014c\u014d\3\2\2\2\u014d?\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014f\u0150\5B\"\2\u0150\u0151\7)\2\2\u0151\u0152")
        buf.write("\5@!\2\u0152\u0155\3\2\2\2\u0153\u0155\5B\"\2\u0154\u014f")
        buf.write("\3\2\2\2\u0154\u0153\3\2\2\2\u0155A\3\2\2\2\u0156\u0157")
        buf.write("\t\b\2\2\u0157\u015a\5B\"\2\u0158\u015a\5D#\2\u0159\u0156")
        buf.write("\3\2\2\2\u0159\u0158\3\2\2\2\u015aC\3\2\2\2\u015b\u015c")
        buf.write("\5F$\2\u015c\u015d\7+\2\2\u015d\u015e\5\64\33\2\u015e")
        buf.write("\u015f\7,\2\2\u015f\u0162\3\2\2\2\u0160\u0162\5F$\2\u0161")
        buf.write("\u015b\3\2\2\2\u0161\u0160\3\2\2\2\u0162E\3\2\2\2\u0163")
        buf.write("\u0164\b$\1\2\u0164\u0165\5H%\2\u0165\u016b\3\2\2\2\u0166")
        buf.write("\u0167\f\4\2\2\u0167\u0168\7\63\2\2\u0168\u016a\5H%\2")
        buf.write("\u0169\u0166\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3")
        buf.write("\2\2\2\u016b\u016c\3\2\2\2\u016cG\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016e\u016f\7\r\2\2\u016f\u0170\5H%\2\u0170\u0172")
        buf.write("\7/\2\2\u0171\u0173\5L\'\2\u0172\u0171\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\7\60\2\2\u0175")
        buf.write("\u0178\3\2\2\2\u0176\u0178\5N(\2\u0177\u016e\3\2\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178I\3\2\2\2\u0179\u017a\5\64\33\2\u017a")
        buf.write("\u017b\7\63\2\2\u017b\u017c\79\2\2\u017c\u0182\3\2\2\2")
        buf.write("\u017d\u017e\79\2\2\u017e\u017f\7\63\2\2\u017f\u0182\7")
        buf.write("9\2\2\u0180\u0182\5.\30\2\u0181\u0179\3\2\2\2\u0181\u017d")
        buf.write("\3\2\2\2\u0181\u0180\3\2\2\2\u0182K\3\2\2\2\u0183\u0184")
        buf.write("\5\64\33\2\u0184\u0185\7\64\2\2\u0185\u0186\5L\'\2\u0186")
        buf.write("\u0189\3\2\2\2\u0187\u0189\5\64\33\2\u0188\u0183\3\2\2")
        buf.write("\2\u0188\u0187\3\2\2\2\u0189M\3\2\2\2\u018a\u018d\79\2")
        buf.write("\2\u018b\u018d\5P)\2\u018c\u018a\3\2\2\2\u018c\u018b\3")
        buf.write("\2\2\2\u018dO\3\2\2\2\u018e\u018f\t\n\2\2\u018fQ\3\2\2")
        buf.write("\2\u0190\u0191\7-\2\2\u0191\u0196\5P)\2\u0192\u0193\7")
        buf.write("\64\2\2\u0193\u0195\5P)\2\u0194\u0192\3\2\2\2\u0195\u0198")
        buf.write("\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0199\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\7.\2\2")
        buf.write("\u019aS\3\2\2\2,W_fjnrz\u0086\u008d\u008f\u0092\u0097")
        buf.write("\u00a4\u00aa\u00ae\u00b1\u00b6\u00be\u00c4\u00ce\u00d4")
        buf.write("\u00e0\u00e8\u00ff\u0106\u0110\u011a\u0121\u012b\u0136")
        buf.write("\u0141\u014c\u0154\u0159\u0161\u016b\u0172\u0177\u0181")
        buf.write("\u0188\u018c\u0196")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", "'>'", 
                     "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "'['", 
                     "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", "'.'", 
                     "','", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                      "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
                      "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", "MOD", 
                      "NOT_EQ", "DBEQ", "LT", "GT", "LTEQ", "GTEQ", "OR", 
                      "AND", "NOT", "CONCAT", "LSB", "RSB", "LP", "RP", 
                      "LB", "RB", "SEMI", "COLON", "DOT", "COMMA", "INT_LIT", 
                      "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "ID", "BLOCKCOMMENT", 
                      "LINECOMMENT", "EQ", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declare = 1
    RULE_memberlist = 2
    RULE_attribute_decl = 3
    RULE_all_type = 4
    RULE_primitive_type = 5
    RULE_array_type = 6
    RULE_attr_list = 7
    RULE_method_decl = 8
    RULE_param_list = 9
    RULE_idlist = 10
    RULE_block_stmt = 11
    RULE_var_list = 12
    RULE_stmt = 13
    RULE_list_stmt = 14
    RULE_assign_stmt = 15
    RULE_lhs = 16
    RULE_if_stmt = 17
    RULE_for_stmt = 18
    RULE_break_stmt = 19
    RULE_continue_stmt = 20
    RULE_return_stmt = 21
    RULE_invocation_stmt = 22
    RULE_instance_method = 23
    RULE_static_method = 24
    RULE_exp = 25
    RULE_exp1 = 26
    RULE_exp2 = 27
    RULE_exp3 = 28
    RULE_exp4 = 29
    RULE_exp5 = 30
    RULE_exp6 = 31
    RULE_exp7 = 32
    RULE_exp8 = 33
    RULE_exp9 = 34
    RULE_exp10 = 35
    RULE_member_access = 36
    RULE_explist = 37
    RULE_operands = 38
    RULE_literal = 39
    RULE_array_lit = 40

    ruleNames =  [ "program", "declare", "memberlist", "attribute_decl", 
                   "all_type", "primitive_type", "array_type", "attr_list", 
                   "method_decl", "param_list", "idlist", "block_stmt", 
                   "var_list", "stmt", "list_stmt", "assign_stmt", "lhs", 
                   "if_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "invocation_stmt", "instance_method", 
                   "static_method", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", "member_access", 
                   "explist", "operands", "literal", "array_lit" ]

    EOF = Token.EOF
    BOOLEAN=1
    BREAK=2
    CLASS=3
    CONTINUE=4
    DO=5
    ELSE=6
    EXTENDS=7
    FLOAT=8
    IF=9
    INT=10
    NEW=11
    STRING=12
    THEN=13
    FOR=14
    RETURN=15
    TRUE=16
    FALSE=17
    VOID=18
    NIL=19
    THIS=20
    FINAL=21
    STATIC=22
    TO=23
    DOWNTO=24
    ADD=25
    SUB=26
    MUL=27
    FLOAT_DIV=28
    INT_DIV=29
    MOD=30
    NOT_EQ=31
    DBEQ=32
    LT=33
    GT=34
    LTEQ=35
    GTEQ=36
    OR=37
    AND=38
    NOT=39
    CONCAT=40
    LSB=41
    RSB=42
    LP=43
    RP=44
    LB=45
    RB=46
    SEMI=47
    COLON=48
    DOT=49
    COMMA=50
    INT_LIT=51
    FLOAT_LIT=52
    BOOL_LIT=53
    STRING_LIT=54
    ID=55
    BLOCKCOMMENT=56
    LINECOMMENT=57
    EQ=58
    WS=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

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
            return self.getToken(BKOOLParser.EOF, 0)

        def declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.DeclareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.DeclareContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.declare()
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 87
            self.match(BKOOLParser.EOF)
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

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def memberlist(self):
            return self.getTypedRuleContext(BKOOLParser.MemberlistContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_declare




    def declare(self):

        localctx = BKOOLParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(BKOOLParser.CLASS)
            self.state = 90
            self.match(BKOOLParser.ID)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 91
                self.match(BKOOLParser.EXTENDS)
                self.state = 92
                self.match(BKOOLParser.ID)


            self.state = 95
            self.match(BKOOLParser.LP)
            self.state = 96
            self.memberlist()
            self.state = 97
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Attribute_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Attribute_declContext,i)


        def method_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Method_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Method_declContext,i)


        def STATIC(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.STATIC)
            else:
                return self.getToken(BKOOLParser.STATIC, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_memberlist




    def memberlist(self):

        localctx = BKOOLParser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memberlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 99
                    self.match(BKOOLParser.STATIC)


                self.state = 104
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 102
                    self.attribute_decl()
                    pass

                elif la_ == 2:
                    self.state = 103
                    self.method_decl()
                    pass


                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_type(self):
            return self.getTypedRuleContext(BKOOLParser.All_typeContext,0)


        def attr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_decl




    def attribute_decl(self):

        localctx = BKOOLParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 111
                self.match(BKOOLParser.FINAL)


            self.state = 114
            self.all_type()
            self.state = 115
            self.attr_list()
            self.state = 116
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_all_type




    def all_type(self):

        localctx = BKOOLParser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_all_type)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
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


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 125
            self.match(BKOOLParser.LSB)
            self.state = 126
            self.match(BKOOLParser.INT_LIT)
            self.state = 127
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_listContext,0)


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attr_list




    def attr_list(self):

        localctx = BKOOLParser.Attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr_list)
        self._la = 0 # Token type
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(BKOOLParser.ID)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQ:
                    self.state = 130
                    self.match(BKOOLParser.EQ)
                    self.state = 131
                    self.exp()


                self.state = 134
                self.match(BKOOLParser.COMMA)
                self.state = 135
                self.attr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(BKOOLParser.ID)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQ:
                    self.state = 137
                    self.match(BKOOLParser.EQ)
                    self.state = 138
                    self.exp()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0):
                self.state = 143
                self.primitive_type()


            self.state = 146
            self.match(BKOOLParser.ID)
            self.state = 147
            self.match(BKOOLParser.LB)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0):
                self.state = 148
                self.param_list()


            self.state = 151
            self.match(BKOOLParser.RB)
            self.state = 152
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_list)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.primitive_type()
                self.state = 155
                self.idlist()
                self.state = 156
                self.match(BKOOLParser.SEMI)
                self.state = 157
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.primitive_type()
                self.state = 160
                self.idlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idlist)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(BKOOLParser.ID)
                self.state = 165
                self.match(BKOOLParser.COMMA)
                self.state = 166
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_listContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.List_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(BKOOLParser.LP)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL))) != 0):
                self.state = 171
                self.var_list()


            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 174
                self.list_stmt()


            self.state = 177
            self.match(BKOOLParser.RP)
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

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_listContext,0)


        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_list




    def var_list(self):

        localctx = BKOOLParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.FINAL:
                    self.state = 179
                    self.match(BKOOLParser.FINAL)


                self.state = 182
                self.primitive_type()
                self.state = 183
                self.idlist()
                self.state = 184
                self.match(BKOOLParser.SEMI)
                self.state = 185
                self.var_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.FINAL:
                    self.state = 187
                    self.match(BKOOLParser.FINAL)


                self.state = 190
                self.primitive_type()
                self.state = 191
                self.idlist()
                self.state = 192
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 200
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 201
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 202
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 203
                self.invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.List_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_stmt




    def list_stmt(self):

        localctx = BKOOLParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_stmt)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.stmt()
                self.state = 207
                self.list_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.stmt()
                pass


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
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.lhs()
            self.state = 213
            self.match(BKOOLParser.EQ)
            self.state = 214
            self.exp()
            self.state = 215
            self.match(BKOOLParser.SEMI)
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
            return self.getToken(BKOOLParser.ID, 0)

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lhs)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(BKOOLParser.ID)
                self.state = 219
                self.match(BKOOLParser.LSB)
                self.state = 220
                self.match(BKOOLParser.INT_LIT)
                self.state = 221
                self.match(BKOOLParser.RSB)
                pass


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
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(BKOOLParser.IF)
            self.state = 225
            self.exp()
            self.state = 226
            self.match(BKOOLParser.THEN)
            self.state = 227
            self.stmt()
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 228
                self.match(BKOOLParser.ELSE)
                self.state = 229
                self.stmt()


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
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(BKOOLParser.FOR)
            self.state = 233
            self.match(BKOOLParser.ID)
            self.state = 234
            self.match(BKOOLParser.EQ)
            self.state = 235
            self.exp()
            self.state = 236
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 237
            self.exp()
            self.state = 238
            self.match(BKOOLParser.DO)
            self.state = 239
            self.stmt()
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
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(BKOOLParser.BREAK)
            self.state = 242
            self.match(BKOOLParser.SEMI)
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
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = BKOOLParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(BKOOLParser.CONTINUE)
            self.state = 245
            self.match(BKOOLParser.SEMI)
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
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(BKOOLParser.RETURN)
            self.state = 248
            self.exp()
            self.state = 249
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invocation_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method(self):
            return self.getTypedRuleContext(BKOOLParser.Instance_methodContext,0)


        def static_method(self):
            return self.getTypedRuleContext(BKOOLParser.Static_methodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_invocation_stmt




    def invocation_stmt(self):

        localctx = BKOOLParser.Invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_invocation_stmt)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.instance_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.static_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instance_method




    def instance_method(self):

        localctx = BKOOLParser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_instance_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.exp()
            self.state = 256
            self.match(BKOOLParser.DOT)
            self.state = 257
            self.match(BKOOLParser.ID)
            self.state = 258
            self.match(BKOOLParser.LB)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 259
                self.explist()


            self.state = 262
            self.match(BKOOLParser.RB)
            self.state = 263
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_static_method




    def static_method(self):

        localctx = BKOOLParser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(BKOOLParser.ID)
            self.state = 266
            self.match(BKOOLParser.DOT)
            self.state = 267
            self.match(BKOOLParser.ID)
            self.state = 268
            self.match(BKOOLParser.LB)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 269
                self.explist()


            self.state = 272
            self.match(BKOOLParser.RB)
            self.state = 273
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LTEQ(self):
            return self.getToken(BKOOLParser.LTEQ, 0)

        def GTEQ(self):
            return self.getToken(BKOOLParser.GTEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.exp1()
                self.state = 276
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LTEQ) | (1 << BKOOLParser.GTEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 277
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp2Context,i)


        def DBEQ(self):
            return self.getToken(BKOOLParser.DBEQ, 0)

        def NOT_EQ(self):
            return self.getToken(BKOOLParser.NOT_EQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.exp2(0)
                self.state = 283
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NOT_EQ or _la==BKOOLParser.DBEQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 284
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 292
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 293
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 294
                    self.exp3(0) 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 303
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 304
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 305
                    self.exp4(0) 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def INT_DIV(self):
            return self.getToken(BKOOLParser.INT_DIV, 0)

        def FLOAT_DIV(self):
            return self.getToken(BKOOLParser.FLOAT_DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 314
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 315
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INT_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 316
                    self.exp5(0) 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 330
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 325
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 326
                    self.match(BKOOLParser.CONCAT)
                    self.state = 327
                    self.exp6() 
                self.state = 332
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp6)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.exp7()
                self.state = 334
                self.match(BKOOLParser.NOT)
                self.state = 335
                self.exp6()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.exp7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 341
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.exp8()
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


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8




    def exp8(self):

        localctx = BKOOLParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp8)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.exp9(0)
                self.state = 346
                self.match(BKOOLParser.LSB)
                self.state = 347
                self.exp()
                self.state = 348
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.exp9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 356
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 357
                    self.match(BKOOLParser.DOT)
                    self.state = 358
                    self.exp10() 
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(BKOOLParser.NEW)
                self.state = 365
                self.exp10()
                self.state = 366
                self.match(BKOOLParser.LB)
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 367
                    self.explist()


                self.state = 370
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.operands()
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


    class Member_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member_access




    def member_access(self):

        localctx = BKOOLParser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_member_access)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.exp()
                self.state = 376
                self.match(BKOOLParser.DOT)
                self.state = 377
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.match(BKOOLParser.ID)
                self.state = 380
                self.match(BKOOLParser.DOT)
                self.state = 381
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 382
                self.invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_explist




    def explist(self):

        localctx = BKOOLParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_explist)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.exp()
                self.state = 386
                self.match(BKOOLParser.COMMA)
                self.state = 387
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_operands




    def operands(self):

        localctx = BKOOLParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_operands)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.literal()
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

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKOOLParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STRING_LIT))) != 0)):
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


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LiteralContext,i)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lit




    def array_lit(self):

        localctx = BKOOLParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(BKOOLParser.LP)
            self.state = 399
            self.literal()
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 400
                self.match(BKOOLParser.COMMA)
                self.state = 401
                self.literal()
                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 407
            self.match(BKOOLParser.RP)
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
        self._predicates[27] = self.exp2_sempred
        self._predicates[28] = self.exp3_sempred
        self._predicates[29] = self.exp4_sempred
        self._predicates[30] = self.exp5_sempred
        self._predicates[34] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




