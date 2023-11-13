start: listDef;

program  : functiondef* expression;

functiondef:  DEF ID LPAR (parameter  (',' parameter)*)*  RPAR LCBR expression RCBR;

parameter: something|listDef|functioncall;

//List 
listDef: LPAR ID '[' 'list' elements ']' RPAR;
elements: (something)*;
something: ID|number;

@expression:
	  parexpression
	| conditional
	| functioncall
	| mulexpr
	| addexpr
	| number 
	| variable
	| listDef
	;

parexpression:
  LPAR expression RPAR;

conditional:
	IF LPAR logicalexpression RPAR LCBR expression RCBR ELSE LCBR expression RCBR;

functioncall:
	ID LPAR (expression (',' expression)*)* RPAR;

mulexpr:
	expression (MUL | DIV | MOD) expression;

addexpr:
	expression (ADD | SUB) expression;

variable:
	ID;

logicalexpression:
	expression (LT | GT | LEQ | GEQ | EQ | NEQ) expression
	| TRUE
	| FALSE
	;
/**
 * Lexer rules
 *
 * Here we define the tokens identified by the lexer.
 */

// Comments
OPEN_COMMENT :  '/\*';
CLOSE_COMMENT :  '\*/';
COMMENT : OPEN_COMMENT '.*?' CLOSE_COMMENT (%ignore);

// Arithmetic operations
ADD  :  '\+';
SUB  :  '-';
MUL  :  '\*';
DIV  :  '/';
MOD  :  '%';

// Boolean operations
LT  :  '<';
GT  :  '>';
LEQ :  '<=';
GEQ :  '>=';
EQ  :  '==';
NEQ  : '!=';

LPAR : '\(';
RPAR : '\)';
LCBR : '{';
RCBR : '}';

// Integers and identifiers
number: '[0-9]+';
ID: '[a-z]+'
	(%unless
		DEF: 'def';
		IF    : 'if';
		ELSE  : 'else';
		TRUE  : 'true';
		FALSE : 'false';		
	);

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);		