# muh language

## Language Spec
Primitives:
    - One integer number type
    - One floating point number type
    - Built-in Arraylist
    - Built-in String
    - Built-in Tuple
    
Module System:
    - Every file is a "module". [file].[identifier] to access value
    - Imperative code is only allowed in functions. At the top level only declarations such as variable, struct, functions are allowed.
    - Entry point must have a main function.
    
Control Flow:
    - Semicolons and braces.
    - never unless
    - maybe, please (default 50% chance of execution, each please increases likelihood by a factor of 5%, capped at 99%)
    - while loop
    - Functions
    
## Language syntax



### primitives

ints:
```
1
100
100_000_103
0x932423
chinese character integer constants
```



Array literal:

```
[]
[1, 2]
["a" * 5] => ["a", "a", "a", "a", "a"]
```

String literal:

```
"asdf"
"\n"
```

Tuple:

```
// () empty tuple disallowed b/c alan said so
(1, 2)
("a", 2, [1, 2]) // heterogenous bby
```



### identifiers

All identfiers must be alphanumeric or underscore, cant start with number `[a-zA-Z][0-9]`

a
abc1
a2b3


### variable decl

// TODO

<type> .... 



