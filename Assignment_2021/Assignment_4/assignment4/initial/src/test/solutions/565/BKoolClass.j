.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field static d F
.field bb F

.method public static main()V
.var 0 is d F from Label0 to Label1
.var 1 is e Z from Label0 to Label1
Label0:
	bipush 19
	bipush 10
	idiv
	fstore_0
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
