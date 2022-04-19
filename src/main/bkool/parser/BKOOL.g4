grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: mptype 'main' LB RB LP body? RP EOF;

mptype: INTTYPE | VOIDTYPE | FLOATTYPE;

body: funcall SEMI;

exp:
	LB exp RB
	| exp (MULOP | DIVOP) exp
	| exp (ADDOP | SUBOP) exp
	| funcall
	| INTLIT
	| FLOATLIT;

funcall: ID LB exp? RB;

INTTYPE: 'int';

VOIDTYPE: 'void';

FLOATTYPE: 'float';

ID: [a-zA-Z]+;

INTLIT: [0-9]+;

ADDOP: '+';

SUBOP: '-';

MULOP: '*';

DIVOP: '/';

FLOATLIT: [+-]? ([0-9]* [.])? [0-9]+;

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;