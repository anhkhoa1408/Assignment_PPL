.source D.java
.class public D
.super java.lang.Object
.field a [I

.method public foo(I)I
.var 0 is this LD; from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_1
	aload_0
	getfield D.a [I
	iconst_1
Label1:
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LD; from Label0 to Label1
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
	iconst_1
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_3
	iastore
	putfield D.a [I
Label1:
	return
.limit stack 4
.limit locals 1
.end method
