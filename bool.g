start: logicalexpression;

logicalexpression:
        parenle
    |   negation 
    |   conj
    |   disyu
    |   implication
    |   dimplication
    |   TRUE
    |   FALSE
    ;



parenle: '\(' logicalexpression '\)';

negation: '!' logicalexpression;

conj: logicalexpression AND logicalexpression |
        logicalexpression ANDM logicalexpression;

disyu: logicalexpression OR logicalexpression
    |   logicalexpression ORA logicalexpression;

implication: logicalexpression IMPL logicalexpression;

dimplication: logicalexpression DIMPL logicalexpression;


AND: 'and';
ANDM: '\*';
DIMPL: '<=>';
IMPL: '=>';
OR: 'or';
ORA: '\+';
TRUE : 'true';
FALSE : 'false';



OPC: '/\*';
CPC: '\*/';
COMMENT: OPC'.*?' CPC (%ignore);

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);		