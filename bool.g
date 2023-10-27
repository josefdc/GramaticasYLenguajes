start: logicalexpression;

logicalexpression:
     '\(' logicalexpression '\)'
     |logicalexpression TCONJ logicalexpression
    | '!' logicalexpression 
    |TRUE
    |FALSE
    ;

TCONJ : 'and';
TRUE : 'true';
FALSE : 'false';

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);		