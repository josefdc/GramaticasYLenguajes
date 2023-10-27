start: logicalexpression;

logicalexpression:
     '\(' logicalexpression '\)'
    | '!' logicalexpression 
    |  logicalexpression OR logicalexpression
    |  logicalexpression ORA logicalexpression
    |  logicalexpression IMPL logicalexpression
    |  logicalexpression DIMPL logicalexpression
    |TRUE
    |FALSE
    ;


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