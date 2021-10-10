# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01ab\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\6\2X\n\2\r\2\16")
        buf.write("\2Y\3\2\3\2\3\3\3\3\3\3\3\3\5\3b\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\5\4i\n\4\3\4\3\4\5\4m\n\4\7\4o\n\4\f\4\16\4r\13\4\3")
        buf.write("\5\5\5u\n\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\177\n")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\n")
        buf.write("\u008d\n\n\3\n\3\n\3\n\3\n\3\n\5\n\u0094\n\n\5\n\u0096")
        buf.write("\n\n\3\13\5\13\u0099\n\13\3\13\3\13\3\13\5\13\u009e\n")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u00ab\n\f\3\r\3\r\3\r\3\r\5\r\u00b1\n\r\3\16\3\16\5\16")
        buf.write("\u00b5\n\16\3\16\5\16\u00b8\n\16\3\16\3\16\3\17\5\17\u00bd")
        buf.write("\n\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00c5\n\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00cb\n\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00d4\n\20\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u00da\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u00e8\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u00f0\n\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\5\31\u0108\n\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\5\32\u0111\n\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u011a\n\33\3\33\3\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\5\34\u0123\n\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u012a\n\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\7\36\u0132\n\36\f\36\16\36\u0135\13\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\7\37\u013d\n\37\f\37\16\37\u0140\13")
        buf.write("\37\3 \3 \3 \3 \3 \3 \7 \u0148\n \f \16 \u014b\13 \3!")
        buf.write("\3!\3!\3!\3!\3!\7!\u0153\n!\f!\16!\u0156\13!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\5\"\u015d\n\"\3#\3#\3#\5#\u0162\n#\3$\3$\3")
        buf.write("$\3$\3$\3$\5$\u016a\n$\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0174")
        buf.write("\n%\3%\5%\u0177\n%\7%\u0179\n%\f%\16%\u017c\13%\3&\3&")
        buf.write("\3&\3&\5&\u0182\n&\3&\3&\3&\5&\u0187\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u018e\n\'\3(\3(\3(\3(\5(\u0194\n(\3)\3)\3)")
        buf.write("\3)\5)\u019a\n)\3*\3*\3*\3*\7*\u01a0\n*\f*\16*\u01a3\13")
        buf.write("*\5*\u01a5\n*\3*\3*\3+\3+\3+\2\7:<>@H,\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRT\2\n\6\2\3\3\n\n\f\f\16\16\3\2\31\32\3\2#&\3\2")
        buf.write("!\"\3\2\'(\3\2\33\34\3\2\35 \3\2\22\23\2\u01b8\2W\3\2")
        buf.write("\2\2\4]\3\2\2\2\6p\3\2\2\2\bt\3\2\2\2\n~\3\2\2\2\f\u0080")
        buf.write("\3\2\2\2\16\u0082\3\2\2\2\20\u0084\3\2\2\2\22\u0095\3")
        buf.write("\2\2\2\24\u0098\3\2\2\2\26\u00aa\3\2\2\2\30\u00b0\3\2")
        buf.write("\2\2\32\u00b2\3\2\2\2\34\u00ca\3\2\2\2\36\u00d3\3\2\2")
        buf.write("\2 \u00d9\3\2\2\2\"\u00db\3\2\2\2$\u00e7\3\2\2\2&\u00e9")
        buf.write("\3\2\2\2(\u00f1\3\2\2\2*\u00fb\3\2\2\2,\u00fe\3\2\2\2")
        buf.write(".\u0101\3\2\2\2\60\u0107\3\2\2\2\62\u010b\3\2\2\2\64\u0114")
        buf.write("\3\2\2\2\66\u0122\3\2\2\28\u0129\3\2\2\2:\u012b\3\2\2")
        buf.write("\2<\u0136\3\2\2\2>\u0141\3\2\2\2@\u014c\3\2\2\2B\u015c")
        buf.write("\3\2\2\2D\u0161\3\2\2\2F\u0169\3\2\2\2H\u016b\3\2\2\2")
        buf.write("J\u0186\3\2\2\2L\u018d\3\2\2\2N\u0193\3\2\2\2P\u0199\3")
        buf.write("\2\2\2R\u019b\3\2\2\2T\u01a8\3\2\2\2VX\5\4\3\2WV\3\2\2")
        buf.write("\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\7\2\2\3")
        buf.write("\\\3\3\2\2\2]^\7\5\2\2^a\78\2\2_`\7\t\2\2`b\78\2\2a_\3")
        buf.write("\2\2\2ab\3\2\2\2bc\3\2\2\2cd\7-\2\2de\5\6\4\2ef\7.\2\2")
        buf.write("f\5\3\2\2\2gi\7\30\2\2hg\3\2\2\2hi\3\2\2\2il\3\2\2\2j")
        buf.write("m\5\b\5\2km\5\24\13\2lj\3\2\2\2lk\3\2\2\2mo\3\2\2\2nh")
        buf.write("\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\7\3\2\2\2rp\3")
        buf.write("\2\2\2su\7\27\2\2ts\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\5\n")
        buf.write("\6\2wx\5\22\n\2xy\7\61\2\2y\t\3\2\2\2z\177\5\16\b\2{\177")
        buf.write("\5\20\t\2|\177\5\f\7\2}\177\78\2\2~z\3\2\2\2~{\3\2\2\2")
        buf.write("~|\3\2\2\2~}\3\2\2\2\177\13\3\2\2\2\u0080\u0081\7\24\2")
        buf.write("\2\u0081\r\3\2\2\2\u0082\u0083\t\2\2\2\u0083\17\3\2\2")
        buf.write("\2\u0084\u0085\t\2\2\2\u0085\u0086\7+\2\2\u0086\u0087")
        buf.write("\7\65\2\2\u0087\u0088\7,\2\2\u0088\21\3\2\2\2\u0089\u008c")
        buf.write("\78\2\2\u008a\u008b\7;\2\2\u008b\u008d\5\66\34\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\u008f\7\64\2\2\u008f\u0096\5\22\n\2\u0090\u0093")
        buf.write("\78\2\2\u0091\u0092\7;\2\2\u0092\u0094\5\66\34\2\u0093")
        buf.write("\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2")
        buf.write("\u0095\u0089\3\2\2\2\u0095\u0090\3\2\2\2\u0096\23\3\2")
        buf.write("\2\2\u0097\u0099\5\n\6\2\u0098\u0097\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\78\2\2\u009b")
        buf.write("\u009d\7/\2\2\u009c\u009e\5\26\f\2\u009d\u009c\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\7")
        buf.write("\60\2\2\u00a0\u00a1\5\32\16\2\u00a1\25\3\2\2\2\u00a2\u00a3")
        buf.write("\5\n\6\2\u00a3\u00a4\5\30\r\2\u00a4\u00a5\7\61\2\2\u00a5")
        buf.write("\u00a6\5\26\f\2\u00a6\u00ab\3\2\2\2\u00a7\u00a8\5\n\6")
        buf.write("\2\u00a8\u00a9\5\30\r\2\u00a9\u00ab\3\2\2\2\u00aa\u00a2")
        buf.write("\3\2\2\2\u00aa\u00a7\3\2\2\2\u00ab\27\3\2\2\2\u00ac\u00ad")
        buf.write("\78\2\2\u00ad\u00ae\7\64\2\2\u00ae\u00b1\5\30\r\2\u00af")
        buf.write("\u00b1\78\2\2\u00b0\u00ac\3\2\2\2\u00b0\u00af\3\2\2\2")
        buf.write("\u00b1\31\3\2\2\2\u00b2\u00b4\7-\2\2\u00b3\u00b5\5\34")
        buf.write("\17\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b7")
        buf.write("\3\2\2\2\u00b6\u00b8\5 \21\2\u00b7\u00b6\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\7.\2\2")
        buf.write("\u00ba\33\3\2\2\2\u00bb\u00bd\7\27\2\2\u00bc\u00bb\3\2")
        buf.write("\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf")
        buf.write("\5\n\6\2\u00bf\u00c0\5\30\r\2\u00c0\u00c1\7\61\2\2\u00c1")
        buf.write("\u00c2\5\34\17\2\u00c2\u00cb\3\2\2\2\u00c3\u00c5\7\27")
        buf.write("\2\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\u00c7\5\n\6\2\u00c7\u00c8\5\30\r\2\u00c8")
        buf.write("\u00c9\7\61\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00bc\3\2\2")
        buf.write("\2\u00ca\u00c4\3\2\2\2\u00cb\35\3\2\2\2\u00cc\u00d4\5")
        buf.write("\"\22\2\u00cd\u00d4\5&\24\2\u00ce\u00d4\5(\25\2\u00cf")
        buf.write("\u00d4\5*\26\2\u00d0\u00d4\5,\27\2\u00d1\u00d4\5.\30\2")
        buf.write("\u00d2\u00d4\5\60\31\2\u00d3\u00cc\3\2\2\2\u00d3\u00cd")
        buf.write("\3\2\2\2\u00d3\u00ce\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d3")
        buf.write("\u00d0\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2")
        buf.write("\u00d4\37\3\2\2\2\u00d5\u00d6\5\36\20\2\u00d6\u00d7\5")
        buf.write(" \21\2\u00d7\u00da\3\2\2\2\u00d8\u00da\5\36\20\2\u00d9")
        buf.write("\u00d5\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da!\3\2\2\2\u00db")
        buf.write("\u00dc\5$\23\2\u00dc\u00dd\7\62\2\2\u00dd\u00de\7;\2\2")
        buf.write("\u00de\u00df\5\66\34\2\u00df\u00e0\7\61\2\2\u00e0#\3\2")
        buf.write("\2\2\u00e1\u00e8\5\66\34\2\u00e2\u00e3\5\66\34\2\u00e3")
        buf.write("\u00e4\7+\2\2\u00e4\u00e5\5\66\34\2\u00e5\u00e6\7,\2\2")
        buf.write("\u00e6\u00e8\3\2\2\2\u00e7\u00e1\3\2\2\2\u00e7\u00e2\3")
        buf.write("\2\2\2\u00e8%\3\2\2\2\u00e9\u00ea\7\13\2\2\u00ea\u00eb")
        buf.write("\5\66\34\2\u00eb\u00ec\7\17\2\2\u00ec\u00ef\5\36\20\2")
        buf.write("\u00ed\u00ee\7\b\2\2\u00ee\u00f0\5\36\20\2\u00ef\u00ed")
        buf.write("\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\'\3\2\2\2\u00f1\u00f2")
        buf.write("\7\20\2\2\u00f2\u00f3\78\2\2\u00f3\u00f4\7\62\2\2\u00f4")
        buf.write("\u00f5\7;\2\2\u00f5\u00f6\5\66\34\2\u00f6\u00f7\t\3\2")
        buf.write("\2\u00f7\u00f8\5\66\34\2\u00f8\u00f9\7\7\2\2\u00f9\u00fa")
        buf.write("\5\36\20\2\u00fa)\3\2\2\2\u00fb\u00fc\7\4\2\2\u00fc\u00fd")
        buf.write("\7\61\2\2\u00fd+\3\2\2\2\u00fe\u00ff\7\6\2\2\u00ff\u0100")
        buf.write("\7\61\2\2\u0100-\3\2\2\2\u0101\u0102\7\21\2\2\u0102\u0103")
        buf.write("\5\66\34\2\u0103\u0104\7\61\2\2\u0104/\3\2\2\2\u0105\u0108")
        buf.write("\5\62\32\2\u0106\u0108\5\64\33\2\u0107\u0105\3\2\2\2\u0107")
        buf.write("\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\7\61\2")
        buf.write("\2\u010a\61\3\2\2\2\u010b\u010c\5\66\34\2\u010c\u010d")
        buf.write("\7\63\2\2\u010d\u010e\78\2\2\u010e\u0110\7/\2\2\u010f")
        buf.write("\u0111\5L\'\2\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111\u0112\3\2\2\2\u0112\u0113\7\60\2\2\u0113\63\3\2")
        buf.write("\2\2\u0114\u0115\78\2\2\u0115\u0116\7\63\2\2\u0116\u0117")
        buf.write("\78\2\2\u0117\u0119\7/\2\2\u0118\u011a\5L\'\2\u0119\u0118")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write("\u011c\7\60\2\2\u011c\65\3\2\2\2\u011d\u011e\58\35\2\u011e")
        buf.write("\u011f\t\4\2\2\u011f\u0120\58\35\2\u0120\u0123\3\2\2\2")
        buf.write("\u0121\u0123\58\35\2\u0122\u011d\3\2\2\2\u0122\u0121\3")
        buf.write("\2\2\2\u0123\67\3\2\2\2\u0124\u0125\5:\36\2\u0125\u0126")
        buf.write("\t\5\2\2\u0126\u0127\5:\36\2\u0127\u012a\3\2\2\2\u0128")
        buf.write("\u012a\5:\36\2\u0129\u0124\3\2\2\2\u0129\u0128\3\2\2\2")
        buf.write("\u012a9\3\2\2\2\u012b\u012c\b\36\1\2\u012c\u012d\5<\37")
        buf.write("\2\u012d\u0133\3\2\2\2\u012e\u012f\f\4\2\2\u012f\u0130")
        buf.write("\t\6\2\2\u0130\u0132\5<\37\2\u0131\u012e\3\2\2\2\u0132")
        buf.write("\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0134;\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0137\b\37\1")
        buf.write("\2\u0137\u0138\5> \2\u0138\u013e\3\2\2\2\u0139\u013a\f")
        buf.write("\4\2\2\u013a\u013b\t\7\2\2\u013b\u013d\5> \2\u013c\u0139")
        buf.write("\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e")
        buf.write("\u013f\3\2\2\2\u013f=\3\2\2\2\u0140\u013e\3\2\2\2\u0141")
        buf.write("\u0142\b \1\2\u0142\u0143\5@!\2\u0143\u0149\3\2\2\2\u0144")
        buf.write("\u0145\f\4\2\2\u0145\u0146\t\b\2\2\u0146\u0148\5@!\2\u0147")
        buf.write("\u0144\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a?\3\2\2\2\u014b\u0149\3\2\2")
        buf.write("\2\u014c\u014d\b!\1\2\u014d\u014e\5B\"\2\u014e\u0154\3")
        buf.write("\2\2\2\u014f\u0150\f\4\2\2\u0150\u0151\7*\2\2\u0151\u0153")
        buf.write("\5B\"\2\u0152\u014f\3\2\2\2\u0153\u0156\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155A\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0157\u0158\5D#\2\u0158\u0159\7)\2\2\u0159")
        buf.write("\u015a\5B\"\2\u015a\u015d\3\2\2\2\u015b\u015d\5D#\2\u015c")
        buf.write("\u0157\3\2\2\2\u015c\u015b\3\2\2\2\u015dC\3\2\2\2\u015e")
        buf.write("\u015f\t\7\2\2\u015f\u0162\5D#\2\u0160\u0162\5F$\2\u0161")
        buf.write("\u015e\3\2\2\2\u0161\u0160\3\2\2\2\u0162E\3\2\2\2\u0163")
        buf.write("\u0164\5H%\2\u0164\u0165\7+\2\2\u0165\u0166\5\66\34\2")
        buf.write("\u0166\u0167\7,\2\2\u0167\u016a\3\2\2\2\u0168\u016a\5")
        buf.write("H%\2\u0169\u0163\3\2\2\2\u0169\u0168\3\2\2\2\u016aG\3")
        buf.write("\2\2\2\u016b\u016c\b%\1\2\u016c\u016d\5J&\2\u016d\u017a")
        buf.write("\3\2\2\2\u016e\u016f\f\4\2\2\u016f\u0170\7\63\2\2\u0170")
        buf.write("\u0176\5J&\2\u0171\u0173\7/\2\2\u0172\u0174\5L\'\2\u0173")
        buf.write("\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0177\7\60\2\2\u0176\u0171\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u0179\3\2\2\2\u0178\u016e\3\2\2\2\u0179")
        buf.write("\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017bI\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017e\7\r\2")
        buf.write("\2\u017e\u017f\5J&\2\u017f\u0181\7/\2\2\u0180\u0182\5")
        buf.write("L\'\2\u0181\u0180\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183\u0184\7\60\2\2\u0184\u0187\3\2\2\2\u0185")
        buf.write("\u0187\5N(\2\u0186\u017d\3\2\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("K\3\2\2\2\u0188\u0189\5\66\34\2\u0189\u018a\7\64\2\2\u018a")
        buf.write("\u018b\5L\'\2\u018b\u018e\3\2\2\2\u018c\u018e\5\66\34")
        buf.write("\2\u018d\u0188\3\2\2\2\u018d\u018c\3\2\2\2\u018eM\3\2")
        buf.write("\2\2\u018f\u0194\78\2\2\u0190\u0194\5P)\2\u0191\u0194")
        buf.write("\5R*\2\u0192\u0194\7\26\2\2\u0193\u018f\3\2\2\2\u0193")
        buf.write("\u0190\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2")
        buf.write("\u0194O\3\2\2\2\u0195\u019a\7\65\2\2\u0196\u019a\7\66")
        buf.write("\2\2\u0197\u019a\5T+\2\u0198\u019a\7\67\2\2\u0199\u0195")
        buf.write("\3\2\2\2\u0199\u0196\3\2\2\2\u0199\u0197\3\2\2\2\u0199")
        buf.write("\u0198\3\2\2\2\u019aQ\3\2\2\2\u019b\u01a4\7-\2\2\u019c")
        buf.write("\u01a1\5P)\2\u019d\u019e\7\64\2\2\u019e\u01a0\5P)\2\u019f")
        buf.write("\u019d\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3")
        buf.write("\2\2\2\u01a4\u019c\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a7\7.\2\2\u01a7S\3\2\2\2\u01a8\u01a9")
        buf.write("\t\t\2\2\u01a9U\3\2\2\2/Yahlpt~\u008c\u0093\u0095\u0098")
        buf.write("\u009d\u00aa\u00b0\u00b4\u00b7\u00bc\u00c4\u00ca\u00d3")
        buf.write("\u00d9\u00e7\u00ef\u0107\u0110\u0119\u0122\u0129\u0133")
        buf.write("\u013e\u0149\u0154\u015c\u0161\u0169\u0173\u0176\u017a")
        buf.write("\u0181\u0186\u018d\u0193\u0199\u01a1\u01a4")
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
                     "<INVALID>", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                      "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
                      "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", "MOD", 
                      "NOT_EQ", "DBEQ", "LT", "GT", "LTEQ", "GTEQ", "OR", 
                      "AND", "NOT", "CONCAT", "LSB", "RSB", "LP", "RP", 
                      "LB", "RB", "SEMI", "COLON", "DOT", "COMMA", "INT_LIT", 
                      "FLOAT_LIT", "STRING_LIT", "ID", "BLOCKCOMMENT", "LINECOMMENT", 
                      "EQ", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declare = 1
    RULE_memberlist = 2
    RULE_attribute_decl = 3
    RULE_all_type = 4
    RULE_void_type = 5
    RULE_primitive_type = 6
    RULE_array_type = 7
    RULE_attr_list = 8
    RULE_method_decl = 9
    RULE_param_list = 10
    RULE_idlist = 11
    RULE_block_stmt = 12
    RULE_var_list = 13
    RULE_stmt = 14
    RULE_list_stmt = 15
    RULE_assign_stmt = 16
    RULE_lhs = 17
    RULE_if_stmt = 18
    RULE_for_stmt = 19
    RULE_break_stmt = 20
    RULE_continue_stmt = 21
    RULE_return_stmt = 22
    RULE_invocation_stmt = 23
    RULE_instance_method = 24
    RULE_static_method = 25
    RULE_exp = 26
    RULE_exp1 = 27
    RULE_exp2 = 28
    RULE_exp3 = 29
    RULE_exp4 = 30
    RULE_exp5 = 31
    RULE_exp6 = 32
    RULE_exp7 = 33
    RULE_exp8 = 34
    RULE_exp9 = 35
    RULE_exp10 = 36
    RULE_explist = 37
    RULE_operands = 38
    RULE_literal = 39
    RULE_array_lit = 40
    RULE_bool_lit = 41

    ruleNames =  [ "program", "declare", "memberlist", "attribute_decl", 
                   "all_type", "void_type", "primitive_type", "array_type", 
                   "attr_list", "method_decl", "param_list", "idlist", "block_stmt", 
                   "var_list", "stmt", "list_stmt", "assign_stmt", "lhs", 
                   "if_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "invocation_stmt", "instance_method", 
                   "static_method", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", "explist", 
                   "operands", "literal", "array_lit", "bool_lit" ]

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
    STRING_LIT=53
    ID=54
    BLOCKCOMMENT=55
    LINECOMMENT=56
    EQ=57
    WS=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.declare()
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 89
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = BKOOLParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(BKOOLParser.CLASS)
            self.state = 92
            self.match(BKOOLParser.ID)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 93
                self.match(BKOOLParser.EXTENDS)
                self.state = 94
                self.match(BKOOLParser.ID)


            self.state = 97
            self.match(BKOOLParser.LP)
            self.state = 98
            self.memberlist()
            self.state = 99
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlist" ):
                return visitor.visitMemberlist(self)
            else:
                return visitor.visitChildren(self)




    def memberlist(self):

        localctx = BKOOLParser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memberlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 101
                    self.match(BKOOLParser.STATIC)


                self.state = 106
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 104
                    self.attribute_decl()
                    pass

                elif la_ == 2:
                    self.state = 105
                    self.method_decl()
                    pass


                self.state = 112
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl" ):
                return visitor.visitAttribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl(self):

        localctx = BKOOLParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 113
                self.match(BKOOLParser.FINAL)


            self.state = 116
            self.all_type()
            self.state = 117
            self.attr_list()
            self.state = 118
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def void_type(self):
            return self.getTypedRuleContext(BKOOLParser.Void_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_all_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_type" ):
                return visitor.visitAll_type(self)
            else:
                return visitor.visitChildren(self)




    def all_type(self):

        localctx = BKOOLParser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_all_type)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.array_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.void_type()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Void_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_void_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoid_type" ):
                return visitor.visitVoid_type(self)
            else:
                return visitor.visitChildren(self)




    def void_type(self):

        localctx = BKOOLParser.Void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_void_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(BKOOLParser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
            self.match(BKOOLParser.LSB)
            self.state = 132
            self.match(BKOOLParser.INT_LIT)
            self.state = 133
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_list" ):
                return visitor.visitAttr_list(self)
            else:
                return visitor.visitChildren(self)




    def attr_list(self):

        localctx = BKOOLParser.Attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr_list)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(BKOOLParser.ID)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQ:
                    self.state = 136
                    self.match(BKOOLParser.EQ)
                    self.state = 137
                    self.exp()


                self.state = 140
                self.match(BKOOLParser.COMMA)
                self.state = 141
                self.attr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(BKOOLParser.ID)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQ:
                    self.state = 143
                    self.match(BKOOLParser.EQ)
                    self.state = 144
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
        __slots__ = 'parser'

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


        def all_type(self):
            return self.getTypedRuleContext(BKOOLParser.All_typeContext,0)


        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 149
                self.all_type()


            self.state = 152
            self.match(BKOOLParser.ID)
            self.state = 153
            self.match(BKOOLParser.LB)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0):
                self.state = 154
                self.param_list()


            self.state = 157
            self.match(BKOOLParser.RB)
            self.state = 158
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_type(self):
            return self.getTypedRuleContext(BKOOLParser.All_typeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_list)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.all_type()
                self.state = 161
                self.idlist()
                self.state = 162
                self.match(BKOOLParser.SEMI)
                self.state = 163
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.all_type()
                self.state = 166
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_idlist)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(BKOOLParser.ID)
                self.state = 171
                self.match(BKOOLParser.COMMA)
                self.state = 172
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(BKOOLParser.LP)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 177
                self.var_list()


            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 180
                self.list_stmt()


            self.state = 183
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_type(self):
            return self.getTypedRuleContext(BKOOLParser.All_typeContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKOOLParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.FINAL:
                    self.state = 185
                    self.match(BKOOLParser.FINAL)


                self.state = 188
                self.all_type()
                self.state = 189
                self.idlist()
                self.state = 190
                self.match(BKOOLParser.SEMI)
                self.state = 191
                self.var_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.FINAL:
                    self.state = 193
                    self.match(BKOOLParser.FINAL)


                self.state = 196
                self.all_type()
                self.state = 197
                self.idlist()
                self.state = 198
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 206
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 208
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.List_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmt" ):
                return visitor.visitList_stmt(self)
            else:
                return visitor.visitChildren(self)




    def list_stmt(self):

        localctx = BKOOLParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_stmt)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.stmt()
                self.state = 212
                self.list_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.lhs()
            self.state = 218
            self.match(BKOOLParser.COLON)
            self.state = 219
            self.match(BKOOLParser.EQ)
            self.state = 220
            self.exp()
            self.state = 221
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lhs)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.exp()
                self.state = 225
                self.match(BKOOLParser.LSB)
                self.state = 226
                self.exp()
                self.state = 227
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(BKOOLParser.IF)
            self.state = 232
            self.exp()
            self.state = 233
            self.match(BKOOLParser.THEN)
            self.state = 234
            self.stmt()
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 235
                self.match(BKOOLParser.ELSE)
                self.state = 236
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(BKOOLParser.FOR)
            self.state = 240
            self.match(BKOOLParser.ID)
            self.state = 241
            self.match(BKOOLParser.COLON)
            self.state = 242
            self.match(BKOOLParser.EQ)
            self.state = 243
            self.exp()
            self.state = 244
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 245
            self.exp()
            self.state = 246
            self.match(BKOOLParser.DO)
            self.state = 247
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(BKOOLParser.BREAK)
            self.state = 250
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKOOLParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(BKOOLParser.CONTINUE)
            self.state = 253
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(BKOOLParser.RETURN)
            self.state = 256
            self.exp()
            self.state = 257
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def instance_method(self):
            return self.getTypedRuleContext(BKOOLParser.Instance_methodContext,0)


        def static_method(self):
            return self.getTypedRuleContext(BKOOLParser.Static_methodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocation_stmt" ):
                return visitor.visitInvocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def invocation_stmt(self):

        localctx = BKOOLParser.Invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 259
                self.instance_method()
                pass

            elif la_ == 2:
                self.state = 260
                self.static_method()
                pass


            self.state = 263
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_methodContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instance_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method" ):
                return visitor.visitInstance_method(self)
            else:
                return visitor.visitChildren(self)




    def instance_method(self):

        localctx = BKOOLParser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_instance_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.exp()
            self.state = 266
            self.match(BKOOLParser.DOT)
            self.state = 267
            self.match(BKOOLParser.ID)
            self.state = 268
            self.match(BKOOLParser.LB)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 269
                self.explist()


            self.state = 272
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_static_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method" ):
                return visitor.visitStatic_method(self)
            else:
                return visitor.visitChildren(self)




    def static_method(self):

        localctx = BKOOLParser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(BKOOLParser.ID)
            self.state = 275
            self.match(BKOOLParser.DOT)
            self.state = 276
            self.match(BKOOLParser.ID)
            self.state = 277
            self.match(BKOOLParser.LB)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 278
                self.explist()


            self.state = 281
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.exp1()
                self.state = 284
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LTEQ) | (1 << BKOOLParser.GTEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 285
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.exp2(0)
                self.state = 291
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NOT_EQ or _la==BKOOLParser.DBEQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 292
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 300
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 301
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 302
                    self.exp3(0) 
                self.state = 307
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 313
                    self.exp4(0) 
                self.state = 318
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 322
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 323
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INT_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 324
                    self.exp5(0) 
                self.state = 329
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 333
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 334
                    self.match(BKOOLParser.CONCAT)
                    self.state = 335
                    self.exp6() 
                self.state = 340
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp6)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.exp7()
                self.state = 342
                self.match(BKOOLParser.NOT)
                self.state = 343
                self.exp6()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 349
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKOOLParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp8)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.exp9(0)
                self.state = 354
                self.match(BKOOLParser.LSB)
                self.state = 355
                self.exp()
                self.state = 356
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 365
                    self.match(BKOOLParser.DOT)
                    self.state = 366
                    self.exp10()
                    self.state = 372
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        self.state = 367
                        self.match(BKOOLParser.LB)
                        self.state = 369
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                            self.state = 368
                            self.explist()


                        self.state = 371
                        self.match(BKOOLParser.RB)

             
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(BKOOLParser.NEW)
                self.state = 380
                self.exp10()
                self.state = 381
                self.match(BKOOLParser.LB)
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 382
                    self.explist()


                self.state = 385
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
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


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = BKOOLParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_explist)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.exp()
                self.state = 391
                self.match(BKOOLParser.COMMA)
                self.state = 392
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Array_litContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKOOLParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_operands)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.literal()
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.array_lit()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 400
                self.match(BKOOLParser.THIS)
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Bool_litContext,0)


        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literal)
        try:
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 405
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 406
                self.match(BKOOLParser.STRING_LIT)
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


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKOOLParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(BKOOLParser.LP)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT))) != 0):
                self.state = 410
                self.literal()
                self.state = 415
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 411
                    self.match(BKOOLParser.COMMA)
                    self.state = 412
                    self.literal()
                    self.state = 417
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 420
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = BKOOLParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.exp2_sempred
        self._predicates[29] = self.exp3_sempred
        self._predicates[30] = self.exp4_sempred
        self._predicates[31] = self.exp5_sempred
        self._predicates[35] = self.exp9_sempred
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
         




