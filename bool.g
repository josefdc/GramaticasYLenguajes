start: logicalexpression;

logicalexpression:
     '\(' logicalexpression '\)'
    | '!' logicalexpression 
    |TRUE
    |FALSE
    ;

TRUE : 'true';
FALSE : 'false';

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);		