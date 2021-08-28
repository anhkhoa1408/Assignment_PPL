import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    """Test Comment"""
    def test_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a comment **", "<EOF>", 101))

    def test_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("""** This\n * is\n * a\n comment **""", "<EOF>", 102))

    def test_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("""** \n *\r\n  *\n **""", "<EOF>", 103))

    def test_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("""** ankvjwnwe .;120dqd **""", "<EOF>", 104))

    def test_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme("""** * * * * **""", "<EOF>", 105))

    def test_comment_6(self):
        self.assertTrue(TestLexer.checkLexeme("""** ************************* **""", "<EOF>", 106))

    def test_comment_7(self):
        self.assertTrue(TestLexer.checkLexeme("""** \n * \n **""", "<EOF>", 107))

    def test_comment_8(self):
        self.assertTrue(TestLexer.checkLexeme("""** \n *124sa* \n **""", "<EOF>", 108))

    def test_comment_9(self):
        self.assertTrue(TestLexer.checkLexeme("""**  *1x2x*a*kmam&12*s4sa*  **""", "<EOF>", 109))

    def test_comment_10(self):
        self.assertTrue(TestLexer.checkLexeme("""** \n \n \t \f  **""", "<EOF>", 110))


    """Test Identifier"""
    def test_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",111))

    def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("xawffVVVawaar","xawffVVVawaar,<EOF>",112))

    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("uwqbuewqeANFWKNKF0_j12JKJNKJN1JFNdsnmKEFjdnfvjn","uwqbuewqeANFWKNKF0_j12JKJNKJN1JFNdsnmKEFjdnfvjn,<EOF>",113))

    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("uv 8 a9Aziw ko9jjjj axxzdwq bn0x0x009","uv,8,a9Aziw,ko9jjjj,axxzdwq,bn0x0x009,<EOF>",114))

    def test_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("ajdjdjjjdj 9akk 12ksAVU 100jfnd [nNnNnNkNn12","ajdjdjjjdj,9,akk,12,ksAVU,100,jfnd,[,nNnNnNkNn12,<EOF>",115))

    def test_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("hvbwe + - wn 0 9 ","hvbwe,+,-,wn,0,9,<EOF>",116))

    def test_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme("a88jdjij + a2x - 40 > 12","a88jdjij,+,a2x,-,40,>,12,<EOF>",117))

    def test_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme("as<.>iooi" ,"as,<.,>,iooi,<EOF>",118))

    def test_identifier_9(self):
        self.assertTrue(TestLexer.checkLexeme("[;]12kkkasijiasdijANXNMXMM\t","[,;,],12,kkkasijiasdijANXNMXMM,<EOF>",119))

    def test_identifier_10(self):
        self.assertTrue(TestLexer.checkLexeme(":a:sxassa:,irejgioj0990hiju.",":,a,:,sxassa,:,,,irejgioj0990hiju,.,<EOF>",120))


    """Test Literal"""
    def test_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme("12 45 -90 100 0 0XA1A 0xAD","12,45,-90,100,0,0XA1A,0xAD,<EOF>",121))

    def test_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme("0xA1B2C3D4 0XAAAA 0x123ABCDF 0o211 0O12453160 0O84321","0xA1B2C3D4,0XAAAA,0x123ABCDF,0o211,0O12453160,0O84321,<EOF>",122))

    def test_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5 12.0e3 12000. 120000e-1","12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>",123))

    def test_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme("-45.0E124459 -382.98989428 -3. -0.E99","-45.0E124459,-382.98989428,-3.,-0.E99,<EOF>",124))

    def test_literal_5(self):
        self.assertTrue(TestLexer.checkLexeme("0.11e849 0.33e-12 0.E+0 0.E-00 10e+425 -0.E+991299","0.11e849,0.33e-12,0.E+0,0.E-00,10e+425,-0.E+991299,<EOF>",125))

    def test_string_literal_1(self):
         self.assertTrue(TestLexer.checkLexeme("""\"abc def\"""" ,"abc def,<EOF>",126))

    def test_string_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme("""\"ab'"c\\n def\"""","""ab'"c\\n def,<EOF>""",127))

    def test_string_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme("""\"abc\" 0 \"12ab\\fc0.1\"""","""abc,0,12ab\\fc0.1,<EOF>""",128))

    def test_string_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc \"abc1!!@#$$%^i\\n\" 12yz ""","""abc,abc1!!@#$$%^i\\n,12,yz,<EOF>""",129))

    def test_string_literal_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" True False xyz 4\"&J^1a_.\" pQGn\"?67Sp\"{,}6pAsz\"pYx](\" ""","""True,False,xyz,4,&J^1a_.,pQGn,?67Sp,{,,,},6,pAsz,pYx](,<EOF>""",130))

    def test_string_literal_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"He asked me:'"What is your name'"\"""","""He asked me:'"What is your name'",<EOF>""",131))

    def test_string_literal_7(self):
        self.assertTrue(TestLexer.checkLexeme("""\"'"abc snn'"aT ure fnjan '" Tujwqnj '"\"""","""'"abc snn'"aT ure fnjan '" Tujwqnj '",<EOF>""",132))

    def test_string_literal_8(self):
        self.assertTrue(TestLexer.checkLexeme("""\"a+11.2+'"mam.123'" 12 %^&\"""","""a+11.2+'"mam.123'" 12 %^&,<EOF>""",133))

    def test_string_literal_9(self):
        self.assertTrue(TestLexer.checkLexeme("""\"38n\"aFfs&&0aED\"0.\"!!=!7n""","""38n,aFfs,&&,0,aED,0.,!,!=,!,7,n,<EOF>""",134))


    """Test Keyword"""
    def test_keyword_1(self):
         self.assertTrue(TestLexer.checkLexeme("Body Break Continue Do EndDo","Body,Break,Continue,Do,EndDo,<EOF>",135))

    def test_keyword_2(self):
         self.assertTrue(TestLexer.checkLexeme("Else ElseIf EndBody EndIf","Else,ElseIf,EndBody,EndIf,<EOF>",136))

    def test_keyword_3(self):
         self.assertTrue(TestLexer.checkLexeme("EndFor EndWhile For Function","EndFor,EndWhile,For,Function,<EOF>",137))

    def test_keyword_4(self):
         self.assertTrue(TestLexer.checkLexeme("If Parameter Return Then","If,Parameter,Return,Then,<EOF>",138))

    def test_keyword_5(self):
         self.assertTrue(TestLexer.checkLexeme("Var While True False","Var,While,True,False,<EOF>",139))


    """Test Operator """
    def test_operator_1(self):
         self.assertTrue(TestLexer.checkLexeme("ddsls<l>02>=d1s<=123","ddsls,<,l,>,0,2,>=,d1s,<=,123,<EOF>",140))

    def test_operator_2(self):
         self.assertTrue(TestLexer.checkLexeme("abcd+s+.-sfqAA-.","abcd,+,s,+.,-,sfqAA,-.,<EOF>",141))

    def test_operator_3(self):
         self.assertTrue(TestLexer.checkLexeme(" adsd\\45sa\\.21*9(*.3.0) " , "adsd,\\,45,sa,\\.,21,*,9,(,*.,3.0,),<EOF>" ,142))

    def test_operator_4(self):
         self.assertTrue(TestLexer.checkLexeme("True && False % 19 +!x || ui ","True,&&,False,%,19,+,!,x,||,ui,<EOF>",143))

    def test_operator_5(self):
         self.assertTrue(TestLexer.checkLexeme("x==4x!=5+12a=45*9Whilea<b==a+5>100","x,==,4,x,!=,5,+,12,a,=,45,*,9,While,a,<,b,==,a,+,5,>,100,<EOF>",144))

    def test_operator_6(self):
         self.assertTrue(TestLexer.checkLexeme("q<=bassdMain>=120usx+9=/=klcamklTrueEndIf","q,<=,bassdMain,>=,120,usx,+,9,=/=,klcamklTrueEndIf,<EOF>",145))

    def test_operator_7(self):
         self.assertTrue(TestLexer.checkLexeme("a+sanf=jd>.sjd For<.EndForWhileIf>=.","a,+,sanf,=,jd,>.,sjd,For,<.,EndFor,While,If,>=.,<EOF>",146))

    def test_operator_8(self):
         self.assertTrue(TestLexer.checkLexeme("ax+b>=c 4.0<.5.0 \\ annsdjtnhj *.32+.0.5","ax,+,b,>=,c,4.0,<.,5.0,\\,annsdjtnhj,*.,32,+.,0.5,<EOF>",147))

    def test_operator_9(self):
         self.assertTrue(TestLexer.checkLexeme("==>.<!=<><><=><.=/=\\","==,>.,<,!=,<,>,<,>,<=,>,<.,=/=,\\,<EOF>",148))

    def test_operator_10(self):
         self.assertTrue(TestLexer.checkLexeme("(True + False)\\.2.0*10E-12+9x>=12","(,True,+,False,),\\.,2.0,*,10E-12,+,9,x,>=,12,<EOF>",149))

    """Test wrong token"""
    def test_wrong_token_1(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",150))

    def test_wrong_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("smkassrj4AORqwExkrCxZPi`","smkassrj4AORqwExkrCxZPi,Error Token `",151))

    def test_wrong_token_3(self):
        self.assertTrue(TestLexer.checkLexeme("True12E+4b(9kZ~YBraRCF","True,12E+4,b,(,9,kZ,Error Token ~",152))

    def test_wrong_token_4(self):
        self.assertTrue(TestLexer.checkLexeme("asas12pQ*6'q0+Y==}f(>9Xn","asas12pQ,*,6,Error Token '",153))

    def test_wrong_token_5(self):
        self.assertTrue(TestLexer.checkLexeme("0x123aFG[@WQS{QBW7Y6]le5","0x123,aFG,[,Error Token @",154))

    def test_wrong_token_6(self):
        self.assertTrue(TestLexer.checkLexeme(";0O1244lJ~IbbnQL!x-OBd",";,0O1244,lJ,Error Token ~",155))
    
    def test_wrong_token_7(self):
        self.assertTrue(TestLexer.checkLexeme("kz-70abbS9+0s)f<)?0gg","kz,-70,abbS9,+,0,s,),f,<,),Error Token ?",156))

    def test_wrong_token_8(self):
        self.assertTrue(TestLexer.checkLexeme("A123jmkmf+-%km","Error Token A",157))

    def test_wrong_token_9(self):
        self.assertTrue(TestLexer.checkLexeme("!== != && * % $ ... ","!=,=,!=,&&,*,%,Error Token $",158))

    def test_wrong_token_10(self):
        self.assertTrue(TestLexer.checkLexeme("a := a & 1","a,:,=,a,Error Token &",159))


    """test illegal escape"""
    def test_illegal_escape_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"abc\\h def\" ""","""Illegal Escape In String: abc\\h""",160))
    
    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"ado\\mado\"  ""","""Illegal Escape In String: ado\\m""",161))
    
    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123abc \"xyz\\k 456\"  ""","""123,abc,Illegal Escape In String: xyz\\k""",162))
    
    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12+3>9-3x \"**asndabc+\\^ def\"  ""","""12,+,3,>,9,-3,x,Illegal Escape In String: **asndabc+\\^""",163))
    
    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"1.2+1.3+1.4\\o'\"0x9999  ""","""Illegal Escape In String: 1.2+1.3+1.4\\o""",164))
    
    def test_illegal_escape_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" (*0O12*)+1.1 \"ba\\qm\f\" ""","""(,*,0O12,*,),+,1.1,Illegal Escape In String: ba\\q""",165))

    def test_illegal_escape_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc \"abc1!!@#$$%^i\\u\" 12yz  ""","""abc,Illegal Escape In String: abc1!!@#$$%^i\\u""",166))

    def test_illegal_escape_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"\\!LScna\" ""","""Illegal Escape In String: \\!""",167))

    def test_illegal_escape_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"&^3u89,dls\\F12!LS\\kc\\na\"  ""","""Illegal Escape In String: &^3u89,dls\\F""",168))

    def test_illegal_escape_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"ahiuhfuiTure*12-==\\|skldmfO02 \"  ""","""Illegal Escape In String: ahiuhfuiTure*12-==\\|""",169))
    
    
    """ test unclosed string """
    def test_unterminated_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,170))
    
    def test_unterminated_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" acnkNmkobYn{!}+xI1+\"`YS2h.J(""","""acnkNmkobYn,{,!,},+,xI1,+,Unclosed String: `YS2h.J(""",171))
    
    def test_unterminated_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"acJDJVBms!,lds \" {\"abc\"} 123\"abc ""","""acJDJVBms!,lds ,{,abc,},123,Unclosed String: abc """,172))

    def test_unterminated_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" hbsdjn\"vkmm*y32ryikk ""","""hbsdjn,Unclosed String: vkmm*y32ryikk """,173))

    def test_unterminated_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" \".akdn&***&&Hub`22Y\"<{;}\"Y`=DxXhZKwdmqh """,""".akdn&***&&Hub`22Y,<,{,;,},Unclosed String: Y`=DxXhZKwdmqh """,174))

    def test_unterminated_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" {aaSRass}\"Nk8U;\"rA\"@Y3*\"oV\"bh1  ""","""{,aaSRass,},Nk8U;,rA,@Y3*,oV,Unclosed String: bh1  """,175))

    def test_unterminated_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" a+11.2+\"mam.123\" 12 \"%^&  ""","""a,+,11.2,+,mam.123,12,Unclosed String: %^&  """,176))

    def test_unterminated_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" ioevioo&&qjjwq+==++12je\"bacxyc  ""","""ioevioo,&&,qjjwq,+,==,+,+,12,je,Unclosed String: bacxyc  """,177))
    
    def test_unterminated_string_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"acnv \" \"abc  ""","""acnv ,Unclosed String: abc  """,178))
    
    def test_unterminated_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" aF&&)aLqwpokpokq912p9i9+--iowjwqX\"+>.<.+>aX+#Fft""","""aF,&&,),aLqwpokpokq912p9i9,+,-,-,iowjwqX,Unclosed String: +>.<.+>aX+#""",179))

    """Test Unterminated Comment"""
    def test_unterminated_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" **abc def  ""","""Unterminated Comment""",180))
    
    def test_unterminated_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" **nevnn \t \t uauhuqhwid  ""","""Unterminated Comment""",181))

    def test_unterminated_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" **abc def \n \t axnsdj * *\t * * ""","""Unterminated Comment""",182))

    def test_unterminated_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12 mand **vniwesdn &&& jns  ""","""12,mand,Unterminated Comment""",183))

    def test_unterminated_comment_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" >=kvmw* 12 12E+1234 aMmk ** iqiod \r \t \r \n  """,""">=,kvmw,*,12,12E+1234,aMmk,Unterminated Comment""",184))

    def test_unterminated_comment_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" %%123p&&|| jnp != ! xxyz 0XABCD44 are ** qadmk *\nxx *a\t  ""","""%,%,123,p,&&,||,jnp,!=,!,xxyz,0XABCD44,are,Unterminated Comment""",185))

    def test_unterminated_comment_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12E+9 12. kmqmw && *. .. wini ** \b\n\n\n\\ ""","""12E+9,12.,kmqmw,&&,*.,.,.,wini,Unterminated Comment""",186))

    def test_unterminated_comment_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" EndWhile For True xx01 ** jnaqdwm ""","""EndWhile,For,True,xx01,Unterminated Comment""",187))

    def test_unterminated_comment_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" a \t \\ \n bcd asdmm kllmas **  ""","""a,\\,bcd,asdmm,kllmas,Unterminated Comment""",188))
    
    def test_unterminated_comment_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" efujiowq || && (0) \\ \t \n ici ** kss 0(0q0&&8iqdq\\adhwq   ""","""efujiowq,||,&&,(,0,),\\,ici,Unterminated Comment""",189))
    
    """Test all token"""
    def test_all_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" True False xx_xx__49u While 19 -203 -2.99 -4.99E+1290 ""","""True,False,xx_xx__49u,While,19,-203,-2.99,-4.99E+1290,<EOF>""",190))
    
    def test_all_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" If && +. <. \"odkok\'"ksmfffjujn\" 0x91209 0oa""","""If,&&,+.,<.,odkok'"ksmfffjujn,0x91209,0,oa,<EOF>""",191))

    def test_all_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" ksdcm akak % == lap al 10.94 ! @ ksmdk ""","""ksdcm,akak,%,==,lap,al,10.94,!,Error Token @""",192))

    def test_all_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" t \"\\{abcd}\\x\" efg ""","""t,Illegal Escape In String: \\{""",193))

    def test_all_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" (*(*abcd*)*) ** *\n \t * * ""","""(,*,(,*,abcd,*,),*,),Unterminated Comment""",194))

    def test_all_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" . Var Parameter True False a_s_ 49u While 19 -203 -2.99 -4.99E+1290 ij ;:;{||0.*} """,""".,Var,Parameter,True,False,a_s_,49,u,While,19,-203,-2.99,-4.99E+1290,ij,;,:,;,{,||,0.,*,},<EOF>""",195))

    def test_all_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" csjkjjk \"\'" sdiwkopslssal ""","""csjkjjk,Unclosed String: '" sdiwkopslssal """,196))

    def test_all_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" b=x+9&&a23+=12kv.456E954-12+-.5*100/ ""","""b,=,x,+,9,&&,a23,+,=,12,kv,.,456E954,-12,+,-.,5,*,100,Error Token /""",197))

    def test_all_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" wepofffds ,.;()kepm j306 ()8*81m iqo \t \n \\.v isk _ ""","""wepofffds,,,.,;,(,),kepm,j306,(,),8,*,81,m,iqo,\\.,v,isk,Error Token _""",198))

    def test_all_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var Main main Parameter xyz += +- -2 EndWhile EndIf ""","""Var,Main,main,Parameter,xyz,+,=,+,-,-2,EndWhile,EndIf,<EOF>""",199))
    
    def test_all_11(self):
        self.assertTrue(TestLexer.checkLexeme(""" 10E+9.23 aAKK -45e10 + 2-- 0.e34 +00 ;  ; {]][:][;<.>,.<.,.>,]} ""","""10E+9,.,23,aAKK,-45e10,+,2,-,-,0.e34,+,0,0,;,;,{,],],[,:,],[,;,<.,>,,,.,<.,,,.,>,,,],},<EOF>""",200))


