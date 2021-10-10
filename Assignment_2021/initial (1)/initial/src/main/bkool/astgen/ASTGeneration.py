from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.declare()])

    def visitDeclare(self, ctx: BKOOLParser.DeclareContext):
        classname = Id(ctx.ID(0).getText())
        memlist = self.visit(ctx.memberlist())
        parentname = None
        if ctx.ID(1) != None:
            parentname = Id(ctx.ID(1).getText())
        return ClassDecl(classname, memlist, parentname)

    def visitMemberlist(self, ctx: BKOOLParser.MemberlistContext):
        listChild = [x for x in range(ctx.getChildCount())] if ctx.getChildCount() > 0 else []
        return reduce(lambda x, y: x + self.visit(ctx.getChild(y)), listChild, []) if listChild != [] else []

    def visitAttribute_decl(self, ctx: BKOOLParser.Attribute_declContext):
        idList = self.visit(ctx.attr_list())
        varType = self.visit(ctx.all_type())
        isClassType = True if "ClassType" in str(varType) else False
        isStatic = True if ctx.STATIC() else False
        isFinal = True if ctx.FINAL() else False
        attrList = []
        for x in idList:
            if not isStatic and isFinal:
                attrList.append(AttributeDecl(Instance(), ConstDecl(x[0], varType, x[1])))
            elif isStatic and isFinal:
                attrList.append(AttributeDecl(Static(), ConstDecl(x[0], varType, x[1])))
            elif not isStatic and not isFinal:
                attrList.append(AttributeDecl(Instance(), VarDecl(x[0], varType, x[1])))
            elif isStatic and not isFinal:
                attrList.append(AttributeDecl(Static(), VarDecl(x[0], varType, x[1])))
        return attrList

    def visitAll_type(self, ctx: BKOOLParser.All_typeContext):
        return ClassType(Id(ctx.ID().getText())) if ctx.ID() else self.visit(ctx.getChild(0))

    def visitVoid_type(self, ctx: BKOOLParser.Void_typeContext):
        return VoidType()

    def visitPrimitive_type(self, ctx: BKOOLParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()

    def visitArray_type(self, ctx: BKOOLParser.Array_typeContext):
        type = self.visit(ctx.getChild(0))
        size = int(ctx.getChild(2).getText())
        return ArrayType(size, type)

    def visitAttr_list(self, ctx: BKOOLParser.Attr_listContext):
        if not ctx.attr_list():
            id = ctx.ID().getText()
            exp = self.visit(ctx.exp()) if ctx.exp() else None
            return [(id, exp)]
        else:
            id = ctx.ID().getText()
            exp = self.visit(ctx.exp()) if ctx.exp() else None
            return [(id, exp)] + self.visit(ctx.attr_list())

    def visitMethod_decl(self, ctx: BKOOLParser.Method_declContext):
        isStatic = True if ctx.getChild(0).getText() == 'static' else False
        type = self.visit(ctx.all_type()) if ctx.all_type() else None
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.param_list()) if ctx.param_list() else []
        body = self.visit(ctx.block_stmt())
        return [MethodDecl(Static(), name, param, type, body)] if isStatic else [
            MethodDecl(Instance(), name, param, type, body)]

    def visitParam_list(self, ctx: BKOOLParser.Param_listContext):
        idlist = self.visit(ctx.idlist())
        type = self.visit(ctx.all_type())
        exp = None
        if ctx.getChildCount() == 2:
            return [VarDecl(x, type, exp) for x in idlist]
        else:
            return [VarDecl(x, type, exp) for x in idlist] + self.visit(ctx.param_list())

    def visitIdlist(self, ctx: BKOOLParser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())

    def visitBlock_stmt(self, ctx: BKOOLParser.Block_stmtContext):
        decl = self.visit(ctx.var_list()) if ctx.var_list() else []
        stmt = self.visit(ctx.list_stmt()) if ctx.list_stmt() else []
        return Block(decl, stmt)

    def visitVar_list(self, ctx: BKOOLParser.Var_listContext):
        idlist = self.visit(ctx.idlist()) if ctx.idlist() else []
        type = self.visit(ctx.all_type())
        exp = None
        if not ctx.var_list():
            return [VarDecl(x, type, exp) for x in idlist]
        else:
            return [VarDecl(x, type, exp) for x in idlist] + self.visit(ctx.var_list())

    def visitList_stmt(self, ctx: BKOOLParser.List_stmtContext):
        stmt = self.visit(ctx.stmt())
        if ctx.getChildCount() == 1:
            return [stmt]
        else:
            return [stmt] + self.visit(ctx.list_stmt())

    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        return self.visit(ctx.getChild(0))

    def visitAssign_stmt(self, ctx: BKOOLParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.exp())
        return Assign(lhs, exp)

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp(0))
        else:
            exp1 = self.visit(ctx.exp(0))
            exp2 = self.visit(ctx.exp(1))
            return ArrayCell(exp1, exp2)

    def visitIf_stmt(self, ctx: BKOOLParser.If_stmtContext):
        exp = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.stmt(0))
        elseStmt = self.visit(ctx.stmt(1)) if ctx.stmt(1) else None
        return If(exp, thenStmt, elseStmt)

    def visitFor_stmt(self, ctx: BKOOLParser.For_stmtContext):
        id = Id(ctx.ID().getText())
        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        isUp = True if ctx.TO() else False
        loop = self.visit(ctx.stmt())
        return For(id, exp1, exp2, isUp, loop)

    def visitBreak_stmt(self, ctx: BKOOLParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: BKOOLParser.Continue_stmtContext):
        return Continue()

    def visitReturn_stmt(self, ctx: BKOOLParser.Return_stmtContext):
        exp = self.visit(ctx.exp())
        return Return(exp)

    def visitInvocation_stmt(self, ctx: BKOOLParser.Invocation_stmtContext):
        return self.visit(ctx.getChild(0))

    def visitInstance_method(self, ctx: BKOOLParser.Instance_methodContext):
        obj = self.visit(ctx.exp())
        method = Id(ctx.ID().getText())
        expList = self.visit(ctx.explist()) if ctx.explist() else []
        return CallExpr(obj, method, expList)

    def visitStatic_method(self, ctx: BKOOLParser.Static_methodContext):
        obj = Id(ctx.ID(0).getText())
        method = Id(ctx.ID(1).getText())
        expList = self.visit(ctx.explist()) if ctx.explist() else []
        return CallExpr(obj, method, expList)

    def visitExp(self, ctx: BKOOLParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.exp1(0))
        right = self.visit(ctx.exp1(1))
        op = ""
        if ctx.LT():
            op = ctx.LT().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.LTEQ():
            op = ctx.LTEQ().getText()
        elif ctx.GTEQ():
            op = ctx.GTEQ().getText()
        return BinaryOp(op, left, right)

    def visitExp1(self, ctx: BKOOLParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.exp2(0))
        right = self.visit(ctx.exp2(1))
        op = ""
        if ctx.DBEQ():
            op = ctx.DBEQ().getText()
        elif ctx.NOT_EQ():
            op = ctx.NOT_EQ().getText()
        return BinaryOp(op, left, right)

    def visitExp2(self, ctx: BKOOLParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        op = ""
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()
        return BinaryOp(op, left, right)

    def visitExp3(self, ctx: BKOOLParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())
        op = ""
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        return BinaryOp(op, left, right)

    def visitExp4(self, ctx: BKOOLParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.exp4())
        right = self.visit(ctx.exp5())
        op = ""
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.INT_DIV():
            op = ctx.INT_DIV().getText()
        elif ctx.FLOAT_DIV():
            op = ctx.FLOAT_DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        return BinaryOp(op, left, right)

    def visitExp5(self, ctx: BKOOLParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.exp5())
        right = self.visit(ctx.exp6())
        op = ctx.CONCAT().getText()
        return BinaryOp(op, left, right)

    def visitExp6(self, ctx: BKOOLParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.exp7())
        right = self.visit(ctx.exp6())
        op = ctx.NOT().getText()
        return BinaryOp(op, left, right)

    def visitExp7(self, ctx: BKOOLParser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        body = self.visit(ctx.exp7())
        op = ""
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        return UnaryOp(op, body)

    def visitExp8(self, ctx: BKOOLParser.Exp8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        arr = self.visit(ctx.exp9())
        idx = self.visit(ctx.exp())
        return ArrayCell(arr, idx)

    def visitExp9(self, ctx: BKOOLParser.Exp9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.getChildCount() == 3:
            obj = self.visit(ctx.exp9())
            field = self.visit(ctx.exp10())
            return FieldAccess(obj, field)
        obj = self.visit(ctx.exp9())
        method = self.visit(ctx.exp10())
        expList = self.visit(ctx.explist()) if ctx.explist() else []
        return CallExpr(obj, method, expList)

    def visitExp10(self, ctx: BKOOLParser.Exp10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        id = self.visit(ctx.exp10())
        expList = self.visit(ctx.explist()) if ctx.explist() else []
        return NewExpr(id, expList)

    def visitExplist(self, ctx: BKOOLParser.ExplistContext):
        if ctx.getChildCount() == 1:
            exp = self.visit(ctx.exp())
            return [exp]
        else:
            exp = self.visit(ctx.exp())
            return [exp] + self.visit(ctx.explist())

    def visitOperands(self, ctx: BKOOLParser.OperandsContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.NIL():
            return NullLiteral()
        else:
            return self.visit(ctx.getChild(0))

    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(str(ctx.STRING_LIT().getText()))
        elif ctx.bool_lit():
            return self.visit(ctx.bool_lit())

    def visitArray_lit(self, ctx: BKOOLParser.Array_litContext):
        if ctx.getChildCount() == 2:
            return ArrayLiteral([])
        else:
            return ArrayLiteral(self.visit(ctx.list_literal()))

    def visitList_literal(self, ctx: BKOOLParser.List_literalContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.literal())]
        else:
            return [self.visit(ctx.literal())] + self.visit(ctx.list_literal())

    def visitBool_lit(self, ctx: BKOOLParser.Bool_litContext):
        return BooleanLiteral(True) if ctx.getChild(0).getText() == 'true' else BooleanLiteral(False)
        

    
