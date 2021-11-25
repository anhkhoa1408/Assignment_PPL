.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field static final z I

.method public static foo(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is t I from Label0 to Label1
.var 3 is abc Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	istore_2
	ldc "avkjn"
	astore_3
	iconst_1
	putstatic BKoolClass.z I
	ldc "1"
	astore_3
Label1:
.limit stack 1
.limit locals 4
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

.method public static <clinit>()V
Label0:
	bipush 22
	putstatic BKoolClass.z I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
