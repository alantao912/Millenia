from lark import Lark

l = Lark('''start: WORD "," WORD "!"
            %import common.WORD   // imports from terminal library
            %ignore " "           // Disregard spaces in text
            
            
            ?conditional_branch: "if" "(" BOOL_EXPR ")" STATEMENT 
                               | "if" "(" BOOL_EXPR ")" BLOCK
            ?while_loop: "while" "(" BOOL_EXPR ")" STATEMENT
                       | "while" "(" BOOL_EXPR ")" BLOCK
            ?for_loop: 
         ''')
print(l.parse("Hello, World!"))