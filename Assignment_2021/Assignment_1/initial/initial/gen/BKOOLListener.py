# Generated from D:/Assignment_PPL/Assignment_2021/Assignment_1/initial/initial/src/main/bkool/parser\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete listener for a parse tree produced by BKOOLParser.
class BKOOLListener(ParseTreeListener):

    # Enter a parse tree produced by BKOOLParser#program.
    def enterProgram(self, ctx:BKOOLParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKOOLParser#program.
    def exitProgram(self, ctx:BKOOLParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKOOLParser#declare.
    def enterDeclare(self, ctx:BKOOLParser.DeclareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#declare.
    def exitDeclare(self, ctx:BKOOLParser.DeclareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#memberlist.
    def enterMemberlist(self, ctx:BKOOLParser.MemberlistContext):
        pass

    # Exit a parse tree produced by BKOOLParser#memberlist.
    def exitMemberlist(self, ctx:BKOOLParser.MemberlistContext):
        pass


    # Enter a parse tree produced by BKOOLParser#attribute_decl.
    def enterAttribute_decl(self, ctx:BKOOLParser.Attribute_declContext):
        pass

    # Exit a parse tree produced by BKOOLParser#attribute_decl.
    def exitAttribute_decl(self, ctx:BKOOLParser.Attribute_declContext):
        pass


    # Enter a parse tree produced by BKOOLParser#all_type.
    def enterAll_type(self, ctx:BKOOLParser.All_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#all_type.
    def exitAll_type(self, ctx:BKOOLParser.All_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#void_type.
    def enterVoid_type(self, ctx:BKOOLParser.Void_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#void_type.
    def exitVoid_type(self, ctx:BKOOLParser.Void_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#primitive_type.
    def enterPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#primitive_type.
    def exitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#array_type.
    def enterArray_type(self, ctx:BKOOLParser.Array_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#array_type.
    def exitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#attr_list.
    def enterAttr_list(self, ctx:BKOOLParser.Attr_listContext):
        pass

    # Exit a parse tree produced by BKOOLParser#attr_list.
    def exitAttr_list(self, ctx:BKOOLParser.Attr_listContext):
        pass


    # Enter a parse tree produced by BKOOLParser#method_decl.
    def enterMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        pass

    # Exit a parse tree produced by BKOOLParser#method_decl.
    def exitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        pass


    # Enter a parse tree produced by BKOOLParser#param_list.
    def enterParam_list(self, ctx:BKOOLParser.Param_listContext):
        pass

    # Exit a parse tree produced by BKOOLParser#param_list.
    def exitParam_list(self, ctx:BKOOLParser.Param_listContext):
        pass


    # Enter a parse tree produced by BKOOLParser#idlist.
    def enterIdlist(self, ctx:BKOOLParser.IdlistContext):
        pass

    # Exit a parse tree produced by BKOOLParser#idlist.
    def exitIdlist(self, ctx:BKOOLParser.IdlistContext):
        pass


    # Enter a parse tree produced by BKOOLParser#block_stmt.
    def enterBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#block_stmt.
    def exitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#var_list.
    def enterVar_list(self, ctx:BKOOLParser.Var_listContext):
        pass

    # Exit a parse tree produced by BKOOLParser#var_list.
    def exitVar_list(self, ctx:BKOOLParser.Var_listContext):
        pass


    # Enter a parse tree produced by BKOOLParser#stmt.
    def enterStmt(self, ctx:BKOOLParser.StmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#stmt.
    def exitStmt(self, ctx:BKOOLParser.StmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#list_stmt.
    def enterList_stmt(self, ctx:BKOOLParser.List_stmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#list_stmt.
    def exitList_stmt(self, ctx:BKOOLParser.List_stmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#assign_stmt.
    def enterAssign_stmt(self, ctx:BKOOLParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#assign_stmt.
    def exitAssign_stmt(self, ctx:BKOOLParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#lhs.
    def enterLhs(self, ctx:BKOOLParser.LhsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#lhs.
    def exitLhs(self, ctx:BKOOLParser.LhsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#if_stmt.
    def enterIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#if_stmt.
    def exitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#for_stmt.
    def enterFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#for_stmt.
    def exitFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#break_stmt.
    def enterBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#break_stmt.
    def exitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#continue_stmt.
    def enterContinue_stmt(self, ctx:BKOOLParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#continue_stmt.
    def exitContinue_stmt(self, ctx:BKOOLParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#return_stmt.
    def enterReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#return_stmt.
    def exitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#invocation_stmt.
    def enterInvocation_stmt(self, ctx:BKOOLParser.Invocation_stmtContext):
        pass

    # Exit a parse tree produced by BKOOLParser#invocation_stmt.
    def exitInvocation_stmt(self, ctx:BKOOLParser.Invocation_stmtContext):
        pass


    # Enter a parse tree produced by BKOOLParser#instance_method.
    def enterInstance_method(self, ctx:BKOOLParser.Instance_methodContext):
        pass

    # Exit a parse tree produced by BKOOLParser#instance_method.
    def exitInstance_method(self, ctx:BKOOLParser.Instance_methodContext):
        pass


    # Enter a parse tree produced by BKOOLParser#static_method.
    def enterStatic_method(self, ctx:BKOOLParser.Static_methodContext):
        pass

    # Exit a parse tree produced by BKOOLParser#static_method.
    def exitStatic_method(self, ctx:BKOOLParser.Static_methodContext):
        pass


    # Enter a parse tree produced by BKOOLParser#exp.
    def enterExp(self, ctx:BKOOLParser.ExpContext):
        pass

    # Exit a parse tree produced by BKOOLParser#exp.
    def exitExp(self, ctx:BKOOLParser.ExpContext):
        pass


    # Enter a parse tree produced by BKOOLParser#exp1.
    def enterExp1(self, ctx:BKOOLParser.Exp1Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp1.
    def exitExp1(self, ctx:BKOOLParser.Exp1Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp2.
    def enterExp2(self, ctx:BKOOLParser.Exp2Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp2.
    def exitExp2(self, ctx:BKOOLParser.Exp2Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp3.
    def enterExp3(self, ctx:BKOOLParser.Exp3Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp3.
    def exitExp3(self, ctx:BKOOLParser.Exp3Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp4.
    def enterExp4(self, ctx:BKOOLParser.Exp4Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp4.
    def exitExp4(self, ctx:BKOOLParser.Exp4Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp5.
    def enterExp5(self, ctx:BKOOLParser.Exp5Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp5.
    def exitExp5(self, ctx:BKOOLParser.Exp5Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp6.
    def enterExp6(self, ctx:BKOOLParser.Exp6Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp6.
    def exitExp6(self, ctx:BKOOLParser.Exp6Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp7.
    def enterExp7(self, ctx:BKOOLParser.Exp7Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp7.
    def exitExp7(self, ctx:BKOOLParser.Exp7Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp8.
    def enterExp8(self, ctx:BKOOLParser.Exp8Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp8.
    def exitExp8(self, ctx:BKOOLParser.Exp8Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp9.
    def enterExp9(self, ctx:BKOOLParser.Exp9Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp9.
    def exitExp9(self, ctx:BKOOLParser.Exp9Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp10.
    def enterExp10(self, ctx:BKOOLParser.Exp10Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp10.
    def exitExp10(self, ctx:BKOOLParser.Exp10Context):
        pass


    # Enter a parse tree produced by BKOOLParser#member_access.
    def enterMember_access(self, ctx:BKOOLParser.Member_accessContext):
        pass

    # Exit a parse tree produced by BKOOLParser#member_access.
    def exitMember_access(self, ctx:BKOOLParser.Member_accessContext):
        pass


    # Enter a parse tree produced by BKOOLParser#explist.
    def enterExplist(self, ctx:BKOOLParser.ExplistContext):
        pass

    # Exit a parse tree produced by BKOOLParser#explist.
    def exitExplist(self, ctx:BKOOLParser.ExplistContext):
        pass


    # Enter a parse tree produced by BKOOLParser#operands.
    def enterOperands(self, ctx:BKOOLParser.OperandsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#operands.
    def exitOperands(self, ctx:BKOOLParser.OperandsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#literal.
    def enterLiteral(self, ctx:BKOOLParser.LiteralContext):
        pass

    # Exit a parse tree produced by BKOOLParser#literal.
    def exitLiteral(self, ctx:BKOOLParser.LiteralContext):
        pass


    # Enter a parse tree produced by BKOOLParser#array_lit.
    def enterArray_lit(self, ctx:BKOOLParser.Array_litContext):
        pass

    # Exit a parse tree produced by BKOOLParser#array_lit.
    def exitArray_lit(self, ctx:BKOOLParser.Array_litContext):
        pass



del BKOOLParser