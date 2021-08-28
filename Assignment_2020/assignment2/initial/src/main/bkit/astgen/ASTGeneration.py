from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        declList = []
        for x in ctx.declare():
            decl = self.visit(x)
            if isinstance(decl,list):
                declList = declList + decl
            else:
                declList.append(decl)
        return Program(declList)


    def visitDeclare(self, ctx: BKITParser.DeclareContext):
        return self.visit(ctx.getChild(0))


    def visitVar_declare(self, ctx: BKITParser.Var_declareContext):
        for x in ctx.var_list():
            return self.visitVar_list(x)


    def visitVar_list(self, ctx: BKITParser.Var_listContext):
        varList = []
        for x in ctx.var_stmt():
            varlist = self.visitVar_stmt(x)
            if isinstance(varlist, list):
                varList = varList + varlist
            else:
                varList.append(varlist)
        return varList


    def visitVar_stmt(self, ctx: BKITParser.Var_stmtContext):
        if ctx.ID() and ctx.getChildCount() == 1:
            return VarDecl(Id(ctx.ID().getText()), [], None)
        elif ctx.ID() and ctx.integer_literal():
            varDimen = [int(x.getText()) for x in ctx.integer_literal()]
            return VarDecl(Id(ctx.ID().getText()), varDimen, None)
        else:
            return self.visit(ctx.init_stmt())


    def visitInit_stmt(self, ctx: BKITParser.Init_stmtContext):
        variable = Id(ctx.ID().getText())
        varDimen = [int(x.getText()) for x in ctx.integer_literal()]
        varInit = self.visit(ctx.init_val()) if ctx.init_val() else None
        return VarDecl(variable, varDimen, varInit)


    def visitLhs(self, ctx: BKITParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            arr = self.visit(ctx.expression())
            idx = self.visit(ctx.index_operator())
            return ArrayCell(arr,idx)


    def visitInit_val(self, ctx: BKITParser.Init_valContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.array_init():
            return self.visit(ctx.array_init())


    def visitArray_init(self, ctx: BKITParser.Array_initContext):
        if ctx.one_dimension():
            return self.visit(ctx.one_dimension())
        else:
            return self.visit(ctx.multi_dimension())


    def visitOne_dimension(self, ctx: BKITParser.One_dimensionContext):
        literalList = []
        for x in ctx.literal():
            literallst = self.visit(x)
            if isinstance(literallst,list):
                literalList = literalList + literallst
            else:
                literalList.append(literallst)
        return ArrayLiteral(literalList)


    def visitMulti_dimension(self, ctx: BKITParser.Multi_dimensionContext):
        dimensionList = []
        for x in ctx.one_dimension():
            dimensionlist = self.visit(x)
            if isinstance(dimensionlist,list):
                dimensionList = dimensionList + dimensionlist
            else:
                dimensionList.append(dimensionlist)
        return ArrayLiteral(dimensionList)


    def visitFunc_declare(self, ctx: BKITParser.Func_declareContext):
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.parameter_declare()) if ctx.parameter_declare() else []
        VarDecl = self.visit(ctx.var_declare()) if ctx.var_declare() else []
        Stmt = self.visit(ctx.compound_stmt()) if ctx.compound_stmt() else []
        body = (VarDecl,Stmt)
        return FuncDecl(name, param, body)


    def visitParameter_declare(self, ctx: BKITParser.Parameter_declareContext):
        return self.visit(ctx.parameter_list())


    def visitParameter_list(self, ctx: BKITParser.Parameter_listContext):
        paraList = []
        for x in ctx.var_stmt():
            paralist = self.visit(x)
            if isinstance(paralist,list):
                paraList = paralist + paraList
            else:
                paraList.append(paralist)
        return paraList


    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        return self.visit(ctx.getChild(0))


    def visitCompound_stmt(self, ctx:BKITParser.Compound_stmtContext):
        compoundList = []
        for x in ctx.stmt_list():
            compoundlist = self.visit(x)
            if isinstance(compoundlist,list):
                compoundList = compoundList + compoundlist
            else:
                compoundList.append(compoundlist)
        return compoundList


    def visitAssign_stmt(self,ctx:BKITParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expression())
        return Assign(lhs,rhs)


    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        exp0 = self.visit(ctx.expression())
        vardecl0 = self.visit(ctx.var_declare(0)) if ctx.var_declare(0) else []
        stmt0 = self.visit(ctx.compound_stmt(0)) if ctx.compound_stmt(0) else []
        ifthenStmt = [(exp0,vardecl0,stmt0)]
        for x in ctx.elseif_stmt():
            ifthenstmt = self.visit(x)
            if isinstance(ifthenStmt,list):
                ifthenStmt = ifthenStmt + ifthenstmt
            else:
                ifthenStmt.append(ifthenstmt)
        vardecl1 = self.visit(ctx.var_declare(1)) if ctx.var_declare(1) else []
        stmt1 = self.visit(ctx.compound_stmt(1)) if ctx.compound_stmt(1) else []
        elseStmt = (vardecl1,stmt1)
        return If(ifthenStmt,elseStmt)


    def visitElseif_stmt(self, ctx:BKITParser.Elseif_stmtContext):
        exp = self.visit(ctx.expression())
        vardecl = self.visit(ctx.var_declare()) if ctx.var_declare() else []
        stmt = self.visit(ctx.compound_stmt()) if ctx.compound_stmt() else []
        return [(exp,vardecl,stmt)]


    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        idx1 = Id(ctx.ID().getText())
        exp1 = self.visit(ctx.expression(0))
        exp2 = self.visit(ctx.expression(1))
        exp3 = self.visit(ctx.expression(2))
        vardecl = self.visit(ctx.var_declare()) if ctx.var_declare() else []
        stmt = self.visit(ctx.compound_stmt()) if ctx.compound_stmt() else []
        loop = (vardecl,stmt)
        return For(idx1,exp1,exp2,exp3,loop)


    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        exp = self.visit(ctx.expression())
        vardecl = self.visit(ctx.var_declare()) if ctx.var_declare() else []
        stmt = self.visit(ctx.compound_stmt()) if ctx.compound_stmt() else []
        sl = (vardecl,stmt)
        return While(exp,sl)


    def visitDowhile_stmt(self, ctx:BKITParser.Dowhile_stmtContext):
        vardecl = self.visit(ctx.var_declare()) if ctx.var_declare() else []
        stmt = self.visit(ctx.compound_stmt()) if ctx.compound_stmt() else []
        exp = self.visit(ctx.expression())
        sl = (vardecl,stmt)
        return Dowhile(sl,exp)


    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return Break()


    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()


    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.exp_list()) if ctx.exp_list() else []
        return CallStmt(method,param)

    
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return Return(expr)


    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        op = ""
        if ctx.DBEQ():
            op = ctx.DBEQ().getText()
        elif ctx.NEQ():
            op = ctx.NEQ().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.LTE():
            op = ctx.LTE().getText()
        elif ctx.GTE():
            op = ctx.GTE().getText()
        elif ctx.NEQF():
            op = ctx.NEQF().getText()
        elif ctx.GTF():
            op = ctx.GTF().getText()
        elif ctx.LTF():
            op = ctx.LTF().getText()
        elif ctx.GTEF():
            op = ctx.GTEF().getText()
        elif ctx.LTEF():
            op = ctx.LTEF().getText()
        else:
            return self.visit(ctx.expression1(0))
        left = self.visit(ctx.expression1(0))
        right = self.visit(ctx.expression1(1))
        return BinaryOp(op,left,right)


    def visitExpression1(self, ctx:BKITParser.Expression1Context):
        op = ""
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()
        else:
            return self.visit(ctx.expression2())
        left = self.visit(ctx.expression1())
        right = self.visit(ctx.expression2())
        return BinaryOp(op,left,right)
            

    def visitExpression2(self, ctx:BKITParser.Expression2Context):
        op = ""
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.ADDF():
            op = ctx.ADDF().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        elif ctx.SUBF():
            op = ctx.SUBF().getText()
        else:
            return self.visit(ctx.expression3())
        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())
        return BinaryOp(op,left,right)  
    

    def visitExpression3(self, ctx:BKITParser.Expression3Context):
        op = ""
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.MULF():
            op = ctx.MULF().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.DIVF():
            op = ctx.DIVF().getText()
        elif ctx.RMD():
            op = ctx.RMD().getText()
        else:
            return self.visit(ctx.expression4())
        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinaryOp(op,left,right)  


    def visitExpression4(self, ctx:BKITParser.Expression4Context):
        op = ""
        if ctx.NOT():
            op = ctx.NOT().getText()
        else:
            return self.visit(ctx.expression5())
        body = self.visit(ctx.expression4())
        return UnaryOp(op,body)


    def visitExpression5(self, ctx:BKITParser.Expression5Context):
        op = ""
        if ctx.SUB():
            op = ctx.SUB().getText()
        elif ctx.SUBF():
            op = ctx.SUBF().getText()
        else:
            return self.visit(ctx.expression6())
        body = self.visit(ctx.expression5())
        return UnaryOp(op,body)


    def visitExpression6(self, ctx:BKITParser.Expression6Context):
        if ctx.getChildCount() == 2:
            arr = self.visit(ctx.expression6())
            idx = self.visit(ctx.index_operator())
            return ArrayCell(arr,idx)
        else:
            return self.visit(ctx.expression7())


    def visitExpression7(self, ctx:BKITParser.Expression7Context):
        if ctx.function_call():
            return self.visit(ctx.function_call())
        else:
            return self.visit(ctx.operand())


    def visitOperand(self, ctx:BKITParser.OperandContext):
        if ctx.LP() and ctx.RP():
            return self.visit(ctx.expression())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())


    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.integer_literal():
            return self.visit(ctx.integer_literal())
        elif ctx.REAL_LITERAL():
            return FloatLiteral(float((ctx.REAL_LITERAL().getText())))
        elif ctx.boolean_literal():
            return self.visit(ctx.boolean_literal())
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())


    def visitExp_list(self, ctx:BKITParser.Exp_listContext):
        expList = []
        for x in ctx.expression():
            explist = self.visit(x)
            if isinstance(explist,list):
                expList = expList + explist
            else:
                expList.append(explist)
        return expList


    def visitIndex_operator(self, ctx: BKITParser.Index_operatorContext):
        indexList = []
        for x in ctx.expression():
            indexlist = self.visit(x)
            if isinstance(indexlist,list):
                indexList = indexList + indexlist
            else:
                indexList.append(indexlist)
        return indexList


    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.exp_list()) if ctx.exp_list() else []
        return CallExpr(method,param)

    def visitBoolean_literal(self, ctx: BKITParser.Boolean_literalContext):
        str = ctx.getText()
        if len(str) == 4:
            return BooleanLiteral(True)
        elif len(str) == 5:
            return BooleanLiteral(False)


    def visitInteger_literal(self,ctx:BKITParser.Integer_literalContext):
        if ctx.HEXADECIMAL():
            return IntLiteral(int(ctx.HEXADECIMAL().getText(),16))
        elif ctx.OCTALDECIMAL():
            return IntLiteral(int(ctx.OCTALDECIMAL().getText(),8))
        else:
            return IntLiteral(int(ctx.getText()))


    
