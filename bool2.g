start: ifexpression;


expression:
    ifexpression
    ;



ifexpression: IF '\w+' THEN '\w+' ELSE '\w+' END;



IF    : 'if';
ELSE  : 'else';
END: 'end';
THEN: 'then';
ID: '\w+';



OPC: '/\*';
CPC: '\*/';
COMMENT: OPC'.*?' CPC (%ignore);






// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);