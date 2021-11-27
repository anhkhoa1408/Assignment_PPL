.source D.java
.class public D
.super java.lang.Object
.field z I
.field static c I
.field static bk2 LBKoolClass;
.field z Z
.field z1 Z

.method public foo2(II)I
.var 0 is this LD; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_2
	if_icmple Label3
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
.limit stack 3
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LD; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield D.z I
	aload_0
	iconst_1
	putfield D.z I
	aload_0
	iconst_0
	putfield D.z1 Z
Label1:
	return
.limit stack 9
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_1
	putstatic D.c I
	new BKoolClass
	dup
	invokespecial BKoolClass()V
	putstatic D.bk2 LBKoolClass;
Label1:
	return
.limit stack 2
.limit locals 0
.end method
