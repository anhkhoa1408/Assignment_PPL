from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, store, value=None):
        self.name = name
        self.mtype = mtype
        self.store = store
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"


class GetEnvironment(BaseVisitor):
    def visit(self, ast, param):
        return ast.accept(self, param)

    def visitProgram(self, ast, c):
        env = c.copy()

        for x in ast.decl:
            cls = self.visit(x, env)
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

        kind = self.visit(ast.kind, env)
        decl = self.visit(ast.decl, env)

        return {"kind": kind, "decl": decl}

    def visitVarDecl(self, ast, c):
        typ = self.visit(ast.varType, c)
        name = ast.variable
        storeType = type(ast)
        return Symbol(name, typ, storeType, None)

    def visitConstDecl(self, ast, c):
        name = ast.constant
        typ = self.visit(ast.constType, c)
        storeType = type(ast)
        return Symbol(name, typ, storeType, None)

    def visitMethodDecl(self, ast, c):
        env = {}
        env['global'] = [] + c['global']
        if c['current']['listmem'] != []:
            env['class'] = [] + c['current']['listmem']
        kind = self.visit(ast.kind, env)
        name = ast.name
        env['param'] = []

        for x in ast.param:
            ele = self.visit(x, env['param'])
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


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        io_listmem = [
            {
                "kind": Static(),
                "decl": Symbol(Id("readInt"), MType([], IntType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("writeInt"), MType([IntType()], VoidType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("writeIntLn"), MType([IntType()], VoidType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("readFloat"), MType([], FloatType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("writeFloat"), MType([FloatType()], VoidType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("writeFloatLn"), MType([FloatType()], VoidType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("readBool"), MType([], BoolType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("writeBool"), MType([BoolType()], VoidType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("writeBoolLn"), MType([BoolType()], VoidType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("readStr"), MType([], StringType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("writeStr"), MType([StringType()], VoidType()), None),
                "body": None
            },
            {
                "kind": Static(),
                "decl": Symbol(Id("writeStrLn"), MType([StringType()], VoidType()), None),
                "body": None
            },
        ]

        global_envi = [
            {
                "parent": None,
                "decl": Symbol(Id("io"), ClassDecl(Id("io"), [], None), io_listmem)
            }
        ]

        return global_envi

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        c = GetEnvironment().visit(ast, gl)
        gc = CodeGenVisitor(ast, c, path)
        gc.visit(ast, c)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast, c):
        [self.visit(i, c)for i in ast.decl]
        return c

    def visitClassDecl(self, ast, c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object")) if not ast.parentname else self.emit.printout(
            self.emit.emitPROLOG(self.className, ast.parentname.name))

        env = {}
        env['global'] = c
        env['current'] = {}
        env['current']['name'] = ast.classname
        env['current']['parent'] = ast.parentname
        env['current']['listmem'] = []

        for ele in c:
            if ele['decl'].name == ast.classname:
                env['current']['listmem'] = ele['decl'].store
                break

        [self.visit(ele, SubBody(None, env))
         for ele in ast.memlist]

        instanceAttrList = []
        staticAttrList = []
        for ele in ast.memlist:
            if type(ele) is AttributeDecl:
                if type(ele.kind) is Instance:
                    if type(ele.decl) is VarDecl and not ele.decl.varInit is None:
                        instanceAttrList.append(
                            Assign(ele.decl.variable, ele.decl.varInit))
                    elif type(ele.decl) is ConstDecl and not ele.decl.value is None:
                        instanceAttrList.append(
                            Assign(ele.decl.constant, ele.decl.value))
                elif type(ele.kind) is Static:
                    if type(ele.decl) is VarDecl and not ele.decl.varInit is None:
                        staticAttrList.append(
                            Assign(ele.decl.variable, ele.decl.varInit))
                    elif type(ele.decl) is ConstDecl and not ele.decl.value is None:
                        staticAttrList.append(
                            Assign(ele.decl.constant, ele.decl.value))

        # generate default constructor or constructor with parameter
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), VoidType(), Block([], instanceAttrList)), env, Frame("<init>", VoidType()))

        # int a = 0;

        # generate class init method
        if len(staticAttrList) > 0:
            self.genMETHOD(MethodDecl(Static(), Id("<clinit>"), list(
            ), VoidType(), Block([], staticAttrList)), env, Frame("<clinit>", VoidType()))

        # static a = 0;

        self.emit.emitEPILOG()
        return c

    def visitAttributeDecl(self, ast, c):
        isFinal = type(ast.decl) is ConstDecl
        isStatic = type(ast.kind) is Static

        self.emit.printout(self.emit.emitATTRIBUTE(ast.decl.constant.name, ast.decl.constType, True, isStatic, None) if isFinal else
                           self.emit.emitATTRIBUTE(ast.decl.variable.name, ast.decl.varType, False, isStatic, None))

    def visitVarDecl(self, ast, o):
        index = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(index, ast.variable.name, ast.varType,
                           o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        return Symbol(ast.variable.name, ast.varType, None, Index(index))

    def visitConstDecl(self, ast, o):
        index = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(o.frame.getNewIndex(
        ), ast.constant.name, ast.constType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        return Symbol(ast.constant.name, ast.constType, None, Index(index))

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.name.name == "<init>"

        isClassInit = consdecl.name.name == "<clinit>"

        isMain = consdecl.name.name == "main" and len(
            consdecl.param) == 0 and type(consdecl.returnType) is VoidType

        isStaticEle = next(filter(lambda x: consdecl.name ==
                           x['decl'].name, o['current']['listmem']), None)

        if (isStaticEle and type(isStaticEle['kind']) is Static) or isClassInit:
            isStatic = True
        else:
            isStatic = False

        returnType = consdecl.returnType

        methodName = consdecl.name.name

        intype = [] if isMain else list(
            map(lambda x: x.varType, consdecl.param))

        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, isStatic, frame))

        frame.enterScope(True)

        glenv = o
        glenv['local'] = []

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                o['current']['name']), frame.getStartLabel(), frame.getEndLabel(), frame))

        elif isClassInit:
            pass

        elif isMain:
            pass

        else:
            if not isStatic:
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                    o['current']['name']), frame.getStartLabel(), frame.getEndLabel(), frame))

            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)] + env.sym), consdecl.param, SubBody(frame, []))
            glenv['local'] += local.sym

        body = consdecl.body

        local = reduce(lambda env, ele: SubBody(
            frame, [self.visit(ele, env)] + env.sym), body.decl, SubBody(frame, []))

        initStmt = []
        for ele in body.decl:
            if type(ele) is VarDecl:
                if ele.varInit:
                    initStmt.append(Assign(ele.variable, ele.varInit))
            else:
                if ele.value:
                    initStmt.append(Assign(ele.constant, ele.value))

        body.stmt = initStmt + body.stmt

        glenv['local'] += local.sym

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            copy_env = glenv.copy()
            copy_env['initField'] = True
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            list(map(lambda x: self.visit(x, SubBody(frame, copy_env)), body.stmt))
        elif isClassInit:
            clcopy_env = glenv.copy()
            clcopy_env['initStatic'] = True
            list(map(lambda x: self.visit(x, SubBody(frame, clcopy_env)), body.stmt))
        else:
            list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className))

    def visitAssign(self, ast, o):
        if 'initField' in o.sym and o.sym['initField']:
            self.emit.printout(self.emit.emitREADVAR(
                "<init>", ClassType(Id("<init>")), 0, o.frame))
        else:
            if type(ast.lhs) is Id:
                local_ele = next(filter(
                    lambda x: x.name == ast.lhs.name, o.sym['local']), None)
                if not local_ele:
                    cls_ele = next(filter(
                        lambda x: x['decl'].name == ast.lhs, o.sym['current']['listmem']), None)
                    if cls_ele and type(cls_ele['kind']) is Instance:
                        self.emit.printout(self.emit.emitREADVAR(
                            ast.lhs.name, ClassType(o.sym['current']['name']), 0, o.frame))
            elif type(ast.lhs) is FieldAccess:
                if type(ast.lhs.obj) is SelfLiteral:
                    self.emit.printout(self.emit.emitREADVAR(
                        'this', ClassType(o.sym['current']['name']), 0, o.frame))

        if isinstance(ast.exp, ArrayLiteral):
            self.emit.printout(self.emit.emitNEWARRAY(IntType()))

        rcode, rtype = self.visit(ast.exp, Access(o.frame, o.sym, False)) if not self.visit(
            ast.exp, Access(o.frame, o.sym, False)) is None else ("", "")

        lcode, ltype = self.visit(ast.lhs, Access(o.frame, o.sym, True))

        if not type(ltype) is ArrayType and not type(rtype) is ArrayType:
            self.emit.printout(rcode)
            self.emit.printout(lcode)

        else:
            self.emit.printout(rcode)
            # self.emit.printout(self.emit.emitALOAD(rtype.eleType, o.frame))
            self.emit.printout(lcode)
            # self.emit.printout(self.emit.emitASTORE(ltype.eleType, o.frame))




    def visitIf(self, ast, o):
        falseLabel = o.frame.getNewLabel()
        if type(ast.expr) is BinaryOp:
            code, exp = self.visit(ast.expr, Access(
                o.frame, o.sym, False, (True, falseLabel, None)))
        elif type(ast.expr) is UnaryOp:
            code, exp = self.visit(ast.expr, Access(
                o.frame, o.sym, False, (True, falseLabel, True)))
        self.emit.printout(code)
        self.visit(ast.thenStmt, o)
        if not ast.elseStmt:
            self.emit.printout(self.emit.emitLABEL(falseLabel, o.frame))
        else:
            nextLabel = o.frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(nextLabel, o.frame))
            self.emit.printout(self.emit.emitLABEL(falseLabel, o.frame))
            self.visit(ast.elseStmt, o)
            self.emit.printout(self.emit.emitLABEL(nextLabel, o.frame))

    def visitFor(self, ast, o):
        o.frame.enterLoop()
        id_code, id_typ = self.visit(ast.id, Access(o.frame, o.sym, True))
        e1c, e1t = self.visit(ast.expr1, o)
        e2c, e2t = self.visit(BinaryOp('>', ast.id, ast.expr2), Access(
            o.frame, o.sym, False, (True, o.frame.getBreakLabel())))
        self.emit.printout(e1c + id_code)
        self.emit.printout(self.emit.emitLABEL(
            o.frame.getContinueLabel(), o.frame))
        self.emit.printout(e2c)

        if type(ast.loop) is Break:
            pass
        else:
            self.visit(ast.loop, o)
            inc_exp, inc_exptype = self.visit(BinaryOp('+' if ast.up else '-', ast.id, IntLiteral(
                1)), Access(o.frame, o.sym, False))

            self.emit.printout(inc_exp + id_code)
            self.emit.printout(self.emit.emitGOTO(
                o.frame.getContinueLabel(), o.frame))

            self.emit.printout(self.emit.emitLABEL(
                o.frame.getBreakLabel(), o.frame))

        o.frame.exitLoop()

    def visitCallStmt(self, ast, o):
        pass

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(
            o.frame.getBreakLabel(), o.frame))

    def visitArrayCell(self, ast, o):
        arr_code, arr_type = self.visit(ast.arr, o)
        idx_code, idx_type = self.visit(ast.idx, o)


        return arr_code + idx_code, arr_type

    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)

        typ = None
        if type(e1t) is type(e2t):
            typ = e1t
        elif type(e1t) is FloatType and type(e2t) is IntType:
            typ = FloatType()
            e2c += self.emit.emitI2F(o.frame)
        elif type(e1t) is IntType and type(e2t) is FloatType:
            typ = FloatType()
            e1c += self.emit.emitI2F(o.frame)

        if ast.op in ['+', '-']:
            opc = self.emit.emitADDOP(ast.op, typ, o.frame)
        elif ast.op in ['*', '\\']:
            opc = self.emit.emitMULOP(ast.op, typ, o.frame)
        elif ast.op in ['/']:
            if type(typ) is IntType:
                e1c += self.emit.emitI2F(o.frame)
                e2c += self.emit.emitI2F(o.frame)
                typ = FloatType()
            opc = self.emit.emitMULOP(ast.op, typ, o.frame)
        elif ast.op in ['%']:
            opc = self.emit.emitMOD(o.frame)
        elif ast.op in ['<', '<=', '>', '>=', '==', '!=']:
            if o.isFirst and o.isFirst[0]:
                opc = self.emit.emitRELOP(
                    ast.op, typ, str(o.isFirst[1]), o.frame)
            else:
                opc = self.emit.emitREOP(ast.op, typ, o.frame)
            typ = BoolType()
        elif ast.op == '&&':
            opc = self.emit.emitANDOP(o.frame)
            typ = BoolType()
        elif ast.op == '||':
            opc = self.emit.emitOROP(o.frame)
            typ = BoolType()

        return e1c + e2c + opc, typ

    def visitUnaryOp(self, ast, o):
        code, typ = self.visit(ast.body, o)
        if ast.op == '-':
            opc = self.emit.emitNEGOP(typ, o.frame)
        elif ast.op == '!':
            if o.isFirst and o.isFirst[0] and o.isFirst[2]:
                opc = self.emit.emitNOT(
                    typ, o.frame, o.isFirst[1], o.isFirst[2])
            else:
                opc = self.emit.emitNOT(typ, o.frame)

        return code + opc, typ

    def visitNewExpr(self, ast, o):
        param = [self.visit(x, o) for x in ast.param]
        code = self.emit.emitNEW(ast.classname.name)
        code += self.emit.emitDUP(o.frame)

        if ast.classname.name == o.sym['current']['name'].name:
            code += self.emit.emitINVOKESPECIAL(o.frame)
        else:
            code += self.emit.emitINVOKESPECIAL(
                o.frame, ast.classname.name, MType([x[1] for x in param], VoidType()))

        return code, VoidType()

    def visitCallExpr(self, ast, o):
        param = [self.visit(x, o) for x in ast.param]
        if type(ast.obj) is SelfLiteral:
            ele = next(filter(
                lambda x: x['decl'].name == ast.method, o.sym['current']['listmem']), None)
            if type(ele['kind']) is Static:
                typ = ele['decl'].mtype
                code = self.emit.emitINVOKESTATIC(
                    o.sym['current']['name'].name + '/' + ast.method.name, MType([x[1] for x in param], typ), o.frame)
                return code, typ
            else:
                typ = ele['decl'].mtype
                code = self.emit.emitINVOKEVIRTUAL(
                    o.sym['current']['name'].name + '/' + ast.method.name, MType([x[1] for x in param], typ), o.frame)
                return code, typ
        elif type(ast.obj) is Id:
            id_code, id_type = self.visit(
                ast.obj, Access(o.frame, o.sym, False))
            ele = next(filter(
                lambda x: x['decl'].name == ast.obj, o.sym['current']['listmem']), None)
            if ele:
                if type(ele['kind']) is Static:
                    typ = ele['decl'].mtype
                    code = self.emit.emitINVOKESTATIC(
                        ast.obj.name + '/' + ast.method.name, MType([x[1] for x in param], typ), o.frame)
                    return code, typ
                else:
                    typ = ele['decl'].mtype

                    for cls_ele in o.sym['global']:
                        if cls_ele['decl'].name == typ.classname:
                            for mem in cls_ele['decl'].store:
                                if mem['decl'].name == ast.method:
                                    rettype = mem['decl'].mtype.rettype

                    code = id_code + (self.emit.emitINVOKEVIRTUAL(
                        ele['decl'].mtype.classname.name + '/' + ast.method.name, MType([x[1] for x in param], rettype), o.frame))

                    return code, typ
            else:
                cls_ele = next(filter(
                    lambda x: x['decl'].name == ast.obj, o.sym['global']), None)
                if cls_ele:
                    field = next(
                        filter(lambda x: x['decl'].name == ast.method, cls_ele['decl'].store), None)
                    typ = field['decl'].mtype
                    code = self.emit.emitINVOKESTATIC(
                        ast.obj.name + '/' + ast.method.name, MType([x[1] for x in param], typ), o.frame)
                    return code, typ
        else:
            code, typ = self.visit(ast.obj, o)
            new_typ = None
            if type(ast.obj) is FieldAccess:
                cls_ele = next(filter(
                    lambda x: x['decl'].name == ast.obj.fieldname, o.sym['current']['listmem']), None)

                if cls_ele:
                    for ele in o.sym['global']:
                        if ele['decl'].name == cls_ele['decl'].mtype.classname:
                            for mem in ele['decl'].store:
                                if mem['decl'].name == ast.method:
                                    new_typ = mem['decl'].mtype

                    code += self.emit.emitINVOKEVIRTUAL(
                        cls_ele['decl'].mtype.classname.name + '/' + ast.method.name, MType([x[1] for x in param], new_typ.rettype), o.frame)

                    return code, new_typ

    def visitFieldAccess(self, ast, o):
        if type(ast.obj) is SelfLiteral:
            ele = next(filter(
                lambda x: x['decl'].name == ast.fieldname, o.sym['current']['listmem']), None)
            if type(ele['kind']) is Static:
                typ = ele['decl'].mtype
                code = self.emit.emitPUTSTATIC(o.sym['current']['name'].name + '.' + ast.fieldname.name, ele['decl'].mtype, o.frame) if o.isLeft else self.emit.emitGETSTATIC(
                    o.sym['current']['name'].name + '.' + ast.fieldname.name, ele['decl'].mtype, o.frame)
                return code, typ
            else:
                typ = ele['decl'].mtype
                code = self.emit.emitREADVAR(
                    "this", ClassType(o.sym['current']['name']), 0, o.frame) if not o.isLeft else ""
                code += self.emit.emitPUTFIELD(o.sym['current']['name'].name + '.' + ast.fieldname.name, typ, o.frame) if o.isLeft else self.emit.emitGETFIELD(
                    o.sym['current']['name'].name + '.' + ast.fieldname.name, typ, o.frame)
                return code, typ
        elif type(ast.obj) is Id:
            id_code, t = self.visit(ast.obj, Access(o.frame, o.sym, False))

            local_ele = next(filter(
                lambda x: x.name == ast.obj.name, o.sym['local']), None)

            if local_ele:
                typ = local_ele.mtype
                for ele in o.sym['global']:
                    if ele['decl'].name == local_ele.mtype.classname:
                        for mem in ele['decl'].store:
                            if mem['decl'].name == ast.fieldname:
                                typ = mem['decl'].mtype

                code = self.emit.emitREADVAR(ast.fieldname.name, ClassType(
                    local_ele.mtype.classname), local_ele.value.value, o.frame)
                code += c + self.emit.emitPUTFIELD(local_ele.mtype.classname.name + '.' + ast.fieldname.name, typ, o.frame) if o.isLeft else self.emit.emitGETFIELD(
                    local_ele.mtype.classname.name + '.' + ast.fieldname.name, typ, o.frame)
                return code, typ
            else:
                ele = next(filter(
                    lambda x: x['decl'].name == ast.obj, o.sym['current']['listmem']), None)

                if ele:
                    if type(ele['kind']) is Static:
                        typ = ele['decl'].mtype
                        code = self.emit.emitPUTSTATIC(ast.obj.name + '.' + ast.fieldname.name, typ, o.frame) if o.isLeft else self.emit.emitGETSTATIC(
                            ast.obj.name + '.' + ast.fieldname.name, typ, o.frame)
                        return code, typ
                    else:

                        typ = None
                        for cls_ele in o.sym['global']:
                            if cls_ele['decl'].name == ele['decl'].mtype.classname:
                                for mem in cls_ele['decl'].store:
                                    if mem['decl'].name == ast.fieldname:
                                        typ = mem['decl'].mtype

                        code = id_code + (self.emit.emitPUTFIELD(o.sym['current']['name'].name + '.' + ast.fieldname.name, typ, o.frame) if o.isLeft else self.emit.emitGETFIELD(
                            o.sym['current']['name'].name + '.' + ast.fieldname.name, typ, o.frame))

                        return code, typ
                else:
                    cls_ele = next(filter(
                        lambda x: x['decl'].name == ast.obj, o.sym['global']), None)

                    if cls_ele:
                        field = next(
                            filter(lambda x: x['decl'].name == ast.fieldname, cls_ele['decl'].store), None)

                        typ = field['decl'].mtype
                        code = self.emit.emitPUTSTATIC(ast.obj.name + '.' + ast.fieldname.name, typ, o.frame) if o.isLeft else self.emit.emitGETSTATIC(
                            ast.obj.name + '.' + ast.fieldname.name, typ, o.frame)

                        return code, typ
        else:
            field_code, field_typ = self.visit(ast.obj, o)
            new_typ = None

            if type(ast.obj) is FieldAccess:
                cls_ele = next(filter(
                    lambda x: x['decl'].name == ast.obj.fieldname, o.sym['current']['listmem']), None)
                if cls_ele:
                    for ele in o.sym['global']:
                        if ele['decl'].name == cls_ele['decl'].mtype.classname:
                            for mem in ele['decl'].store:
                                if mem['decl'].name == ast.fieldname:
                                    new_typ = mem['decl'].mtype

                    code = field_code + (self.emit.emitPUTFIELD(cls_ele['decl'].mtype.classname.name + '.' + ast.fieldname.name, new_typ, o.frame) if o.isLeft else self.emit.emitGETFIELD(
                        cls_ele['decl'].mtype.classname.name + '.' + ast.fieldname.name, new_typ, o.frame))
                    return code, new_typ
                else:
                    global_ele = next(filter(
                        lambda x: x['decl'].name == ast.obj.obj, o.sym['global']), None)
                    if global_ele:
                        for ele in global_ele['decl'].store:
                            if ele['decl'].name == ast.obj.fieldname:
                                name = ele['decl'].mtype.classname.name

                        for ele in o.sym['global']:
                            if ele['decl'].name.name == name:
                                for mem in ele['decl'].store:
                                    if mem['decl'].name == ast.fieldname:
                                        typ = mem['decl'].mtype

                        code = field_code + (self.emit.emitPUTFIELD(name + '.' + ast.fieldname.name, typ, o.frame) if o.isLeft else self.emit.emitGETFIELD(
                            name + '.' + ast.fieldname.name, typ, o.frame))

                        return code, typ

        # return "", ""

    def visitReturn(self, ast, o):
        code, typ = self.visit(ast.expr, Access(o.frame, o.sym, False))
        code += self.emit.emitRETURN(typ, o.frame)
        self.emit.printout(code)

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value), o.frame), BoolType()

    def visitArrayType(self, ast, o):
        code = self.emit.emitPUSHICONST(ast.size, o.frame)
        code += self.emit.emitNEWARRAY(ast.eleType)
        return code

    def visitArrayLiteral(self, ast, o):
        code = ''
        for index in range(0, len(ast.value)):
            code += self.emit.emitDUP(o.frame)
            code += self.emit.emitPUSHICONST(index, o.frame)
            if type(ast.value[index]) is IntLiteral:
                typ = IntType()
                code += self.emit.emitPUSHICONST(
                    ast.value[index].value, o.frame)
            elif type(ast.value[index]) is FloatLiteral:
                typ = FloatType()
                code += self.emit.emitPUSHFCONST(
                    ast.value[index].value, o.frame)
            elif type(ast.value[index]) is StringLiteral:
                typ = StringType()
                code += self.emit.emitPUSHCONST(
                    ast.value[index].value, StringType(), o.frame)
            elif type(ast.value[index]) is BooleanLiteral:
                typ = BoolType()
                code += self.emit.emitPUSHICONST(
                    str(ast.value[index].value), o.frame)

            code += self.emit.emitASTORE(typ, o.frame)

        return code, ArrayType(len(ast.value), typ)

    def visitId(self, ast, o):
        if 'initField' in o.sym and o.sym['initField'] is True:
            typ = next(filter(lambda ele: ele['decl'].name == ast, o.sym['current']['listmem']), None)[
                'decl'].mtype
            code = self.emit.emitPUTFIELD(
                o.sym['current']['name'].name + '.' + ast.name, typ, o.frame)
            return code, typ
        elif 'initStatic' in o.sym and o.sym['initStatic'] is True:
            typ = next(filter(lambda ele: ele['decl'].name == ast, o.sym['current']['listmem']), None)[
                'decl'].mtype
            code = self.emit.emitPUTSTATIC(
                o.sym['current']['name'].name + '.' + ast.name, typ, o.frame)
            return code, typ

        for ele in o.sym['local']:
            if ast.name == ele.name:
                typ = ele.mtype
                code = self.emit.emitWRITEVAR(ast.name, ele.mtype, ele.value.value, o.frame) if o.isLeft else self.emit.emitREADVAR(
                    ast.name, ele.mtype, ele.value.value, o.frame)
                return code, typ

        for ele in o.sym['current']['listmem']:
            if ast == ele['decl'].name:
                if type(ele['kind']) is Static:
                    typ = ele['decl'].mtype
                    code = self.emit.emitPUTSTATIC(o.sym['current']['name'].name + '.' + ast.name, ele['decl'].mtype, o.frame) if o.isLeft else self.emit.emitGETSTATIC(
                        o.sym['current']['name'].name + '.' + ast.name, ele['decl'].mtype, o.frame)
                    
                    return code, typ
                else:
                    typ = ele['decl'].mtype
                    code = self.emit.emitREADVAR(
                        ast.name, ClassType(o.sym['current']['name']), 0, o.frame) if not o.isLeft or type(typ) is ArrayType else ""
                    code += self.emit.emitPUTFIELD(o.sym['current']['name'].name + '.' + ast.name, typ, o.frame) if o.isLeft and not type(typ) is ArrayType else self.emit.emitGETFIELD(
                        o.sym['current']['name'].name + '.' + ast.name, typ, o.frame)

                    return code, typ

        return "", ""
