.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field bk LBkoolClass;
.field bas LBKoolClass;
.field class_d LD;
.field c I

.method public foo2()I
.var 0 is this LBKoolClass; from Label0 to Label1
.var 1 is bas2 LBKoolClass; from Label0 to Label1
Label0:
	new BKoolClass
	dup
	invokespecial java/lang/Object/<init>()V
	astore_1
	aload_0
	aload_1
	getfield BKoolClass.class_d LD;
	invokevirtual D/foo2()I
	putfield BKoolClass.c I
	iconst_0
	ireturn
Label1:
.limit stack 5
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	new BkoolClass
	dup
	invokespecial BkoolClass()V
	putfield BKoolClass.bk LBkoolClass;
	aload_0
	new BKoolClass
	dup
	invokespecial java/lang/Object/<init>()V
	putfield BKoolClass.bas LBKoolClass;
	aload_0
	new D
	dup
	invokespecial D()V
	putfield BKoolClass.class_d LD;
	aload_0
	iconst_0
	putfield BKoolClass.c I
Label1:
	return
.limit stack 4
.limit locals 1
.end method
