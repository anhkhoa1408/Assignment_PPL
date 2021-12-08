.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field z I

.method public foo()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public static main()V
.var 0 is bk LBKoolClass; from Label0 to Label1
Label0:
	new BKoolClass
	dup
	invokespecial java/lang/Object/<init>()V
	astore_0
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 6
	putfield BKoolClass.z I
Label1:
	return
.limit stack 3
.limit locals 1
.end method
