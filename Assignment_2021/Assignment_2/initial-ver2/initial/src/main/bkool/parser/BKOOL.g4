// 1812649
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declare+ EOF ;

declare: CLASS ID (EXTENDS ID)? LP memberlist RP;

memberlist: (attribute_decl | method_decl)*;

attribute_decl: STATIC? FINAL? all_type attr_list SEMI;

all_type: primitive_type | array_type | void_type | ID;

void_type: VOID;

primitive_type: INT | FLOAT | BOOLEAN | STRING;

array_type: primitive_type LSB INT_LIT RSB;

attr_list: ID (EQ exp)? COMMA attr_list | ID (EQ exp)?;

method_decl: STATIC? all_type? ID LB param_list? RB block_stmt;

param_list: all_type idlist SEMI param_list | all_type idlist;

idlist: ID COMMA idlist | ID;

block_stmt: LP var_list? list_stmt? RP;

var_list: FINAL? all_type idlist SEMI var_list | FINAL? all_type idlist SEMI;

stmt: assign_stmt
    | if_stmt
    | for_stmt
    | break_stmt
    | continue_stmt
    | return_stmt
    | invocation_stmt;

list_stmt: stmt list_stmt | stmt;

assign_stmt: lhs COLON EQ exp SEMI;

lhs: ID | exp LSB exp RSB;

if_stmt: IF exp THEN stmt (ELSE stmt)?;

for_stmt: FOR ID COLON EQ exp (TO | DOWNTO) exp DO stmt;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN exp SEMI;

invocation_stmt: (instance_method | static_method) SEMI;

instance_method: exp DOT ID LB explist? RB;

static_method: ID DOT ID LB explist? RB;

exp: exp1 (LT | GT | LTEQ | GTEQ) exp1 | exp1;

exp1: exp2 (DBEQ | NOT_EQ) exp2 | exp2;

exp2: exp2 (AND | OR) exp3 | exp3;

exp3: exp3 (ADD | SUB) exp4 | exp4;

exp4: exp4 (MUL | INT_DIV | FLOAT_DIV | MOD) exp5 | exp5;

exp5: exp5 CONCAT exp6 | exp6;

exp6: exp7 NOT exp6 | exp7;

exp7: (ADD | SUB) exp7 | exp8;

exp8: exp9 LSB exp RSB | exp9;

exp9: exp9 DOT exp10 (LB explist? RB)? | exp10;

exp10: NEW exp10 LB explist? RB | operands;

explist: exp COMMA explist | exp;

operands: ID | literal | array_lit | THIS;

literal: INT_LIT
    | FLOAT_LIT
    | bool_lit
    | STRING_LIT;

array_lit: LP list_literal? RP;

list_literal: literal COMMA list_literal | literal;

// Keyword

BOOLEAN: 'boolean';

BREAK:'break';

CLASS: 'class';

CONTINUE:'continue';

DO: 'do';

ELSE: 'else';

EXTENDS: 'extends';

FLOAT: 'float';

IF: 'if';

INT: 'int';

NEW: 'new';

STRING: 'string';

THEN: 'then';

FOR: 'for';

RETURN: 'return';

TRUE: 'true';

FALSE: 'false';

VOID: 'void';

NIL: 'nil';

THIS: 'this';

FINAL: 'final';

STATIC: 'static';

TO: 'to';

DOWNTO: 'downto';

// Operator

ADD: '+';

SUB: '-';

MUL: '*';

FLOAT_DIV: '/';

INT_DIV: '\\';

MOD: '%';

NOT_EQ: '!=';

DBEQ: '==';

LT: '<';

GT: '>';

LTEQ: '<=';

GTEQ: '>=';

OR: '||';

AND: '&&';

NOT: '!';

CONCAT: '^';

// Seperator

LSB: '[';

RSB: ']';

LP: '{';

RP: '}';

LB: '(' ;

RB: ')' ;

SEMI: ';' ;

COLON: ':';

DOT: '.';

COMMA: ',';

// Literal

INT_LIT: '0' | [1-9] DIGIT*;

FLOAT_LIT: DIGIT+ (DECIMAL EXPONENT? | EXPONENT);

bool_lit: TRUE | FALSE;

STRING_LIT: '"' CHAR* '"';


ID: (LETTER | '_') [_a-zA-Z0-9]*;

// Comment

BLOCKCOMMENT: '/*' ~[EOF]* '*/' -> skip;

LINECOMMENT: '#' ~[EOF\n]* -> skip;

EQ: '=';

WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment DIGIT: [0-9];

fragment DECIMAL: DOT DIGIT*;

fragment EXPONENT: [eE] (SUB | ADD)? DIGIT+;

fragment LETTER: [a-zA-Z];

fragment ESC_CHAR: '\\'[bfrnt"\\];

fragment CHAR:  ~[\b\f\r\n\t"\\] | ESC_CHAR;

ERROR_CHAR:.
{
    raise ErrorToken(self.text)
}
;
UNCLOSE_STRING: '"' CHAR*
{       
        raise UncloseString(self.text[0:])
};
ILLEGAL_ESCAPE: '"' CHAR* '\\'~[bfrnt"\\]
{       
        raise IllegalEscape(self.text[0:])
};