.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field bk LBkoolClass;
.field c I
.field d I
.field static sjoefij I
.field e LD;

.method public foo1()I
.var 0 is this LBKoolClass; from Label0 to Label1
.var 1 is aeopw I from Label0 to Label1
.var 2 is uriuwm I from Label0 to Label1
.var 3 is basd LBKoolClass; from Label0 to Label1
Label0:
	new BKoolClass
	dup
	invokespecial java/lang/Object/<init>()V
	astore_3
	aload_0
	getstatic D.c I
	putfield BKoolClass.c I
	aload_0
	getfield BKoolClass.c I
	aload_0
	getfield BKoolClass.d I
	imul
	ireturn
Label1:
.limit stack 3
.limit locals 4
.end method

.method public foo2()F
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	getfield BKoolClass.c I
	aload_0
	getfield BKoolClass.d I
	iadd
	getstatic BKoolClass.sjoefij I
	isub
	ireturn
Label1:
.limit stack 2
.limit locals 1
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
	iconst_0
	putfield BKoolClass.c I
	aload_0
	invokevirtual D/foo(II)LD;
	iconst_1
	fadd
	putfield BKoolClass.d I
	aload_0
	new D
	dup
	invokespecial D(II)V
	putfield BKoolClass.e LD;
Label1:
	return
.limit stack 6
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_1
	putstatic BKoolClass.sjoefij I
Label1:
	return
.limit stack 2
.limit locals 0
.end method
