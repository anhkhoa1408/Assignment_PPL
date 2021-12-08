.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field static d F
.field bb F

.method public static main()V
.var 0 is d F from Label0 to Label1
.var 1 is e Z from Label0 to Label1
Label0:
	iconst_1
	iconst_5
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_1
Label1:
	return
.limit stack 6
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
