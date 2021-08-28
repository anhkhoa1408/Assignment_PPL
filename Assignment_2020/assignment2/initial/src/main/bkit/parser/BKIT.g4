//Name: Nguyen Anh Khoa
//ID: 1812649
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

/* Parser */
program: declare+ EOF;

declare: var_declare|func_declare;

var_declare: VAR COLON (var_list SEMI)+;

var_list: var_stmt (COMMA var_stmt)*;

var_stmt:
        init_stmt
        |ID
        |ID (LSB integer_literal RSB)+
;

init_stmt:
        ID EQ init_val
        |ID (LSB integer_literal RSB)+ EQ init_val
;

lhs: 
        ID
        |expression index_operator
;

init_val:
        literal
        |array_init
;

array_init: 
        LCB one_dimension RCB
        |LCB multi_dimension RCB
;

one_dimension: literal (COMMA literal)*;

multi_dimension: LCB one_dimension RCB (COMMA LCB one_dimension RCB)*;

func_declare: FUNCTION COLON ID parameter_declare? BODY COLON var_declare? compound_stmt ENDBODY DOT;

parameter_declare: PARAMETER COLON parameter_list SEMI;

parameter_list: var_stmt (COMMA var_stmt)*;

stmt_list:
         assign_stmt
        |if_stmt
        |for_stmt
        |while_stmt
        |dowhile_stmt
        |break_stmt
        |continue_stmt
        |call_stmt
        |return_stmt
;

compound_stmt: stmt_list*;

assign_stmt: lhs EQ expression SEMI;

if_stmt: 
        IF expression THEN var_declare? compound_stmt
        elseif_stmt*
        (ELSE var_declare? compound_stmt)?
        ENDIF DOT 
;

elseif_stmt: ELSEIF expression THEN var_declare? compound_stmt;

for_stmt: 
        FOR LP ID EQ expression COMMA expression COMMA expression RP
        DO var_declare? compound_stmt
        ENDFOR DOT
;

while_stmt: WHILE expression DO var_declare? compound_stmt ENDWHILE DOT;

dowhile_stmt: DO var_declare? compound_stmt WHILE expression ENDDO DOT;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

call_stmt:ID LP exp_list? RP SEMI;

return_stmt: RETURN expression? SEMI;

expression: expression1 (DBEQ | NEQ | GT | LT | LTE | GTE | NEQF | GTF | LTF | GTEF | LTEF) expression1 | expression1;

expression1: expression1 (AND | OR) expression2 | expression2;

expression2: expression2 (ADD | ADDF | SUB | SUBF) expression3 | expression3;

expression3: expression3 (MUL | MULF | DIV | DIVF | RMD) expression4 | expression4;

expression4: NOT expression4 | expression5;

expression5: (SUB | SUBF) expression5 | expression6;

expression6: expression6 index_operator | expression7;

expression7: function_call | operand;

operand: LP expression RP | literal | ID;

literal:
         integer_literal
        |REAL_LITERAL
        |boolean_literal
        |STRING_LITERAL
;

exp_list: expression (COMMA expression)*
;

index_operator: (LSB expression RSB)+
; 

function_call: ID LP exp_list? RP;

/*Lexer declaration */

/* Literals */

boolean_literal: TRUE | FALSE;

integer_literal :NUM
                |'0'
                |HEXADECIMAL
                |OCTALDECIMAL
;

REAL_LITERAL:SUB?DIGIT+DOT(DIGIT|EXPONENT)*
            |SUB?DIGIT+EXPONENT 
;

STRING_LITERAL:'"' CHAR* '"'
{
	self.text=self.text[1:-1]
};

/* Keyword */
BODY: 'Body';

BREAK: 'Break';

CONTINUE: 'Continue';

DO:'Do';

ELSE: 'Else';

ELSEIF: 'ElseIf';

ENDBODY: 'EndBody';

ENDIF: 'EndIf';

ENDFOR: 'EndFor';

ENDWHILE: 'EndWhile';

FOR: 'For';

FUNCTION: 'Function';

IF: 'If';

PARAMETER: 'Parameter';

RETURN: 'Return';

THEN: 'Then';

VAR: 'Var' ;

WHILE: 'While';

TRUE: 'True';

FALSE: 'False';

ENDDO: 'EndDo';

MAIN: 'Main';

/* Arithmetic Operators */

/* Integer */
ADD: '+';

SUB: '-';

MUL: '*';

DIV: '\\';

RMD: '%';

/* Float */
ADDF: '+.';

SUBF: '-.';

MULF: '*.';

DIVF: '\\.';

/* Boolean Operators */
NOT: '!';

AND: '&&';

OR: '||';

/* Relational Operators */

/* Integer */
DBEQ: '==';

NEQ: '!=';

LT: '<';

GT: '>';

LTE: '<=';

GTE: '>=';

/* Float */
NEQF: '=/=';

LTF: '<.';

GTF: '>.';

LTEF: '<=.';

GTEF: '>=.';

/* Comment */
BLOCK_COMMENT: ('**' .*? '**') -> skip ;

//MULTI_LINE_BLOCK_COMMENT: ('**'.*? ('*'.+?)+ '**')->skip;

/*Specific character */
COMMA:',';

SEMI: ';' ;

COLON: ':' ;

LP: '('; // Left Parenthesis

RP: ')'; // Right Parenthesis

LCB: '{'; // Left Curly Bracket

RCB: '}'; // Right Curly Bracket

LSB: '['; // Left Square Bracket

RSB: ']'; // Right Square Bracket

DOT: '.';

EQ: '=';


fragment CHAR:  ~["EOF\b\f\r\n\t'\\] | ESC_CHAR | QUOTE  ;

fragment ESC_CHAR:'\\'[bfrnt'\\];

fragment QUOTE:'\'"';

HEXADECIMAL: '0'[xX][1-9A-F][0-9A-F]*;

OCTALDECIMAL: '0'[oO][1-9][0-7]* ;

NUM: SUB?[1-9]DIGIT*;
/* Identifiers */

fragment DIGIT: [0-9];

fragment EXPONENT:[eE]SIGN?DIGIT+;

fragment SIGN: [+-];

fragment ILLEGAL_ESC: '\\' ~[bfrnt'\\];

WS : [ \t\f\r\n]+ -> skip ;

ID: [a-z][A-Za-z_0-9]* ;

ERROR_CHAR:.
        {
                raise ErrorToken(self.text)
        }
;
UNCLOSE_STRING: '"' CHAR*
        {       
                raise UncloseString(self.text[1:])
        }
;
ILLEGAL_ESCAPE: '"' CHAR* '\\'~[bfrnt'\\QUOTE]
        {       
                raise IllegalEscape(self.text[1:])
        }
;
UNTERMINATED_COMMENT: '**' .*?
        {
                raise UnterminatedComment()
        }
;