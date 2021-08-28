# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#declare.
    def visitDeclare(self, ctx:BKITParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declare.
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_stmt.
    def visitVar_stmt(self, ctx:BKITParser.Var_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#init_stmt.
    def visitInit_stmt(self, ctx:BKITParser.Init_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lhs.
    def visitLhs(self, ctx:BKITParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#init_val.
    def visitInit_val(self, ctx:BKITParser.Init_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_init.
    def visitArray_init(self, ctx:BKITParser.Array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#one_dimension.
    def visitOne_dimension(self, ctx:BKITParser.One_dimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multi_dimension.
    def visitMulti_dimension(self, ctx:BKITParser.Multi_dimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_declare.
    def visitParameter_declare(self, ctx:BKITParser.Parameter_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_list.
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_list.
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#compound_stmt.
    def visitCompound_stmt(self, ctx:BKITParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseif_stmt.
    def visitElseif_stmt(self, ctx:BKITParser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:BKITParser.Dowhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression1.
    def visitExpression1(self, ctx:BKITParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression2.
    def visitExpression2(self, ctx:BKITParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression3.
    def visitExpression3(self, ctx:BKITParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression4.
    def visitExpression4(self, ctx:BKITParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression5.
    def visitExpression5(self, ctx:BKITParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression6.
    def visitExpression6(self, ctx:BKITParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression7.
    def visitExpression7(self, ctx:BKITParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp_list.
    def visitExp_list(self, ctx:BKITParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operator.
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boolean_literal.
    def visitBoolean_literal(self, ctx:BKITParser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#integer_literal.
    def visitInteger_literal(self, ctx:BKITParser.Integer_literalContext):
        return self.visitChildren(ctx)



del BKITParser