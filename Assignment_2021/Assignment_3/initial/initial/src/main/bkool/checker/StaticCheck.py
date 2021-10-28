
"""
 * @author nhphung
"""
from AST import *
from Visitor import BaseVisitor
from StaticError import *


class MType:
    def __init__(self, partype, rettype, listName = None):
        self.partype = partype
        self.rettype = rettype
        self.listName = listName



class Symbol:
    def __init__(self, name, mtype, store, value = None):
        self.name = name
        self.mtype = mtype
        self.store = store
        self.value = value


class GetEnvironment(BaseVisitor):
    def visit(self, ast, param):
        return ast.accept(self, param)

    def visitProgram(self, ast, c):
        env = c.copy()
        
        for x in ast.decl:
            cls = self.visit(x, env)
            if cls['decl'].name in list(map(lambda ele: ele['decl'].name, env)):
                raise Redeclared(Class(), str(cls['decl'].name.name))
            env.append(cls)

        return env

    def visitClassDecl(self, ast, c):
        env = {}
        env['global'] = c
        env['current'] = {}
        env['current']['name'] = ast.classname
        env['current']['parent'] = ast.parentname if ast.parentname else None
        env['current']['listmem'] = []

        if isinstance(ast.memlist, list):
            for x in ast.memlist:
                ele = self.visit(x, env)
                env['current']['listmem'] += [ele]

        return {
            "parent": ast.parentname,
            "decl": Symbol(ast.classname, ast, env['current']['listmem'], None)
        }

    def visitAttributeDecl(self, ast, c):
        env = {}
        env['global'] = [] + c['global']
        env['class'] = [] + c['current']['listmem']
        env['checkClass'] = True

        kind = self.visit(ast.kind, env)
        decl = self.visit(ast.decl, env)

        return {"kind": kind, "decl": decl}

    def visitVarDecl(self, ast, c):
        typ = self.visit(ast.varType, c)
        if isinstance(c, dict):
            if 'decl' in c and c['decl'] != []:
                for ele in c['decl']:
                    if ast.variable == ele.name:
                        raise Redeclared(Class() if type(
                            typ) is ClassType else Attribute(), str(ast.variable.name))
            elif 'param' in c and c['param'] != []:
                for ele in c['param']:
                    if ast.variable == ele.name:
                        raise Redeclared(Class() if type(
                            typ) is ClassType else Attribute(), str(ast.variable.name))
            elif 'class' in c and c['class'] != [] and c['checkClass'] == True:
                for ele in c['class']:
                    if ast.variable == ele['decl'].name:
                        raise Redeclared(Class() if type(
                            typ) is ClassType else Attribute(), str(ast.variable.name))

        name = ast.variable
        storeType = type(ast)
        return Symbol(name, typ, storeType, None)

    def visitConstDecl(self, ast, c):
        if isinstance(c, dict):
            if 'decl' in c:
                for ele in c['decl']:
                    if ast.constant == ele.name:
                        raise Redeclared(Constant(), str(ast.constant.name))
            elif 'class' in c:
                for ele in c['class']:
                    if ast.constant == ele['decl'].name:
                        raise Redeclared(Constant(), str(ast.constant.name))

        if isinstance(c, list):
            for ele in c:
                if ast.constant == ele.name:
                    raise Redeclared(Constant(), str(ast.constant.name))

        name = ast.constant
        typ = self.visit(ast.constType, c)
        storeType = type(ast)


        return Symbol(name, typ, storeType, None)

    def visitMethodDecl(self, ast, c):
        for ele in c['current']['listmem']:
            if ast.name == ele['decl'].name:
                raise Redeclared(Method(), str(ast.name.name))

        env = {}
        env['global'] = [] + c['global']
        if c['current']['listmem'] != []:
            env['class'] = [] + c['current']['listmem']
        kind = self.visit(ast.kind, env)
        name = ast.name
        env['param'] = []
        for x in ast.param:
            ele = self.visit(x, env['param'])
            if ele.name in list(map(lambda x: x.name, env['param'])):
                raise Redeclared(Parameter(), str(ele.name.name))
            env['param'].append(ele)

        returnType = self.visit(
            ast.returnType, env) if ast.returnType else None

        return {
            'kind': kind,
            'decl': Symbol(name, MType(env['param'], returnType), None, None),
            'body': None
        }

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitIntType(self, ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBoolType(self, ast, c):
        return BoolType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitClassType(self, ast, c):
        return ClassType(ast.classname)

    def visitArrayType(self, ast, c):
        return ArrayType(ast.size, ast.eleType)

    def visitIntLiteral(self, ast, c):
        return MType(None, IntType())

    def visitFloatLiteral(self, ast, c):
        return MType(None, FloatType())

    def visitBoolLiteral(self, ast, c):
        return MType(None, BoolType())

    def visitStringLiteral(self, ast, c):
        return MType(None, StringType())

    def visitNullLiteral(self, ast, c):
        return MType(None, NullLiteral())

    def visitStatic(self, ast, param):
        return Static()

    def visitInstance(self, ast, param):
        return Instance()


class StaticChecker(BaseVisitor):
    io_listmem = [
        {
            "kind": Static(),
            "decl": Symbol(Id("readInt"), MType([], IntType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("writeInt"), MType([IntType()], VoidType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("writeIntLn"), MType([IntType()], VoidType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("readFloat"), MType([], FloatType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("writeFloat"), MType([FloatType()], VoidType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("writeFloatLn"), MType([FloatType()], VoidType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("readBool"), MType([], BoolType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("writeBool"), MType([BoolType()], VoidType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("writeBoolLn"), MType([BoolType()], VoidType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("readStr"), MType([], StringType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("writeStr"), MType([StringType()], VoidType()), None)
        },
        {
            "kind": Static(),
            "decl": Symbol(Id("writeStrLn"), MType([StringType()], VoidType()), None)
        },
    ]

    global_envi = [
        {
            "parent": None,
            "decl": Symbol(Id("io"), ClassDecl(Id("io"), [], None), io_listmem)
        }
    ]

    def __init__(self, ast):
        self.ast = ast

    def visit(self, ast, param):
        return ast.accept(self, param)

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        env = GetEnvironment().visitProgram(ast, c)
        
        for x in ast.decl:
            self.visit(x, env)
        return []

    def visitClassDecl(self, ast, c):
        env = {}
        env['global'] = c
        env['current'] = {}
        env['current']['name'] = ast.classname
        env['current']['parent'] = ast.parentname
        env['current']['listmem'] = []

        if ast.parentname:
            if ast.parentname not in list(map(lambda x: x['decl'].name, c)):
                raise Undeclared(Class(), ast.parentname.name)

        for ele in c:
            if ele['decl'].name == ast.classname:
                env['current']['listmem'] = ele['decl'].store

        if isinstance(ast.memlist, list):
            for x in ast.memlist:
                ele = self.visit(x, env)

    def visitAttributeDecl(self, ast, c):
        env = {}
        env['global'] = [] + c['global']
        env['class'] = [] + c['current']['listmem']
        env['checkClass'] = True
        env['kind'] = self.visit(ast.kind, env)

        self.visit(ast.decl, env)

    def visitVarDecl(self, ast, c):
        name = ast.variable
        storeType = type(ast)
        typ = self.visit(ast.varType, c)
        init = self.visit(ast.varInit, c) if ast.varInit else None

        if type(typ) is FloatType:
            if init and not type(init.rettype) in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast.varInit)
        elif init and not type(init.rettype) is type(typ):
            raise TypeMismatchInExpression(ast.varInit)

        return Symbol(name, typ, storeType, init)

    def visitConstDecl(self, ast, c):
        name = ast.constant
        typ = self.visit(ast.constType, c)
        init = self.visit(ast.value, c) if ast.value else None
        storeType = type(ast)

        if init is None:
            raise IllegalConstantExpression(ast.value)

        if type(typ) is FloatType:
            if not type(init.rettype) in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast.value)
        elif not type(init.rettype) is type(typ):
            raise TypeMismatchInConstant(ast)
        
        if init.partype is VarDecl:
            raise IllegalConstantExpression(ast.value)

        elif init.partype is ConstDecl:
            if ast.constant.name in init.listName:
                raise IllegalConstantExpression(ast.value)

        return Symbol(name, typ, storeType, init)

    def visitMethodDecl(self, ast, c):
        env = {}
        env['global'] = [] + c['global']
        env['class'] = [] + c['current']['listmem']
        env['param'] = []

        for ele in env['class']:
            if ele['decl'].name == ast.name:
                env['param'] = ele['decl'].mtype.partype

        self.visit(ast.body, env)

    def visitBlock(self, ast, c):
        env = c
        env['decl'] = []
        env['current_stmt'] = []
        for x in ast.decl:
            ele = self.visit(x, env)
            if env['param'] != [] and ele.name in list(map(lambda x: x.name, env['param'])):
                raise Redeclared(Variable(), str(ele.name.name))
            env['decl'].append(ele)

        for x in ast.stmt:
            self.visit(x, env)
            env.pop('loop', None)

    def visitAssign(self, ast, c):
        lhs = self.visit(ast.lhs, c)
        exp = self.visit(ast.exp, c)

        if lhs.partype is ConstDecl:
            raise CannotAssignToConstant(ast)
        if type(lhs.rettype) is IntType:
            if not type(exp.rettype) is IntType:
                raise TypeMismatchInStatement(ast)
            return IntType()
        elif type(lhs.rettype) is FloatType:
            if not type(exp.rettype) in [IntType, FloatType]:
                raise TypeMismatchInStatement(ast)
            return FloatType()
        
        if not type(lhs.rettype) is type(exp.rettype):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, c):
        expr = self.visit(ast.expr, c)

        self.visit(ast.thenStmt, c)
        self.visit(ast.elseStmt, c) if ast.elseStmt else None
        if not type(expr.rettype) is BoolType:
            raise TypeMismatchInStatement(ast)

    def visitFor(self, ast, c):
        exp1 = self.visit(ast.expr1, c)
        exp2 = self.visit(ast.expr2, c)
        if not type(exp1.rettype) is IntType or not type(exp2.rettype) is IntType:
            raise TypeMismatchInStatement(ast)

        c['loop'] = True
        self.visit(ast.loop, c)

    def visitBreak(self, ast, c):
        if 'loop' not in c:
            raise MustInLoop(ast)

    def visitContinue(self, ast, c):
        if 'loop' not in c:
            raise MustInLoop(ast)

    def visitCallStmt(self, ast, c):
        obj = None
        if type(ast.obj) is Id:
            if 'decl' in c and c['decl'] != []:
                for ele in c['decl']:
                    if ast.obj == ele.name:
                        obj = MType(ele.store, ele.mtype)
            if 'param' in c and c['param'] != [] and obj is None:
                for ele in c['param']:
                    if ast.obj == ele.name:
                        obj = MType(ele.store, ele.mtype)
            if 'class' in c and c['class'] != [] and obj is None:
                for ele in c['class']:
                    if ast.obj == ele['decl'].name:
                        obj = MType(ele['decl'].store, ele['decl'].mtype)
            if 'global' in c and c['global'] != [] and obj is None:
                for ele in c['global']:
                    if ast.obj == ele['decl'].name:
                        obj = MType(ele['decl'].store, ele['decl'].mtype)

            if obj == None:
                raise Undeclared(Class(), str(ast.obj.name))

            if not type(obj.rettype) in [ClassType, ClassDecl]:
                raise TypeMismatchInStatement(ast)

            method = None

            for ele in c['global']:
                if ele['decl'].name == obj.rettype.classname:
                    for member in ele['decl'].store:
                        if member['decl'].name == ast.method:
                            method = member

                    # If method not in child class, then find in parent class
                    if ele['parent'] is not None and method is None:
                        for parentEle in c['global']:
                            if parentEle['decl'].name == ele['parent']:
                                for member in parentEle['decl'].store:
                                    if member['decl'].name == ast.method:
                                        method = member

            if method is None:
                raise Undeclared(Method(), ast.method.name)

            if type(method['kind']) is Instance and type(obj.rettype) is ClassDecl:
                raise IllegalMemberAccess(ast)

            if type(method['kind']) is Static and type(obj.rettype) is ClassType:
                raise IllegalMemberAccess(ast)

            if not type(method['decl'].mtype.rettype) is VoidType:
                raise TypeMismatchInStatement(ast)
        else:
            ele = self.visit(ast.obj, c)
            kind = None
            for ele in c['global']:
                for member in ele['decl'].store:
                    if member['decl'].name == ast.method and 'body' in member:
                        kind = member['kind']
                        obj = MType(member['decl'].store, member['decl'].mtype)

            if obj is None:
                raise Undeclared(Method(), ast.method.name)

            if not type(obj.rettype.rettype) is VoidType:
                raise TypeMismatchInStatement(ast)
            
            if type(kind) is Static:
                raise IllegalMemberAccess(ast)

            

        

    def visitId(self, ast, c):
        if 'decl' in c and c['decl'] != []:
            for ele in c['decl']:
                if ast.name == ele.name.name:
                    return MType(ele.store, ele.mtype, ast.name)
        if 'param' in c and c['param'] != []:
            for ele in c['param']:
                if ast.name == ele.name.name:
                    return MType(ele.store, ele.mtype, ast.name)
        if 'class' in c and c['class'] != []:
            for ele in c['class']:
                if ast.name == ele['decl'].name.name:
                    return MType(ele['decl'].store, ele['decl'].mtype, ast.name)
        if 'global' in c and c['global'] != []:
            for ele in c['global']:
                if ast.name == ele['decl'].name.name:
                    return MType(ele['decl'].store, ele['decl'].mtype, ast.name)
        raise Undeclared(Identifier(), ast.name)

    def visitBinaryOp(self, ast, c):
        op = ast.op
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        typ = left.partype if left.partype is VarDecl else right.partype

        if op in ['+', '-', '*', '/']:
            if type(left.rettype) in [IntType, FloatType] and type(right.rettype) in [IntType, FloatType]:
                if type(left.rettype) is FloatType or type(right.rettype) is FloatType:
                    return MType(typ, FloatType(), [left.name, right.name])
                return MType(typ, IntType(), [left.listName, right.listName])
            raise TypeMismatchInExpression(ast)
        elif op in ['\\', '%']:
            if type(left.rettype) is IntType and type(right.rettype) is IntType:
                return MType(typ, IntType(), [left.listName, right.listName])
            raise TypeMismatchInExpression(ast)
        elif op in ['==', '!=']:
            if type(left.rettype) in [IntType, BoolType] and type(right.rettype) in [IntType, BoolType]:
                if type(left.rettype) == type(right.rettype):
                    return MType(typ, BoolType(), [left.listName, right.listName])
            raise TypeMismatchInExpression(ast)
        elif op in ['>', '>=', '<', '<=']:
            if type(left.rettype) in [IntType, FloatType] and type(right.rettype) in [IntType, FloatType]:
                return MType(typ, BoolType(), [left.listName, right.listName])
            raise TypeMismatchInExpression(ast)
        elif op in ['&&', '||']:
            if type(left.rettype) is BoolType and type(right.rettype) is BoolType:
                return MType(typ, BoolType(), [left.listName, right.listName])
            raise TypeMismatchInExpression(ast)
        elif op == '^':
            if type(left.rettype) is StringType and type(right.rettype) is StringType:
                return MType(typ, StringType(), [left.listName, right.listName])
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        op = ast.op
        body = self.visit(ast.body, c)
        if op in ['+', '-']:
            if type(body.rettype) in [IntType, FloatType]:
                return MType(body.partype, body.rettype, [body.listName])
            raise TypeMismatchInExpression(ast)
        elif op == '!':
            if type(body.rettype) is BoolType:
                return MType(body.partype, body.rettype, [body.listName])
            raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        obj = None
        if type(ast.obj) is Id:
            if 'decl' in c and c['decl'] != []:
                for ele in c['decl']:
                    if ast.obj == ele.name:
                        obj = MType(ele.store, ele.mtype)
            if 'param' in c and c['param'] != [] and obj is None:
                for ele in c['param']:
                    if ast.obj == ele.name:
                        obj = MType(ele.store, ele.mtype)
            if 'class' in c and c['class'] != [] and obj is None:
                for ele in c['class']:
                    if ast.obj == ele['decl'].name:
                        obj = MType(ele['decl'].store, ele['decl'].mtype)
            if 'global' in c and c['global'] != [] and obj is None:
                for ele in c['global']:
                    if ast.obj == ele['decl'].name:
                        obj = MType(ele['decl'].store, ele['decl'].mtype)

            if obj == None:
                raise Undeclared(Class(), str(ast.obj.name))

            if not type(obj.rettype) in [ClassType, ClassDecl]:
                raise TypeMismatchInExpression(ast)

            method = None

            for ele in c['global']:
                if ele['decl'].name == obj.rettype.classname:
                    for member in ele['decl'].store:
                        if member['decl'].name == ast.method:
                            method = member
                    # If method not in child class, then find in parent class
                    if ele['parent'] is not None and method is None:
                        for parentEle in c['global']:
                            if parentEle['decl'].name == ele['parent']:
                                for member in parentEle['decl'].store:
                                    if member['decl'].name == ast.method:
                                        method = member

            if method is None:
                raise Undeclared(Method(), ast.method.name)

            if type(method['kind']) is Instance and type(obj.rettype) is ClassDecl:
                raise IllegalMemberAccess(ast)

            if type(method['kind']) is Static and type(obj.rettype) is ClassType:
                raise IllegalMemberAccess(ast)

            if type(method['decl'].mtype.rettype) is VoidType:
                raise TypeMismatchInStatement(ast)

            return MType(None, method['decl'].mtype.rettype)

        else:
            ele = self.visit(ast.obj, c)
            kind = None
            for ele in c['global']:
                for member in ele['decl'].store:
                    if member['decl'].name == ast.method and 'body' in member:
                        kind = member['kind']
                        obj = MType(member['decl'].store, member['decl'].mtype.rettype)

            if obj is None:
                raise Undeclared(Attribute(), ast.method.name)

            if type(obj.rettype) is VoidType:
                raise TypeMismatchInStatement(ast)

            if type(kind) is Static:
                raise IllegalMemberAccess(ast)

            return obj

        

    def visitNewExpr(self, ast, c):
        # Raise if don't have special method (constructor)
        specialMethod = None
        for ele in c['global']:
            if ele['decl'].name == ast.classname:
                for member in ele['decl'].store:
                    if member['decl'].name == ast.classname:
                        specialMethod = member

        if specialMethod is None:
            raise Undeclared(SpecialMethod(), ast.classname.name)

        return MType(None, ClassType(ast.classname))

    def visitFieldAccess(self, ast, c):
        obj = None
        if type(ast.obj) is Id:
            if 'decl' in c and c['decl'] != []:
                for ele in c['decl']:
                    if ast.obj == ele.name:
                        obj = MType(ele.store, ele.mtype)
            if 'param' in c and c['param'] != [] and obj is None:
                for ele in c['param']:
                    if ast.obj == ele.name:
                        obj = MType(ele.store, ele.mtype)
            if 'class' in c and c['class'] != [] and obj is None:
                for ele in c['class']:
                    if ast.obj == ele['decl'].name:
                        obj = MType(ele['decl'].store, ele['decl'].mtype)
            if 'global' in c and c['global'] != [] and obj is None:
                for ele in c['global']:
                    if ast.obj == ele['decl'].name:
                        obj = MType(ele['decl'].store, ele['decl'].mtype)


            if not type(obj.rettype) in [ClassType, ClassDecl]:
                raise TypeMismatchInExpression(ast)

            field = None
            for ele in c['global']:
                if ele['decl'].name == obj.rettype.classname:
                    for member in ele['decl'].store:
                        if member['decl'].name == ast.fieldname:
                            field = member

                    # If field not in child class, then find in parent class
                    if ele['parent'] is not None and field is None:
                        for parentEle in c['global']:
                            if parentEle['decl'].name == ele['parent']:
                                for member in parentEle['decl'].store:
                                    if member['decl'].name == ast.fieldname:
                                        field = member

            if field is None:
                raise Undeclared(Attribute(), ast.fieldname.name)

            if type(field['kind']) is Instance and type(obj.rettype) is ClassDecl:
                raise IllegalMemberAccess(ast)

            if type(field['kind']) is Static and type(obj.rettype) is ClassType:
                raise IllegalMemberAccess(ast)

            if type(field['decl'].mtype) is VoidType:
                raise TypeMismatchInStatement(ast)

            return MType(field['decl'].store, field['decl'].mtype)

        else:
            ele = self.visit(ast.obj, c)
            for ele in c['global']:
                for member in ele['decl'].store:
                    if member['decl'].name == ast.fieldname and not 'body' in member:
                        kind = member['kind']
                        obj = MType(member['decl'].store, member['decl'].mtype)

            if obj is None:
                raise Undeclared(Attribute(), ast.fieldname.name)

            if type(obj.rettype) is VoidType:
                raise TypeMismatchInStatement(ast)

            if type(kind) is Static:
                raise TypeMismatchInStatement(ast)
            
            return obj
            
    def visitArrayCell(self, ast, c):
        arr, typ = None, None
        if type(ast.arr) is Id:
            if 'decl' in c and c['decl'] != []:
                for ele in c['decl']:
                    if ast.arr == ele.name:
                        arr = MType(ele.store, ele.mtype.eleType)
                        typ = ele.mtype
            if 'param' in c and c['param'] != [] and arr is None:
                for ele in c['param']:
                    if ast.arr == ele.name:
                        arr = MType(ele.store, ele.mtype.eleType)
                        typ = ele.mtype
            if 'class' in c and c['class'] != [] and arr is None:
                for ele in c['class']:
                    if ast.arr == ele['decl'].name:
                        arr = MType(ele['decl'].store,
                                    ele['decl'].mtype.eleType)
                        typ = ele['decl'].mtype
            if 'global' in c and c['global'] != [] and arr is None:
                for ele in c['global']:
                    if ast.arr == ele['decl'].name:
                        arr = MType(ele['decl'].store,
                                    ele['decl'].mtype.eleType)
                        typ = ele['decl'].mtype

        idx = self.visit(ast.idx, c)
        if not type(typ) is ArrayType or not type(idx.rettype) is IntType:
            raise TypeMismatchInExpression(ast)

        return MType(arr.partype, arr.rettype)

    def visitArrayLiteral(self, ast, c):
        typ = self.visit(ast.value[0], c).rettype
        for ele in ast.value[1:]:
            eleType = self.visit(ele, c).rettype
            if not type(eleType) is type(typ):
                raise IllegalArrayLiteral(ast)

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitIntType(self, ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBoolType(self, ast, c):
        return BoolType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitClassType(self, ast, c):
        return ClassType(ast.classname)

    def visitArrayType(self, ast, c):
        return ArrayType(ast.size, ast.eleType)

    def visitIntLiteral(self, ast, c):
        return MType(None, IntType())

    def visitFloatLiteral(self, ast, c):
        return MType(None, FloatType())

    def visitBooleanLiteral(self, ast, c):
        return MType(None, BoolType())

    def visitStringLiteral(self, ast, c):
        return MType(None, StringType())

    def visitNullLiteral(self, ast, c):
        return MType(None, NullLiteral())

    def visitSelfLiteral(self, ast, c):
        return MType(None, SelfLiteral())

    def visitStatic(self, ast, param):
        return Static()

    def visitInstance(self, ast, param):
        return Instance()
