.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

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
.var 1 is i I from Label0 to Label1
Label0:
	new BKoolClass
	dup
	invokespecial java/lang/Object/<init>()V
	astore_0
	iconst_0
	istore_1
	iconst_1
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmple Label3
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
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
