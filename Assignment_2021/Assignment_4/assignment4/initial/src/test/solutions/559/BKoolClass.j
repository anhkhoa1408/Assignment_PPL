.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public static main()V
.var 0 is a I from Label0 to Label1
Label0:
	iconst_0
	istore_0
	iconst_5
	istore_0
Label2:
	iload_0
	bipush 10
	if_icmple Label3
	iload_0
	iconst_1
	iadd
	istore_0
	goto Label2
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
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
