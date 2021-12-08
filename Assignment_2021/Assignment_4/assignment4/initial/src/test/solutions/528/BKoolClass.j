.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public foo()I
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	bipush 100
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main()V
.var 0 is bk LBKoolClass; from Label0 to Label1
.var 1 is spkt LBKoolClass; from Label0 to Label1
.var 2 is zoo I from Label0 to Label1
Label0:
	new BKoolClass
	dup
	invokespecial java/lang/Object/<init>()V
	astore_0
	new BKoolClass
	dup
	invokespecial java/lang/Object/<init>()V
	astore_1
	istore_2
Label1:
	return
.limit stack 1
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
