import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # Test Identifier
    def test_identifier_1(self):
        self.assertTrue(TestLexer.test("abcdbcdbc","abcdbcdbc,<EOF>",101))

    def test_identifier_2(self):
        self.assertTrue(TestLexer.test("asdaAAAABBB_CCojoqdw","asdaAAAABBB_CCojoqdw,<EOF>",102))

    def test_identifier_3(self):
        self.assertTrue(TestLexer.test("_abcdbcdbc","_abcdbcdbc,<EOF>",103))

    def test_identifier_4(self):
        self.assertTrue(TestLexer.test("__abcdbcdbc","__abcdbcdbc,<EOF>",104))

    def test_identifier_5(self):
        self.assertTrue(TestLexer.test("__abcdbcd128u12840812048bc","__abcdbcd128u12840812048bc,<EOF>",105))

    def test_identifier_6(self):
        self.assertTrue(TestLexer.test("__12331323","__12331323,<EOF>",106))

    def test_identifier_7(self):
        self.assertTrue(TestLexer.test("__abcdbcdbc","__abcdbcdbc,<EOF>",107))

    def test_identifier_8(self):
        self.assertTrue(TestLexer.test("__aovpwe__12093__bcdbcdbc","__aovpwe__12093__bcdbcdbc,<EOF>",108))

    def test_identifier_9(self):
        self.assertTrue(TestLexer.test("_________________","_________________,<EOF>",109))

    def test_identifier_10(self):
        self.assertTrue(TestLexer.test("__abcdbc19823U13VKJSNDJW__________3iwfjiwjef748989uuwof_______dbc","__abcdbc19823U13VKJSNDJW__________3iwfjiwjef748989uuwof_______dbc,<EOF>",110))

    # Test string literal
    def test_string_literal_1(self):
         self.assertTrue(TestLexer.test("""\"abc def\"""", """"abc def",<EOF>""", 111))

    def test_string_literal_2(self):
        self.assertTrue(TestLexer.test("""\"ab def\"""",""""ab def",<EOF>""",112))

    def test_string_literal_3(self):
        self.assertTrue(TestLexer.test(""""He asked me: \\"Where is John?\\"" """,""""He asked me: \\"Where is John?\\"",<EOF>""",113))

    def test_string_literal_4(self):
        self.assertTrue(TestLexer.test("""\"abc1!!@#$$%^in\"""",""""abc1!!@#$$%^in",<EOF>""",114))

    def test_string_literal_5(self):
        self.assertTrue(TestLexer.test("""\"&J^1a_.\" \"?67Sp\" \"{,}6pAsz\" """,""""&J^1a_.","?67Sp","{,}6pAsz",<EOF>""",115))

    def test_string_literal_6(self):
        self.assertTrue(TestLexer.test("""\"He asked me: \\"What is your name\\"\"""", """"He asked me: \\"What is your name\\"",<EOF>""",116))

    def test_string_literal_7(self):
        self.assertTrue(TestLexer.test("\"abc snn aT\" \" \" \" ure fnjan  Tujwqnj \"",""""abc snn aT"," "," ure fnjan  Tujwqnj ",<EOF>""",117))

    def test_string_literal_8(self):
        self.assertTrue(TestLexer.test("\"a+11.2+\"mam.123\" 12 %^&\"",""""a+11.2+",mam,.,123," 12 %^&",<EOF>""",118))

    def test_string_literal_9(self):
        self.assertTrue(TestLexer.test("""\"38n\"aFfs&&0aED\"0.!!=!7n\"""",""""38n",aFfs,&&,0,aED,"0.!!=!7n",<EOF>""",119))

    def test_string_literal_10(self):
        self.assertTrue(TestLexer.test("""\"38n +- [] { asdsd }qdqw, : aFfs&&0aED\"0.\"!!=!7n\"""",""""38n +- [] { asdsd }qdqw, : aFfs&&0aED",0.,"!!=!7n",<EOF>""",120))

    # Test int literal
    def test_int_literal_1(self):
         self.assertTrue(TestLexer.test("0 1555 15" ,"0,1555,15,<EOF>",121))

    def test_int_literal_2(self):
         self.assertTrue(TestLexer.test("121 2565661161 1665616 151516 116161 6516815351561 86116518 151611" ,"121,2565661161,1665616,151516,116161,6516815351561,86116518,151611,<EOF>",122))

    def test_int_literal_3(self):
         self.assertTrue(TestLexer.test("12392" ,"12392,<EOF>",123))

    def test_int_literal_4(self):
         self.assertTrue(TestLexer.test("12380 122000 0220200 020012 0102030200 001230129301 0130" ,"12380,122000,0,220200,0,20012,0,102030200,0,0,1230129301,0,130,<EOF>",124))

    def test_int_literal_5(self):
         self.assertTrue(TestLexer.test("0123901230901301300 0103 0130 101030 010 3013093019392929229 2 1292929929292100 0 1 10" ,"0,123901230901301300,0,103,0,130,101030,0,10,3013093019392929229,2,1292929929292100,0,1,10,<EOF>",125))

    def test_int_literal_6(self):
         self.assertTrue(TestLexer.test("1239 123990318239809 12038 093809890 1" ,"1239,123990318239809,12038,0,93809890,1,<EOF>",126))

    def test_int_literal_7(self):
         self.assertTrue(TestLexer.test("00000000100000001 00 0001010100 00000000  10010 012030 231" ,"0,0,0,0,0,0,0,0,100000001,0,0,0,0,0,1010100,0,0,0,0,0,0,0,0,10010,0,12030,231,<EOF>",127))

    def test_int_literal_8(self):
         self.assertTrue(TestLexer.test("21309 90123901203 9120309913 0123990 31903830983091280 7318297 91823787123987 189 78971 89789222222222222222222222222 379231 1312" ,"21309,90123901203,9120309913,0,123990,31903830983091280,7318297,91823787123987,189,78971,89789222222222222222222222222,379231,1312,<EOF>",128))

    def test_int_literal_9(self):
         self.assertTrue(TestLexer.test("1320139 90183 08999999999998123333333333 000000000000010000000000000 88888888888888102398 20398282103" ,"1320139,90183,0,8999999999998123333333333,0,0,0,0,0,0,0,0,0,0,0,0,0,10000000000000,88888888888888102398,20398282103,<EOF>",129))

    def test_int_literal_10(self):
         self.assertTrue(TestLexer.test("103988888888888888888888888888888091 8012830 938 091380983 09" ,"103988888888888888888888888888888091,8012830,938,0,91380983,0,9,<EOF>",130))

    # Test float literal
    def test_float_literal_1(self):
        self.assertTrue(TestLexer.test("""0.12E+10""", """0.12E+10,<EOF>""", 131))

    def test_float_literal_2(self):
        self.assertTrue(TestLexer.test("""00000012000.0000E00000""", """00000012000.0000E00000,<EOF>""", 132))

    def test_float_literal_3(self):
        self.assertTrue(TestLexer.test("""12.e-3""", """12.e-3,<EOF>""", 133))

    def test_float_literal_4(self):
        self.assertTrue(TestLexer.test("""9E-1020323412331321""", """9E-1020323412331321,<EOF>""", 134))

    def test_float_literal_5(self):
        self.assertTrue(TestLexer.test("""131738912739e+231830123090 12393910380921e-0""", """131738912739e+231830123090,12393910380921e-0,<EOF>""", 135))

    def test_float_literal_6(self):
        self.assertTrue(TestLexer.test("""4E123123 23921837981E1 478923749.123139E12 1.""", """4E123123,23921837981E1,478923749.123139E12,1.,<EOF>""", 136))

    def test_float_literal_7(self):
        self.assertTrue(TestLexer.test("""127389127389. 18320923. 1281388908488943e-123901309 12e0""", """127389127389.,18320923.,1281388908488943e-123901309,12e0,<EOF>""", 137))

    def test_float_literal_8(self):
        self.assertTrue(TestLexer.test("""14989283198.13123123 12. 2.32 123.2 2.2 0.000 12.2""", """14989283198.13123123,12.,2.32,123.2,2.2,0.000,12.2,<EOF>""", 138))

    def test_float_literal_9(self):
        self.assertTrue(TestLexer.test("""14989283198.13123123 12. 2.32 123.2 2.2 0.000 12.2""", """14989283198.13123123,12.,2.32,123.2,2.2,0.000,12.2,<EOF>""", 139))

    def test_float_literal_10(self):
        self.assertTrue(TestLexer.test("""14989283198.13123123 12. 2.32 123.2 2.2 0.000 12.2""", """14989283198.13123123,12.,2.32,123.2,2.2,0.000,12.2,<EOF>""", 140))

    # Test keyword
    def test_keyword_1(self):
        self.assertTrue(TestLexer.test("""boolean class""", """boolean,class,<EOF>""", 141))

    def test_keyword_2(self):
        self.assertTrue(TestLexer.test("""break continue""", """break,continue,<EOF>""", 142))

    def test_keyword_3(self):
        self.assertTrue(TestLexer.test("""do else""", """do,else,<EOF>""", 143))

    def test_keyword_4(self):
        self.assertTrue(TestLexer.test("""extends float""", """extends,float,<EOF>""", 144))

    def test_keyword_5(self):
        self.assertTrue(TestLexer.test("""if int new string""", """if,int,new,string,<EOF>""", 145))

    def test_keyword_6(self):
        self.assertTrue(TestLexer.test("""then for return true""", """then,for,return,true,<EOF>""", 146))

    def test_keyword_7(self):
        self.assertTrue(TestLexer.test("""false void nil""", """false,void,nil,<EOF>""", 147))

    def test_keyword_8(self):
        self.assertTrue(TestLexer.test("""this final static""", """this,final,static,<EOF>""", 148))

    def test_keyword_9(self):
        self.assertTrue(TestLexer.test("""to downto""", """to,downto,<EOF>""", 149))

    def test_keyword_10(self):
        self.assertTrue(TestLexer.test("""boolean class boolean class to downto this final static false void nil string int float""", """boolean,class,boolean,class,to,downto,this,final,static,false,void,nil,string,int,float,<EOF>""", 150))

    # Test comment
    def test_comment_1(self):
        self.assertTrue(TestLexer.test("""/* */""", """<EOF>""", 151))

    def test_comment_2(self):
        self.assertTrue(TestLexer.test("""/* aaskjjasdkjlsdjljaldjk */""", """<EOF>""", 152))

    def test_comment_3(self):
        self.assertTrue(TestLexer.test("""/* This is a block comment so # has no meaning here */""", """<EOF>""", 153))

    def test_comment_4(self):
        self.assertTrue(TestLexer.test("""/* ufhwqla * 9))90 90()909 ;"qwldkqwk \t \n \r  */""", """<EOF>""", 154))

    def test_comment_5(self):
        self.assertTrue(TestLexer.test("""/* ufhwqla iwjvpowjep /* */ qwldkqwk \t \n \r  */""", """<EOF>""", 155))

    def test_comment_6(self):
        self.assertTrue(TestLexer.test("""# iqajdoiqwjdoiqjwdoijo""", """<EOF>""", 156))

    def test_comment_7(self):
        self.assertTrue(TestLexer.test("""# hadasdiosajdo \t \f \t \\ #""", """<EOF>""", 157))

    def test_comment_8(self):
        self.assertTrue(TestLexer.test("""# "1 6163188*()*098v098 9088 281938127 *&(&789 \r""", """<EOF>""", 158))

    def test_comment_9(self):
        self.assertTrue(TestLexer.test("""#### oqwdoij jqwoijj ijwdj""", """<EOF>""", 159))

    def test_comment_10(self):
        self.assertTrue(TestLexer.test("""#owejejiofjfi j 05ewf1e5f1 "5we53e1f31 jwduhqwh iojjqow #$%^*^**&* kjw9""", """<EOF>""", 160))

    # Test
    def test_error_char_1(self):
        self.assertTrue(TestLexer.test("""ab?svn""", """ab,Error Token ?""", 161))

    def test_error_char_2(self):
        self.assertTrue(TestLexer.test("""smkassrj4AORqwExkrCxZPi`""", """smkassrj4AORqwExkrCxZPi,Error Token `""", 162))

    def test_error_char_3(self):
        self.assertTrue(TestLexer.test("""True12E+4b(9kZ~YBraRCF""", """True12E,+,4,b,(,9,kZ,Error Token ~""", 163))

    def test_error_char_4(self):
        self.assertTrue(TestLexer.test("""asas12pQ*6'q0+Y==}f(>9Xn""", """asas12pQ,*,6,Error Token '""", 164))

    def test_error_char_5(self):
        self.assertTrue(TestLexer.test("""0x123aFG[@WQS{QBW7Y6]le5""", """0,x123aFG,[,Error Token @""", 165))

    def test_error_char_6(self):
        self.assertTrue(TestLexer.test("""|A123jmkmf+-%km""", """Error Token |""", 166))

    def test_error_char_7(self):
        self.assertTrue(TestLexer.test("""!== != && * % $ ... """, """!=,=,!=,&&,*,%,Error Token $""", 167))

    def test_error_char_8(self):
        self.assertTrue(TestLexer.test("""a,:,=,a,Error Token &""", """a,,,:,,,=,,,a,,,Error,Token,Error Token &""", 168))

    def test_error_char_9(self):
        self.assertTrue(TestLexer.test(""";0O1244lJ~IbbnQL!x-OBd "qwdjqwdjoijo"  qwiodjwj qw8ys09""", """;,0,O1244lJ,Error Token ~""", 169))

    def test_error_char_10(self):
        self.assertTrue(TestLexer.test(""" jodijwjijkn kjnsnjknasjkn nuisniqwnoi $ """, """jodijwjijkn,kjnsnjknasjkn,nuisniqwnoi,Error Token $""", 170))

    # Test unclosed string
    def test_unterminated_string_1(self):
        self.assertTrue(TestLexer.test(""" "abc def  """, """Unclosed String: "abc def  """, 171))

    def test_unterminated_string_2(self):
        self.assertTrue(TestLexer.test(""" acnkNmkobYn{!}+xI1+\"`YS2h.J(""","""acnkNmkobYn,{,!,},+,xI1,+,Unclosed String: "`YS2h.J(""", 172))

    def test_unterminated_string_3(self):
        self.assertTrue(TestLexer.test(""" \"acJDJVBms!,lds \" {\"abc\"} 123\"abc """,""""acJDJVBms!,lds ",{,"abc",},123,Unclosed String: "abc """, 173))

    def test_unterminated_string_4(self):
        self.assertTrue(TestLexer.test(""" hbsdjn\"vkmm*y32ryikk """, """hbsdjn,Unclosed String: "vkmm*y32ryikk """, 174))

    def test_unterminated_string_5(self):
        self.assertTrue(TestLexer.test(""" \".akdn&***&&Hub`22Y\"<{;}\"Y`=DxXhZKwdmqh ""","""".akdn&***&&Hub`22Y",<,{,;,},Unclosed String: "Y`=DxXhZKwdmqh """, 175))

    def test_unterminated_string_6(self):
        self.assertTrue(TestLexer.test(""" {aaSRass}\"Nk8U;\"rA\"@Y3*\"oV\"bh1  ""","""{,aaSRass,},"Nk8U;",rA,"@Y3*",oV,Unclosed String: "bh1  """, 176))

    def test_unterminated_string_7(self):
        self.assertTrue(TestLexer.test(""" a+11.2+\"mam.123\" 12 \"%^&  ""","""a,+,11.2,+,"mam.123",12,Unclosed String: "%^&  """, 177))

    def test_unterminated_string_8(self):
        self.assertTrue(TestLexer.test("""ioevioo&&qjjwq+==++12je\"bacxyc  ""","""ioevioo,&&,qjjwq,+,==,+,+,12,je,Unclosed String: "bacxyc  """, 178))

    def test_unterminated_string_9(self):
        self.assertTrue(TestLexer.test(""" \"acnv "" \"abc  """, """"acnv "," ",abc,<EOF>""", 179))

    def test_unterminated_string_10(self):
        self.assertTrue(TestLexer.test(""" aF&&)aLqwpokpokq912p9i9+--iowjwqX\"+>.<.+>aX+#Fft""","""aF,&&,),aLqwpokpokq912p9i9,+,-,-,iowjwqX,Unclosed String: "+>.<.+>aX+#Fft""",180))

    # Test illegal escape
    def test_illegal_escape_1(self):
        self.assertTrue(TestLexer.test(""" "abc \\" \\"h def" """, """"abc \\" \\"h def",<EOF>""", 181))

    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.test(""" "ado\\mado"  """, """Illegal Escape In String: "ado\\m""", 182))

    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.test(""" 123abc \"xyz\\k 456\"  """, """123,abc,Illegal Escape In String: "xyz\\k""", 183))

    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.test(""" 12+3>9-3x \"**asndabc+\\^ def\"  ""","""12,+,3,>,9,-,3,x,Illegal Escape In String: "**asndabc+\^""", 184))

    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.test(""" \"1.2+1.3+1.4\\o'\"0x9999  """, """Illegal Escape In String: "1.2+1.3+1.4\\o""",185))

    def test_illegal_escape_6(self):
        self.assertTrue(TestLexer.test(""" (*0O12*)+1.1 \"ba\\qm\f\" ""","""(,*,0,O12,*,),+,1.1,Illegal Escape In String: "ba\q""", 186))

    def test_illegal_escape_7(self):
        self.assertTrue(TestLexer.test(""" abc \"abc1!!@#$$%^i\\u\" 12yz  ""","""abc,Illegal Escape In String: "abc1!!@#$$%^i\\u""", 187))

    def test_illegal_escape_8(self):
        self.assertTrue(TestLexer.test(""" \"\\!LScna\" """, """Illegal Escape In String: "\\!""", 188))

    def test_illegal_escape_9(self):
        self.assertTrue(TestLexer.test(""" \"&^3u89,dls\\F12!LS\\kc\\na\"  ""","""Illegal Escape In String: "&^3u89,dls\\F""", 189))

    def test_illegal_escape_10(self):
        self.assertTrue(TestLexer.test(""" \"ahiuhfuiTure*12-==\\|skldmfO02 \"  ""","""Illegal Escape In String: "ahiuhfuiTure*12-==\\|""", 190))

    # Test all
    def test_all_1(self):
        self.assertTrue(TestLexer.test("""if && +. <. \"odkok\'ksmfffjujn\" 0x91209 0oa""", """if,&&,+,.,<,.,"odkok'ksmfffjujn",0,x91209,0,oa,<EOF>""", 191))

    def test_all_2(self):
        self.assertTrue(TestLexer.test("""ksdcm akak % == lap al 10.94 ! @ ksmdk""", """ksdcm,akak,%,==,lap,al,10.94,!,Error Token @""", 192))

    def test_all_3(self):
        self.assertTrue(TestLexer.test("""b=x+9&&a23+=12kv.456E954-12+-.5*100/""", """b,=,x,+,9,&&,a23,+,=,12,kv,.,456E954,-,12,+,-,.,5,*,100,/,<EOF>""", 193))

    def test_all_4(self):
        self.assertTrue(TestLexer.test("""10E+9.23 aAKK -45e10 + 2-- 0.e34 +00 ;  ; {]][:][;<.>,.<.,.>,]}""", """10E+9,.,23,aAKK,-,45e10,+,2,-,-,0.e34,+,0,0,;,;,{,],],[,:,],[,;,<,.,>,,,.,<,.,,,.,>,,,],},<EOF>""", 194))

    def test_all_5(self):
        self.assertTrue(TestLexer.test(""" wepofffds ,.;()kepm j306 ()8*81m iqo \t \n \\.v isk _ """, """wepofffds,,,.,;,(,),kepm,j306,(,),8,*,81,m,iqo,\,.,v,isk,_,<EOF>""", 195))

    def test_all_6(self):
        self.assertTrue(TestLexer.test("""class extends final static 45646468 iu89319i09  ^^&&^&&""", """class,extends,final,static,45646468,iu89319i09,^,^,&&,^,&&,<EOF>""", 196))

    def test_all_7(self):
        self.assertTrue(TestLexer.test("""12.912E-10 owejwjoj jwowjoi jojweiojfojo joij))()() 0)()()()()0 9&&**8 787""", """12.912E-10,owejwjoj,jwowjoi,jojweiojfojo,joij,),),(,),(,),0,),(,),(,),(,),(,),0,9,&&,*,*,8,787,<EOF>""", 197))

    def test_all_8(self):
        self.assertTrue(TestLexer.test("""1pi39i 90i90iv jj0wjeoci &&^^||{}!!! && % %%% %% !""", """1,pi39i,90,i90iv,jj0wjeoci,&&,^,^,||,{,},!,!,!,&&,%,%,%,%,%,%,!,<EOF>""", 198))

    def test_all_9(self):
        self.assertTrue(TestLexer.test(""""iqwdkqdwpok kapodkpok opkwpokdwpokpo k((""", """Unclosed String: "iqwdkqdwpok kapodkpok opkwpokdwpokpo k((""", 199))

    def test_all_10(self):
        self.assertTrue(TestLexer.test(""""\\a \q qodkqd \\q \\er\ """"", """Illegal Escape In String: "\\a""", 200))
