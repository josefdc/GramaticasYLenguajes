from plyplus import Grammar

list_parser = Grammar("""
start: expression;
                      

                      expression: if name then name else name end;
                      name: '[a-z]+';
                      if: 'if';
                      then: 'then';
                      else: 'else';
                      end: 'end';
                      
logicalexpression:
        negation
    |   parenle 
    |   conj
    |   disyu
    |   implication
    |   dimplication
    |   TRUE
    |   FALSE
    ;




negation: NEG logicalexpression;


parenle: '\(' logicalexpression '\)';


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
NEG: '!';



OPC: '/\*';
CPC: '\*/';
COMMENT: OPC'.*?' CPC (%ignore);





// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);
                    
        """)

res = list_parser.parse('if p then p else p end')

res.to_png_with_pydot('list_parser_tree.png')