.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field total [I

.method public change(I)V
.var 0 is this LBKoolClass; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	bipush 7
	putfield BKoolClass.total [I
	istore_1
Label1:
	return
.limit stack 2
.limit locals 2
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
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	putfield BKoolClass.total [I
Label1:
	return
.limit stack 4
.limit locals 1
.end method
