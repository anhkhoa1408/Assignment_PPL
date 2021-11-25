.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field static final z I
.field static l I
.field j I
.field k I
.field p I
.field q I
.field r I
.field static c I
.field l I
.field a Ljava/lang/String;
.field b I
.field qwew Z
.field wf9ekp Z

.method public static foo()I
.var 0 is afnalfjoi I from Label0 to Label1
Label0:
	iconst_0
	istore_0
	aload_0
	aload_0
	getfield BKoolClass.wf9ekp Z
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	putfield BKoolClass.qwew Z
	aload_0
	aload_0
	getfield BKoolClass.b I
	ineg
	getstatic BKoolClass.l I
	iadd
	putfield BKoolClass.b I
Label1:
.limit stack 8
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	sipush 1000
	putfield BKoolClass.l I
	aload_0
	ldc "lll"
	putfield BKoolClass.a Ljava/lang/String;
	aload_0
	bipush 10
	putfield BKoolClass.b I
	aload_0
	iconst_1
	putfield BKoolClass.qwew Z
	aload_0
	iconst_0
	putfield BKoolClass.wf9ekp Z
Label1:
	return
.limit stack 11
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	bipush 22
	putstatic BKoolClass.z I
	iconst_1
	putstatic BKoolClass.l I
	bipush 100
	putstatic BKoolClass.c I
Label1:
	return
.limit stack 4
.limit locals 0
.end method
