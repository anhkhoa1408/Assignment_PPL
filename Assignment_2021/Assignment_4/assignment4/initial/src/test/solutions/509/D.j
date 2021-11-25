.source D.java
.class public D
.super java.lang.Object
.field z I
.field static c I
.field static bk2 LBKoolClass;

.method public static foo()I
Label0:
	iconst_0
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public foo2()I
.var 0 is this LD; from Label0 to Label1
Label0:
	iconst_0
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LD; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield D.z I
Label1:
	return
.limit stack 3
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
